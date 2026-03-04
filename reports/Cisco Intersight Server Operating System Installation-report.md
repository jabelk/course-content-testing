# Editorial Review Report: Cisco Intersight Server Operating System Installation

**Quality Score**: 🔴 1.0/10 (Needs work - many unresolved issues)

| Property | Value |
|----------|-------|
| Word Count | 7,170 |
| Sections | 1 |
| Estimated Duration | 47m |
| Processing Time | 1.1s |

## Summary

**Total Issues**: 172

| Fix Type | Count | Description |
|----------|-------|-------------|
| SAFE | 101 | Auto-fixable with high confidence |
| REVIEW | 38 | Applied but needs human verification |
| QUERY | 33 | Questions for author - not auto-fixed |

### Issues by Category

| Category | Count |
|----------|-------|
| Grammar & Punctuation | 127 |
| Acronyms | 29 |
| Cisco Style Guide | 16 |

## Changes by Category

### Cisco Style Guide (16 issues)

**Auto-fixable (SAFE)**:

| Line | Context | Change | Rationale |
|------|---------|--------|-----------|
| 31 | ...You will `initiate` the operatin...... | ~~initiate~~ → **start** | Use 'start' or 'begin' instead of 'in... |
| 41 | ...The **Custom... `allows you to` use your con...... | ~~allows you to~~ → **lets you** | 'lets you' instead of 'allows you to' |
| 41 | ...s. The **Cus... `allows you to` use your cus...... | ~~allows you to~~ → **lets you** | 'lets you' instead of 'allows you to' |
| 207 | ...rom the navi... `click on` **System**. ...... | ~~click on~~ → **click** | Use 'click' instead of 'click on' |
| 207 | ...re** **Repos... `click on` **OS Image L...... | ~~click on~~ → **click** | Use 'click' instead of 'click on' |
| 234 | ...rating syste... `click on` **Add**:... | ~~click on~~ → **click** | Use 'click' instead of 'click on' |
| 275 | ...rom the navi... `click on` **System**. ...... | ~~click on~~ → **click** | Use 'click' instead of 'click on' |
| 275 | ...ftware Repos... `click on` **SCU Links*...... | ~~click on~~ → **click** | Use 'click' instead of 'click on' |
| 302 | ...rating syste... `click on` **Add**:... | ~~click on~~ → **click** | Use 'click' instead of 'click on' |
| 357 | ...\| 8.  Before... `initiate` operating sy...... | ~~initiate~~ → **start** | Use 'start' or 'begin' instead of 'in... |
| 357 | ...llation from... `make sure` that you upl...... | ~~make sure~~ → **ensure** | Use 'ensure' or 'verify' instead of '... |
| 386 | ...Cisco M5 ser... `make sure` that you hav...... | ~~make sure~~ → **ensure** | Use 'ensure' or 'verify' instead of '... |
| 459 | ...values that ... `Make sure` that you val...... | ~~Make sure~~ → **Ensure** | Use 'ensure' or 'verify' instead of '... |
| 541 | ...After you `initiate` the operatin...... | ~~initiate~~ → **start** | Use 'start' or 'begin' instead of 'in... |
| 541 | ..., and the se... `initiates` the installa...... | ~~initiates~~ → **starts** | Use 'start' or 'begin' instead of 'in... |
| ... | *1 more* | | |

### Acronyms (29 issues)

**Needs Review (REVIEW)**:

| Line | Context | Change | Rationale |
|------|---------|--------|-----------|
| 375 | ...for a **Stat... `DHCP` ** configura...... | ~~DHCP~~ → **Dynamic Host Conf...** | Acronym 'DHCP' not expanded on first use |

**Questions for Author (QUERY)**:

- **Line 27**: ...in the opera... `ISO` image. The I......
  - Unknown acronym 'ISO' - please provide expansion or confirm intentional
- **Line 58**: ...C. Cisco UCS `HX` -Series in s......
  - Unknown acronym 'HX' - please provide expansion or confirm intentional
- **Line 79**: ...C-Series Ser... `UCSC` -C220-M7, UC......
  - Unknown acronym 'UCSC' - please provide expansion or confirm intentional
