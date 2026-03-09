# Editorial Review Report: Network Access for Non-Supplicant Devices_Sec 01_orig

**Quality Score**: 🔴 1.0/10 (Needs work - many unresolved issues)

| Property | Value |
|----------|-------|
| Word Count | 7,600 |
| Sections | 1 |
| Estimated Duration | 50m |
| Processing Time | 49.9s |

## Summary

**Total Issues**: 169

| Fix Type | Count | Description |
|----------|-------|-------------|
| SAFE | 83 | Auto-fixable with high confidence |
| REVIEW | 70 | Applied but needs human verification |
| QUERY | 16 | Questions for author - not auto-fixed |

### Issues by Category

| Category | Count |
|----------|-------|
| Grammar & Punctuation | 126 |
| Acronyms | 22 |
| Cisco Style Guide | 21 |

## Changes by Category

### Cisco Style Guide (21 issues)

**Auto-fixable (SAFE)**:

| Line | Context | Change | Rationale |
|------|---------|--------|-----------|
| 135 | ...ssage to the... `initiate` authentication.... | ~~initiate~~ → **start** | Use 'start' or 'begin' instead of 'in... |
| 207 | ...o authentica... `e.g. ` printers, IP...... | ~~e.g. ~~ → **for example, ** | Use 'for example' instead of 'e.g.' |
| 209 | ...t need to be... `e.g. ` Cisco Cataly...... | ~~e.g. ~~ → **for example, ** | Use 'for example' instead of 'e.g.' |
| 213 | ...ing (AAA) se... `e.g. ` Cisco Identi...... | ~~e.g. ~~ → **for example, ** | Use 'for example' instead of 'e.g.' |
| 215 | ...ollected MAC... `e.g. ` Lightweight ...... | ~~e.g. ~~ → **for example, ** | Use 'for example' instead of 'e.g.' |
| 250 | ...d MAC addres... `wish to` authenticate...... | ~~wish to~~ → **want to** | Use 'want to' instead of 'wish to' |
| 259 | ...ord to the M... `e.g. ` Cisco ISE st...... | ~~e.g. ~~ → **for example, ** | Use 'for example' instead of 'e.g.' |
| 505 | ...02.1X times ... `initiates` a MAB reques...... | ~~initiates~~ → **starts** | Use 'start' or 'begin' instead of 'in... |
| 511 | ...5.  The client `initiates` an HTTP or H...... | ~~initiates~~ → **starts** | Use 'start' or 'begin' instead of 'in... |
| 596 | ...Link your WL... `desired` policy profile.... | ~~desired~~ → **wanted** | Use 'want' or 'wanted' instead of 'de... |
| 806 | ...to understan... `initiated` and authorized.... | ~~initiated~~ → **started** | Use 'start' or 'begin' instead of 'in... |
| 847 | ...ss point to ... `boot up` , examine th...... | ~~boot up~~ → **start** | Use 'start' or 'boot' instead of 'boo... |
| 1039 | ...access devic... `initiate` a MAB reques...... | ~~initiate~~ → **start** | Use 'start' or 'begin' instead of 'in... |

**Needs Review (REVIEW)**:

| Line | Context | Change | Rationale |
|------|---------|--------|-----------|
| 346 | ...2. `Click Add` to add a RAD...... | ~~Click Add~~ → **Add bold formatti...** | GUI elements after 'click' should be ... |
| 757 | ...ial configur... `switchport` we are going...... | ~~switchport~~ → **Change 'switchpor...** | Use 'switch port' (two words) in narr... |
| 771 | `switchport` access vlan 50\... | ~~switchport~~ → **Change 'switchpor...** | Use 'switch port' (two words) in narr... |
| 772 | `switchport` mode access\... | ~~switchport~~ → **Change 'switchpor...** | Use 'switch port' (two words) in narr... |
| 791 | `switchport` access vlan 50\... | ~~switchport~~ → **Change 'switchpor...** | Use 'switch port' (two words) in narr... |
| 792 | `switchport` mode access\... | ~~switchport~~ → **Change 'switchpor...** | Use 'switch port' (two words) in narr... |
| 931 | `switchport` access vlan 50\... | ~~switchport~~ → **Change 'switchpor...** | Use 'switch port' (two words) in narr... |
| 932 | `switchport` mode access\... | ~~switchport~~ → **Change 'switchpor...** | Use 'switch port' (two words) in narr... |

### Acronyms (22 issues)

**Needs Review (REVIEW)**:

| Line | Context | Change | Rationale |
|------|---------|--------|-----------|
| 5 | ...tirely or pl... `VLANs` , underminin...... | ~~VLANs~~ → **virtual LAN (VLAN)** | Acronym 'VLAN' not expanded on first use |
| 10 | ...fallback mec... `MAC` Authenticati...... | ~~MAC~~ → **Media Access Cont...** | Acronym 'MAC' not expanded on first use |
| 17 | ...ies, integra... `RADIUS` authenticati...... | ~~RADIUS~~ → **Remote Authentica...** | Acronym 'RADIUS' not expanded on firs... |
| 135 | ...ort, the swi... `EAP` Request-Iden...... | ~~EAP~~ → **Extensible Authen...** | Acronym 'EAP' not expanded on first use |
| 400 | ...dress-to-MAC... `DHCP` | ~~DHCP~~ → **Dynamic Host Conf...** | Acronym 'DHCP' not expanded on first use |
| 497 | ...s through th... `ACL` configuratio...... | ~~ACL~~ → **access control li...** | Acronym 'ACL' not expanded on first use |

**Questions for Author (QUERY)**:

- **Line 5**: ...ion has alre... `IEEE` 802.1X authe......
  - Unknown acronym 'IEEE' - please provide expansion or confirm intentional
- **Line 126**: ...nter's proto... `IPP` (Internet Pr......
  - Unknown acronym 'IPP' - please provide expansion or confirm intentional
- **Line 126**: ...et Printing ... `LPR` (Line Printe......
  - Unknown acronym 'LPR' - please provide expansion or confirm intentional
- **Line 141**: ...IUS Access-R... `PAP` by default....
  - Unknown acronym 'PAP' - please provide expansion or confirm intentional
- **Line 330**: ...ess Method D... `FQ` Session ID\...
  - Unknown acronym 'FQ' - please provide expansion or confirm intentional
- **Line 332**: ...1/0/3 0050.5... `DATA` Auth A0A0A03......
  - Unknown acronym 'DATA' - please provide expansion or confirm intentional
- **Line 362**: ...**Configure `WLAN` Profile to U......
  - Unknown acronym 'WLAN' - please provide expansion or confirm intentional
- **Line 473**: ...vice, such a... `LAN` controller....
  - Unknown acronym 'LAN' - please provide expansion or confirm intentional
- *...and 8 more questions*

### Grammar & Punctuation (126 issues)

**Auto-fixable (SAFE)**:

| Line | Context | Change | Rationale |
|------|---------|--------|-----------|
| 135 | ...\| 1 `.  ` Initiation... | ~~.  ~~ → **. ** | Use single space after period |
| 135 | ...o initiate a... `.                ...` \|... | ~~.                ...~~ → **. ** | Use single space after period |
| 137 | ...maximum numb... `.                ...` \|... | ~~.                ...~~ → **. ** | Use single space after period |
| 139 | ...on Bypass), ... `.                ...` \|... | ~~.                ...~~ → **. ** | Use single space after period |
| 141 | ...\| 2 `.  ` MAC Address ...... | ~~.  ~~ → **. ** | Use single space after period |
| 141 | ...uest using P... `.                ...` \|... | ~~.                ...~~ → **. ** | Use single space after period |
| 143 | ...h with a dif... `.                ...` \|... | ~~.                ...~~ → **. ** | Use single space after period |
| 145 | ...ther authent... `.                ...` \|... | ~~.                ...~~ → **. ** | Use single space after period |
| 147 | ...and identify... `.                ...` \|... | ~~.                ...~~ → **. ** | Use single space after period |
| 149 | ...\| 3 `.  ` Session Auth...... | ~~.  ~~ → **. ** | Use single space after period |
| 149 | ...ion methods ... `.       ` \|... | ~~.       ~~ → **. ** | Use single space after period |
| 153 | ...eps the port... `.                ...` \|... | ~~.                ...~~ → **. ** | Use single space after period |
| 155 | ...ary control-... `.                ...` \|... | ~~.                ...~~ → **. ** | Use single space after period |
| 157 | ...on timer res... `.                ...` \|... | ~~.                ...~~ → **. ** | Use single space after period |
| 159 | ...\| 4 `.  ` Accounting... | ~~.  ~~ → **. ** | Use single space after period |
| ... | *55 more* | | |

**Needs Review (REVIEW)**:

