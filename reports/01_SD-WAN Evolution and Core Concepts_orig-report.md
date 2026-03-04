# Editorial Review Report: 01_SD-WAN Evolution and Core Concepts_orig

**Quality Score**: 🔴 1.0/10 (Needs work - many unresolved issues)

| Property | Value |
|----------|-------|
| Word Count | 15,309 |
| Sections | 1 |
| Estimated Duration | 1h42m |
| Processing Time | 2.0s |

## Summary

**Total Issues**: 251

| Fix Type | Count | Description |
|----------|-------|-------------|
| SAFE | 94 | Auto-fixable with high confidence |
| REVIEW | 66 | Applied but needs human verification |
| QUERY | 91 | Questions for author - not auto-fixed |

### Issues by Category

| Category | Count |
|----------|-------|
| Grammar & Punctuation | 148 |
| Acronyms | 83 |
| Cisco Style Guide | 20 |

## Changes by Category

### Cisco Style Guide (20 issues)

**Auto-fixable (SAFE)**:

| Line | Context | Change | Rationale |
|------|---------|--------|-----------|
| 13 | ...© 2025 `Cisco Systems` , Inc.... | ~~Cisco Systems~~ → **Cisco** | Use 'Cisco' instead of 'Cisco Systems' |
| 15 | ...© 2025 `Cisco Systems` , Inc.... | ~~Cisco Systems~~ → **Cisco** | Use 'Cisco' instead of 'Cisco Systems' |
| 21 | `Cisco Systems` , Inc.\... | ~~Cisco Systems~~ → **Cisco** | Use 'Cisco' instead of 'Cisco Systems' |
| 21 | `Cisco Systems` (USA) Pte. L...... | ~~Cisco Systems~~ → **Cisco** | Use 'Cisco' instead of 'Cisco Systems' |
| 21 | ...stems (USA) ... `Cisco Systems` Internationa...... | ~~Cisco Systems~~ → **Cisco** | Use 'Cisco' instead of 'Cisco Systems' |
| 41 | ...e changing t... `blacklist` /whitelist a...... | ~~blacklist~~ → **blocked list** | Use 'blocked list' instead of 'blackl... |
| 41 | ...terms such a... `whitelist` and master/s...... | ~~whitelist~~ → **allowed list** | Use 'allowed list' instead of 'whitel... |
| 157 | ...why your com... `leverage` more afforda...... | ~~leverage~~ → **use** | Use 'use' instead of 'leverage' |
| 397 | ...[A. Its capa... `leverage` lower-cost i...... | ~~leverage~~ → **use** | Use 'use' instead of 'leverage' |
| 577 | ...[The overlay... `leverages` virtual tunn...... | ~~leverages~~ → **uses** | Use 'use' instead of 'leverage' |
| 643 | ...nks, but you... `utilized` MPLS link av...... | ~~utilized~~ → **used** | Use 'use' instead of 'utilize' |
| 655 | ...yption keys ... `etc.` ) and lock s...... | ~~etc.~~ → **and so on** | Use 'and so on' instead of 'etc.' |
| 697 | ...ysical infra... `leveraged` by intellige...... | ~~leveraged~~ → **used** | Use 'use' instead of 'leverage' |
| 853 | ...for large-sc... `allows you to` think about ...... | ~~allows you to~~ → **lets you** | 'lets you' instead of 'allows you to' |
| 931 | ...ty and multi... `allows you to` logically is...... | ~~allows you to~~ → **lets you** | 'lets you' instead of 'allows you to' |
| ... | *3 more* | | |

**Needs Review (REVIEW)**:

| Line | Context | Change | Rationale |
|------|---------|--------|-----------|
| 41 | ...blacklist/wh... `master` /slave to mo...... | ~~master~~ → **Consider using 'p...** | Use 'primary/secondary' or 'active/st... |
| 41 | ...ist/whitelis... `slave` to more appr...... | ~~slave~~ → **Consider using 'p...** | Use 'primary/secondary' or 'active/st... |

### Acronyms (83 issues)

**Needs Review (REVIEW)**:

| Line | Context | Change | Rationale |
|------|---------|--------|-----------|
| 3 | ...SD- `WAN` Evolution an...... | ~~WAN~~ → **Wide Area Network...** | Acronym 'WAN' not expanded on first use |
| 111 | ...cture built ... `MPLS` circuits and...... | ~~MPLS~~ → **Multiprotocol Lab...** | Acronym 'MPLS' not expanded on first use |
| 323 | ...doption and ... `IT` infrastructu...... | ~~IT~~ → **Information Techn...** | Acronym 'IT' not expanded on first use |
| 489 | ...e Internet p... `NAT` devices, and...... | ~~NAT~~ → **Network Address T...** | Acronym 'NAT' not expanded on first use |
| 766 | ...ted green li... `TLOC` /Key Exchang...... | ~~TLOC~~ → **Transport Locatio...** | Acronym 'TLOC' not expanded on first use |
| 927 | ...ng this with... `VLANs` and ACLs acr...... | ~~VLANs~~ → **virtual LAN (VLAN)** | Acronym 'VLAN' not expanded on first use |
| 927 | ...th tradition... `ACLs` across many ...... | ~~ACLs~~ → **access control li...** | Acronym 'ACL' not expanded on first use |
| 1008 | ...pes indicate... `TLS` control tunn...... | ~~TLS~~ → **Transport Layer S...** | Acronym 'TLS' not expanded on first use |

**Questions for Author (QUERY)**:

- **Line 3**: `SD` -WAN Evoluti......
  - Unknown acronym 'SD' - please provide expansion or confirm intentional
- **Line 21**: ...co Systems I... `BV` Amsterdam,\...
  - Unknown acronym 'BV' - please provide expansion or confirm intentional
- **Line 22**: ...San Jose, `CA`
  - Unknown acronym 'CA' - please provide expansion or confirm intentional
- **Line 28**: `DISCLAIMER` WARRANTY: TH......
  - Unknown acronym 'DISCLAIMER' - please provide expansion or confirm intentional
- **Line 28**: ...DISCLAIMER `WARRANTY` : THIS CONTE......
  - Unknown acronym 'WARRANTY' - please provide expansion or confirm intentional
- **Line 28**: ...DISCLAIMER W... `THIS` CONTENT IS B......
  - Unknown acronym 'THIS' - please provide expansion or confirm intentional
- **Line 28**: ...ISCLAIMER WA... `CONTENT` IS BEING PRO......
  - Unknown acronym 'CONTENT' - please provide expansion or confirm intentional
- **Line 28**: ...R WARRANTY: ... `IS` BEING PROVID......
  - Unknown acronym 'IS' - please provide expansion or confirm intentional
- *...and 67 more questions*

### Grammar & Punctuation (148 issues)

**Auto-fixable (SAFE)**:

| Line | Context | Change | Rationale |
|------|---------|--------|-----------|
| 24 | ...ww.cisco.com... `                 ...` | `                 ...` (question) | Remove trailing whitespace |
| 24 | ...www.cisco.co... `.                ...` | ~~.                ...~~ → **. ** | Use single space after period |
| 26 | ...ny other com... `                 ...` | `                 ...` (question) | Remove trailing whitespace |
| 28 | ...to the discl... `                 ...` | `                 ...` (question) | Remove trailing whitespace |
| 28 | ...t to the dis... `.                ...` | ~~.                ...~~ → **. ** | Use single space after period |
| 47 | ...1 `.  ` **Course eva...... | ~~.  ~~ → **. ** | Use single space after period |
| 49 | ...2 `.  ` **Digital ki...... | ~~.  ~~ → **. ** | Use single space after period |
| 73 | ...cking Modern... `--` A Strategic ...... | ~~--~~ → **—** | Use em dash (—) instead of double hyp... |
| 99 | ...- `   ` | `   ` (question) | Remove trailing whitespace |
| 100 | ...- `   ` | `   ` (question) | Remove trailing whitespace |
| 101 | ...- `   ` | `   ` (question) | Remove trailing whitespace |
| 126 | ...- `   ` | `   ` (question) | Remove trailing whitespace |
| 127 | ...- `   ` | `   ` (question) | Remove trailing whitespace |
| 128 | ...- `   ` | `   ` (question) | Remove trailing whitespace |
| 567 | ...hed the unde... `--` your physica...... | ~~--~~ → **—** | Use em dash (—) instead of double hyp... |
| ... | *61 more* | | |

**Needs Review (REVIEW)**:

| Line | Context | Change | Rationale |
|------|---------|--------|-----------|
| 59 | ...ution and Co... `1` ](#_Toc21568...... | ~~1~~ → **Spell out the num...** | spelling out numbers one through nine... |
| 61 | ...ions and Mod... `3` ](#_Toc21568...... | ~~3~~ → **Spell out the num...** | spelling out numbers one through nine... |
| 107 | ...it\'s time t... `!` ](#_Toc49677...... | ~~!~~ → **Consider using a ...** | removing exclamation point from techn... |
| 183 | ...tions makes ... `to quickly adapt` to changing ...... | ~~to quickly adapt~~ → **Consider moving t...** | avoiding split infinitives when possible |
| 191 | ...advantage. T... `to rapidly deploy` new sites or...... | ~~to rapidly deploy~~ → **Consider moving t...** | avoiding split infinitives when possible |
| 225 | ...t:** Without... `to intelligently ...` and prioriti...... | ~~to intelligently ...~~ → **Consider moving t...** | avoiding split infinitives when possible |
| 237 | ...tection at e... `However, deployin...` individual s...... | ~~However, deployin...~~ → **Add comma before ...** | adding serial comma before 'and' in l... |
| 245 | ...[A. The requ... `to manually confi...` every networ...... | ~~to manually confi...~~ → **Consider moving t...** | avoiding split infinitives when possible |
| 247 | ...[B. The inab... `to dynamically pr...` business-cri...... | ~~to dynamically pr...~~ → **Consider moving t...** | avoiding split infinitives when possible |
| 271 | ...[Consider ` which ` pain points ...... | ~~ which ~~ → **If this is a rest...** | using 'that' for restrictive clauses ... |
| ... | *46 more* | | |

**Questions for Author (QUERY)**:

- **Line 46**: ` 1. ` **Course eva......
  - Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1405**: ` 1. `
  - Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1412**: ` 1. `
  - Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1416**: ` 1. `
  - Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1422**: ` 1. `
  - Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1426**: ` 1. `
  - Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1430**: ` 1. `
  - Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1436**: ` 1. `
  - Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- *...and 8 more questions*

## Detailed Changes

*All issues sorted by line number for easy review:*

<details>
<summary>Click to expand all 251 issues</summary>

| Line | Type | Rule | Message |
|------|------|------|---------|
| 3 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'SD' - please provide expansion... |
| 3 | 🟡 | ACRONYM_FIRST_USE | Acronym 'WAN' not expanded on first use |
| 13 | 🟢 | TERM_CISCO_SYSTEMS | Use 'Cisco' instead of 'Cisco Systems' |
| 15 | 🟢 | TERM_CISCO_SYSTEMS | Use 'Cisco' instead of 'Cisco Systems' |
| 21 | 🟢 | TERM_CISCO_SYSTEMS | Use 'Cisco' instead of 'Cisco Systems' |
| 21 | 🟢 | TERM_CISCO_SYSTEMS | Use 'Cisco' instead of 'Cisco Systems' |
| 21 | 🟢 | TERM_CISCO_SYSTEMS | Use 'Cisco' instead of 'Cisco Systems' |
| 21 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'BV' - please provide expansion... |
| 22 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'CA' - please provide expansion... |
| 24 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 24 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 26 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 28 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 28 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'DISCLAIMER' - please provide e... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'WARRANTY' - please provide exp... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'THIS' - please provide expansi... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'CONTENT' - please provide expa... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'IS' - please provide expansion... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'BEING' - please provide expans... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'PROVIDED' - please provide exp... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'AS' - please provide expansion... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'AND' - please provide expansio... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'SUCH' - please provide expansi... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'MAY' - please provide expansio... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'INCLUDE' - please provide expa... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'TYPOGRAPHICAL' - please provid... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'GRAPHICS' - please provide exp... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'OR' - please provide expansion... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'FORMATTING' - please provide e... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'ERRORS' - please provide expan... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'CISCO' - please provide expans... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'MAKES' - please provide expans... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'YOU' - please provide expansio... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'RECEIVE' - please provide expa... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'NO' - please provide expansion... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'WARRANTIES' - please provide e... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'IN' - please provide expansion... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'CONNECTION' - please provide e... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'WITH' - please provide expansi... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'THE' - please provide expansio... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'HEREUNDER' - please provide ex... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'EXPRESS' - please provide expa... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'IMPLIED' - please provide expa... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'STATUTORY' - please provide ex... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'ANY' - please provide expansio... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'OTHER' - please provide expans... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'PROVISION' - please provide ex... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'OF' - please provide expansion... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'COMMUNICATION' - please provid... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'BETWEEN' - please provide expa... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'SPECIFICALLY' - please provide... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'DISCLAIMS' - please provide ex... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'ALL' - please provide expansio... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'INCLUDING' - please provide ex... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'MERCHANTABILITY' - please prov... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'NON' - please provide expansio... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'INFRINGEMENT' - please provide... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'FITNESS' - please provide expa... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'FOR' - please provide expansio... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'PARTICULAR' - please provide e... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'PURPOSE' - please provide expa... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'ARISING' - please provide expa... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'FROM' - please provide expansi... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'COURSE' - please provide expan... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'DEALING' - please provide expa... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'USAGE' - please provide expans... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'TRADE' - please provide expans... |
| 28 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'PRACTICE' - please provide exp... |
| 41 | 🟢 | TERM_BLACKLIST | Use 'blocked list' instead of 'blacklist' (bias... |
| 41 | 🟢 | TERM_WHITELIST | Use 'allowed list' instead of 'whitelist' (bias... |
| 41 | 🟡 | TERM_MASTER_SLAVE | Use 'primary/secondary' or 'active/standby' ins... |
| 41 | 🟡 | TERM_MASTER_SLAVE | Use 'primary/secondary' or 'active/standby' ins... |
| 46 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 47 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 49 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 59 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 61 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 73 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 99 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 100 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 101 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 107 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 111 | 🟡 | ACRONYM_FIRST_USE | Acronym 'MPLS' not expanded on first use |
| 126 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 127 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 128 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 157 | 🟢 | TERM_LEVERAGE | Use 'use' instead of 'leverage' |
| 157 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'CFO' - please provide expansio... |
| 183 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 191 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 219 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'DATA' - please provide expansi... |
| 221 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'CRM' - please provide expansio... |
| 225 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 237 | 🟡 | GRAMMAR_SERIAL_COMMA | Consider adding serial comma before 'and' in li... |
| 245 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 247 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 266 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'CEO' - please provide expansio... |
| 271 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 302 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'INET' - please provide expansi... |
| 304 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'LTE' - please provide expansio... |
| 323 | 🟡 | ACRONYM_FIRST_USE | Acronym 'IT' not expanded on first use |
| 331 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 331 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 343 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'DIA' - please provide expansio... |
| 351 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'CISO' - please provide expansi... |
| 363 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'HQ' - please provide expansion... |
| 383 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 395 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 397 | 🟢 | TERM_LEVERAGE | Use 'use' instead of 'leverage' |
| 401 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 452 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'CIO' - please provide expansio... |
| 457 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'ROI' - please provide expansio... |
| 489 | 🟡 | ACRONYM_FIRST_USE | Acronym 'NAT' not expanded on first use |
| 493 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'VPN' - please provide expansio... |
| 501 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 544 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 546 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 548 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'GPS' - please provide expansio... |
| 567 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 577 | 🟢 | TERM_LEVERAGE | Use 'use' instead of 'leverage' |
| 585 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 643 | 🟢 | TERM_UTILIZE | Use 'use' instead of 'utilize' |
| 655 | 🟢 | TERM_ETC | Use 'and so on' instead of 'etc.' |
| 697 | 🟢 | TERM_LEVERAGE | Use 'use' instead of 'leverage' |
| 708 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 729 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 752 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 754 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 756 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 760 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 762 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 764 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 766 | 🟡 | ACRONYM_FIRST_USE | Acronym 'TLOC' not expanded on first use |
| 768 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 770 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 772 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 776 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 778 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 780 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 810 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 811 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 821 | 🟡 | GRAMMAR_SERIAL_COMMA | Consider adding serial comma before 'and' in li... |
| 827 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 827 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 853 | 🟢 | TERM_ALLOWS_YOU_TO | Consider 'lets you' instead of 'allows you to' |
| 879 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 903 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 927 | 🟡 | ACRONYM_FIRST_USE | Acronym 'VLAN' not expanded on first use |
| 927 | 🟡 | ACRONYM_FIRST_USE | Acronym 'ACL' not expanded on first use |
| 929 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 931 | 🟢 | TERM_ALLOWS_YOU_TO | Consider 'lets you' instead of 'allows you to' |
| 931 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 937 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 953 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 967 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 968 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 969 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 980 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 1008 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'DTLS' - please provide expansi... |
| 1008 | 🟡 | ACRONYM_FIRST_USE | Acronym 'TLS' not expanded on first use |
| 1016 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 1032 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 1034 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 1038 | 🟢 | TERM_ALLOWS_YOU_TO | Consider 'lets you' instead of 'allows you to' |
| 1051 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 1111 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 1124 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 1129 | 🟡 | GRAMMAR_AMPERSAND_IN_PROSE | Use 'and' instead of '&' in prose text |
| 1138 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 1139 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 1151 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 1153 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 1155 | 🟢 | TERM_ALLOWS_YOU_TO | Consider 'lets you' instead of 'allows you to' |
| 1174 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 1174 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 1268 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 1290 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 1294 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 1304 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 1305 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 1306 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 1307 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 1309 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 1317 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 1318 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 1319 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 1320 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 1332 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'NOT' - please provide expansio... |
| 1382 | 🟢 | TERM_LEVERAGE | Use 'use' instead of 'leverage' |
| 1405 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1406 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 1406 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1407 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 1407 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1409 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'CD' - please provide expansion... |
| 1412 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1413 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 1413 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1416 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1417 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 1417 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1422 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1423 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 1423 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1426 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1427 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 1427 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1430 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1431 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 1431 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1436 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1437 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 1437 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1440 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1441 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 1441 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1446 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1447 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 1447 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1450 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1451 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 1451 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1454 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1455 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 1455 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1460 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1461 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 1461 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1464 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1465 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 1465 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1468 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1469 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 1469 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1474 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1475 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 1475 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1476 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 1476 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1477 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 1477 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1478 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 1478 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1479 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 1479 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1480 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 1480 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1481 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 1481 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1483 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'ADBCDAB' - please provide expa... |

</details>

---

*Generated by Course AI Editor on 2026-03-04 15:14*

**Fix Type Legend**:
- 🟢 **SAFE**: High-confidence fix, can be auto-applied
- 🟡 **REVIEW**: Applied fix, please verify
- 🔴 **QUERY**: Question for author, not auto-fixed