- **Line 79**: ...B-Series (M5): `UCSB` -B200-M5, UC......
  - Unknown acronym 'UCSB' - please provide expansion or confirm intentional
- **Line 84**: ...X-Series Ser... `UCSX` -210C-M6\...
  - Unknown acronym 'UCSX' - please provide expansion or confirm intentional
- **Line 90**: ...ftware versi... `IMC` , SCU, BIOS,......
  - Unknown acronym 'IMC' - please provide expansion or confirm intentional
- **Line 90**: ...e version fo... `SCU` , BIOS, and ......
  - Unknown acronym 'SCU' - please provide expansion or confirm intentional
- **Line 90**: ...sion for Cis... `BIOS` , and the de......
  - Unknown acronym 'BIOS' - please provide expansion or confirm intentional
- *...and 20 more questions*

### Grammar & Punctuation (127 issues)

**Auto-fixable (SAFE)**:

| Line | Context | Change | Rationale |
|------|---------|--------|-----------|
| 90 | ...\| 1 `.  ` The requirem...... | ~~.  ~~ → **. ** | Use single space after period |
| 139 | ...\| 2 `.  ` The requirem...... | ~~.  ~~ → **. ** | Use single space after period |
| 222 | ...system insta... `.   ` **Mount Opti...... | ~~.   ~~ → **. ** | Use single space after period |
| 222 | ...system insta... `.   ` **Username/p...... | ~~.   ~~ → **. ** | Use single space after period |
| 224 | ...gured on the... `                 ...` | `                 ...` (question) | Remove trailing whitespace |
| 224 | ...igured on th... `.                ...` | ~~.                ...~~ → **. ** | Use single space after period |
| 230 | ...\| 3 `.  ` HTTP protoco...... | ~~.  ~~ → **. ** | Use single space after period |
| 230 | ...ted for Cisc... `.             ` \|... | ~~.             ~~ → **. ** | Use single space after period |
| 243 | ...\| 4 `.  ` The drop-dow...... | ~~.  ~~ → **. ** | Use single space after period |
| 290 | ...system insta... `.   ` **Mount Opti...... | ~~.   ~~ → **. ** | Use single space after period |
| 290 | ...system insta... `.   ` **Username/p...... | ~~.   ~~ → **. ** | Use single space after period |
| 292 | ...gured on the... `                 ...` | `                 ...` (question) | Remove trailing whitespace |
| 292 | ...igured on th... `.                ...` | ~~.                ...~~ → **. ** | Use single space after period |
| 298 | ...\| 5 `.  ` HTTP protoco...... | ~~.  ~~ → **. ** | Use single space after period |
| 298 | ...ted for Cisc... `.             ` \|... | ~~.             ~~ → **. ** | Use single space after period |
| ... | *70 more* | | |

**Needs Review (REVIEW)**:

| Line | Context | Change | Rationale |
|------|---------|--------|-----------|
| 31 | ...g to the tar... ` which ` you want to ...... | ~~ which ~~ → **If this is a rest...** | using 'that' for restrictive clauses ... |
| 52 | `1` \. Which of ...... | ~~1~~ → **Spell out the num...** | spelling out numbers one through nine... |
| 72 | ...type of targ... ` which ` an operating...... | ~~ which ~~ → **If this is a rest...** | using 'that' for restrictive clauses ... |
| 173 | ...partitions g... `2` TIB. UEFI bo...... | ~~2~~ → **Spell out the num...** | spelling out numbers one through nine... |
| 173 | ...partitions g... `2` TIB.... | ~~2~~ → **Spell out the num...** | spelling out numbers one through nine... |
| 175 | `1` \. For which...... | ~~1~~ → **Spell out the num...** | spelling out numbers one through nine... |
| 175 | ...1\. For ` which ` operating sy...... | ~~ which ~~ → **If this is a rest...** | using 'that' for restrictive clauses ... |
| 213 | ...as the organ... ` which ` the operatin...... | ~~ which ~~ → **If this is a rest...** | using 'that' for restrictive clauses ... |
| 255 | `1` \. Which one...... | ~~1~~ → **Spell out the num...** | spelling out numbers one through nine... |
| 281 | ...as the organ... ` which ` the operatin...... | ~~ which ~~ → **If this is a rest...** | using 'that' for restrictive clauses ... |
| ... | *27 more* | | |

