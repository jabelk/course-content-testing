# Editorial Review Report: Network Access for Non-Supplicant Devices_Sec 01_orig

**Quality Score**: 🔴 1.0/10 (Needs work - many unresolved issues)

| Property | Value |
|----------|-------|
| Word Count | 7,600 |
| Sections | 1 |
| Estimated Duration | 50m |
| Processing Time | 50.5s |

## Summary

**Total Issues**: 216

| Fix Type | Count | Description |
|----------|-------|-------------|
| SAFE | 82 | Auto-fixable with high confidence |
| REVIEW | 118 | Applied but needs human verification |
| QUERY | 16 | Questions for author - not auto-fixed |

### Issues by Category

| Category | Count |
|----------|-------|
| Grammar & Punctuation | 181 |
| Acronyms | 22 |
| Cisco Style Guide | 13 |

## Changes by Category

### Cisco Style Guide (13 issues)

**Auto-fixable (SAFE)**:

| Line | Original | Suggested | Rationale |
|------|----------|-----------|-----------|
| 135 | `initiate` | `start` | Use 'start' or 'begin' instead of 'in... |
| 207 | `e.g. ` | `for example, ` | Use 'for example' instead of 'e.g.' |
| 209 | `e.g. ` | `for example, ` | Use 'for example' instead of 'e.g.' |
| 213 | `e.g. ` | `for example, ` | Use 'for example' instead of 'e.g.' |
| 215 | `e.g. ` | `for example, ` | Use 'for example' instead of 'e.g.' |
| 259 | `e.g. ` | `for example, ` | Use 'for example' instead of 'e.g.' |
| 505 | `initiates` | `starts` | Use 'start' or 'begin' instead of 'in... |
| 511 | `initiates` | `starts` | Use 'start' or 'begin' instead of 'in... |
| 596 | `desired` | `wanted` | Use 'want' or 'wanted' instead of 'de... |
| 806 | `initiated` | `started` | Use 'start' or 'begin' instead of 'in... |
| 847 | `boot up` | `start` | Use 'start' or 'boot' instead of 'boo... |
| 1039 | `initiate` | `start` | Use 'start' or 'begin' instead of 'in... |

**Needs Review (REVIEW)**:

| Line | Original | Suggested | Rationale |
|------|----------|-----------|-----------|
| 346 | `Click Add` | `Add bold formatting to the ...` | GUI elements after 'click' should be ... |

### Acronyms (22 issues)

**Needs Review (REVIEW)**:

| Line | Original | Suggested | Rationale |
|------|----------|-----------|-----------|
| 5 | `VLANs` | `virtual LAN (VLAN)` | Acronym 'VLAN' not expanded on first use |
| 10 | `MAC` | `Media Access Control (MAC)` | Acronym 'MAC' not expanded on first use |
| 17 | `RADIUS` | `Remote Authentication Dial-...` | Acronym 'RADIUS' not expanded on firs... |
| 135 | `EAP` | `Extensible Authentication P...` | Acronym 'EAP' not expanded on first use |
| 400 | `DHCP` | `Dynamic Host Configuration ...` | Acronym 'DHCP' not expanded on first use |
| 497 | `ACL` | `access control list (ACL)` | Acronym 'ACL' not expanded on first use |

**Questions for Author (QUERY)**:

- **Line 5**: Unknown acronym 'IEEE' - please provide expansion or confirm intentional
- **Line 126**: Unknown acronym 'IPP' - please provide expansion or confirm intentional
- **Line 126**: Unknown acronym 'LPR' - please provide expansion or confirm intentional
- **Line 141**: Unknown acronym 'PAP' - please provide expansion or confirm intentional
- **Line 330**: Unknown acronym 'FQ' - please provide expansion or confirm intentional
- **Line 332**: Unknown acronym 'DATA' - please provide expansion or confirm intentional
- **Line 362**: Unknown acronym 'WLAN' - please provide expansion or confirm intentional
- **Line 473**: Unknown acronym 'LAN' - please provide expansion or confirm intentional
- *...and 8 more questions*

### Grammar & Punctuation (181 issues)

**Auto-fixable (SAFE)**:

| Line | Original | Suggested | Rationale |
|------|----------|-----------|-----------|
| 135 | `.  ` | `. ` | Use single space after period |
| 135 | `.                          ...` | `. ` | Use single space after period |
| 137 | `.                          ...` | `. ` | Use single space after period |
| 139 | `.                          ...` | `. ` | Use single space after period |
| 141 | `.  ` | `. ` | Use single space after period |
| 141 | `.                          ...` | `. ` | Use single space after period |
| 143 | `.                          ...` | `. ` | Use single space after period |
| 145 | `.                          ...` | `. ` | Use single space after period |
| 147 | `.                          ...` | `. ` | Use single space after period |
| 149 | `.  ` | `. ` | Use single space after period |
| 149 | `.       ` | `. ` | Use single space after period |
| 153 | `.                          ...` | `. ` | Use single space after period |
| 155 | `.                         ` | `. ` | Use single space after period |
| 157 | `.                          ...` | `. ` | Use single space after period |
| 159 | `.  ` | `. ` | Use single space after period |
| ... | *55 more* | | |

**Needs Review (REVIEW)**:

| Line | Original | Suggested | Rationale |
|------|----------|-----------|-----------|
| 10 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 14 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 17 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 17 | `to securely onboard` | `Consider moving the adverb ...` | avoiding split infinitives when possible |
| 45 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 60 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 70 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 87 | `2` | `Spell out the number (e.g.,...` | spelling out numbers one through nine... |
| 106 | `1` | `Spell out the number (e.g.,...` | spelling out numbers one through nine... |
| 114 | `3` | `Spell out the number (e.g.,...` | spelling out numbers one through nine... |
| ... | *101 more* | | |

