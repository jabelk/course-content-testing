# Editorial Review Report: Cisco Intersight Server Operating System Installation

**Quality Score**: 🔴 1.0/10 (Needs work - many unresolved issues)

| Property | Value |
|----------|-------|
| Word Count | 7,170 |
| Sections | 1 |
| Estimated Duration | 47m |
| Processing Time | 15.4s |

## Summary

**Total Issues**: 191

| Fix Type | Count | Description |
|----------|-------|-------------|
| SAFE | 101 | Auto-fixable with high confidence |
| REVIEW | 62 | Applied but needs human verification |
| QUERY | 28 | Questions for author - not auto-fixed |

### Issues by Category

| Category | Count |
|----------|-------|
| Grammar & Punctuation | 146 |
| Acronyms | 29 |
| Cisco Style Guide | 16 |

## Changes by Category

### Cisco Style Guide (16 issues)

**Auto-fixable (SAFE)**:

| Line | Original | Suggested | Rationale |
|------|----------|-----------|-----------|
| 31 | `initiate` | `start` | Use 'start' or 'begin' instead of 'in... |
| 41 | `allows you to` | `lets you` | 'lets you' instead of 'allows you to' |
| 41 | `allows you to` | `lets you` | 'lets you' instead of 'allows you to' |
| 207 | `click on` | `click` | Use 'click' instead of 'click on' |
| 207 | `click on` | `click` | Use 'click' instead of 'click on' |
| 234 | `click on` | `click` | Use 'click' instead of 'click on' |
| 275 | `click on` | `click` | Use 'click' instead of 'click on' |
| 275 | `click on` | `click` | Use 'click' instead of 'click on' |
| 302 | `click on` | `click` | Use 'click' instead of 'click on' |
| 357 | `initiate` | `start` | Use 'start' or 'begin' instead of 'in... |
| 357 | `make sure` | `ensure` | Use 'ensure' or 'verify' instead of '... |
| 386 | `make sure` | `ensure` | Use 'ensure' or 'verify' instead of '... |
| 459 | `Make sure` | `Ensure` | Use 'ensure' or 'verify' instead of '... |
| 541 | `initiate` | `start` | Use 'start' or 'begin' instead of 'in... |
| 541 | `initiates` | `starts` | Use 'start' or 'begin' instead of 'in... |
| ... | *1 more* | | |

### Acronyms (29 issues)

**Needs Review (REVIEW)**:

| Line | Original | Suggested | Rationale |
|------|----------|-----------|-----------|
| 375 | `DHCP` | `Dynamic Host Configuration ...` | Acronym 'DHCP' not expanded on first use |

**Questions for Author (QUERY)**:

- **Line 27**: Unknown acronym 'ISO' - please provide expansion or confirm intentional
- **Line 58**: Unknown acronym 'HX' - please provide expansion or confirm intentional
- **Line 79**: Unknown acronym 'UCSC' - please provide expansion or confirm intentional
- **Line 79**: Unknown acronym 'UCSB' - please provide expansion or confirm intentional
- **Line 84**: Unknown acronym 'UCSX' - please provide expansion or confirm intentional
- **Line 90**: Unknown acronym 'IMC' - please provide expansion or confirm intentional
- **Line 90**: Unknown acronym 'SCU' - please provide expansion or confirm intentional
- **Line 90**: Unknown acronym 'BIOS' - please provide expansion or confirm intentional
- *...and 20 more questions*

### Grammar & Punctuation (146 issues)

**Auto-fixable (SAFE)**:

| Line | Original | Suggested | Rationale |
|------|----------|-----------|-----------|
| 90 | `.  ` | `. ` | Use single space after period |
| 139 | `.  ` | `. ` | Use single space after period |
| 222 | `.   ` | `. ` | Use single space after period |
| 222 | `.   ` | `. ` | Use single space after period |
| 224 | `                           ...` | `` | Remove trailing whitespace |
| 224 | `.                          ...` | `. ` | Use single space after period |
| 230 | `.  ` | `. ` | Use single space after period |
| 230 | `.             ` | `. ` | Use single space after period |
| 243 | `.  ` | `. ` | Use single space after period |
| 290 | `.   ` | `. ` | Use single space after period |
| 290 | `.   ` | `. ` | Use single space after period |
| 292 | `                           ...` | `` | Remove trailing whitespace |
| 292 | `.                          ...` | `. ` | Use single space after period |
| 298 | `.  ` | `. ` | Use single space after period |
| 298 | `.             ` | `. ` | Use single space after period |
| ... | *70 more* | | |

**Needs Review (REVIEW)**:

| Line | Original | Suggested | Rationale |
|------|----------|-----------|-----------|
| 15 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 17 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 29 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 31 | ` which ` | `If this is a restrictive cl...` | using 'that' for restrictive clauses ... |
| 33 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 50 | `!` | `Consider using a period ins...` | removing exclamation point from techn... |
| 52 | `1` | `Spell out the number (e.g.,...` | spelling out numbers one through nine... |
| 72 | ` which ` | `If this is a restrictive cl...` | using 'that' for restrictive clauses ... |
| 173 | `2` | `Spell out the number (e.g.,...` | spelling out numbers one through nine... |
| 173 | `2` | `Spell out the number (e.g.,...` | spelling out numbers one through nine... |
| ... | *51 more* | | |

## Detailed Changes

*All issues sorted by line number for easy review:*

