# Editorial Review Report: DCNAUTO-Sec 01_orig

**Quality Score**: 🔴 1.0/10 (Needs work - many unresolved issues)

| Property | Value |
|----------|-------|
| Word Count | 8,700 |
| Sections | 1 |
| Estimated Duration | 58m |
| Processing Time | 27.9s |

## Summary

**Total Issues**: 195

| Fix Type | Count | Description |
|----------|-------|-------------|
| SAFE | 120 | Auto-fixable with high confidence |
| REVIEW | 26 | Applied but needs human verification |
| QUERY | 49 | Questions for author - not auto-fixed |

### Issues by Category

| Category | Count |
|----------|-------|
| Chicago Manual | 132 |
| Acronyms | 52 |
| Cisco Style Guide | 11 |

## Changes by Category

### Cisco Style Guide (11 issues)

**Auto-fixable (SAFE)**:

| Line | Original | Suggested | Rationale |
|------|----------|-----------|-----------|
| 238 | `desired` | `wanted` | Use 'want' or 'wanted' instead of 'de... |
| 328 | `initiate` | `start` | Use 'start' or 'begin' instead of 'in... |
| 400 | `allows you to` | `lets you` | 'lets you' instead of 'allows you to' |
| 659 | `initiate` | `start` | Use 'start' or 'begin' instead of 'in... |
| 697 | `allows you to` | `lets you` | 'lets you' instead of 'allows you to' |
| 703 | `click on` | `click` | Use 'click' instead of 'click on' |
| 780 | `initiate` | `start` | Use 'start' or 'begin' instead of 'in... |
| 1086 | `leverage` | `use` | Use 'use' instead of 'leverage' |

**Needs Review (REVIEW)**:

| Line | Original | Suggested | Rationale |
|------|----------|-----------|-----------|
| 157 | `abort` | `Consider changing 'abort' t...` | using 'cancel' or 'terminate' instead... |
| 157 | `aborted` | `Consider changing 'abort' t...` | using 'cancel' or 'terminate' instead... |
| 157 | `aborted` | `Consider changing 'abort' t...` | using 'cancel' or 'terminate' instead... |

### Acronyms (52 issues)

**Needs Review (REVIEW)**:

| Line | Original | Suggested | Rationale |
|------|----------|-----------|-----------|
| 119 | `DHCP` | `Dynamic Host Configuration ...` | Acronym 'DHCP' not expanded on first use |
| 308 | `SSH` | `Secure Shell (SSH)` | Acronym 'SSH' not expanded on first use |
| 955 | `VLANs` | `virtual LAN (VLAN)` | Acronym 'VLAN' not expanded on first use |

**Questions for Author (QUERY)**:

- **Line 36**: Unknown acronym 'DCNAUTO' - please provide expansion or confirm intentional
- **Line 99**: Unknown acronym 'VXLAN' - please provide expansion or confirm intentional
- **Line 173**: Unknown acronym 'MAC' - please provide expansion or confirm intentional
- **Line 312**: Unknown acronym 'CML' - please provide expansion or confirm intentional
- **Line 361**: Unknown acronym 'MTU' - please provide expansion or confirm intentional
- **Line 361**: Unknown acronym 'BW' - please provide expansion or confirm intentional
- **Line 361**: Unknown acronym 'DLY' - please provide expansion or confirm intentional
- **Line 363**: Unknown acronym 'ARPA' - please provide expansion or confirm intentional
- *...and 41 more questions*

### Chicago Manual (132 issues)

**Auto-fixable (SAFE)**:

| Line | Original | Suggested | Rationale |
|------|----------|-----------|-----------|
| 40 | ` ` | `` | Remove trailing whitespace |
| 161 | `.  ` | `. ` | Use single space after period |
| 163 | `.  ` | `. ` | Use single space after period |
| 171 | `.  ` | `. ` | Use single space after period |
| 173 | `.  ` | `. ` | Use single space after period |
| 175 | `.  ` | `. ` | Use single space after period |
| 214 | `--` | `—` | Use em dash (—) instead of double hyp... |
| 214 | `--` | `—` | Use em dash (—) instead of double hyp... |
| 227 | `--` | `—` | Use em dash (—) instead of double hyp... |
| 227 | `--` | `—` | Use em dash (—) instead of double hyp... |
| 241 | `--` | `—` | Use em dash (—) instead of double hyp... |
| 241 | `--` | `—` | Use em dash (—) instead of double hyp... |
| 431 | `:` | `Add space after colon` | Add space after colon |
| 437 | `:` | `Add space after colon` | Add space after colon |
| 437 | `:` | `Add space after colon` | Add space after colon |
| ... | *97 more* | | |

**Needs Review (REVIEW)**:

| Line | Original | Suggested | Rationale |
|------|----------|-----------|-----------|
| 17 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 36 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 62 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 105 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 113 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 157 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 299 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 539 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 566 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 699 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| ... | *10 more* | | |

## Detailed Changes

*All issues sorted by line number for easy review:*

<details>
<summary>Click to expand all 195 issues</summary>