## Detailed Changes

*All issues sorted by line number for easy review:*

<details>
<summary>Click to expand all 216 issues</summary>

| Line | Type | Rule | Message |
|------|------|------|---------|
| 5 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'IEEE' - please provide expansi... |
| 5 | 🟡 | ACRONYM_FIRST_USE | Acronym 'VLAN' not expanded on first use |
| 10 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 10 | 🟡 | ACRONYM_FIRST_USE | Acronym 'MAC' not expanded on first use |
| 14 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 17 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 17 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 17 | 🟡 | ACRONYM_FIRST_USE | Acronym 'RADIUS' not expanded on first use |
| 45 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 60 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 70 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 87 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 106 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 114 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 122 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 124 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 126 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'IPP' - please provide expansio... |
| 126 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'LPR' - please provide expansio... |
| 130 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 135 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 135 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 135 | 🟢 | TERM_INITIATE | Use 'start' or 'begin' instead of 'initiate' |
| 135 | 🟡 | ACRONYM_FIRST_USE | Acronym 'EAP' not expanded on first use |
| 137 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 139 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 141 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 141 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 141 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'PAP' - please provide expansio... |
| 143 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 143 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 143 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 145 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 147 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 147 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 149 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 149 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 153 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 155 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 157 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 159 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 159 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 163 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 167 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 177 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 187 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 189 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 191 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 195 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 203 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 207 | 🟢 | TERM_EG | Use 'for example' instead of 'e.g.' |
| 207 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 209 | 🟢 | TERM_EG | Use 'for example' instead of 'e.g.' |
| 213 | 🟢 | TERM_EG | Use 'for example' instead of 'e.g.' |
| 213 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 215 | 🟢 | TERM_EG | Use 'for example' instead of 'e.g.' |
| 220 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 252 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 259 | 🟢 | TERM_EG | Use 'for example' instead of 'e.g.' |
| 266 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 280 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 306 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 329 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 330 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'FQ' - please provide expansion... |
| 331 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 332 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'DATA' - please provide expansi... |
| 340 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 343 | 🟡 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 344 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 346 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 346 | 🟡 | GUI_BOLD_CLICK | GUI elements after 'click' should be bold |
| 348 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 360 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 362 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'WLAN' - please provide expansi... |
| 363 | 🟡 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 364 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 364 | 🟡 | GRAMMAR_AMPERSAND_IN_PROSE | Use 'and' instead of '&' in prose text |
| 366 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 368 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 368 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 376 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 380 | 🟡 | GRAMMAR_AMPERSAND_IN_PROSE | Use 'and' instead of '&' in prose text |
| 381 | 🟡 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 382 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 384 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 386 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 388 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 392 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 398 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 400 | 🟡 | ACRONYM_FIRST_USE | Acronym 'DHCP' not expanded on first use |
| 408 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 418 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 418 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 440 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 442 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 444 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 447 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 459 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 473 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'LAN' - please provide expansio... |
| 478 | 🟡 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 479 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 479 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'SSID' - please provide expansi... |
| 481 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 483 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 483 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'WLC' - please provide expansio... |
| 485 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 487 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 489 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 491 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 497 | 🟡 | ACRONYM_FIRST_USE | Acronym 'ACL' not expanded on first use |
| 501 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 503 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 505 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 505 | 🟢 | TERM_INITIATE | Use 'start' or 'begin' instead of 'initiate' |
| 507 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 509 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 511 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 511 | 🟢 | TERM_INITIATE | Use 'start' or 'begin' instead of 'initiate' |
| 513 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 515 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 517 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 519 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 525 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 541 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 549 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 557 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 596 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 617 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 623 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 623 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 632 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 638 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 642 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 652 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 682 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 694 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 703 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 707 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 707 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'CX' - please provide expansion... |
| 709 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 711 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 724 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 733 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 735 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 741 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 746 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'USER' - please provide expansi... |
| 746 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'ATTRIBUTES' - please provide e... |
| 749 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'ACSACL' - please provide expan... |
| 757 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 757 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 760 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 760 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 760 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 760 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 760 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 764 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 768 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 779 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 779 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 802 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 806 | 🟢 | TERM_INITIATE | Use 'start' or 'begin' instead of 'initiate' |
| 810 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 812 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 818 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 818 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 820 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 823 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 824 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'UNKNOWN' - please provide expa... |
| 826 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 828 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 834 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 837 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 840 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 847 | 🟢 | TERM_BOOT_UP | Use 'start' or 'boot' instead of 'boot up' |
| 847 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 851 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 855 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 879 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 887 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 889 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 920 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 928 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 955 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 969 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 999 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 999 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 1001 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 1003 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 1003 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'BYPASS' - please provide expan... |
| 1007 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 1009 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 1015 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 1019 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 1029 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 1029 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 1039 | 🟢 | TERM_INITIATE | Use 'start' or 'begin' instead of 'initiate' |
| 1039 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 1049 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 1063 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1068 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1070 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1072 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1076 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1081 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1083 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1085 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1089 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1094 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1096 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1098 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1102 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1104 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1106 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1108 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1110 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1112 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1114 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |

</details>

---

*Generated by Course AI Editor on 2026-03-02 21:48*

**Fix Type Legend**:
- 🟢 **SAFE**: High-confidence fix, can be auto-applied
- 🟡 **REVIEW**: Applied fix, please verify
- 🔴 **QUERY**: Question for author, not auto-fixed