# SMI Sensei Mode — skill set (v1.0.0, free)

Three Claude skills that turn Claude into **Sensei**: a strict teacher of business, credit, tax, capital, payments, banking, legal exposure, real property, digital assets and markets who grades every claim by the strength of its evidence and says out loud when the record is silent or a figure may have changed.

Published by Synthetic Media Investigator (SMI). The companion Sensei Mode Dojo web app is free at syntheticmediainvestigator.com.

> ## Education, not professional advice
> Sensei teaches how the rules and the evidence work — mostly the federal law of the United States of America, with some state examples (California, New York, Washington and others). It has **not** seen your books, contracts, entity documents, property or state, and it is **not** a substitute for a licensed CPA, attorney, enrolled agent, appraiser, lender, broker or securities counsel. Rules and figures change: every time-sensitive fact carries an "as of" date, and the record was last spot-checked on **1 October 2026** (see `SOURCES.md`). Verify anything you will act on with the official source Sensei names, and with a professional who can see your facts. AI output can be wrong.

---

## Who it is for

Founders, freelancers, small-business owners, real-estate investors and students who want to *understand* the rules well enough to ask a professional the right question — and to stop believing statistics and "loopholes" that do not survive a source check.

## What's inside

### `sensei` — the master and the fact base
Sensei answers from a graded fact base (`references/fact-base.md`, ~350 lines): FCRA and credit reporting, business credit, 2026 federal tax figures and doctrine, SBA and other capital, securities exemptions, digital assets, investing evidence, counterparty verification, base rates, real-property tax, financing, law and valuation, advertising and marketing evidence, red flags, payments, deposits and benefits. Every claim carries a tier from **A** (statute / randomized evidence) to **F** (false or untraceable). Legal claims also get a **status test** — bill, proposed rule, or law in force. When nothing in the record covers a question, Sensei says "ungraded" before reasoning. Replies are short and end with one concrete next move.

Try saying:
- "/sensei — is a 609 letter a real way to get collections deleted?"
- "Sensei, grade this: '90% of startups fail.'"
- "I'm a manufacturer getting an SBA 7(a) loan of $760,000 approved next week. What upfront fee should I expect?"
- "Explain the short-term rental loophole and what would make it not work for me."

### `sensei-live` — the dated layer
The parts that move: the GENIUS Act effective date and rulemaking, the federal CBDC prohibition, the CLARITY Act's failed cloture vote, SEC crypto proposals, Form 1099-DA phase-in, and the FY2027 SBA 7(a) and 504 fee schedules. **Every item carries an as-of date.** Where it disagrees with the fact base, it wins. If web search is on, Sensei re-checks items older than a month at the official source.

Try saying:
- "When does the GENIUS Act actually take effect — is it the later or earlier date?"
- "Is the CLARITY Act law yet?"
- "Which SBA fee schedule applies to a loan approved on 2 October 2026?"

### `sensei-method` — the teaching protocol
How Sensei teaches when you want to learn rather than look something up: you attempt before you are told, commit to a prediction and a confidence level (50/65/80/95%), then get a fixed four-question debrief, discrimination drills, transfer trials and a pre-mortem on whatever you are about to do. Calibration is scored with the Brier score.

Try saying:
- "Teach me passive-loss rules — quiz me, don't lecture."
- "I just lost a deal because the 1031 deadline passed. Debrief me."
- "Give me 10 true/false claims about business credit and score my calibration."

## What it will and won't do

**Will:** explain rules and evidence, grade claims and statistics, name the official source to check, say when something is uncertain, out of date or outside the record, and tell you which facts decide your question and which professional to bring them to.

**Won't:** decide your specific legal, tax or investment question; draft filings, bureau dispute letters, offering documents, leases or anything for signature; promise results; or help defeat a lawful obligation.

## Requirements

- **Claude (claude.ai or the desktop app)** on a Pro, Max, Team or Enterprise plan, with **code execution** turned on (needed for custom skills). Or **Claude Code**.
- **Optional: web search** in Claude. Not required. With it on, Sensei can re-check dated items against official sites; without it, Sensei quotes the as-of date and tells you what to check.
- **No connectors, accounts, API keys or paid services are required.**
- **Scripts:** none. All three skills are plain markdown files.
- **External services the kit touches:** none by itself. If you have web search enabled, Claude may visit public official sites such as congress.gov, govinfo.gov, federalregister.gov, irs.gov, sec.gov, sba.gov, treasury.gov and federalreserve.gov.

## Install

Short version below; click-by-click steps and how to verify are in `INSTALL.md`.

**Claude (claude.ai / desktop):** Settings > Capabilities → Skills → "Upload skill" → upload each ZIP from the `upload/` folder (`sensei.zip`, `sensei-live.zip`, `sensei-method.zip`). Install all three — `sensei` is the core; the other two layer on it.

**Claude Code:** copy the three folders from `skills/` into `~/.claude/skills/` (all your projects) or `.claude/skills/` inside one project.

## First run

1. Start a new conversation.
2. Ask: *"Sensei, grade this claim: 'An LLC protects my personal assets no matter what.'"*
3. You should get a short answer that opens with an "education, not advice" line, grades the claim (tier A–F), names the factor courts weigh most (commingling), and ends with one next move.
4. Then ask a dated question — *"Is the GENIUS Act in effect yet?"* — and check that the answer gives an as-of date.

See `examples/` for two worked examples (yours will differ).

## Privacy — what leaves your machine

- The skills are text instructions. They contain no tracking, no telemetry and no calls to SMI.
- Your conversation goes to Anthropic as with any Claude chat, under your Claude account's terms and settings.
- If web search is enabled, your search queries go to the search provider Claude uses.
- SMI never receives your questions, answers or data.

## Read before you install

Anthropic recommends installing skills only from sources you trust and reviewing their files first. Everything in this kit is plain text you can open and read: three `SKILL.md` files and one `references/fact-base.md`. There are no scripts or binaries.

## Troubleshooting

- **Upload rejected:** upload the ZIP from `upload/`, not the whole kit ZIP. Each upload ZIP contains one folder whose name matches the skill name. If your plan or organisation blocks custom skills, ask your admin.
- **Skill doesn't seem to trigger:** say "Sensei" or "/sensei" in your message, or name the topic directly ("Sensei, explain FCRA §611"). Make sure code execution is on.
- **Answers lack an as-of date on a time-sensitive question:** make sure `sensei-live` is installed alongside `sensei`.
- **A figure looks out of date:** it may be. Check the as-of date, ask Sensei to verify it with web search on, and check the official source. Tell us at syntheticmediainvestigator.com so the next version fixes it.

## Updating

Updates to the 1.x line are posted on syntheticmediainvestigator.com. To update: delete the old skills (Settings > Capabilities → Skills on claude.ai; or remove the folders in Claude Code), then install the new ZIPs or folders the same way. `CHANGELOG.md` lists what changed.

## Files

```
smi-kit-sensei/
  README.md  INSTALL.md  LICENSE.md  CHANGELOG.md  SOURCES.md
  skills/sensei/SKILL.md
  skills/sensei/references/fact-base.md
  skills/sensei-live/SKILL.md
  skills/sensei-method/SKILL.md
  upload/sensei.zip  upload/sensei-live.zip  upload/sensei-method.zip
  examples/
```

Licensed under the SMI Skill Kit License v1.0 (`LICENSE.md`). Free to use; not for resale or redistribution. "Claude" is a trademark of Anthropic. SMI is not affiliated with or endorsed by Anthropic.