**Questions for Author (QUERY)**:

- **Line 364**: ` 1. ` The wizard o......
  - Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 470**: ` 1. ` The wizard o......
  - Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 516**: ` 1. ` Extract the ......
  - Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 530**: ` 1. ` The wizard o......
  - Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)
- **Line 713**: ` 1. ` Initiate the......
  - Numbered list may need a procedural introduction (e.g., 'To configure the service:') (AI unavailable - manual review needed)

## Detailed Changes

*All issues sorted by line number for easy review:*

<details>
<summary>Click to expand all 172 issues</summary>

| Line | Type | Rule | Message |
|------|------|------|---------|
| 27 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'ISO' - please provide expansio... |
| 31 | 🟢 | TERM_INITIATE | Use 'start' or 'begin' instead of 'initiate' |
| 31 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 41 | 🟢 | TERM_ALLOWS_YOU_TO | Consider 'lets you' instead of 'allows you to' |
| 41 | 🟢 | TERM_ALLOWS_YOU_TO | Consider 'lets you' instead of 'allows you to' |
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
| 207 | 🟢 | TERM_CLICK_ON | Use 'click' instead of 'click on' |
| 207 | 🟢 | TERM_CLICK_ON | Use 'click' instead of 'click on' |
| 213 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 222 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 222 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 224 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 224 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 230 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 230 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 234 | 🟢 | TERM_CLICK_ON | Use 'click' instead of 'click on' |
| 243 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 255 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 275 | 🟢 | TERM_CLICK_ON | Use 'click' instead of 'click on' |
| 275 | 🟢 | TERM_CLICK_ON | Use 'click' instead of 'click on' |
| 281 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 290 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 290 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 292 | 🟢 | PUNCT_TRAILING_SPACE | Remove trailing whitespace |
| 292 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 298 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 298 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 302 | 🟢 | TERM_CLICK_ON | Use 'click' instead of 'click on' |
| 308 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 311 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
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
| 364 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 365 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 365 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 367 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 369 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 371 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 375 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 375 | 🟡 | ACRONYM_FIRST_USE | Acronym 'DHCP' not expanded on first use |
| 383 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 383 | 🟡 | GRAMMAR_THAT_WHICH | Consider using 'that' for restrictive clauses (... |
| 383 | 🟡 | GRAMMAR_SPLIT_INFINITIVE | Consider avoiding split infinitives when possible |
| 386 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 386 | 🟢 | TERM_MAKE_SURE | Use 'ensure' or 'verify' instead of 'make sure' |
| 390 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 413 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 417 | 🟡 | GRAMMAR_NUMBER_SPELL_OUT | Consider spelling out numbers one through nine ... |
| 421 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'AHCI' - please provide expansi... |
| 444 | 🔴 | ACRONYM_UNKNOWN | Unknown acronym 'DCUI' - please provide expansi... |
| 447 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 447 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 449 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 449 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 451 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 451 | 🟢 | PUNCT_DOUBLE_HYPHEN | Use em dash (—) instead of double hyphen (--) |
| 459 | 🟢 | TERM_MAKE_SURE | Use 'ensure' or 'verify' instead of 'make sure' |
| 470 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
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
| 516 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 517 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 519 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 521 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 530 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
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
| 713 | 🔴 | AI_PROCEDURAL_INTRO | Numbered list may need a procedural introductio... |
| 714 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 718 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 720 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 722 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 724 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 726 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 728 | 🟢 | PUNCT_DOUBLE_SPACE | Use single space after period |
| 728 | 🟢 | TERM_MAKE_SURE | Use 'ensure' or 'verify' instead of 'make sure' |
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

</details>

---

*Generated by Course AI Editor on 2026-03-04 15:15*

**Fix Type Legend**:
- 🟢 **SAFE**: High-confidence fix, can be auto-applied
- 🟡 **REVIEW**: Applied fix, please verify
- 🔴 **QUERY**: Question for author, not auto-fixed