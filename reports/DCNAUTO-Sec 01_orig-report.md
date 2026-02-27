# Editorial Review Report: DCNAUTO-Sec 01_orig

**Quality Score**: 🔴 1.0/10 (Needs work - many unresolved issues)

| Property | Value |
|----------|-------|
| Word Count | 8,682 |
| Sections | 1 |
| Estimated Duration | 57m |
| Processing Time | 0.6s |

## Summary

**Total Issues**: 299

| Fix Type | Count | Description |
|----------|-------|-------------|
| SAFE | 132 | Auto-fixable with high confidence |
| REVIEW | 127 | Applied but needs human verification |
| QUERY | 40 | Questions for author - not auto-fixed |

### Issues by Category

| Category | Count |
|----------|-------|
| Chicago Manual | 246 |
| Acronyms | 42 |
| Cisco Style Guide | 11 |

## Changes by Category

### Cisco Style Guide (11 issues)

**Auto-fixable (SAFE)**:

| Line | Original | Suggested | Rationale |
|------|----------|-----------|-----------|
| 234 | `desired` | `wanted` | Use 'want' or 'wanted' instead of 'de... |
| 324 | `initiate` | `start` | Use 'start' or 'begin' instead of 'in... |
| 396 | `allows you to` | `lets you` | 'lets you' instead of 'allows you to' |
| 654 | `initiate` | `start` | Use 'start' or 'begin' instead of 'in... |
| 692 | `allows you to` | `lets you` | 'lets you' instead of 'allows you to' |
| 698 | `click on` | `click` | Use 'click' instead of 'click on' |
| 775 | `initiate` | `start` | Use 'start' or 'begin' instead of 'in... |
| 1079 | `leverage` | `use` | Use 'use' instead of 'leverage' |

**Needs Review (REVIEW)**:

| Line | Original | Suggested | Rationale |
|------|----------|-----------|-----------|
| 153 | `abort` | `Consider changing 'abort' t...` | using 'cancel' or 'terminate' instead... |
| 153 | `aborted` | `Consider changing 'abort' t...` | using 'cancel' or 'terminate' instead... |
| 153 | `aborted` | `Consider changing 'abort' t...` | using 'cancel' or 'terminate' instead... |

### Acronyms (42 issues)

**Needs Review (REVIEW)**:

| Line | Original | Suggested | Rationale |
|------|----------|-----------|-----------|
| 95 | `VXLAN` | `Virtual Extensible LAN (VXLAN)` | Acronym 'VXLAN' not expanded on first... |
| 115 | `DHCP` | `Dynamic Host Configuration ...` | Acronym 'DHCP' not expanded on first use |
| 169 | `MAC` | `Media Access Control (MAC)` | Acronym 'MAC' not expanded on first use |
| 304 | `SSH` | `Secure Shell (SSH)` | Acronym 'SSH' not expanded on first use |
| 308 | `CML` | `Cisco Modeling Labs (CML)` | Acronym 'CML' not expanded on first use |
| 357 | `MTU` | `Maximum Transmission Unit (...` | Acronym 'MTU' not expanded on first use |
| 480 | `PID` | `Product Identifier (PID)` | Acronym 'PID' not expanded on first use |
| 654 | `ZTP` | `Zero Touch Provisioning (ZTP)` | Acronym 'ZTP' not expanded on first use |
| 871 | `IT` | `Information Technology (IT)` | Acronym 'IT' not expanded on first use |
| 948 | `VLANs` | `virtual LAN (VLAN)` | Acronym 'VLAN' not expanded on first use |

**Questions for Author (QUERY)**:

- **Line 494**: Unknown acronym 'LSB' - please provide expansion or confirm intentional
- **Line 494**: Unknown acronym 'HPA' - please provide expansion or confirm intentional
- **Line 735**: Unknown acronym 'DEGKNA' - please provide expansion or confirm intentional
- **Line 741**: Unknown acronym 'FATAL' - please provide expansion or confirm intentional
- **Line 741**: Unknown acronym 'PMON' - please provide expansion or confirm intentional
- **Line 742**: Unknown acronym 'CRITICAL' - please provide expansion or confirm intentional
- **Line 743**: Unknown acronym 'ERROR' - please provide expansion or confirm intentional
- **Line 745**: Unknown acronym 'INFORMATION' - please provide expansion or confirm intentional
- *...and 24 more questions*

### Chicago Manual (246 issues)

**Auto-fixable (SAFE)**:

