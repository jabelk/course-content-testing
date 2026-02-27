"""
Editorial Rules Engine - AI Client with Graceful Degradation

Provides AI-enhanced editorial suggestions for context-dependent rules.
Falls back gracefully when AI is unavailable, converting ai_enhanced rules to QUERY.

Key Features:
    - OAuth2 authentication with Cisco Chat-AI
    - Response caching to reduce API calls
    - Confidence scoring for AI suggestions
    - Graceful degradation when AI unavailable
"""
import os
import json
import base64
import hashlib
from typing import Optional, Dict, List, Tuple
from dataclasses import dataclass, field
from datetime import datetime, timedelta

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False


# API Configuration
OAUTH_URL = "https://id.cisco.com/oauth2/default/v1/token"
LLM_URL = "https://chat-ai.cisco.com/openai/deployments/gpt-4o-mini/chat/completions"

# Cache settings
CACHE_TTL_HOURS = 24
MAX_CACHE_SIZE = 1000


@dataclass
class AIResponse:
    """Represents an AI response with confidence scoring."""
    suggestion: str
    confidence: float  # 0.0 to 1.0
    reasoning: Optional[str] = None
    cached: bool = False


@dataclass
class CacheEntry:
    """Cache entry for AI responses."""
    response: AIResponse
    timestamp: datetime
    content_hash: str


