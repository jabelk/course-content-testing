# Editorial Review Report: DCNAUTO-Sec 01_orig

**Quality Score**: 🔴 1.0/10 (Needs work - many unresolved issues)

| Property | Value |
|----------|-------|
| Word Count | 8,682 |
| Sections | 1 |
| Estimated Duration | 57m |
| Processing Time | 0.6s |

## Summary

**Total Issues**: 220

| Fix Type | Count | Description |
|----------|-------|-------------|
| SAFE | 131 | Auto-fixable with high confidence |
| REVIEW | 32 | Applied but needs human verification |
| QUERY | 57 | Questions for author - not auto-fixed |

### Issues by Category

| Category | Count |
|----------|-------|
| Chicago Manual | 157 |
| Acronyms | 52 |
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

### Acronyms (52 issues)

**Needs Review (REVIEW)**:

| Line | Original | Suggested | Rationale |
|------|----------|-----------|-----------|
| 115 | `DHCP` | `Dynamic Host Configuration ...` | Acronym 'DHCP' not expanded on first use |
| 304 | `SSH` | `Secure Shell (SSH)` | Acronym 'SSH' not expanded on first use |
| 948 | `VLANs` | `virtual LAN (VLAN)` | Acronym 'VLAN' not expanded on first use |

**Questions for Author (QUERY)**:

- **Line 36**: Unknown acronym 'DCNAUTO' - please provide expansion or confirm intentional
- **Line 95**: Unknown acronym 'VXLAN' - please provide expansion or confirm intentional
- **Line 169**: Unknown acronym 'MAC' - please provide expansion or confirm intentional
- **Line 308**: Unknown acronym 'CML' - please provide expansion or confirm intentional
- **Line 357**: Unknown acronym 'MTU' - please provide expansion or confirm intentional
- **Line 357**: Unknown acronym 'BW' - please provide expansion or confirm intentional
- **Line 357**: Unknown acronym 'DLY' - please provide expansion or confirm intentional
- **Line 359**: Unknown acronym 'ARPA' - please provide expansion or confirm intentional
- *...and 41 more questions*

### Chicago Manual (157 issues)

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
| ... | *108 more* | | |

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
| 153 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| ... | *16 more* | | |

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
<summary>Click to expand all 220 issues</summary>

| Line | Type | Rule | Message |
|------|------|------|---------|
| 17 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 36 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 36 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'DCNAUTO' - please provide expa... |
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
| 95 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'VXLAN' - please provide expans... |
| 101 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 109 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 115 | 🟡 | ACRONYM_FIRST_USE | Acronym 'DHCP' not expanded on first use |
| 153 | 🟡 | TERM_ABORT | Consider using 'cancel' or 'terminate' instead ... |
| 153 | 🟡 | TERM_ABORT | Consider using 'cancel' or 'terminate' instead ... |
| 153 | 🟡 | TERM_ABORT | Consider using 'cancel' or 'terminate' instead ... |
| 153 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 156 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 157 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 159 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 167 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 169 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 169 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'MAC' - please provide expansio... |
| 171 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 210 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 210 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 223 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 223 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 234 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 237 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 237 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 295 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 304 | 🟡 | ACRONYM_FIRST_USE | Acronym 'SSH' not expanded on first use |
| 308 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'CML' - please provide expansio... |
| 324 | 🟢 | TERM_INITIATE | Use 'start' or 'begin' instead of 'initiate' |
| 357 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'MTU' - please provide expansio... |
| 357 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'BW' - please provide expansion... |
| 357 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'DLY' - please provide expansio... |
| 359 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'ARPA' - please provide expansi... |
| 396 | 🟢 | TERM_ALLOWS_YOU_TO | Consider 'lets you' instead of 'allows you to' |
| 401 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'INFRA' - please provide expans... |
| 401 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'SERVER' - please provide expan... |
| 427 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 433 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 433 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 447 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 455 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 463 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 463 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 478 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'UTC' - please provide expansio... |
| 479 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 480 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'PID' - please provide expansio... |
| 485 | 🟢 | PUNCT_MULTIPLE_QUESTION | Use single question mark |
| 494 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'LSB' - please provide expansio... |
| 494 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'HPA' - please provide expansio... |
| 497 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 503 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 503 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 503 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 503 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 503 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 503 | 🟢 | PUNCT_MULTIPLE_QUESTION | Use single question mark |
| 516 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 516 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 526 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 526 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 527 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 527 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 528 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 528 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 535 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 562 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 624 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 635 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 635 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 636 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 636 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 637 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 637 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 638 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 638 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 639 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 639 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 640 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 640 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 654 | 🟢 | TERM_INITIATE | Use 'start' or 'begin' instead of 'initiate' |
| 654 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'ZTP' - please provide expansio... |
| 670 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 688 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 688 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 692 | 🟢 | TERM_ALLOWS_YOU_TO | Consider 'lets you' instead of 'allows you to' |
| 694 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 694 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'LOGIN' - please provide expans... |
| 698 | 🟢 | TERM_CLICK_ON | Use 'click' instead of 'click on' |
| 700 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 702 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'OPEN' - please provide expansi... |
| 702 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'CONSOLE' - please provide expa... |
| 717 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 718 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 719 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 721 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 735 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'DEGKNA' - please provide expan... |
| 741 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'FATAL' - please provide expans... |
| 741 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'PMON' - please provide expansi... |
| 742 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'CRITICAL' - please provide exp... |
| 743 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'ERROR' - please provide expans... |
| 745 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'INFORMATION' - please provide ... |
| 775 | 🟢 | TERM_INITIATE | Use 'start' or 'begin' instead of 'initiate' |
| 780 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'CNTL' - please provide expansi... |
| 792 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
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
| 871 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'IT' - please provide expansion... |
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
| 940 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'GAKCCK' - please provide expan... |
| 948 | 🟡 | ACRONYM_FIRST_USE | Acronym 'VLAN' not expanded on first use |
| 975 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'PING' - please provide expansi... |
| 981 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 981 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 1079 | 🟢 | TERM_LEVERAGE | Use 'use' instead of 'leverage' |
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

*Generated by Course AI Editor on 2026-02-27 08:18*

**Fix Type Legend**:
- 🟢 **SAFE**: High-confidence fix, can be auto-applied
- 🟡 **REVIEW**: Applied fix, please verify
- 🔴 **QUERY**: Question for author, not auto-fixed