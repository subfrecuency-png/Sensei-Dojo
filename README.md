# Sensei-Dojo

**SMI Technologies**

Sensei-Dojo holds **Sensei Mode: The Dojo**, an interactive teaching web app, together with the **Sensei Mode skill set** for Claude. The topics are business, credit, tax, capital, payments, legal structure, real property, digital assets and markets. The Dojo teaches from an evidence-graded fact base (tiers A to F). It runs a legal "status test" before it treats a rule as law in force, and it says plainly when the record is silent.

> **Education, not professional advice.** Nothing here replaces a licensed CPA, attorney, enrolled agent, appraiser, lender or securities counsel. Figures change. Check every time-sensitive item against the official source it names.

## What's in this repository

```
app/                      Sensei Mode — The Dojo (single-file web app)
  index.html              current build; open it in any modern browser
  thumbnail.png           preview image
  versions/               earlier saved builds of the same app, oldest to newest by timestamp
skill/
  kit/                    SMI Sensei Mode skill set v1.0.0 (free kit)
    skills/sensei/        master skill and graded fact base (references/fact-base.md)
    skills/sensei-live/   dated layer (as-of-dated items that move)
    skills/sensei-method/ teaching protocol (predict, commit, debrief, Brier scoring)
    upload/               one ready-to-upload ZIP per skill for claude.ai / Claude desktop
    README.md, INSTALL.md, CHANGELOG.md, SOURCES.md, LICENSE.md, examples/
  latest-installed/sensei/  the newer single-skill working copy of Sensei
                            (SKILL.md, references/*.md, scripts/stale_check.py)
```

## Run the Dojo

Open `app/index.html` in a browser. It is one self-contained file and needs no install, build step, account or API key. You can also serve it from any static host, such as GitHub Pages.

## Install the skills

- **claude.ai or the Claude desktop app:** upload the ZIPs in `skill/kit/upload/` under Settings → Capabilities → Skills. Code execution must be on.
- **Claude Code:** copy the folders in `skill/kit/skills/` into `~/.claude/skills/`.

Click-by-click steps are in [`skill/kit/INSTALL.md`](skill/kit/INSTALL.md). `skill/latest-installed/sensei` is a later working revision of the master skill. It has a split reference library and a stale-fact checker script. Install it in place of `skill/kit/skills/sensei` if you want that version.

## License

- **Skill kit:** see [`skill/kit/LICENSE.md`](skill/kit/LICENSE.md) (SMI Skill Kit License; free kit).
- **Dojo app:** © 2026 SMI Technologies. No open-source license has been chosen yet, so all rights are reserved until one is added.

"Claude" is a trademark of Anthropic. SMI is not affiliated with or endorsed by Anthropic.
