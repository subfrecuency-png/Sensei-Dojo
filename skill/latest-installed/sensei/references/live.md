# Sensei — the live layer

**Read when:** every Sensei answer that uses a dated status, figure, fee, limit or deadline (Phase 0 step 1), Run Sensei Live Check, and Run Sensei Refresh. Folded in from the retired `sensei-live` skill on 2026-10-01 (Phase 1 lean); content unchanged except paths and cross-references.

## Purpose
`sensei` carries doctrine: rules that hold for years. This file carries the parts that move — statutes not yet in force, bills people mistake for law, proposed rules, and figures with an expiry date. Base skill: **sensei** (its Phase 0 reads this file).

**Precedence: where this file and `sensei` disagree, this file wins** — but only after the stale-on-load check below. Say so when it matters: *"the fact base has that as X; the corrected position is Y, and here's why it moved."*

Not investment, legal or tax advice. Jurisdiction: the United States of America (federal) unless a state is named; California items are tagged `[CA]`.

```
reviewed:       2026-10-01   (previous 2026-09-09, 2026-07-25)
next_review:    2026-11-01   (monthly pass)
event_triggers: 1 Oct fiscal-year reset (SBA fees, SNAP, federal thresholds) · 1 Jan tax year ·
                IRS inflation Rev. Proc. for the next tax year (Oct/Nov) · FHFA conforming and HUD FHA limits (late Nov) ·
                any comment period closing on an item below · 2 Dec 2026 EU AI Act date ·
                ~22 Oct 2026 OMB M-26-15 agency PQC plans (cross-reference, mad-scientist-mode references/live.md) ·
                any Senate floor action on market-structure legislation · weekly Freddie Mac PMMS (Thursdays)
upstream:       research-engine "Run Refresh" — watchlist domain `capital-credit` feeds this file
                (`re-mortgage` and `synthetic-media` feed RP and AI items)
```

## Commands
| Command | What it does |
|---|---|
| (load) | Default. Loaded with `sensei`; run the stale-on-load check, then answer from the items. |
| **Run Sensei Live Check** | Stale-on-load check only: list items past their next event and say whether `next_review` has passed. |
| **Run Sensei Refresh** | The monthly pass: re-verify every item at its primary source, update states and dates, fold settled corrections into `sensei`, log what moved. |

## Phase 0 — stale-on-load (every load)
1. Read today's date from the host clock (FL-011 via verify-kernel).
2. Run `python3 scripts/stale_check.py --file references/live.md` where a shell exists ⚡; otherwise compare today against `next_review` and the Next-event column by eye 👁 and say which you did.
3. **If `next_review` has passed, or an item you are about to use is past its next event, say so before using it**: *"Live item DA-02 was last verified 2026-10-01 and its next event (19 Oct 2026) has passed — treat the state as possibly moved."* Then verify that item (search protocol below) or grade it down one tier and give the query that would settle it.
4. Preflight for Refresh (verify-kernel §PREFLIGHT): web retrieval = TinyFish `search` + `fetch_content` (free, default) → else WebSearch/WebFetch → else research-engine → else report "unverifiable now" and do not edit any item.

