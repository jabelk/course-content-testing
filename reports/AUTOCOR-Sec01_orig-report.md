# Editorial Review Report: AUTOCOR-Sec01_orig

**Quality Score**: 🔴 1.0/10 (Needs work - many unresolved issues)

| Property | Value |
|----------|-------|
| Word Count | 7,157 |
| Sections | 1 |
| Estimated Duration | 47m |
| Processing Time | 0.6s |

## Summary

**Total Issues**: 122

| Fix Type | Count | Description |
|----------|-------|-------------|
| SAFE | 49 | Auto-fixable with high confidence |
| REVIEW | 65 | Applied but needs human verification |
| QUERY | 8 | Questions for author - not auto-fixed |

### Issues by Category

| Category | Count |
|----------|-------|
| Chicago Manual | 91 |
| Cisco Style Guide | 22 |
| Acronyms | 9 |

## Changes by Category

### Cisco Style Guide (22 issues)

**Auto-fixable (SAFE)**:

| Line | Original | Suggested | Rationale |
|------|----------|-----------|-----------|
| 107 | `make sure` | `ensure` | Use 'ensure' or 'verify' instead of '... |
| 107 | `desired` | `wanted` | Use 'want' or 'wanted' instead of 'de... |
| 418 | `desired` | `wanted` | Use 'want' or 'wanted' instead of 'de... |
| 422 | `desired` | `wanted` | Use 'want' or 'wanted' instead of 'de... |
| 462 | `utilizes` | `uses` | Use 'use' instead of 'utilize' |
| 476 | `desired` | `wanted` | Use 'want' or 'wanted' instead of 'de... |
| 486 | `desired` | `wanted` | Use 'want' or 'wanted' instead of 'de... |
| 500 | `desired` | `wanted` | Use 'want' or 'wanted' instead of 'de... |
| 517 | `desired` | `wanted` | Use 'want' or 'wanted' instead of 'de... |
| 579 | `desired` | `wanted` | Use 'want' or 'wanted' instead of 'de... |
| 605 | `datacenter` | `data center` | Use 'data center' (two words) instead... |
| 609 | `desired` | `wanted` | Use 'want' or 'wanted' instead of 'de... |
| 611 | `desired` | `wanted` | Use 'want' or 'wanted' instead of 'de... |
| 627 | `desired` | `wanted` | Use 'want' or 'wanted' instead of 'de... |
| 645 | `desired` | `wanted` | Use 'want' or 'wanted' instead of 'de... |
| ... | *7 more* | | |

### Acronyms (9 issues)

**Needs Review (REVIEW)**:

| Line | Original | Suggested | Rationale |
|------|----------|-----------|-----------|
| 17 | `ACL` | `access control list (ACL)` | Acronym 'ACL' not expanded on first use |
| 39 | `SSH` | `Secure Shell (SSH)` | Acronym 'SSH' not expanded on first use |
| 53 | `NETCONF` | `Network Configuration Proto...` | Acronym 'NETCONF' not expanded on fir... |
| 53 | `RESTCONF` | `REST-based Configuration Pr...` | Acronym 'RESTCONF' not expanded on fi... |
| 219 | `IOS` | `Cisco IOS Software` | Acronym 'IOS' not expanded on first use |
| 224 | `MTU` | `Maximum Transmission Unit (...` | Acronym 'MTU' not expanded on first use |
| 251 | `YANG` | `Yet Another Next Generation...` | Acronym 'YANG' not expanded on first use |
| 367 | `VLAN` | `virtual LAN (VLAN)` | Acronym 'VLAN' not expanded on first use |
| 875 | `IT` | `Information Technology (IT)` | Acronym 'IT' not expanded on first use |

### Chicago Manual (91 issues)

**Auto-fixable (SAFE)**:

| Line | Original | Suggested | Rationale |
|------|----------|-----------|-----------|
| 104 | `.  ` | `. ` | Use single space after period |
| 123 | `built in` | `Change 'built in' to 'built...` | Hyphenate 'built-in' when used as a c... |
| 126 | `.  ` | `. ` | Use single space after period |
| 144 | `.  ` | `. ` | Use single space after period |
| 149 | `.  ` | `. ` | Use single space after period |
| 151 | `.  ` | `. ` | Use single space after period |
| 153 | `.  ` | `. ` | Use single space after period |
| 155 | `.  ` | `. ` | Use single space after period |
| 157 | `.  ` | `. ` | Use single space after period |
| 334 | `.  ` | `. ` | Use single space after period |
| 445 | `.  ` | `. ` | Use single space after period |
| 616 | `.  ` | `. ` | Use single space after period |
| 818 | `out of the box` | `Change 'out of the box' to ...` | Hyphenate 'out-of-the-box' when used ... |
| 1009 | `.  ` | `. ` | Use single space after period |
| 1013 | `.  ` | `. ` | Use single space after period |
| ... | *12 more* | | |

