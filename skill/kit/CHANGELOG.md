# Changelog — SMI Sensei Mode — skill set

## 1.0.0 — 2026-10-01 — first release

First public release as a free SMI skill kit.

### Added
- "Education, not professional advice" frame at the top of every `SKILL.md`, in the fact base and in the README. `sensei` now opens the first substantive answer in a conversation with a one-line reminder, and repeats it when the student asks for a decision or the stakes are a filing, signature, loan or lawsuit.
- Jurisdiction line: the fact base states that it covers federal law of the United States of America unless a state is named.
- "As of" dates on every volatile item in `sensei-live`, with instructions to quote the date and re-check anything older than a month when web search is available.
- Fallbacks so each skill degrades gracefully: `sensei` treats dated figures as "as of" their date if `sensei-live` is missing; `sensei-method` carries a one-line tier summary in case `sensei` is not loaded.
- `SOURCES.md` listing the official sources checked on 1 October 2026.

### Fixed — facts corrected after checking official sources on 1 October 2026
- **GENIUS Act effective date** (fact base): said "the *later* of 18 January 2027 or 120 days after final rules". The statute (Section 20, P.L. 119-27) says the **earlier** of the two. Fixed; 18 January 2027 is the operative date.
- **GENIUS rulemaking** (`sensei-live`): Treasury NPRM comment deadline corrected from "around 16 October 2026" to **19 October 2026** (published in the Federal Register 18 August 2026). Added the Federal Reserve's 24 September 2026 proposals and Treasury's 30 September 2026 interim final rule for the Stablecoin Certification Review Committee.
- **CLARITY Act** (fact base and `sensei-live`): updated from "awaiting a Senate vote" to **cloture rejected 49–50 on 15 September 2026**.
- **SEC crypto positions** (fact base): "no final rule locatable" replaced with the SEC's 23 March 2026 interpretation and its 18 August 2026 proposed Regulation Crypto Assets (comments due 20 October 2026).
- **Anti-CBDC Surveillance State Act vote** (`sensei-live`): 219–217 corrected to **219–210** (17 July 2025).
- **CBDC prohibition** (fact base and `sensei-live`): added the public law number, **P.L. 119-101**, and flagged the title's effective date for checking.
- **QBI thresholds for 2026** (fact base): $201,775 / $403,550 corrected to **$201,750 (single and head of household) / $403,500 (married filing jointly) / $201,775 (married filing separately)** per Rev. Proc. 2025-32; phase-out end points added.
- **EITC investment-income limit for 2026** (fact base): $11,950 (the 2025 figure) corrected to **$12,200** per Rev. Proc. 2025-32.
- **SBA fees** (fact base and `sensei-live`): FY2026 schedule marked expired (30 September 2026); FY2027 schedule (Information Notices 5000-881797 and 5000-881796) confirmed and marked in effect for loans approved 1 October 2026 – 30 September 2027.
- **Debit interchange (Reg II)** (fact base): "appeal to the Eighth Circuit expected" updated — the district-court vacatur in *Corner Post* is stayed pending appeal in the Eighth Circuit (so the cap still applies), and *Linney's Pizza* is on appeal in the Sixth Circuit.

### Changed
- Removed personal and internal references from the original private version: a reference to the author's own web app inside `sensei-method`, first-person anecdotes about the author's past work, an internal audit note, and an internal version note at the end of `sensei`.
- `sensei-method` frontmatter normalised (unquoted `name`), description expanded to say what it does and when to use it.
- `sensei` description shortened slightly to stay under the 1,024-character limit with the new education line.
- `sensei-live` restructured around "what applies today" now that the FY2026 SBA schedule has ended.

### Not verified
- The SBA "rural area" definition (reported as SOP 50 10 8.1's 30%-rural county test) could not be confirmed from the SOP text. It stays tier D and is labelled unverified.
- The effective date of the CBDC title within P.L. 119-101 was not confirmed from the enrolled text.
- Fact-base items marked "as of July 2026" (for example the Corporate Transparency Act exemption, Opportunity Zone nomination dates, the 163(j) withdrawal window) were not re-checked in this release.