| Line | Original | Suggested | Rationale |
|------|----------|-----------|-----------|
| 40 | `--` | `—` | Use em dash (—) instead of double hyp... |
| 40 | `--` | `—` | Use em dash (—) instead of double hyp... |
| 67 | `--` | `—` | Use em dash (—) instead of double hyp... |
| 67 | `--` | `—` | Use em dash (—) instead of double hyp... |
| 77 | `--` | `—` | Use em dash (—) instead of double hyp... |
| 77 | `--` | `—` | Use em dash (—) instead of double hyp... |
| 81 | `--` | `—` | Use em dash (—) instead of double hyp... |
| 81 | `--` | `—` | Use em dash (—) instead of double hyp... |
| 157 | `.  ` | `. ` | Use single space after period |
| 159 | `.  ` | `. ` | Use single space after period |
| 167 | `.  ` | `. ` | Use single space after period |
| 169 | `.  ` | `. ` | Use single space after period |
| 171 | `.  ` | `. ` | Use single space after period |
| 210 | `--` | `—` | Use em dash (—) instead of double hyp... |
| 210 | `--` | `—` | Use em dash (—) instead of double hyp... |
| ... | *109 more* | | |

**Needs Review (REVIEW)**:

| Line | Original | Suggested | Rationale |
|------|----------|-----------|-----------|
| 17 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 36 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 40 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 61 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 67 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 77 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 81 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 101 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 109 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 133 | `1` | `Spell out the number (e.g.,...` | spelling out numbers one through nine... |
| ... | *104 more* | | |

**Questions for Author (QUERY)**:

- **Line 156**: Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1096**: Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1100**: Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1104**: Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1108**: Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1112**: Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1116**: Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 1120**: Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)

## Detailed Changes

*All issues sorted by line number for easy review:*

<details>
<summary>Click to expand all 299 issues</summary>