## Dated items
| ID | Item | Tier | State | Effective | Next event | verified_on | Primary source | Fold into base when |
|---|---|---|---|---|---|---|---|---|
| DA-01 | CLARITY Act (H.R. 3633) is not law; Senate cloture on motion to proceed failed 49–50 | A (negative claim) | bill — stalled | — | 2026-11-03 midterms; any new cloture filing | 2026-10-01 | senate.gov roll call vote 234, 119th Cong. 2nd sess. | enacted (Public Law number) or dead at end of the 119th Congress |
| DA-02 | GENIUS Act effective date = earlier of 18 Jan 2027 or 120 days after final regs; rulemaking open | A | enacted, not yet effective; NPRMs open | 2027-01-18 | 2026-10-19 Treasury §3 comments close | 2026-10-01 | federalreserve.gov bcreg20260924a1.pdf; federalregister.gov 2026-16796 | effective date passes (fold "in force since 18 Jan 2027") |
| DA-03 | Federal CBDC barred (FRA §16A, P.L. 119-101), sunset 31 Dec 2030 | A | law in force | 2026-07-11 | 2030-12-31 sunset | 2026-10-01 | govinfo.gov BILLS-119hr6644enr §1101 | already folded (fact base updated); remove here once the traps stop recurring |
| DA-04 | 1099-DA: gross proceeds from 2025, basis from 2026 (covered assets); Notice 2026-20 ID relief through 31 Dec 2026 | A | final regs in force; relief temporary | 2025-01-01 / 2026-01-01 | 2026-12-31 relief ends | 2026-10-01 | irs.gov/pub/irs-drop/n-26-20.pdf | relief expires without extension |
| DA-05 | GENIUS §3(b): digital asset service providers may not offer non-permitted payment stablecoins from 18 Jul 2028 | A | enacted, future | 2028-07-18 | 2028-07-18 | 2026-10-01 | govinfo.gov PLAW-119publ27 | date passes |
| DA-06 | SEC "Regulation Crypto Assets" (offering exemption up to $75M, safe harbor to non-security status, $5M startup exemption) | C | proposed rule | — | 60 days after FR publication (date unconfirmed) | 2026-10-01 | secondary: bakerdonelson.com (SEC release 18 Aug 2026) | final rule in the Federal Register |
| SBA-01 | FY2027 7(a) fee schedule | A | in force | 2026-10-01 | 2027-09-30 schedule ends (FY2028 notice ~Aug–Sep 2027) | 2026-10-01 | secondary: colemanreport.com 2026-09-08 (SBA notice 5000-881797 not reachable) | never — annual; replace each fiscal year |
| SBA-02 | FY2027 504 fee schedule | A | in force | 2026-10-01 | 2027-09-30 | 2026-09-09 | SBA notice 5000-881796 (not re-fetched) | never — annual |
| SBA-03 | "Rural area" for the FY2027 waiver | C mechanism / D threshold | in force, definition unconfirmed | 2026-10-01 | read SOP 50 10 8.1 text | 2026-10-01 | secondary: colemanreport.com 2026-09-08 | SOP text confirms the threshold |
| BN-01 | FY2027 SNAP maximum allotments | B | in force | 2026-10-01 | 2027-10-01 reset | 2026-10-01 | usda.gov fna.snap-cola2027.pdf | never — annual |
| TX-01 | Tax-year 2026 figures in `sensei` references/tax.md | A | in force for 2026 | 2026-01-01 | 2026-11-15 IRS 2027 inflation Rev. Proc. (expected Oct/Nov) | 2026-07-27 | IRS Rev. Proc. 2025-32 (via base) | fold the 2027 table into tax.md on 1 Jan 2027 |
| RP-01 | Freddie Mac PMMS 30-year fixed 7.03% (week of 24 Sep 2026) | B | weekly survey | 2026-09-24 | weekly (Thursdays) | 2026-10-01 | freddiemac.com/pmms | never — always live |
| RP-02 | 2026 conforming and FHA loan limits | A | in force for 2026 | 2026-01-01 | 2026-11-30 FHFA/HUD 2027 limits (late Nov) | 2026-10-01 (FHFA); FHA 2026-07-27 | fhfa.gov news release "conforming loan limit values for 2026" | never — annual |
| RP-03 | 2026 cap-rate survey ranges | C | survey | 2026 | 2027-01-31 next survey cycle | 2026-07-27 (not re-verified) | broker surveys cited at compile | never — survey |
| RP-04 | `[CA]` AB 1482 cap, San Francisco CPI region: 8.8% for 1 Aug 2026–31 Jul 2027 | A | in force | 2026-08-01 | 2027-08-01 next year's cap | 2026-10-01 | sf.gov "California Tenant Protection Act 2019 (AB 1482)" | never — annual |
| RP-05 | Opportunity Zone 2.0 nominations (Rev. Proc. 2026-14) and designation window | B | nomination period open | 2027-01-01 map | 2026-10-28 extended nomination deadline | 2026-10-01 | secondary: afslaw.com alert on Rev. Proc. 2026-14 | map published and in effect |
| RP-06 | Zonda Cost vs. Value — 38th annual (Sep 2025) is the latest verified edition | C | published | 2025-09 | 2026-10-31 check for a 39th edition | 2026-07-27 | costvsvalue.com (not re-fetched) | n/a — replace the edition note in the base when a new one is verified |
| LW-01 | CTA: domestic companies and US persons permanently exempt from BOI reporting | A | final rule in force | 2026-08-14 | none (litigation or new statute only) | 2026-10-01 | secondary: mofo.com 2026-08-20 (FinCEN final rule, FR 14 Aug 2026) | fold at next monthly pass if unchallenged (primary FR citation first) |
| LW-02 | `[CA]` Notary: fee cap $15 per signature for an acknowledgment, $15 per oath/jurat (Gov. Code §8211); "notario" / "notario publico" as a translation of "notary public" is prohibited (Gov. Code §8219.5(c)) | A | law in force; amended by AB 1597 (Stats. 2026, ch. 39, signed 2026-06-30) | 2017-01-01 (§8211 as amended by AB 2217) | 2027-01-01 acknowledgment and jurat caps rise to $20 (AB 1597) | 2026-10-01 | leginfo.legislature.ca.gov GOV §8211, §8219.5; AB 1597: legiscan.com/CA/bill/AB1597/2172 (chaptered) + nationalnotary.org law update (amounts, date) — secondary, leginfo blocks automated reads | never — statutory figure; re-read §8211 each Refresh; after 2027-01-01 replace $15 with $20 |
| PY-01 | Reg II interchange standard: vacated in D.N.D. (Aug 2025), on appeal in the 8th Cir.; upheld in W.D. Ky. (Linney's Pizza), on appeal in the 6th Cir. | D | litigation pending | — | appellate decision (date unknown) | 2026-10-01 (status as of Jun 2026) | secondary: bankingjournal.aba.com 2026-06-09 | an appellate ruling settles the standard |
| MK-01 | Worked "as of when" example: one 2026 Bitcoin YTD return circulated as −7% and −24.22% in one week | C | historical illustration | 2026 | none | 2026-07-27 | base compile | n/a — teaching example; keep while useful |
| AI-01 | EU AI Act as amended by Regulation (EU) 2026/1744 | A (EU law) | in force; staged application | 2026-07-27 | 2026-12-02 Art. 50(2) grace ends and new Art. 5 prohibition applies | 2026-10-01 | eur-lex.europa.eu CELEX 32026R1744; secondary cdp.cooley.com | after 2 Dec 2027 when the last tier is close (fold the table) |
| AI-02 | US federal AI obligations are mostly executive action and procurement terms | C | mixed | — | monthly | 2026-07-25 | — (structural claim) | holds two passes unchanged → fold |
| AI-03 | NIST AI RMF is voluntary unless a contract or regulator adopts it | C | voluntary framework | — | monthly | 2026-07-25 | nist.gov AI RMF | holds two passes unchanged → fold |
| X-01 | Federal PQC deadlines (EO 14412, OMB M-26-15) | A | in force | 2026-06-22 | 2026-10-22 agency plans due | 2026-10-01 | see mad-scientist-mode references/live.md PQ-03 | owned by mad-scientist-mode references/live.md |

The table is the index; the sections below carry the full text. Every row here has a section below with the same ID.

---

## Digital assets

### DA-01 · The CLARITY Act is not law — and its 2026 Senate window closed with a failed vote
The **CLARITY Act** (H.R. 3633) passed the House. A Senate Banking substitute advanced **15–9 on 14 May 2026** and sat on the calendar with no floor vote, still to be reconciled with Senate Agriculture's bill and the House version; new Senate text circulated in late July 2026 alongside an ethics agreement meant to attract bipartisan support; the Senate left for the August recess without voting and pushed the vote to September.

**On 15 September 2026 the motion to invoke cloture on the motion to proceed to H.R. 3633 was rejected 49–50, with one senator not voting; 60 votes were required** (senate.gov roll call vote 234, verified 2026-10-01). Earlier reporting circulated the tally both as 50–49 and 49–50 — the Senate's own record says 49–50. Trade press read the failure as ending the Senate's market-structure push for 2026, with little time to revive it before the November midterms.

**What this file previously said, and why it was wrong:** the 9 September pass carried this as "live, very tight." After 15 September that framing overrode a correct base fact ("not law") with a hopeful forecast. **Tier A on the negative claim — it is not law.** Anything about *whether* it passes in a lame-duck session or the next Congress is a forecast; state it as one, with a probability, and never as a fact. Anyone describing SEC/CFTC jurisdiction over digital assets as resolved is describing a bill; until something passes, jurisdiction is set by enforcement posture and case law, both of which can turn.

### DA-02 · GENIUS Act — the effective date and the rulemaking
**Effective date (folded into `sensei` references/digital-assets.md on 2026-10-01).** Section 20 of the GENIUS Act (Pub. L. 119-27, enacted 18 July 2025) takes the **earlier** of (1) 18 months after enactment — **18 January 2027** — or (2) 120 days after the primary federal payment stablecoin regulators issue final implementing regulations. The Federal Reserve restated it verbatim on 24 September 2026: *"The GENIUS Act's effective date is the earlier of (i) January 18, 2027, or (ii) 120 days after the primary federal payment stablecoin regulators issue any final regulations implementing the Act."* Under "earlier of," 18 January 2027 is a **ceiling, not a floor**. Regulators missed the statutory one-year rulemaking deadline of 18 July 2026; a final rule issued after about 20 September 2026 cannot land 120 days before the backstop. **18 January 2027 is the operative date and will not move earlier.** Treat the implementation window as fixed and compressed.

**Rulemaking — every item below is a proposal or procedure, not a final substantive rule (status test):**
- **OCC** — proposal issued February 2026, published 11 March 2026 (secondary: Mayer Brown). The Comptroller said on 20 August 2026 that the OCC "will have a GENIUS Act final rule out by November" (icba.org, 2026-08-20). A November final rule would make prong (2) land around March 2027 — later than the backstop, so it changes nothing about the date.
- **FDIC** — application-procedures NPRM 19 December 2025; second NPRM (reserves, redemption, capital, custody, pass-through insurance for reserve deposits, tokenized deposits) approved **7 April 2026**, 60-day comment period (fdic.gov press release; Mayer Brown dates issuance 9 April with comments to 9 June 2026).
- **Federal Reserve** — two proposals on **24 September 2026**: reserve-asset and capital requirements for Board-supervised issuers, and an application process for state member banks; comments close 60 days after Federal Register publication (federalreserve.gov press release bcreg20260924a).
- **Treasury §3** — NPRM "GENIUS Act Regulations on Payment Stablecoin Issuance, Offer, and Sale," proposed 12 CFR Part 1523, **published 18 August 2026, comments due 19 October 2026** (federalregister.gov 2026-16796). The previous pass said "17 August, closes ~16 October"; the Register says 18 August and 19 October.
- **Stablecoin Certification Review Committee** — interim final rule on forms and procedures for reviewing state regimes under §4(c), **published and effective 30 September 2026**, comments to 30 November 2026; certifications accepted only after Paperwork Reduction Act approval (federalregister.gov 2026-19966). Procedural, not a substantive standard.

Fold the NPRM list out of this file when final rules publish; replace with final-rule citations.

### DA-03 · A federal CBDC is barred through 31 December 2030 — this is law
The prohibition became law on **11 July 2026**, carried in the **21st Century ROAD to Housing Act** (H.R. 6644, **Public Law 119-101**), which became law without the President's signature after presentment on 29 June 2026. Section 1101 adds **Federal Reserve Act §16A**: the Board and the Reserve Banks "may not issue or create a central bank digital currency or any digital asset that is substantially similar to a central bank digital currency directly or indirectly through a financial institution or other intermediary." Exception: "any dollar-denominated currency that is open, permissionless, and private, and fully preserves the privacy protections of United States coins and physical currency." Sunset: the section "shall cease to be effective on December 31, 2030." Rule of construction: nothing in it allows a CBDC "absent authorization by an Act of Congress." (Enrolled text read at govinfo.gov, 2026-10-01.) Reported Senate tallies conflict (85–5 on 22 June 2026 in the previous pass; 89–10 in a bill tracker) — do not quote either.

Two traps here:
- **It did not arrive on the vehicle people expect.** The Anti-CBDC Surveillance State Act (H.R. 1919) passed the House 219–217 in July 2025 and **never became law**. A House rider on the FY2026 NDAA also did not carry it. Anyone citing H.R. 1919 as the authority is citing a bill. *(Carried from the 9 Sep 2026 pass; not re-fetched.)*
- **It sunsets.** 31 December 2030 is a real date, not a permanent settlement. And "digital asset" takes the GENIUS Act definition (cryptographically secured ledgers), so commentators argue a centralised-ledger digital dollar sits outside the ban (secondary: Duke FinReg blog, 2026-07-20) — an argument, not a holding.

Tier **A**.

### DA-04 · Digital-asset broker reporting is mid-phase-in
- **Gross proceeds** — required for transactions on or after **1 January 2025** (first forms landed early 2026).
- **Cost basis** — required for transactions on or after **1 January 2026**, but **only for covered assets**: acquired on or after 1 January 2026 *and* held continuously in the same broker's account until sale.

Anything acquired earlier, or transferred in from an outside wallet or another broker, is **noncovered** — the broker reports no basis and the taxpayer still owes the calculation. Expect broker-reported basis and personal records to diverge wherever assets moved between venues. Reconcile before filing, not after a notice. Authority: Reg. §1.6045-1, final custodial broker regulations (July 2024). Tier **A**.

**IRS Notice 2026-20** (modifies Notice 2025-7) extends temporary relief for **identifying which units were sold**: taxpayers may make the identification in their own books and records or by standing order with the broker, for a relief period from **1 January 2025 through 31 December 2026**. It does **not** change Form 1099-DA reporting — the notice says it does not affect brokers' gross-proceeds reporting beginning in 2025 — and it warns that broker-reported acquisition dates and basis may not match taxpayer records. (irs.gov/pub/irs-drop/n-26-20.pdf, read 2026-10-01.) Next event: the relief ends 31 December 2026 unless extended again.

### DA-05 · The 2028 date for exchanges and wallets
Beginning **18 July 2028** (three years after enactment), a digital asset service provider may not offer or sell a payment stablecoin in the United States unless it was issued by a permitted payment stablecoin issuer (GENIUS Act §3(b)(1); govinfo.gov PLAW-119publ27, read 2026-10-01). Planning consequence: venues listing offshore stablecoins have a hard date distinct from the 18 January 2027 effective date.

### DA-06 · SEC crypto proposals are proposals
SEC released **"Regulation Crypto Assets"** on **18 August 2026** as a **proposed rule** (secondary: Baker Donelson): a two-tier offering exemption (Tier 2 up to $75 million per 12 months with audited financials), an investment-contract safe harbor under which an asset ceases to be a security once the issuer has completed or permanently ceased its promised essential managerial efforts (Form TR), and a startup "innovation exemption" for one-time offerings up to $5 million within a four-year window. Comments run 60 days after Federal Register publication (date not confirmed). **Tier C — agency proposal. Nothing here is in force**, and the base's line on the 2025–26 "innovation exemption" and token taxonomy stands: treat as proposed until a final rule appears in the Federal Register.

---

## SBA fees — FY2027 is in force; FY2026 has expired

### SBA-01 · FY2027 7(a) fees (loans approved 1 October 2026 – 30 September 2027)
SBA published the FY 2027 fee notices in early September 2026 — Information Notice **5000-881797** (7(a)) and **5000-881796** (504) (the previous pass recorded publication on 3 September; a trade-press summary is dated 8 September). **Approval date, not application date, picks the schedule.**

The manufacturer waiver did not simply continue and did not simply lapse. It was replaced by a differently-shaped one — **broader in who qualifies, lower in how much qualifies.**

| | FY 2026 (approved through 30 Sep 2026) — expired | FY 2027 (approved 1 Oct 2026 onward) |
|---|---|---|
| Who gets the 7(a) 0% upfront fee | Manufacturers only | Manufacturers (NAICS 31–33), food supply chain, **and** businesses in a rural area |
| Loan size ceiling for that waiver | $950,000 | **$700,000** |

**The cliff moved down by $250,000 and it moved for everyone.** A manufacturer with an $800,000 loan paid 0% if approved on 30 September 2026 and pays 3.5% of the guaranteed portion if approved on 1 October 2026.

- **Lender's Annual Service Fee:** 0.55% of the outstanding guaranteed balance, including WCP loans. **Lenders may not pass this to the borrower.**
- **Upfront (guaranty) fee, 0%** for loans of **$700,000 or less** to manufacturers (NAICS sectors 31–33), food supply chain (NAICS 1111, 1112, 1113, 1121–1125, 1129, 1141, 1151, 1152, 423820, 4244, 4245, 424910, 445110, 484220, 484230, 493120, 493130 — the two trucking codes limited to refrigerated/frozen, farm products, grain and livestock), and businesses located in a rural area.
- **Otherwise, maturity over 12 months** — percentages are of the *guaranteed portion*, size bands on the *gross* approval amount:
  - $150,000 or less — **2%** (lender may retain up to 25%; at least 1.5% remitted to SBA)
  - $150,001 to $700,000 — **3%**
  - $700,001 to $5,000,000 — **3.5%** up to $1,000,000, plus **3.75%** above $1,000,000
- **Maturity of 12 months or less:** 0.25%
- **SBA Express to veteran-owned businesses:** $0 — statutory, 15 U.S.C. §636(a)(31)(G), unchanged (documentation required)
- **EWCP:** 0.25% (≤12 mo) · 0.525% (13–24) · 0.80% (25–36)
- **WCP:** 0.25% (≤12 mo) · 0.525% (13–24) · 0.80% (25–36) · 1.075% (37–48) · 1.35% (49–60)
- **Loan increases** carry additional fees under the original-approval rules.

**The 90-day aggregation rule still bites.** Two or more 7(a) loans over 12 months' maturity to the same applicant or its affiliates within 90 days are treated as one loan for guaranty percentage and upfront fee. Splitting loans to avoid fees is prohibited. This is how a borrower lands over the $700,000 line without noticing.

Verified 2026-10-01 against the Coleman Report summary of the notice (dated 2026-09-08): waiver groups, $700,000 ceiling, 2% / 3% / 3.5% + 3.75% bands, 0.25% short-term, 0.55% annual, 90-day aggregation, $0 veteran Express all match. The SBA notice page itself was not reachable this pass. Tier **A** for the schedule (published agency notice with stated effective dates), carried on a secondary confirmation.

### SBA-02 · FY2027 504 fees
Manufacturers, food supply chain and rural-area businesses: **both the upfront guaranty fee and the annual service fee waived — no dollar cap.** All other 504 loans: upfront 0.50%, annual service 0.203%. 504 Debt Refinance without Expansion (non-manufacturer): upfront 0.50%, annual service 0.204%.

Note the asymmetry: 7(a) caps the waiver at $700,000, **504 does not cap it at all**. For a qualifying borrower above the cap, that difference alone can decide which program to use. *(Carried from the 9 Sep 2026 pass; not re-fetched.)*

### SBA-03 · "Rural area" — mechanism confirmed, threshold not
The notices say "located in a **rural area**" without defining it inline. The trade summary of the notice says **E-Tran determines rural status from Census Bureau data keyed to the project's ZIP code** — so the lender's system decides, not the borrower's description. Practitioner commentary reports SOP 50 10 8.1 defining it as any county the Census Bureau classifies as at least 30% rural — a much lower bar than the USDA test, reportedly qualifying a large majority of US counties. **That threshold is unverified against the SOP and should not be quoted as settled.** It is the whole ballgame for the newly-eligible third group: run the E-Tran check (through the lender) before relying on it. Tier **C** for the mechanism, **D** for the threshold.

---

## Benefits and tax-year figures

### BN-01 · SNAP maximum allotments, FY2027 (48 states + DC), effective 1 October 2026
One person **$306** · two $562 · three $808 · four **$1,023** · five $1,217 · six $1,463 · seven $1,616 · eight $1,841 · each additional $225. Minimum benefit $25 for one- and two-person households. (USDA memo dated 21 August 2026, usda.gov fna.snap-cola2027.pdf, read 2026-10-01.) Allotments and eligibility standards adjust every 1 October. Tier **B**.

### TX-01 · Tax-year figures
`sensei` references/tax.md carries the **tax year 2026** table (standard deduction, wage base, §179, 461(l), QBI, deferral limits, HSA, estate exclusion, mileage). They hold for 2026 returns. **Event trigger:** when the IRS publishes the tax-year-2027 inflation Revenue Procedure (expected October–November 2026), add the 2027 figures here and fold them into tax.md on 1 January 2027. Until then, a question about 2027 figures is "not yet published" — not the 2026 number.

---

## Real property

### RP-01 · Mortgage rate
Freddie Mac PMMS, 30-year fixed: **7.03%** for the week of **24 September 2026** (15-year 6.42%; prior week 6.95% / 6.26%; a year earlier 6.30%) — freddiemac.com/pmms, read 2026-10-01. Weekly survey, published Thursdays: quote it only with its week, and re-check before quoting. The base's earlier figure (6.58%, week ended 23 July 2026, then the highest since August 2025) is superseded.

### RP-02 · 2026 loan limits (reset each January)
Conforming one-unit **$832,750** baseline, **$1,249,125** high-cost ceiling, which is also the baseline in Alaska, Hawaii, Guam and the USVI (FHFA release for 2026, confirmed 2026-10-01). FHA one-unit **$541,287** floor to **$1,249,125**; two-unit $693,050–$1,599,375; three-unit $837,700–$1,933,200; four-unit $1,041,125–$2,402,625. HUD raised FHA limits 3.26%, effective for case numbers assigned on or after 1 Jan 2026 (carried from the July 2026 compile; not re-fetched). **Event:** FHFA and HUD announce 2027 limits in late November 2026.

### RP-03 · Cap rates, 2026 (survey ranges)
Multifamily all classes around 5.6%, Class A primary 4.50–5.25% · industrial 5.0–6.25% · retail large centres about 6.55%, strip about 6.44%, single-tenant net lease about 6.80% · office Class A 6.0–8.0%, **Class B repriced to 8.5–11%**. Use these to sanity-check a broker's assumption, never as your own. Tier **C**; carried from the July 2026 compile, not re-verified.

### RP-04 · `[CA]` AB 1482 — the cap is regional and annual
Statewide formula: 5% plus regional CPI, maximum 10%. For the **San Francisco CPI region** (which covers Pacifica and the Bay Area metro): **6.3% for 1 Aug 2025 – 31 Jul 2026** (5% + 1.3% CPI) and **8.8% for 1 Aug 2026 – 31 Jul 2027** (sf.gov AB 1482 page, read 2026-10-01). Other California regions use their own CPI, so their caps differ — never quote the SF figure statewide. The 8.8% reflects a high CPI print and should not be extrapolated. Correction to the base's earlier phrasing: it presented 6.3%/8.8% without naming the region.

### RP-05 · Opportunity Zone 2.0 — nomination window
Under Rev. Proc. 2026-14 (secondary: Arent Fox Schiff alert): nominations opened 1 July 2026; original deadline 28 September 2026, **optional extension to 28 October 2026**; Treasury has 30 days to consider (plus an optional 30). **The new map takes effect 1 January 2027 and designations run through 31 December 2036.** OZ 1.0 designations sunset 31 December 2028. Qualified Rural Opportunity Funds get a 30% basis step-up (versus 10%) for five-year holds. **Conflict to resolve:** `sensei` property-tax.md says OZ 2.0 runs "through 31 Dec 2033"; the secondary reading of the Rev. Proc. says designations run through 2036. Do not quote either end date as settled until the Rev. Proc. text is read. OZ 1.0's 31 December 2026 gain-recognition date is unaffected.

### RP-06 · Renovation ROI — edition watch
Zonda's Cost vs. Value Report: the 38th annual (September 2025) is the latest edition verified at compile. Zonda has released in late summer/autumn, so a 39th edition may now exist — **check before quoting "the current report"**, and keep the base's tier F rule on any citation to an edition you have not seen.

---

## Law, payments and markets

### LW-01 · Corporate Transparency Act — domestic companies are out, by final rule
FinCEN's interim final rule of **21 March 2025** narrowed "reporting company" to entities formed under foreign law and registered to do business in a US state, removing over 99% of previously covered entities. **A final rule followed: issued 11 August 2026, published and effective 14 August 2026, permanently exempting domestic reporting companies and US persons** from BOI reporting; foreign reporting companies still report, and only their non-US beneficial owners; FinCEN said it will remove previously filed data of domestic companies and US persons (secondary: Morrison Foerster, 2026-08-20; several firm alerts agree). Tier **A** on the existence of a final rule — **read the Federal Register text before advising a foreign-formed entity.**

### LW-02 · `[CA]` Notary fees and the "notario" ban (RES notary and signing-agent copy)
**Gov. Code §8211** caps California notary fees: **$15 for each signature taken** on an acknowledgment or proof, **$15** for an oath or affirmation with jurat, $15 to certify a copy of a power of attorney, $30 plus $7 + $7 for a deposition; **no fee** on vote-by-mail ballot envelopes or on a veteran's benefits application (§8211(d), (f); §6107). Last amended by AB 2217 (Stats. 2016, ch. 133), effective 1 January 2017 — verified at leginfo.legislature.ca.gov on 2026-10-01. Travel fees are not in §8211; a mobile signing fee must be stated as separate from the notarial fee. **Gov. Code §8219.5(c)** prohibits translating "notary public" as "notario publico" or "notario"; a non-attorney notary advertising in another language must post the "I am not an attorney" notice with the statutory fees (§8219.5(a)); suspension of at least one year, revocation on a second offence (§8219.5(d)). **AB 1597** (Stats. 2026, ch. 39, signed 30 June 2026) raises the acknowledgment and jurat caps from $15 to **$20 from 1 January 2027** — chaptered status from legiscan.com, amounts and date from the National Notary Association's law update, both read 2026-10-01 (leginfo blocks automated reads; confirm the chaptered text there before the first 2027 quote). Tier **A**. This is the figure FL-153 points to for RES notary copy — quote "up to $15 per signature" through 31 December 2026 ("up to $20" from 1 January 2027), never a higher bundled "notary fee"; pricing-desk's `quote.py` checks the same schedule (rates-live NT-01).

### PY-01 · Debit interchange — two courts, two answers, both on appeal
The Fed's 2023 proposal to cut the cap to 14.4 cents was never finalised. A federal district court in North Dakota (*Corner Post* and retailer associations) **vacated** Reg II's interchange standard in August 2025; that decision is on appeal in the **Eighth Circuit**. A district court in Kentucky (*Linney's Pizza*) ruled **for** the Fed in September 2025; that appeal is in the **Sixth Circuit**, in briefing as of June 2026 (ABA Banking Journal, 2026-06-09). No appellate decision was found in this pass. Tier **D** for any fixed future cap. Do not model debit economics on a fixed number without flagging the challenge.

### MK-01 · The "as of when" worked example
The same 2026 Bitcoin year-to-date return circulated as **−7%** and **−24.22%** in one week. Neither source lied; they measured on different days in a falling market. The one naming its date and price is usable; the other is not. Use it to teach the question, never as a current figure.

---

## AI regulation (moved here from DOC's live layer — authority questions belong in Sensei's court)

### AI-01 · The EU AI Act was amended — several widely-quoted deadlines are now wrong
**Regulation (EU) 2026/1744 of 8 July 2026** (the "Digital Omnibus on AI") amends Regulation (EU) 2024/1689; published in the Official Journal **24 July 2026**, in force **27 July 2026** (EUR-Lex, read 2026-10-01). Path: proposed 19 November 2025, provisional agreement 6–7 May 2026, Parliament 16 June, Council 29 June.

| Obligation | Date |
|---|---|
| Article 50 transparency (general) | **2 August 2026 — did not move** |
| Art. 50(2) marking of AI-generated content, systems placed on the market before 2 Aug 2026 | grace to **2 December 2026** |
| New Art. 5 prohibition — AI-generated non-consensual intimate imagery and CSAM, incl. "nudifiers" | **2 December 2026** (Cooley; the EUR-Lex summary read this pass was ambiguous — confirm in Art. 113 before advising) |
| High-risk, Annex III stand-alone | 2 August 2026 → **2 December 2027** |
| High-risk, Annex I embedded in regulated products | 2 August 2027 → **2 August 2028** |

**"The EU delayed the AI Act" is half true and dangerously imprecise** — the transparency obligations landed on schedule while the high-risk tiers slipped sixteen months. A team that heard "delayed" and stood down is non-compliant on the part that did not move. **Anyone generating synthetic images, audio or video is inside Article 50(2) and the new Article 5 prohibition**, on the December 2026 clock, regardless of the high-risk deferral. This matters directly to S.M.I. and to any of the user's generative content work aimed at EU audiences. EU law: not legal advice; the jurisdiction here is the European Union, not the United States of America.

### AI-02 · US federal AI requirements are mostly not statute
US federal AI requirements are largely executive action, agency guidance and procurement conditions rather than statute, and executive action reverses with administrations. State law — particularly on automated decision-making, biometrics and disclosure — is where most currently binding obligation sits for a private company, and it is fragmented by state. **The status test applies verbatim: bill, proposed rule, or law in force, and a voluntary framework is none of the three.** Tier **C**.

### AI-03 · NIST's AI Risk Management Framework is voluntary
Genuinely useful as a structure; binds nothing on its own. It becomes binding only where a contract, a procurement clause or a sectoral regulator incorporates it — which increasingly happens, so check the contract rather than the framework. Tier **C**.

### X-01 · Federal post-quantum deadlines
EO 14412 and OMB M-26-15 are law-in-force instruments with dates (31 Dec 2030 key establishment, 31 Dec 2031 signatures for high-value assets and high-impact systems). They live in **PQ-03 of `mad-scientist-mode` references/live.md** because the engineering is the hard part; answer the authority question here and send the migration question there.

---

## Bills, proposals and standards people cite as law — they are not
**Standing rule for this whole area.** Passing one chamber is not law. Advancing out of committee is not law. Filing cloture is not a vote — and **losing a cloture vote is not a pause, it is a failure that needs a new vehicle or a new Congress**. An executive order binds the executive branch and can be revoked by the next one. An agency **proposal**, a no-action letter, and an "innovation exemption" are agency positions, not statute — and a notice of proposed rulemaking is not a rule. An interim final rule is in force but usually procedural; read what it governs. Grade accordingly, and say which one you're looking at.

### Things cited as settled that are not (check before letting the student plan around them)
- **"The CLARITY Act is about to pass" / "market structure is settled."** Cloture failed 49–50 on 15 Sep 2026 (DA-01).
- **"The GENIUS Act applies now."** Enacted 18 July 2025; effective 18 January 2027 (DA-02). "Enacted 18 July 2025, effective 18 January 2027" is the honest form.
- **"GENIUS rules are final."** As of 2026-10-01 every substantive GENIUS rule is a proposal; the only thing in force is a procedural interim final rule (DA-02).
- **H.R. 1919 cited as the CBDC ban.** A House bill that never became law; the ban is FRA §16A via P.L. 119-101 (DA-03).
- **"SEC exempted tokens."** A proposed rule (DA-06).
- **"The manufacturer SBA fee waiver is $950,000."** Expired 30 September 2026 (SBA-01).
- **"Rural means USDA rural."** Unverified; E-Tran decides (SBA-03).
- **"AB 1482 is 8.8%."** Only in the San Francisco CPI region, only for Aug 2026–Jul 2027 (RP-04).
- **"The EU delayed the AI Act."** Article 50 did not move (AI-01).
- **"Basel requires X."** A standard binds nothing until a national regulator implements it (base: payments-deposits.md).

## Search protocol (Run Sensei Refresh, and any single-item check)
1. **List the item's claim, state and next event.** Decide what would change it: a vote, a Federal Register document, a notice, a court ruling, a published figure.
2. **Go to the primary register first**: congress.gov / senate.gov roll calls / govinfo.gov (enrolled bills, public laws) for statute; federalregister.gov and regulations.gov for rules and comment deadlines; the agency's own site (federalreserve.gov, fdic.gov, occ.gov, irs.gov/pub/irs-drop, sba.gov, usda.gov, fhfa.gov, hud.gov) for notices; courtlistener.com for opinions; eur-lex.europa.eu for EU law. Retrieval: TinyFish `search` + `fetch_content` (free) → WebSearch/WebFetch → research-engine.
3. **If the primary page is unreachable** (robots, 404, challenge), take a named secondary (law-firm alert, trade press quoting the document), **say "secondary" in the item**, and keep the primary as the next event.
4. **Two sources disagree on a number or date** (e.g., a vote tally, a comment deadline): the primary record wins; if none is reachable, state both and do not quote either.
5. **Write the result in the item's format**: claim · tier · state · effective · next event · verified_on + URL · fold rule. Mark anything not re-fetched this pass as "carried, not re-fetched."
6. **Grade down on silence.** An item you cannot re-verify past its next event drops one tier and carries "unverified since <date>".

## How to use this file
1. **Check here first** for anything touching stablecoins, CBDCs, crypto market structure, digital-asset tax reporting, SBA fees, benefits figures, rates and loan limits, rent caps, OZ deadlines, CTA, interchange, or AI regulation.
2. **State what is in force today**, not what is enacted-but-dormant.
3. **For SBA fees, ask which fiscal year the loan is approved in before quoting a number.** On either side of 1 October there are two schedules and the approval date picks one.
4. **Name the vehicle** when a rule arrived somewhere unexpected — the CBDC ban riding a housing bill is exactly the kind of thing a careful reader gets wrong.
5. **Flag expiry** whenever you quote a figure from the table above.
6. **Separate the verified from the reported.** Say "primary", "secondary" or "carried, not re-fetched" — the rural-area threshold, the CTA final rule text, the OZ end date and the EU Art. 5 date are the current examples.

## Fold-back rule and superseded log
When a correction has held through one full monthly pass and its primary source is read, **fold it into the matching `sensei` reference and delete it here** (leave a one-line pointer in the base). Annual figures never fold — they are replaced. Expired rows leave the dated-items table and get one line in this log, so the fact is kept without overriding anything:
- 2026-10-01 — GENIUS "earlier of" correction folded into `sensei` digital-assets.md (the base had "later of" at tier A).
- 2026-10-01 — CBDC enrolled-text wording folded into digital-assets.md.
- 2026-10-01 — Expired: FY2026 7(a) upfront fee 0% on loans ≤ $950,000 to manufacturers (NAICS 31–33), worth ≈$24,938 at $950,000; expired 30 September 2026.
- 2026-10-01 — Expired: FY2026 SNAP maximum allotments (48 states + DC), effective 1 October 2025: one person $298, two $546, three $785, four $994, five $1,183, six $1,421.
- 2026-10-01 — Superseded: 30-year fixed averaged 6.58% (Freddie Mac PMMS, week ended 23 July 2026 — highest since August 2025).
- 2026-10-01 — Superseded: CLARITY "Senate September window — live, very tight" (cloture failed 15 Sep 2026).
- 2026-10-01 — Superseded: Treasury §3 NPRM "17 August, comments ~16 October" → FR 18 August, comments 19 October.
- 2026-10-01 — Superseded: CTA "final rule expected during 2026" → final rule 14 August 2026 (LW-01).
- 2026-09-09 — Closed: "rules finalised before ~20 September 2026 could still pull the GENIUS date in."

## Handoff files and state
- **Reads:** research-engine finding records and `_runs/RUN-<id>.md` for watchlist `capital-credit` (at `vault/research/`); `sensei` references when folding.
- **Writes:** nothing inside this folder at runtime. A Refresh produces a **refresh report** (items changed, items stale, proposed edits as a diff) delivered as a file in the session's outputs, or to `SKILLS_HOME/live-refresh/sensei-live-YYYY-MM-DD.md` when SKILLS_HOME is mounted. The edits land through the normal skill-update path (skill-master), never by the skill rewriting itself.
- **Fallback:** no writable storage → deliver the refresh report in the conversation.

## Cost and side effects
- Retrieval (TinyFish search/fetch, WebSearch/WebFetch) is free. Nothing is sent or published.
- **Optional sentinel (P7):** a TinyFish `create_monitor` on a watch source (Senate roll calls, a Federal Register docket, the SBA notices page) is **metered (about $0.005 per run)** — propose the count and cadence, cap it, and create only on the user's approval (verify-kernel §GATES). A scheduled task (create_trigger) for the monthly Refresh likewise only if the user sets it up.

## Field lessons
- **FL-013 (WIN) Primary sources:** every item names its primary source; secondary confirmations say "secondary". This pass found three corrections at the primary record (Senate tally 49–50; Treasury comment deadline 19 Oct not ~16 Oct; CTA final rule) — that is the lesson repeating.
- **FL-075 (WIN) Grades and "insufficient evidence":** unverifiable thresholds stay tier D (SBA-03) instead of being rounded up; conflicting tallies are not quoted.
- **FL-100 (COMPLIANCE) Compliance gates the architecture:** the GENIUS dates (DA-02, DA-05), the EU Art. 50(2)/Art. 5 clock (AI-01) and fee schedules feed build and pricing decisions — check them before a design is locked.
- **FL-105 (DECISION):** jurisdiction written "the United States of America"; EU items say they are EU law.
- **FL-121 (WIN) Compliance research before build:** for any RES, S.M.I. or stablecoin-adjacent build, run the relevant items here before the spec freezes.
- **FL-153 (COMPLIANCE) Notary copy:** never "notario" (Gov. Code §8219.5) and fees within the §8211 per-signature cap — the current figure is LW-02; blog-studio and ads-lab read it from here.
- **FL-117 (WIN) Versioned releases with acceptance tests:** a Refresh ships only when `scripts/stale_check.py` exits 0 on the new file (no item past its next event without a note, `next_review` in the future) and every table ID has a section.

## Failure paths
- **Missing input:** question outside the items — say this file is silent and hand to research-engine for new sourcing.
- **Tool or connector down:** no web retrieval available — run the stale-on-load check, say which items are past their next event, grade them down one tier, and give the exact primary URL to check. Do not edit items.
- **Wrong environment:** no shell for the script — do the date comparison by eye and label it 👁.
- **No writable storage:** this file is edited only on a refresh pass; with no writable copy, put the proposed item changes in the report for the user to apply and leave the file as is.
- **Primary source blocked** (robots, 404, challenge): use a named secondary, label it, keep the primary as the next event (search protocol step 3).
- **`sensei` not loaded:** this file is not doctrine; answer only the dated question and say the doctrine lives in `sensei`.

## Anti-patterns (each happened)
- Leaving a forecast ("live, very tight") in place after the event that settled it — the live layer then overrides a correct base fact with a wrong one.
- Stating a statutory "earlier of" as "later of" at tier A — inverting the planning advice.
- Keeping an expired fee row in the active table next to its replacement.
- Quoting a regional rent cap as statewide.
- Quoting a vote tally from trade press when the chamber's roll call is one fetch away.

## Orchestration
**Run Sensei Refresh** splits by item cluster (digital assets · SBA/benefits/tax · real property · law/payments · AI): pattern **P2 fan-out by unit**, one agent per cluster with this file's item format as the result schema, then **P4 adversarial verify** — a second agent tries to break each changed item at its primary source; only survivors merge. The parent runs `stale_check.py` and the fold-back rule. **P7 sentinel** (monitor or scheduled task) is optional and gated as above.

## Changelog
- 2026-10-01 — Phase 1 lean: folded from the retired `sensei-live` skill (last v2.3) into `sensei/references/live.md`; `stale_check.py` moved to `sensei/scripts/`; Phase 0 path and cross-references to the other folded live layers updated; every item, date and source unchanged.
- v2.3 (2026-10-01) — cycle 2 round 3, 2026-10-01: LW-02 records AB 1597 (Stats. 2026, ch. 39): notary acknowledgment and jurat caps rise to $20 on 2027-01-01 (found while adding pricing-desk's CAP check); Failure paths open with the four house labels (Missing input · Tool or connector down · Wrong environment · No writable storage), existing lines relabelled without changing their meaning.
- v2.2 (2026-10-01) — cycle 2, 2026-10-01: new item LW-02 `[CA]` notary fee cap ($15 per signature, Gov. Code §8211 as amended eff. 2017-01-01) and the §8219.5 "notario" ban, verified at leginfo.legislature.ca.gov 2026-10-01; FL-153 cited (C2-A3 routing).
- v2.1 (2026-10-01) — fixes from P3 review R4, 2026-10-01: `scripts/stale_check.py` exits 2 (never 1) on a missing, unreadable or malformed file and gains `--selftest` (10/10 ⚡; identical code in every library copy); "ARTIFACTS: PLANNED path" wording removed.
- v2.0 (2026-10-01) — Hotfix rebuild in the uniform live format (header, dated-items table, per-item verified_on + primary URL + fold rule, stale-on-load, search protocol, things cited as settled). CLARITY corrected to failed cloture 49–50 on 15 Sep 2026 (was "live, very tight"); GENIUS "earlier of" confirmed and folded into sensei; added OCC, FDIC, Fed and Treasury §3 NPRMs, the Certification Review Committee IFR and the 18 Jul 2028 DASP date; Treasury comment deadline corrected to 19 Oct; CBDC verified against enrolled text (P.L. 119-101); Notice 2026-20 added; SBA FY2027 confirmed, FY2026 row expired, rural mechanism via E-Tran; SNAP FY2027; moved dated figures in from sensei (rate, limits, cap rates, AB 1482, OZ 2.0, CTA, Reg II, YTD example); CTA updated to the 2026 final rule; AI regulation moved in from mad-scientist-live with Regulation (EU) 2026/1744; added stale_check.py. Because the live layer was overriding correct facts with wrong ones. SKILL-LOG SL-002.
- v1.x (2026-07-25, 2026-09-09) — monthly passes (prior format).