| Line | Context | Change | Rationale |
|------|---------|--------|-----------|
| 17 | ...o network ac... `to securely onboard` non-supplica...... | ~~to securely onboard~~ → **Consider moving t...** | avoiding split infinitives when possible |
| 87 | ...MAB acts at ... `2` , allowing y...... | ~~2~~ → **Spell out the num...** | spelling out numbers one through nine... |
| 124 | ...st any Layer... `3` packets to l...... | ~~3~~ → **Spell out the num...** | spelling out numbers one through nine... |
| 143 | ...tes: Usernam... `1` ), Password ...... | ~~1~~ → **Spell out the num...** | spelling out numbers one through nine... |
| 143 | ...1), Password... `2` ), and Calli...... | ~~2~~ → **Spell out the num...** | spelling out numbers one through nine... |
| 147 | ...o switches s... `6` (Service-Typ...... | ~~6~~ → **Spell out the num...** | spelling out numbers one through nine... |
| 207 | ...-   Determining ` which ` devices you ...... | ~~ which ~~ → **If this is a rest...** | using 'that' for restrictive clauses ... |
| 213 | ...-   Determining ` which ` Authenticati...... | ~~ which ~~ → **If this is a rest...** | using 'that' for restrictive clauses ... |
| 329 | ...ess session ... `1` /0/3**\... | ~~1~~ → **Spell out the num...** | spelling out numbers one through nine... |
| 343 | ` 1. ` Navigate to ...... | ~~ 1. ~~ → **To enable a RADIU...** | Numbered list may need a procedural i... |
| ... | *46 more* | | |

## Detailed Changes

*All issues sorted by line number for easy review:*

<details>
<summary>Click to expand all 169 issues</summary>

| Line | Type | Rule | Message |
|------|------|------|---------|
| 5 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'IEEE' - please provide expansi... |
| 5 | 🟡 | ACRONYM_FIRST_USE | Acronym 'VLAN' not expanded on first use |
| 10 | 🟡 | ACRONYM_FIRST_USE | Acronym 'MAC' not expanded on first use |
| 17 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 17 | 🟡 | ACRONYM_FIRST_USE | Acronym 'RADIUS' not expanded on first use |
| 87 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 124 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 126 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'IPP' - please provide expansio... |
| 126 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'LPR' - please provide expansio... |
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
| 207 | 🟢 | TERM_EG | Use 'for example' instead of 'e.g.' |
| 207 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 209 | 🟢 | TERM_EG | Use 'for example' instead of 'e.g.' |
| 213 | 🟢 | TERM_EG | Use 'for example' instead of 'e.g.' |
| 213 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 215 | 🟢 | TERM_EG | Use 'for example' instead of 'e.g.' |
| 250 | 🟢 | TERM_WISH_TO | Use 'want to' instead of 'wish to' |
| 259 | 🟢 | TERM_EG | Use 'for example' instead of 'e.g.' |
| 329 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 330 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'FQ' - please provide expansion... |
| 331 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 332 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'DATA' - please provide expansi... |
| 343 | 🟡 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 344 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 346 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 346 | 🟡 | GUI_BOLD_CLICK | GUI elements after 'click' should be bold |
| 348 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 362 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'WLAN' - please provide expansi... |
| 363 | 🟡 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 364 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 364 | 🟡 | GRAMMAR_AMPERSAND_IN_PROSE | Use 'and' instead of '&' in prose text |
| 366 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 368 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 380 | 🟡 | GRAMMAR_AMPERSAND_IN_PROSE | Use 'and' instead of '&' in prose text |
| 381 | 🟡 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 382 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 384 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 386 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 388 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 400 | 🟡 | ACRONYM_FIRST_USE | Acronym 'DHCP' not expanded on first use |
| 418 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 442 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 444 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
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
| 502 | 🟡 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
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
| 549 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 596 | 🟢 | TERM_DESIRE | Use 'want' or 'wanted' instead of 'desire/desired' |
| 617 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 623 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 623 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 694 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 703 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 707 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 707 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'CX' - please provide expansion... |
| 711 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 724 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 733 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 735 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 741 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 746 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'USER' - please provide expansi... |
| 746 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'ATTRIBUTES' - please provide e... |
| 749 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'ACSACL' - please provide expan... |
| 757 | 🟡 | TERM_SWITCHPORT | Use 'switch port' (two words) in narrative text |
| 757 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 757 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 760 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 760 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 760 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 760 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 764 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 768 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 771 | 🟡 | TERM_SWITCHPORT | Use 'switch port' (two words) in narrative text |
| 772 | 🟡 | TERM_SWITCHPORT | Use 'switch port' (two words) in narrative text |
| 779 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 779 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 791 | 🟡 | TERM_SWITCHPORT | Use 'switch port' (two words) in narrative text |
| 792 | 🟡 | TERM_SWITCHPORT | Use 'switch port' (two words) in narrative text |
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
| 931 | 🟡 | TERM_SWITCHPORT | Use 'switch port' (two words) in narrative text |
| 932 | 🟡 | TERM_SWITCHPORT | Use 'switch port' (two words) in narrative text |
| 999 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 1003 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'BYPASS' - please provide expan... |
| 1029 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 1039 | 🟢 | TERM_INITIATE | Use 'start' or 'begin' instead of 'initiate' |
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

*Generated by Course AI Editor on 2026-03-09 18:31*

**Fix Type Legend**:
- 🟢 **SAFE**: High-confidence fix, can be auto-applied
- 🟡 **REVIEW**: Applied fix, please verify
- 🔴 **QUERY**: Question for author, not auto-fixed