class AIEditorialClient:
    """
    Client for AI-enhanced editorial suggestions.

    Provides context-aware suggestions for rules that require
    understanding beyond simple pattern matching.
    """

    def __init__(self):
        """Initialize the AI client with optional credentials."""
        self.client_id = os.environ.get("CLIENT_ID")
        self.client_secret = os.environ.get("CLIENT_SECRET")
        self.app_key = os.environ.get("APP_KEY")
        self._access_token: Optional[str] = None
        self._token_expiry: Optional[datetime] = None
        self._cache: Dict[str, CacheEntry] = {}

    @property
    def is_available(self) -> bool:
        """Check if AI client is available and configured."""
        if not REQUESTS_AVAILABLE:
            return False
        if not all([self.client_id, self.client_secret, self.app_key]):
            return False
        return True

    def _get_cache_key(self, content: str, rule_id: str) -> str:
        """Generate a cache key from content and rule ID."""
        content_hash = hashlib.sha256(content.encode()).hexdigest()[:16]
        return f"{rule_id}:{content_hash}"

    def _get_cached(self, cache_key: str) -> Optional[AIResponse]:
        """Get cached response if available and not expired."""
        if cache_key not in self._cache:
            return None

        entry = self._cache[cache_key]
        if datetime.now() - entry.timestamp > timedelta(hours=CACHE_TTL_HOURS):
            del self._cache[cache_key]
            return None

        response = entry.response
        response.cached = True
        return response

    def _set_cached(self, cache_key: str, response: AIResponse, content_hash: str):
        """Cache a response, evicting old entries if needed."""
        # Evict oldest entries if cache is full
        if len(self._cache) >= MAX_CACHE_SIZE:
            oldest_key = min(self._cache.keys(),
                           key=lambda k: self._cache[k].timestamp)
            del self._cache[oldest_key]

        self._cache[cache_key] = CacheEntry(
            response=response,
            timestamp=datetime.now(),
            content_hash=content_hash
        )

    def _get_access_token(self) -> Optional[str]:
        """Get or refresh OAuth access token."""
        if not self.is_available:
            return None

        # Return cached token if still valid
        if self._access_token and self._token_expiry:
            if datetime.now() < self._token_expiry:
                return self._access_token

        try:
            payload = "grant_type=client_credentials"
            auth_value = base64.b64encode(
                f'{self.client_id}:{self.client_secret}'.encode('utf-8')
            ).decode('utf-8')

            headers = {
                "Accept": "*/*",
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": f"Basic {auth_value}"
            }

            response = requests.post(OAUTH_URL, headers=headers, data=payload, timeout=30)
            response.raise_for_status()

            token_data = response.json()
            self._access_token = token_data.get('access_token')
            # Token typically expires in 1 hour, refresh a bit early
            self._token_expiry = datetime.now() + timedelta(minutes=55)

            return self._access_token

        except Exception as e:
            print(f"Warning: Could not get AI access token: {e}")
            return None

    def _make_request(self, prompt: str, content: str) -> Optional[str]:
        """Make a request to the AI API."""
        token = self._get_access_token()
        if not token:
            return None

        try:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
                "appkey": self.app_key
            }

            payload = {
                "messages": [
                    {
                        "role": "system",
                        "content": "You are an editorial assistant for Cisco technical tutorials. Provide concise, specific suggestions for improving content quality."
                    },
                    {
                        "role": "user",
                        "content": f"{prompt}\n\nContent to analyze:\n{content}"
                    }
                ],
                "temperature": 0.3,
                "max_tokens": 500
            }

            response = requests.post(
                LLM_URL,
                headers=headers,
                json=payload,
                timeout=60
            )
            response.raise_for_status()

            data = response.json()
            return data.get('choices', [{}])[0].get('message', {}).get('content', '')

        except Exception as e:
            print(f"Warning: AI request failed: {e}")
            return None

    def analyze_procedural_intro(
        self,
        content: str,
        file_path: str,
        line_number: int
    ) -> Optional[AIResponse]:
        """
        Analyze if procedural content needs a "To [action]:" intro.

        Args:
            content: The paragraph or section to analyze
            file_path: File being analyzed
            line_number: Line number of the content

        Returns:
            AIResponse with suggestion or None if AI unavailable
        """
        if not self.is_available:
            return None

        cache_key = self._get_cache_key(content, "PROC_INTRO")
        cached = self._get_cached(cache_key)
        if cached:
            return cached

        prompt = """Analyze this content and determine if it needs a procedural introduction.

A procedural introduction is needed when:
- The content introduces numbered steps
- There's no "To [action]:" prefix before the steps
- The steps describe a task the user should complete

If a procedural intro is needed, respond in this format:
NEEDED: To [suggested action]:
CONFIDENCE: [0.0-1.0]
REASONING: [brief explanation]

If NOT needed, respond:
NOT_NEEDED
CONFIDENCE: [0.0-1.0]
REASONING: [brief explanation]"""

        ai_response = self._make_request(prompt, content)
        if not ai_response:
            return None

        response = self._parse_procedural_response(ai_response)
        if response:
            self._set_cached(cache_key, response, self._get_cache_key(content, "")[-16:])

        return response

    def _parse_procedural_response(self, ai_response: str) -> Optional[AIResponse]:
        """Parse AI response for procedural intro analysis."""
        lines = ai_response.strip().split('\n')

        if not lines:
            return None

        first_line = lines[0].strip()

        if first_line.startswith('NOT_NEEDED'):
            return None

        if first_line.startswith('NEEDED:'):
            suggestion = first_line.replace('NEEDED:', '').strip()
            confidence = 0.7  # Default confidence
            reasoning = None

            for line in lines[1:]:
                if line.startswith('CONFIDENCE:'):
                    try:
                        confidence = float(line.replace('CONFIDENCE:', '').strip())
                    except ValueError:
                        pass
                elif line.startswith('REASONING:'):
                    reasoning = line.replace('REASONING:', '').strip()

            return AIResponse(
                suggestion=suggestion,
                confidence=min(1.0, max(0.0, confidence)),
                reasoning=reasoning
            )

        return None

    def analyze_heading_conversion(
        self,
        heading: str,
        context: str
    ) -> Optional[AIResponse]:
        """
        Analyze a gerund heading and suggest imperative conversion.

        Args:
            heading: The heading text (e.g., "## Configuring VLANs")
            context: Surrounding content for context

        Returns:
            AIResponse with suggestion or None if AI unavailable
        """
        if not self.is_available:
            return None

        cache_key = self._get_cache_key(heading, "HEADING_CONVERT")
        cached = self._get_cached(cache_key)
        if cached:
            return cached

        prompt = f"""Convert this gerund heading to imperative form.

Heading: {heading}

Rules:
- Remove -ing suffix and use verb base form
- "Configuring" -> "Configure"
- "Installing" -> "Install"
- "Understanding" -> "Understand" or suggest better action verb

Respond with:
SUGGESTION: [converted heading]
CONFIDENCE: [0.0-1.0]"""

        ai_response = self._make_request(prompt, context)
        if not ai_response:
            return None

        response = self._parse_heading_response(ai_response)
        if response:
            self._set_cached(cache_key, response, self._get_cache_key(heading, "")[-16:])

        return response

    def _parse_heading_response(self, ai_response: str) -> Optional[AIResponse]:
        """Parse AI response for heading conversion."""
        lines = ai_response.strip().split('\n')

        suggestion = None
        confidence = 0.8  # Default confidence for heading conversion

        for line in lines:
            if line.startswith('SUGGESTION:'):
                suggestion = line.replace('SUGGESTION:', '').strip()
            elif line.startswith('CONFIDENCE:'):
                try:
                    confidence = float(line.replace('CONFIDENCE:', '').strip())
                except ValueError:
                    pass

        if suggestion:
            return AIResponse(
                suggestion=suggestion,
                confidence=min(1.0, max(0.0, confidence))
            )

        return None

    def clear_cache(self):
        """Clear the response cache."""
        self._cache = {}

    def get_cache_stats(self) -> Dict:
        """Get cache statistics."""
        return {
            "size": len(self._cache),
            "max_size": MAX_CACHE_SIZE,
            "ttl_hours": CACHE_TTL_HOURS
        }


# Global client instance (lazy initialization)
_client: Optional[AIEditorialClient] = None


def get_ai_client() -> AIEditorialClient:
    """Get or create the global AI client instance."""
    global _client
    if _client is None:
        _client = AIEditorialClient()
    return _client


def is_ai_available() -> bool:
    """Check if AI enhancement is available."""
    return get_ai_client().is_available