| Line | Type | Rule | Message |
|------|------|------|---------|
| 17 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 36 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 36 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'DCNAUTO' - please provide expa... |
| 40 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 62 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 99 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'VXLAN' - please provide expans... |
| 105 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 113 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 119 | 🟡 | ACRONYM_FIRST_USE | Acronym 'DHCP' not expanded on first use |
| 157 | 🟡 | TERM_ABORT | Consider using 'cancel' or 'terminate' instead ... |
| 157 | 🟡 | TERM_ABORT | Consider using 'cancel' or 'terminate' instead ... |
| 157 | 🟡 | TERM_ABORT | Consider using 'cancel' or 'terminate' instead ... |
| 157 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 161 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 163 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 171 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 173 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 173 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'MAC' - please provide expansio... |
| 175 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 214 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 214 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 227 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 227 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 238 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 241 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 241 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 299 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 308 | 🟡 | ACRONYM_FIRST_USE | Acronym 'SSH' not expanded on first use |
| 312 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'CML' - please provide expansio... |
| 328 | 🟢 | TERM_INITIATE | Use 'start' or 'begin' instead of 'initiate' |
| 361 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'MTU' - please provide expansio... |
| 361 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'BW' - please provide expansion... |
| 361 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'DLY' - please provide expansio... |
| 363 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'ARPA' - please provide expansi... |
| 400 | 🟢 | TERM_ALLOWS_YOU_TO | Consider 'lets you' instead of 'allows you to' |
| 405 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'INFRA' - please provide expans... |
| 405 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'SERVER' - please provide expan... |
| 431 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 437 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 437 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 451 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 459 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 467 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 467 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 482 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'UTC' - please provide expansio... |
| 483 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 484 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'PID' - please provide expansio... |
| 489 | 🟢 | PUNCT_MULTIPLE_QUESTION | Use single question mark |
| 498 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'LSB' - please provide expansio... |
| 498 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'HPA' - please provide expansio... |
| 501 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 507 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 507 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 507 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 507 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 507 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 507 | 🟢 | PUNCT_MULTIPLE_QUESTION | Use single question mark |
| 520 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 520 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 530 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 530 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 531 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 531 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 532 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 532 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 539 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 566 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 628 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 640 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 640 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 641 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 641 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 642 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 642 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 643 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 643 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 644 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 644 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 645 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 645 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 659 | 🟢 | TERM_INITIATE | Use 'start' or 'begin' instead of 'initiate' |
| 659 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'ZTP' - please provide expansio... |
| 675 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 693 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 693 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 697 | 🟢 | TERM_ALLOWS_YOU_TO | Consider 'lets you' instead of 'allows you to' |
| 699 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 699 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'LOGIN' - please provide expans... |
| 703 | 🟢 | TERM_CLICK_ON | Use 'click' instead of 'click on' |
| 705 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 707 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'OPEN' - please provide expansi... |
| 707 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'CONSOLE' - please provide expa... |
| 722 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 723 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 724 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 726 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 740 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'DEGKNA' - please provide expan... |
| 746 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'FATAL' - please provide expans... |
| 746 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'PMON' - please provide expansi... |
| 747 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'CRITICAL' - please provide exp... |
| 748 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'ERROR' - please provide expans... |
| 750 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'INFORMATION' - please provide ... |
| 780 | 🟢 | TERM_INITIATE | Use 'start' or 'begin' instead of 'initiate' |
| 785 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'CNTL' - please provide expansi... |
| 797 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 803 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'DHCPDISCOVER' - please provide... |
| 803 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'DHCPOFFER' - please provide ex... |
| 803 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'DHCPREQUEST' - please provide ... |
| 805 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'DHCPACK' - please provide expa... |
| 805 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'ACK' - please provide expansio... |
| 809 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 810 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 811 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 812 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 813 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 814 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 820 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'VDC' - please provide expansio... |
| 822 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 823 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 824 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 825 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 826 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 827 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 828 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 829 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 829 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 830 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 831 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 832 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 833 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 834 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'USER' - please provide expansi... |
| 839 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 840 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 841 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 842 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 843 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 844 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 845 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 846 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 847 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 848 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 849 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 850 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 851 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 853 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 854 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 862 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 862 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 864 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 864 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 866 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 870 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'RSA' - please provide expansio... |
| 876 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 876 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'REMOTE' - please provide expan... |
| 876 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'HOST' - please provide expansi... |
| 876 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'IDENTIFICATION' - please provi... |
| 876 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'HAS' - please provide expansio... |
| 876 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'CHANGED' - please provide expa... |
| 878 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 878 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'IT' - please provide expansion... |
| 878 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'IS' - please provide expansion... |
| 878 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'POSSIBLE' - please provide exp... |
| 878 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'THAT' - please provide expansi... |
| 878 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'SOMEONE' - please provide expa... |
| 878 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'DOING' - please provide expans... |
| 878 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'SOMETHING' - please provide ex... |
| 878 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'NASTY' - please provide expans... |
| 879 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 882 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 886 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 905 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 922 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 923 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 924 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 926 | 🟢 | PUNCT_COLON_SPACE | Add space after colon |
| 947 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'GAKCCK' - please provide expan... |
| 955 | 🟡 | ACRONYM_FIRST_USE | Acronym 'VLAN' not expanded on first use |
| 982 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'PING' - please provide expansi... |
| 988 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 988 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 1086 | 🟢 | TERM_LEVERAGE | Use 'use' instead of 'leverage' |
| 1094 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'RSH' - please provide expansio... |
| 1104 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1108 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1112 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1116 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1121 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1126 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1130 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1132 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1134 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1136 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1138 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1140 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 1142 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |

</details>

---

*Generated by Course AI Editor on 2026-02-27 17:41*

**Fix Type Legend**:
- 🟢 **SAFE**: High-confidence fix, can be auto-applied
- 🟡 **REVIEW**: Applied fix, please verify
- 🔴 **QUERY**: Question for author, not auto-fixed