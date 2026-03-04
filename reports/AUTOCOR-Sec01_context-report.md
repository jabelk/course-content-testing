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
| Grammar & Punctuation | 91 |
| Cisco Style Guide | 22 |
| Acronyms | 9 |

## Changes by Category

### Cisco Style Guide (22 issues)

**Auto-fixable (SAFE)**:

| Line | Context | Change | Rationale |
|------|---------|--------|-----------|
| 107 | ...on, you\'ll ... `make sure` that all you...... | ~~make sure~~ → **ensure** | Use 'ensure' or 'verify' instead of '... |
| 107 | ...Depending on... `desired` option, you\...... | ~~desired~~ → **wanted** | Use 'want' or 'wanted' instead of 'de... |
| 418 | ...rmat. They d... `desired` outcomes in ...... | ~~desired~~ → **wanted** | Use 'want' or 'wanted' instead of 'de... |
| 422 | ...needed, then... `desired` state. Ansib...... | ~~desired~~ → **wanted** | Use 'want' or 'wanted' instead of 'de... |
| 462 | ...A. It `utilizes` YAML syntax ...... | ~~utilizes~~ → **uses** | Use 'use' instead of 'utilize' |
| 476 | ...ation by foc... `desired` end state ra...... | ~~desired~~ → **wanted** | Use 'want' or 'wanted' instead of 'de... |
| 486 | ...Track actual vs `desired` configuration... | ~~desired~~ → **wanted** | Use 'want' or 'wanted' instead of 'de... |
| 500 | ...file, you de... `desired` infrastructu...... | ~~desired~~ → **wanted** | Use 'want' or 'wanted' instead of 'de... |
| 517 | ...uctions, you... `desired` end state an...... | ~~desired~~ → **wanted** | Use 'want' or 'wanted' instead of 'de... |
| 579 | ...\# `desired` state defini...... | ~~desired~~ → **wanted** | Use 'want' or 'wanted' instead of 'de... |
| 605 | ...**, **campus... `datacenter` .tf**. Since...... | ~~datacenter~~ → **data center** | Use 'data center' (two words) instead... |
| 609 | ...astructure t... `desired` state. This ...... | ~~desired~~ → **wanted** | Use 'want' or 'wanted' instead of 'de... |
| 611 | ...rk infrastru... `desired` state.](medi...... | ~~desired~~ → **wanted** | Use 'want' or 'wanted' instead of 'de... |
| 627 | ...You describe... `desired` end state, T...... | ~~desired~~ → **wanted** | Use 'want' or 'wanted' instead of 'de... |
| 645 | ...focuses on d... `desired` end state of...... | ~~desired~~ → **wanted** | Use 'want' or 'wanted' instead of 'de... |
| ... | *7 more* | | |

### Acronyms (9 issues)

**Needs Review (REVIEW)**:

| Line | Context | Change | Rationale |
|------|---------|--------|-----------|
| 17 | ...te, when a m... `ACL` shown in the...... | ~~ACL~~ → **access control li...** | Acronym 'ACL' not expanded on first use |
| 39 | ...Netmiko or p... `SSH` to devices a...... | ~~SSH~~ → **Secure Shell (SSH)** | Acronym 'SSH' not expanded on first use |
| 53 | ...ract with th... `NETCONF` , RESTCONF, ...... | ~~NETCONF~~ → **Network Configura...** | Acronym 'NETCONF' not expanded on fir... |
| 53 | ...the device v... `RESTCONF` , or vendor-...... | ~~RESTCONF~~ → **REST-based Config...** | Acronym 'RESTCONF' not expanded on fi... |
| 219 | ...n a Cisco sw... `IOS` XE 15.x Soft...... | ~~IOS~~ → **Cisco IOS Software** | Acronym 'IOS' not expanded on first use |
| 224 | `MTU` 1500 bytes, ...... | ~~MTU~~ → **Maximum Transmiss...** | Acronym 'MTU' not expanded on first use |
| 251 | ...ata schema i... `YANG` models. Thes...... | ~~YANG~~ → **Yet Another Next ...** | Acronym 'YANG' not expanded on first use |
| 367 | ...se you need ... `VLAN` to 50 switch...... | ~~VLAN~~ → **virtual LAN (VLAN)** | Acronym 'VLAN' not expanded on first use |
| 875 | ...A cloud-managed `IT` platform fro...... | ~~IT~~ → **Information Techn...** | Acronym 'IT' not expanded on first use |

### Grammar & Punctuation (91 issues)

**Auto-fixable (SAFE)**:

| Line | Context | Change | Rationale |
|------|---------|--------|-----------|
| 104 | ...\| 1 `.  ` Multivendor ...... | ~~.  ~~ → **. ** | Use single space after period |
| 123 | ...r**s**:** A ... `built in` but requires...... | ~~built in~~ → **Change 'built in'...** | Hyphenate 'built-in' when used as a c... |
| 126 | ...\| 2 `.  ` Choosing too...... | ~~.  ~~ → **. ** | Use single space after period |
| 144 | ...\| 3 `.  ` Most effecti...... | ~~.  ~~ → **. ** | Use single space after period |
| 149 | ...1 `.  ` Begin with c...... | ~~.  ~~ → **. ** | Use single space after period |
| 151 | ...2 `.  ` Allow the te...... | ~~.  ~~ → **. ** | Use single space after period |
| 153 | ...3 `.  ` Minimize pro...... | ~~.  ~~ → **. ** | Use single space after period |
| 155 | ...4 `.  ` Build confid...... | ~~.  ~~ → **. ** | Use single space after period |
| 157 | ...5 `.  ` Demonstrate ...... | ~~.  ~~ → **. ** | Use single space after period |
| 334 | ...\| 4 `.  ` All these ch...... | ~~.  ~~ → **. ** | Use single space after period |
| 445 | ...\| 5 `.  ` These advant...... | ~~.  ~~ → **. ** | Use single space after period |
| 616 | ...\| 6 `.  ` While Ansibl...... | ~~.  ~~ → **. ** | Use single space after period |
| 818 | ...handle these... `out of the box` .... | ~~out of the box~~ → **Change 'out of th...** | Hyphenate 'out-of-the-box' when used ... |
| 1009 | ...1 `.  ` A, B, D... | ~~.  ~~ → **. ** | Use single space after period |
| 1013 | ...1 `.  ` B... | ~~.  ~~ → **. ** | Use single space after period |
| ... | *12 more* | | |

**Needs Review (REVIEW)**:

| Line | Context | Change | Rationale |
|------|---------|--------|-----------|
| 19 | `!` [ Network sh...... | ~~!~~ → **Consider using a ...** | removing exclamation point from techn... |
| 32 | `!` [Network set...... | ~~!~~ → **Consider using a ...** | removing exclamation point from techn... |
| 46 | `!` [Network set...... | ~~!~~ → **Consider using a ...** | removing exclamation point from techn... |
| 60 | `!` [](media/ima...... | ~~!~~ → **Consider using a ...** | removing exclamation point from techn... |
| 74 | `!` [](media/ima...... | ~~!~~ → **Consider using a ...** | removing exclamation point from techn... |
| 91 | `!` [Two network...... | ~~!~~ → **Consider using a ...** | removing exclamation point from techn... |
| 181 | `1` \. Which thr...... | ~~1~~ → **Spell out the num...** | spelling out numbers one through nine... |
| 225 | ...iability 255... `1` /255, rxload...... | ~~1~~ → **Spell out the num...** | spelling out numbers one through nine... |
| 225 | ...55, txload 1... `1` /255\... | ~~1~~ → **Spell out the num...** | spelling out numbers one through nine... |
| 226 | `5` minute input...... | ~~5~~ → **Spell out the num...** | spelling out numbers one through nine... |
| ... | *46 more* | | |

**Questions for Author (QUERY)**:

- **Line 148**: ` 1. ` Begin with c......
  - Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1008**: ` 1. ` A, B, D...
  - Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1012**: ` 1. ` B...
  - Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1016**: ` 1. ` C...
  - Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1022**: ` 1. ` B, E...
  - Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1026**: ` 1. ` C...
  - Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1030**: ` 1. ` B...
  - Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1034**: ` 1. ` A...
  - Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)

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
| 123 | 🟢 | GRAMMAR_COMPOUND_BUILT_IN | Hyphenate 'built-in' when used as a compound mo... |
| 126 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 144 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 148 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 149 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 151 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 153 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 155 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 157 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 181 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 219 | 🟡 | ACRONYM_FIRST_USE | Acronym 'IOS' not expanded on first use |
| 224 | 🟡 | ACRONYM_FIRST_USE | Acronym 'MTU' not expanded on first use |
| 225 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 225 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 226 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 226 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 227 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 227 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 238 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 238 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 239 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 239 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 240 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 240 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 243 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 251 | 🟡 | ACRONYM_FIRST_USE | Acronym 'YANG' not expanded on first use |
| 289 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 313 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 334 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 337 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 367 | 🟡 | ACRONYM_FIRST_USE | Acronym 'VLAN' not expanded on first use |
| 418 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 420 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 422 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 422 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 426 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 445 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 450 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 460 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 462 | 🟢 | TERM_UTILIZE | Use 'use' instead of 'utilize' |
| 476 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 486 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 500 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 517 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 579 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 594 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 605 | 🟢 | TERM_DATACENTER | Use 'data center' (two words) instead of 'datac... |
| 609 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 611 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 611 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 616 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 627 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 641 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 645 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 651 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 712 | 🟢 | TERM_ALLOWS_YOU_TO | Consider 'lets you' instead of 'allows you to' |
| 712 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 752 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 752 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 753 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 753 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 754 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 754 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 800 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 814 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 814 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 814 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 814 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 814 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 818 | 🟢 | GRAMMAR_COMPOUND_OUT_OF_THE_BOX | Hyphenate 'out-of-the-box' when used as a compo... |
| 822 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 822 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 836 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 850 | 🟢 | TERM_ALLOWS_YOU_TO | Consider 'lets you' instead of 'allows you to' |
| 871 | 🟡 | GRAMMAR_SERIAL_COMMA | Consider adding serial comma before 'and' in li... |
| 875 | 🟡 | ACRONYM_FIRST_USE | Acronym 'IT' not expanded on first use |
| 903 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 905 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 933 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 943 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 953 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 961 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 963 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 965 | 🟢 | TERM_UTILIZE | Use 'use' instead of 'utilize' |
| 975 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 983 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 985 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 995 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
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

*Generated by Course AI Editor on 2026-03-03 17:03*

**Fix Type Legend**:
- 🟢 **SAFE**: High-confidence fix, can be auto-applied
- 🟡 **REVIEW**: Applied fix, please verify
- 🔴 **QUERY**: Question for author, not auto-fixed