**Needs Review (REVIEW)**:

| Line | Original | Suggested | Rationale |
|------|----------|-----------|-----------|
| 19 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 32 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 46 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 60 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 74 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 91 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 181 | `1` | `Spell out the number (e.g.,...` | spelling out numbers one through nine... |
| 225 | `1` | `Spell out the number (e.g.,...` | spelling out numbers one through nine... |
| 225 | `1` | `Spell out the number (e.g.,...` | spelling out numbers one through nine... |
| 226 | `5` | `Spell out the number (e.g.,...` | spelling out numbers one through nine... |
| ... | *46 more* | | |

**Questions for Author (QUERY)**:

- **Line 148**: Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1008**: Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1012**: Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1016**: Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1022**: Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1026**: Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1030**: Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1034**: Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)

## Detailed Changes

*All issues sorted by line number for easy review:*

<details>
<summary>Click to expand all 122 issues</summary>

| Line | Type | Rule | Message |
|------|------|------|---------|
| 17 | 🟡 | ACRONYM_FIRST_USE | Acronym 'ACL' not expanded on first use |
| 19 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 32 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 39 | 🟡 | ACRONYM_FIRST_USE | Acronym 'SSH' not expanded on first use |
| 46 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 53 | 🟡 | ACRONYM_FIRST_USE | Acronym 'NETCONF' not expanded on first use |
| 53 | 🟡 | ACRONYM_FIRST_USE | Acronym 'RESTCONF' not expanded on first use |
| 60 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 74 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 91 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 104 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 107 | 🟢 | TERM_MAKE_SURE | Use 'ensure' or 'verify' instead of 'make sure' |
| 107 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 123 | 🟢 | CMS_COMPOUND_BUILT_IN | Hyphenate 'built-in' when used as a compound mo... |
| 126 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 144 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 148 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 149 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 151 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 153 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 155 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 157 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 181 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 219 | 🟡 | ACRONYM_FIRST_USE | Acronym 'IOS' not expanded on first use |
| 224 | 🟡 | ACRONYM_FIRST_USE | Acronym 'MTU' not expanded on first use |
| 225 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 225 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 226 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 226 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 227 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 227 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 238 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 238 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 239 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 239 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 240 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 240 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 243 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 251 | 🟡 | ACRONYM_FIRST_USE | Acronym 'YANG' not expanded on first use |
| 289 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 313 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 334 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 337 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 367 | 🟡 | ACRONYM_FIRST_USE | Acronym 'VLAN' not expanded on first use |
| 418 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 420 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 422 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 422 | 🟡 | CMS_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 426 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 445 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 450 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 460 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 462 | 🟢 | TERM_UTILIZE | Use 'use' instead of 'utilize' |
| 476 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 486 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 500 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 517 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 579 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 594 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 605 | 🟢 | TERM_DATACENTER | Use 'data center' (two words) instead of 'datac... |
| 609 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 611 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 611 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 616 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 627 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 641 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 645 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 651 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 712 | 🟢 | TERM_ALLOWS_YOU_TO | Consider 'lets you' instead of 'allows you to' |
| 712 | 🟡 | CMS_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 752 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 752 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 753 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 753 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 754 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 754 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 800 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 814 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 814 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 814 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 814 | 🟡 | CMS_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 814 | 🟡 | CMS_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 818 | 🟢 | CMS_COMPOUND_OUT_OF_THE_BOX | Hyphenate 'out-of-the-box' when used as a compo... |
| 822 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 822 | 🟡 | CMS_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 836 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 850 | 🟢 | TERM_ALLOWS_YOU_TO | Consider 'lets you' instead of 'allows you to' |
| 871 | 🟡 | CMS_SERIAL_COMMA | Consider adding serial comma before 'and' in li... |
| 875 | 🟡 | ACRONYM_FIRST_USE | Acronym 'IT' not expanded on first use |
| 903 | 🟡 | CMS_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 905 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 933 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 943 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 953 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 961 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 963 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 965 | 🟢 | TERM_UTILIZE | Use 'use' instead of 'utilize' |
| 975 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 983 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 985 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 995 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 1008 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1009 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1012 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1013 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1016 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1017 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1019 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1022 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1023 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1026 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1027 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1030 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1031 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1034 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1035 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1037 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1039 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1041 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1043 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1045 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1047 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |

</details>

---

*Generated by Course AI Editor on 2026-02-27 11:20*

**Fix Type Legend**:
- 🟢 **SAFE**: High-confidence fix, can be auto-applied
- 🟡 **REVIEW**: Applied fix, please verify
- 🔴 **QUERY**: Question for author, not auto-fixed