| Line | Type | Rule | Message |
|------|------|------|---------|
| 17 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 36 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 40 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 40 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 40 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 61 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 67 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 67 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 67 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 77 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 77 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 77 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 81 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 81 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 81 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 95 | 🟡 | ACRONYM_FIRST_USE | Acronym 'VXLAN' not expanded on first use |
| 101 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 109 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 115 | 🟡 | ACRONYM_FIRST_USE | Acronym 'DHCP' not expanded on first use |
| 133 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 147 | 🟡 | CMS_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 153 | 🟡 | TERM_ABORT | Consider using 'cancel' or 'terminate' instead ... |
| 153 | 🟡 | TERM_ABORT | Consider using 'cancel' or 'terminate' instead ... |
| 153 | 🟡 | TERM_ABORT | Consider using 'cancel' or 'terminate' instead ... |
| 153 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 156 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 157 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 159 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 167 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 169 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 169 | 🟡 | ACRONYM_FIRST_USE | Acronym 'MAC' not expanded on first use |
| 171 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 175 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 193 | 🟡 | CMS_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 210 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 210 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 223 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 223 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 234 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 237 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 237 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 253 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 295 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 304 | 🟡 | ACRONYM_FIRST_USE | Acronym 'SSH' not expanded on first use |
| 308 | 🟡 | ACRONYM_FIRST_USE | Acronym 'CML' not expanded on first use |
| 324 | 🟢 | TERM_INITIATE | Use 'start' or 'begin' instead of 'initiate' |
| 337 | 🟡 | CMS_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 341 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 357 | 🟡 | ACRONYM_FIRST_USE | Acronym 'MTU' not expanded on first use |
| 358 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 358 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 364 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 365 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 371 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 380 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 394 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 396 | 🟢 | TERM_ALLOWS_YOU_TO | Consider 'lets you' instead of 'allows you to' |
| 403 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 427 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 433 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 433 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 440 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 447 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 455 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 463 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 463 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 472 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 479 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 479 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 480 | 🟡 | ACRONYM_FIRST_USE | Acronym 'PID' not expanded on first use |
| 481 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 485 | 🟢 | PUNCT_MULTIPLE_QUESTION | Use single question mark |
| 488 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 494 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'LSB' - please provide expansio... |
| 494 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'HPA' - please provide expansio... |
| 497 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 497 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 499 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 503 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 503 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 503 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 503 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 503 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 503 | 🟢 | PUNCT_MULTIPLE_QUESTION | Use single question mark |
| 506 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 516 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 516 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 518 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 524 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 526 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 526 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 526 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 527 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 527 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 527 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 528 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 528 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 528 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 530 | 🟡 | CMS_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 530 | 🟡 | CMS_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 535 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 562 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 624 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 633 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 635 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 635 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 635 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 636 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 636 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 636 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 637 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 637 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 637 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 638 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 638 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 638 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 639 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 639 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 639 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 640 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 640 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 640 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 642 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 654 | 🟢 | TERM_INITIATE | Use 'start' or 'begin' instead of 'initiate' |
| 654 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 654 | 🟡 | ACRONYM_FIRST_USE | Acronym 'ZTP' not expanded on first use |
| 658 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 660 | 🟢 | CMS_COMPOUND_REAL_TIME | Hyphenate 'real-time' when used as a compound m... |
| 664 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 670 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 688 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 688 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 690 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 692 | 🟢 | TERM_ALLOWS_YOU_TO | Consider 'lets you' instead of 'allows you to' |
| 694 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 696 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 698 | 🟢 | TERM_CLICK_ON | Use 'click' instead of 'click on' |
| 700 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 702 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 711 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 713 | 🟡 | CMS_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 717 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 718 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 718 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 719 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 721 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 721 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 735 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 735 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 735 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'DEGKNA' - please provide expan... |
| 741 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 741 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 741 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'FATAL' - please provide expans... |
| 741 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'PMON' - please provide expansi... |
| 742 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 742 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 742 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'CRITICAL' - please provide exp... |
| 743 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 743 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 743 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'ERROR' - please provide expans... |
| 744 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 744 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 745 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 745 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 745 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'INFORMATION' - please provide ... |
| 747 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 775 | 🟢 | TERM_INITIATE | Use 'start' or 'begin' instead of 'initiate' |
| 775 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 780 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'CNTL' - please provide expansi... |
| 792 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 795 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 797 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'DHCPDISCOVER' - please provide... |
| 797 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'DHCPOFFER' - please provide ex... |
| 797 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'DHCPREQUEST' - please provide ... |
| 799 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'DHCPACK' - please provide expa... |
| 799 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'ACK' - please provide expansio... |
| 803 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 804 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 805 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 806 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 807 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 808 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 810 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 814 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'VDC' - please provide expansio... |
| 816 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 817 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 818 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 819 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 820 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 821 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 822 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 823 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 823 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 824 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 825 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 826 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 827 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 828 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'USER' - please provide expansi... |
| 829 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 833 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 834 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 835 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 836 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 837 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 838 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 839 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 840 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 841 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 842 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 843 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 844 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 845 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 847 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 848 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 853 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 856 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 856 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 858 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 858 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 860 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 863 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'RSA' - please provide expansio... |
| 869 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 869 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'REMOTE' - please provide expan... |
| 869 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'HOST' - please provide expansi... |
| 869 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'IDENTIFICATION' - please provi... |
| 869 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'HAS' - please provide expansio... |
| 869 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'CHANGED' - please provide expa... |
| 871 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 871 | 🟡 | ACRONYM_FIRST_USE | Acronym 'IT' not expanded on first use |
| 871 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'IS' - please provide expansion... |
| 871 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'POSSIBLE' - please provide exp... |
| 871 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'THAT' - please provide expansi... |
| 871 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'SOMEONE' - please provide expa... |
| 871 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'DOING' - please provide expans... |
| 871 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'SOMETHING' - please provide ex... |
| 871 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'NASTY' - please provide expans... |
| 872 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 875 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 879 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 898 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 915 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 916 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 917 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 919 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 919 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 921 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 923 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 926 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 926 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 940 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'GAKCCK' - please provide expan... |
| 946 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 948 | 🟡 | ACRONYM_FIRST_USE | Acronym 'VLAN' not expanded on first use |
| 958 | 🟡 | CMS_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 975 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'PING' - please provide expansi... |
| 979 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 980 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 981 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 981 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 982 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 982 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 987 | 🟡 | CMS_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 989 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 1013 | 🟡 | CMS_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 1019 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 1029 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 1039 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 1049 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 1049 | 🟡 | CMS_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 1059 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 1069 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 1079 | 🟢 | TERM_LEVERAGE | Use 'use' instead of 'leverage' |
| 1079 | 🟡 | CMS_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 1087 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'RSH' - please provide expansio... |
| 1096 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1097 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1100 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1101 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1104 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1105 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1108 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1109 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1111 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 1111 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 1111 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 1112 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1113 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1115 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 1115 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 1115 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 1116 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1117 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1120 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 1121 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1123 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1125 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1127 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1129 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1131 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1133 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |

</details>

---

*Generated by Course AI Editor on 2026-02-27 11:20*

**Fix Type Legend**:
- 🟢 **SAFE**: High-confidence fix, can be auto-applied
- 🟡 **REVIEW**: Applied fix, please verify
- 🔴 **QUERY**: Question for author, not auto-fixed