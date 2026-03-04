# Editorial Review Report: AUTOCOR-Sec01_orig

**Quality Score**: 🔴 1.0/10 (Needs work - many unresolved issues)

| Property | Value |
|----------|-------|
| Word Count | 7,163 |
| Sections | 1 |
| Estimated Duration | 47m |
| Processing Time | 1.3s |

## Summary

**Total Issues**: 111

| Fix Type | Count | Description |
|----------|-------|-------------|
| SAFE | 49 | Auto-fixable with high confidence |
| REVIEW | 54 | Applied but needs human verification |
| QUERY | 8 | Questions for author - not auto-fixed |

### Issues by Category

| Category | Count |
|----------|-------|
| Grammar & Punctuation | 80 |
| Cisco Style Guide | 22 |
| Acronyms | 9 |

## Changes by Category

### Cisco Style Guide (22 issues)

**Auto-fixable (SAFE)**:

| Line | Context | Change | Rationale |
|------|---------|--------|-----------|
| 108 | ...on, you\'ll ... `make sure` that all you...... | ~~make sure~~ → **ensure** | Use 'ensure' or 'verify' instead of '... |
| 108 | ...Depending on... `desired` option, you\...... | ~~desired~~ → **wanted** | Use 'want' or 'wanted' instead of 'de... |
| 422 | ...rmat. They d... `desired` outcomes in ...... | ~~desired~~ → **wanted** | Use 'want' or 'wanted' instead of 'de... |
| 426 | ...needed, then... `desired` state. Ansib...... | ~~desired~~ → **wanted** | Use 'want' or 'wanted' instead of 'de... |
| 467 | ...A. It `utilizes` YAML syntax ...... | ~~utilizes~~ → **uses** | Use 'use' instead of 'utilize' |
| 481 | ...ation by foc... `desired` end state ra...... | ~~desired~~ → **wanted** | Use 'want' or 'wanted' instead of 'de... |
| 491 | ...Track actual vs `desired` configuration... | ~~desired~~ → **wanted** | Use 'want' or 'wanted' instead of 'de... |
| 505 | ...file, you de... `desired` infrastructu...... | ~~desired~~ → **wanted** | Use 'want' or 'wanted' instead of 'de... |
| 522 | ...uctions, you... `desired` end state an...... | ~~desired~~ → **wanted** | Use 'want' or 'wanted' instead of 'de... |
| 584 | ...\# `desired` state defini...... | ~~desired~~ → **wanted** | Use 'want' or 'wanted' instead of 'de... |
| 610 | ...**, **campus... `datacenter` .tf**. Since...... | ~~datacenter~~ → **data center** | Use 'data center' (two words) instead... |
| 614 | ...astructure t... `desired` state. This ...... | ~~desired~~ → **wanted** | Use 'want' or 'wanted' instead of 'de... |
| 616 | ...rk infrastru... `desired` state.](medi...... | ~~desired~~ → **wanted** | Use 'want' or 'wanted' instead of 'de... |
| 633 | ...You describe... `desired` end state, T...... | ~~desired~~ → **wanted** | Use 'want' or 'wanted' instead of 'de... |
| 651 | ...focuses on d... `desired` end state of...... | ~~desired~~ → **wanted** | Use 'want' or 'wanted' instead of 'de... |
| ... | *7 more* | | |

### Acronyms (9 issues)

**Needs Review (REVIEW)**:

| Line | Context | Change | Rationale |
|------|---------|--------|-----------|
| 17 | ...te, when a m... `ACL` shown in the...... | ~~ACL~~ → **access control li...** | Acronym 'ACL' not expanded on first use |
| 39 | ...Netmiko or p... `SSH` to devices a...... | ~~SSH~~ → **Secure Shell (SSH)** | Acronym 'SSH' not expanded on first use |
| 53 | ...ract with th... `NETCONF` , RESTCONF, ...... | ~~NETCONF~~ → **Network Configura...** | Acronym 'NETCONF' not expanded on fir... |
| 53 | ...the device v... `RESTCONF` , or vendor-...... | ~~RESTCONF~~ → **REST-based Config...** | Acronym 'RESTCONF' not expanded on fi... |
| 222 | ...n a Cisco sw... `IOS` XE 15.x Soft...... | ~~IOS~~ → **Cisco IOS Software** | Acronym 'IOS' not expanded on first use |
| 227 | `MTU` 1500 bytes, ...... | ~~MTU~~ → **Maximum Transmiss...** | Acronym 'MTU' not expanded on first use |
| 254 | ...ata schema i... `YANG` models. Thes...... | ~~YANG~~ → **Yet Another Next ...** | Acronym 'YANG' not expanded on first use |
| 371 | ...se you need ... `VLAN` to 50 switch...... | ~~VLAN~~ → **virtual LAN (VLAN)** | Acronym 'VLAN' not expanded on first use |
| 881 | ...A cloud-managed `IT` platform fro...... | ~~IT~~ → **Information Techn...** | Acronym 'IT' not expanded on first use |

### Grammar & Punctuation (80 issues)

**Auto-fixable (SAFE)**:

| Line | Context | Change | Rationale |
|------|---------|--------|-----------|
| 104 | ...\| 1 `.  ` Multivendor ...... | ~~.  ~~ → **. ** | Use single space after period |
| 124 | ...r**s**:** A ... `built in` but requires...... | ~~built in~~ → **Change 'built in'...** | Hyphenate 'built-in' when used as a c... |
| 127 | ...\| 2 `.  ` Choosing too...... | ~~.  ~~ → **. ** | Use single space after period |
| 146 | ...\| 3 `.  ` Most effecti...... | ~~.  ~~ → **. ** | Use single space after period |
| 152 | ...1 `.  ` Begin with c...... | ~~.  ~~ → **. ** | Use single space after period |
| 154 | ...2 `.  ` Allow the te...... | ~~.  ~~ → **. ** | Use single space after period |
| 156 | ...3 `.  ` Minimize pro...... | ~~.  ~~ → **. ** | Use single space after period |
| 158 | ...4 `.  ` Build confid...... | ~~.  ~~ → **. ** | Use single space after period |
| 160 | ...5 `.  ` Demonstrate ...... | ~~.  ~~ → **. ** | Use single space after period |
| 337 | ...\| 4 `.  ` All these ch...... | ~~.  ~~ → **. ** | Use single space after period |
| 449 | ...\| 5 `.  ` These advant...... | ~~.  ~~ → **. ** | Use single space after period |
| 621 | ...\| 6 `.  ` While Ansibl...... | ~~.  ~~ → **. ** | Use single space after period |
| 824 | ...handle these... `out of the box` .... | ~~out of the box~~ → **Change 'out of th...** | Hyphenate 'out-of-the-box' when used ... |
| 1015 | ...1 `.  ` A, B, D... | ~~.  ~~ → **. ** | Use single space after period |
| 1019 | ...1 `.  ` B... | ~~.  ~~ → **. ** | Use single space after period |
| ... | *12 more* | | |

**Needs Review (REVIEW)**:

| Line | Context | Change | Rationale |
|------|---------|--------|-----------|
| 184 | `1` \. Which thr...... | ~~1~~ → **Spell out the num...** | spelling out numbers one through nine... |
| 228 | ...iability 255... `1` /255, rxload...... | ~~1~~ → **Spell out the num...** | spelling out numbers one through nine... |
| 228 | ...55, txload 1... `1` /255\... | ~~1~~ → **Spell out the num...** | spelling out numbers one through nine... |
| 229 | `5` minute input...... | ~~5~~ → **Spell out the num...** | spelling out numbers one through nine... |
| 229 | ...nput rate 10... `2` packets/sec\... | ~~2~~ → **Spell out the num...** | spelling out numbers one through nine... |
| 230 | `5` minute outpu...... | ~~5~~ → **Spell out the num...** | spelling out numbers one through nine... |
| 230 | ...tput rate 20... `3` packets/sec\... | ~~3~~ → **Spell out the num...** | spelling out numbers one through nine... |
| 241 | ...iability 255... `1` /255, rxload...... | ~~1~~ → **Spell out the num...** | spelling out numbers one through nine... |
| 241 | ...55, txload 1... `1` /255\... | ~~1~~ → **Spell out the num...** | spelling out numbers one through nine... |
| 242 | `5` minute input...... | ~~5~~ → **Spell out the num...** | spelling out numbers one through nine... |
| ... | *35 more* | | |

**Questions for Author (QUERY)**:

- **Line 151**: ` 1. ` Begin with c......
  - Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1014**: ` 1. ` A, B, D...
  - Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1018**: ` 1. ` B...
  - Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1022**: ` 1. ` C...
  - Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1028**: ` 1. ` B, E...
  - Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1032**: ` 1. ` C...
  - Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1036**: ` 1. ` B...
  - Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1040**: ` 1. ` A...
  - Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)

