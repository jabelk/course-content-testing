# Why This Approach Works Better Than RAG in Circuit

This document explains the technical differences between our rules-based editorial pipeline and the RAG (Retrieval-Augmented Generation) approach used in Cisco's Circuit.

## The Problem with Circuit's Approach

### How Circuit Works

Circuit uses a conversational AI interface where you:
1. Paste content into the chat
2. Include a "megaprompt" with all your rules
3. Ask the AI to find and apply edits
4. Copy the output back to Word

This seems intuitive, but has fundamental limitations for editorial work.

### Why RAG Fails for Editorial Tasks

**RAG (Retrieval-Augmented Generation)** works by:
1. Storing documents (like style guides) in a vector database
2. When you ask a question, retrieving "relevant" chunks
3. Feeding those chunks to the AI as context
4. Having the AI generate a response

**The problem**: Editorial rules aren't "retrieved" - they need to be **applied systematically**.

| Issue | What Happens |
|-------|--------------|
| **Inconsistent retrieval** | Same content → different rules retrieved → different results |
| **Context window limits** | Can't fit all rules + full document → some rules get dropped |
| **No state tracking** | Acronyms: "Did I already define this?" - AI forgets mid-document |
| **Probabilistic output** | AI generates text → variance in how it phrases suggestions |

### Real Results: 50%+ Variance

From Kim/Jim's testing in Circuit:
> "One time you run it and it says 400 edits. Next time 200. Next time 350."

This isn't a bug - it's how LLMs work. Each run:
- Retrieves slightly different context
- Processes in a different order
- Generates probabilistically different output

## Our Approach: Deterministic Rules Engine

### How It Works

```
DOCX Input
    ↓
[Pandoc] → Markdown
    ↓
[Rules Engine]
    ├── Pattern matching (regex)
    ├── Acronym state tracking
    ├── Heading analysis
    └── Structure validation
    ↓
[Report Generator]
    ↓
Categorized Markdown Report
```

### Key Differences

| Aspect | Circuit (RAG) | Our Pipeline |
|--------|---------------|--------------|
| **Rule application** | AI retrieves, interprets | Direct pattern matching |
| **Consistency** | ~50% variance | **0% variance** |
| **Context limits** | Yes - rules compete for space | No - rules are structured code |
| **Acronym tracking** | Forgets mid-document | State machine tracks all uses |
| **Speed** | Minutes per run | **< 1 second** |
| **Cost** | Per-token for everything | Zero (regex only) or minimal (AI enhancement) |

### Why 0% Variance?

Our rules are deterministic:

```yaml
# Example rule - always fires the same way
- id: em-dash-spacing
  pattern: ' — '           # Exact match
  replacement: '—'         # Exact replacement
  category: punctuation
  fix_type: SAFE
```

The same input **always** produces the same output because:
- Rules are evaluated in order
- Pattern matching is exact
- No probabilistic generation

### Where AI Adds Value

We use AI for **enhancement**, not core processing:

| Layer | Method | Purpose |
|-------|--------|---------|
| Base | Regex patterns | 85% of edits - deterministic |
| Enhanced | Claude Opus | 15% - context-dependent judgment |

AI handles:
- "Should this heading be imperative?" (context matters)
- "Is this acronym relevant to this document?" (semantic judgment)
- "Does this clarity edit preserve technical meaning?" (domain knowledge)

But the AI runs **after** deterministic rules, and only on flagged items.

## The 85/15 Split

From our analysis and Kim's experience:

> "15 to 20% where you really do want a person that understands the technology double checking"

Our classification:

| Fix Type | What It Means | Examples |
|----------|---------------|----------|
| **SAFE (85%)** | Auto-apply, no review | Punctuation, known style rules, spacing |
| **REVIEW (10%)** | Auto-apply, mark for verification | Heading conversions, acronym expansions |
| **QUERY (5%)** | Don't auto-apply, ask author | Technical term changes, clarity edits |

## Why the "Megaprompt" Wasn't Working

Kim's team developed a comprehensive prompt containing all editorial rules. It looked roughly like:

```
You are highly skilled editorial assistant...
Use the Cisco Style Guide and standard grammar rules...
[List of specific rules]
[Categorization requirements]
[Output format instructions]
```

### Why It Produced Inconsistent Results

**1. Attention Degradation**

LLMs use "attention" to decide what parts of the prompt matter for each decision. With a 5,000+ token prompt:

```
Early rules:    ████████████  (high attention)
Middle rules:   ██████        (moderate attention)
Late rules:     ███           (low attention)
```

Rules at the end of the prompt get less consistent application because the model's attention is spread thin.

**2. Order-Dependent Processing**

The AI processes content sequentially but its internal state changes:
- Run 1: Catches rule A at line 50, then forgets to check rule B at line 200
- Run 2: Different random seed → catches rule B first, misses rule A

This explains the "400 edits / 200 edits / 350 edits" variance.

**3. Temperature and Sampling**

Even at temperature=0, LLM outputs aren't fully deterministic:
- Token sampling has randomness
- Model internals vary by server load
- Caching affects different runs differently

**4. Context Window Competition**

Circuit has a finite context window. When you load:
- Full document (maybe 10,000 tokens)
- Megaprompt (maybe 3,000 tokens)
- Conversation history (growing each turn)

Something gets truncated. You never know what.

**5. Semantic vs. Syntactic Matching**

The prompt says: "Fix em dashes with spaces around them"

The AI **interprets** this semantically. It might:
- Miss some because they "look intentional"
- Fix some that shouldn't be fixed
- Apply the rule differently in lists vs. paragraphs

A regex pattern `' — '` → `'—'` fires the same way every time.

### Multi-Pass Made It Worse

Kim tried breaking into 8 separate prompts:
- Pass 1: Critical errors
- Pass 2: Add to previous edits
- Pass 3: Different objectives
- Pass 4: Combine all PDFs

**Result**: "Major failure" - the passes couldn't share state.

Each pass started fresh with no memory of what the previous pass found. When told "don't repeat changes from pass 1," the AI would:
- Miss the original issues
- Find different issues
- Conflict with pass 1's suggestions

## Why Not Just "Better Prompts"?

Kim spent months optimizing prompts in Circuit. The issue isn't the prompt - it's the architecture:

1. **Prompts can't create state** - LLMs are stateless per request
2. **Prompts can't guarantee coverage** - No way to ensure all rules run
3. **Prompts can't be versioned** - Hard to track what changed
4. **Prompts can't be tested** - No unit tests for a prompt

Our YAML rules:
- Track acronym state across full document
- Guarantee every rule evaluates every line
- Version controlled in Git
- Unit tested with known inputs/outputs

## Bottom Line

| Metric | Circuit | Our Pipeline |
|--------|---------|--------------|
| Consistency | 50%+ variance | **0% variance** |
| Processing time | Minutes | **< 1 second** |
| Cost per run | ~$0.10-0.50 | **$0** (regex) / ~$0.05 (with AI) |
| Scalability | Manual per-doc | Automated batch |
| Maintainability | Prompt tweaking | YAML config |

The fundamental insight: **Editorial rules are algorithms, not conversations**.

RAG is great for Q&A ("What does the style guide say about X?").
Rules engines are better for enforcement ("Apply the style guide to this document").

---

*For technical implementation details, see [learnings.md](learnings.md)*