<details>
<summary>Click to expand all 191 issues</summary>

| Line | Type | Rule | Message |
|------|------|------|---------|
| 15 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 17 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 27 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'ISO' - please provide expansio... |
| 29 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 31 | 🟢 | TERM_INITIATE | Use 'start' or 'begin' instead of 'initiate' |
| 31 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 33 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 41 | 🟢 | TERM_ALLOWS_YOU_TO | Consider 'lets you' instead of 'allows you to' |
| 41 | 🟢 | TERM_ALLOWS_YOU_TO | Consider 'lets you' instead of 'allows you to' |
| 50 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 52 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 58 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'HX' - please provide expansion... |
| 72 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 79 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'UCSC' - please provide expansi... |
| 79 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'UCSB' - please provide expansi... |
| 84 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'UCSX' - please provide expansi... |
| 90 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 90 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'IMC' - please provide expansio... |
| 90 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'SCU' - please provide expansio... |
| 90 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'BIOS' - please provide expansi... |
| 96 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'SUSE' - please provide expansi... |
| 139 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 155 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'LAN' - please provide expansio... |
| 173 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 173 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 173 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'TIB' - please provide expansio... |
| 175 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 175 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 199 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 203 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 207 | 🟢 | TERM_CLICK_ON | Use 'click' instead of 'click on' |
| 207 | 🟢 | TERM_CLICK_ON | Use 'click' instead of 'click on' |
| 209 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 213 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 222 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 222 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 224 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 224 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 227 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 230 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 230 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 234 | 🟢 | TERM_CLICK_ON | Use 'click' instead of 'click on' |
| 243 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 251 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 255 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 275 | 🟢 | TERM_CLICK_ON | Use 'click' instead of 'click on' |
| 275 | 🟢 | TERM_CLICK_ON | Use 'click' instead of 'click on' |
| 277 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 281 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 290 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 290 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 292 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 292 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 295 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 298 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 298 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 302 | 🟢 | TERM_CLICK_ON | Use 'click' instead of 'click on' |
| 308 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 311 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 321 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 328 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 328 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 330 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 330 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 334 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 334 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 340 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 352 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 357 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 357 | 🟢 | TERM_INITIATE | Use 'start' or 'begin' instead of 'initiate' |
| 357 | 🟢 | TERM_MAKE_SURE | Use 'ensure' or 'verify' instead of 'make sure' |
| 361 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 365 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 365 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 367 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 369 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 371 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 373 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 375 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 375 | 🟡 | ACRONYM_FIRST_USE | Acronym 'DHCP' not expanded on first use |
| 381 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 383 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 383 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 383 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 386 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 386 | 🟢 | TERM_MAKE_SURE | Use 'ensure' or 'verify' instead of 'make sure' |
| 390 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 413 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 417 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 421 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'AHCI' - please provide expansi... |
| 437 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 444 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'DCUI' - please provide expansi... |
| 447 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 447 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 449 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 449 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 451 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 451 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 459 | 🟢 | TERM_MAKE_SURE | Use 'ensure' or 'verify' instead of 'make sure' |
| 467 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 471 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 471 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 473 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 473 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 475 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 480 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 482 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 487 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 489 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 489 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 491 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 497 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 497 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 516 | 🟡 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 517 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 519 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 521 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 527 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 531 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 531 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 533 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 533 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 535 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 537 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 539 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 541 | 🟢 | TERM_INITIATE | Use 'start' or 'begin' instead of 'initiate' |
| 541 | 🟢 | TERM_INITIATE | Use 'start' or 'begin' instead of 'initiate' |
| 545 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 545 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 546 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'INSTALL' - please provide expa... |
| 546 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'COMPLETED' - please provide ex... |
| 548 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 571 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 571 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 571 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 571 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 571 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 571 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 575 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 576 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 576 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 576 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 576 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 576 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 576 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 584 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'DISKIDPLACEHOLDER' - please pr... |
| 594 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 594 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 594 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 594 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 594 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 594 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 597 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'PARTITIONPLACEHOLDER' - please... |
| 599 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'SERVERDATACENTER' - please pro... |
| 613 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 613 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 630 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 652 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 652 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'SHA' - please provide expansio... |
| 654 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'UTF' - please provide expansio... |
| 666 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 685 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 694 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 696 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'ASCII' - please provide expans... |
| 704 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'CSV' - please provide expansio... |
| 710 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 714 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 716 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 718 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 720 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 722 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 724 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 726 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 728 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 728 | 🟢 | TERM_MAKE_SURE | Use 'ensure' or 'verify' instead of 'make sure' |
| 772 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |
| 776 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 798 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 812 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 826 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 830 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'FTP' - please provide expansio... |
| 836 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'SCP' - please provide expansio... |
| 838 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'SFTP' - please provide expansi... |
| 840 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'TFTP' - please provide expansi... |
| 842 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 854 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 864 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 868 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'DISKPLACEHOLDER' - please prov... |
| 870 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'PARTITIONIDPLACEHOLDER' - plea... |
| 874 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 910 | 🟡 | PUNCT_EXCLAMATION_IN_PROSE | Consider removing exclamation point from techni... |

</details>

---

*Generated by Course AI Editor on 2026-03-03 14:21*

**Fix Type Legend**:
- 🟢 **SAFE**: High-confidence fix, can be auto-applied
- 🟡 **REVIEW**: Applied fix, please verify
- 🔴 **QUERY**: Question for author, not auto-fixed