## Detailed Changes

*All issues sorted by line number for easy review:*

<details>
<summary>Click to expand all 111 issues</summary>

| Line | Type | Rule | Message |
|------|------|------|---------|
| 17 | 🟡 | ACRONYM_FIRST_USE | Acronym 'ACL' not expanded on first use |
| 39 | 🟡 | ACRONYM_FIRST_USE | Acronym 'SSH' not expanded on first use |
| 53 | 🟡 | ACRONYM_FIRST_USE | Acronym 'NETCONF' not expanded on first use |
| 53 | 🟡 | ACRONYM_FIRST_USE | Acronym 'RESTCONF' not expanded on first use |
| 104 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 108 | 🟢 | TERM_MAKE_SURE | Use 'ensure' or 'verify' instead of 'make sure' |
| 108 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 124 | 🟢 | GRAMMAR_COMPOUND_BUILT_IN | Hyphenate 'built-in' when used as a compound mo... |
| 127 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 146 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 151 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 152 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 154 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 156 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 158 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 160 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 184 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 222 | 🟡 | ACRONYM_FIRST_USE | Acronym 'IOS' not expanded on first use |
| 227 | 🟡 | ACRONYM_FIRST_USE | Acronym 'MTU' not expanded on first use |
| 228 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 228 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 229 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 229 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 230 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 230 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 241 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 241 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 242 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 242 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 243 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 243 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 246 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 254 | 🟡 | ACRONYM_FIRST_USE | Acronym 'YANG' not expanded on first use |
| 337 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 341 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 371 | 🟡 | ACRONYM_FIRST_USE | Acronym 'VLAN' not expanded on first use |
| 422 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 426 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 426 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 449 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 455 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 465 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 467 | 🟢 | TERM_UTILIZE | Use 'use' instead of 'utilize' |
| 481 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 491 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 505 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 522 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 584 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 599 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 610 | 🟢 | TERM_DATACENTER | Use 'data center' (two words) instead of 'datac... |
| 614 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 616 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 621 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 633 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 647 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 651 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 657 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 718 | 🟢 | TERM_ALLOWS_YOU_TO | Consider 'lets you' instead of 'allows you to' |
| 718 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 758 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 758 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 759 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 759 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 760 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 760 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 806 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 820 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 820 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 820 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 820 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 820 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 824 | 🟢 | GRAMMAR_COMPOUND_OUT_OF_THE_BOX | Hyphenate 'out-of-the-box' when used as a compo... |
| 828 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 828 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 842 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 856 | 🟢 | TERM_ALLOWS_YOU_TO | Consider 'lets you' instead of 'allows you to' |
| 877 | 🟡 | GRAMMAR_SERIAL_COMMA | Consider adding serial comma before 'and' in li... |
| 881 | 🟡 | ACRONYM_FIRST_USE | Acronym 'IT' not expanded on first use |
| 909 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 911 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 939 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 949 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 959 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 967 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 969 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 971 | 🟢 | TERM_UTILIZE | Use 'use' instead of 'utilize' |
| 981 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 989 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 991 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 1001 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 1014 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1015 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1018 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1019 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1022 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1023 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1025 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1028 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1029 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1032 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1033 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1036 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1037 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1040 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1041 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1043 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1045 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1047 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1049 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1051 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1053 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |

</details>

---

*Generated by Course AI Editor on 2026-03-04 15:15*

**Fix Type Legend**:
- 🟢 **SAFE**: High-confidence fix, can be auto-applied
- 🟡 **REVIEW**: Applied fix, please verify
- 🔴 **QUERY**: Question for author, not auto-fixed