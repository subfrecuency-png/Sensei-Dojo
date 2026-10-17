# Install — SMI Sensei Mode — skill set

You will install 3 skills: `sensei`, `sensei-live` and `sensei-method`. Install all of them; `sensei` is the core and the others build on it.

Before you start, open the files and read them. Everything in this kit is plain text — three `SKILL.md` files and one reference file. There are no scripts. Only install skills from sources you trust.

---

## A. Claude on the web (claude.ai) or the Claude desktop app

**You need:** a Pro, Max, Team or Enterprise plan, and code execution turned on. Custom skills you upload are private to your account.

1. Unzip the kit you downloaded. Inside it, open the `upload/` folder. You will see `sensei.zip`, `sensei-live.zip` and `sensei-method.zip`.
2. In Claude, click your name or initials (bottom-left) → **Settings**.
3. Open **Capabilities**.
4. Make sure **Code execution** (sometimes shown as "Code execution and file creation") is turned **on**. Skills will not run without it.
5. Scroll to the **Skills** section and click **Upload skill**.
6. Choose **sensei.zip** from the `upload/` folder. Wait for it to appear in the list, and make sure its toggle is on.
7. Repeat steps 5–6 for each of the other ZIP files.
8. Start a **new** conversation (skills load at the start of a chat).

**Team or Enterprise:** an owner can provision the skills for the whole organisation from the admin settings instead of each person uploading them.

### Common upload errors
- **"Skill folder name doesn't match the skill name" / "missing SKILL.md":** you uploaded the whole kit ZIP or re-zipped a folder. Upload the files from `upload/` exactly as they are.
- **"ZIP too large":** you uploaded the kit ZIP instead of a single skill ZIP.
- **"Invalid characters in name or description":** the file was edited. Re-download the kit and use the original ZIP.
- **No Skills section:** your plan doesn't include custom skills, code execution is off, or your organisation's admin has disabled them.

---

## B. Claude Code

1. Unzip the kit.
2. Pick where the skills should live:
   - **For all your projects (personal):** `~/.claude/skills/`
   - **For one project only:** `.claude/skills/` inside that project's folder
3. Copy each folder from the kit's `skills/` directory into that location, keeping the folder names exactly as they are:

```bash
mkdir -p ~/.claude/skills
cp -R smi-kit-sensei/skills/sensei smi-kit-sensei/skills/sensei-live smi-kit-sensei/skills/sensei-method ~/.claude/skills/
```

4. You should now have `~/.claude/skills/sensei/SKILL.md`, `~/.claude/skills/sensei/references/fact-base.md`, `~/.claude/skills/sensei-live/SKILL.md` and `~/.claude/skills/sensei-method/SKILL.md`.
5. Start a new Claude Code session in your terminal.

---

## C. Check that it loaded

In a new conversation, type:

> Sensei, grade this claim: "Disputing directly with the creditor is the best way to fix my credit report."

**It loaded if** the reply is short, opens with an "education, not advice" line, gives a tier (A–F), cites FCRA §623 / §611, and ends with one next move.

Then type:

> Is the GENIUS Act in effect yet?

**`sensei-live` loaded if** the answer says the effective date is the *earlier* of two dates, gives 18 January 2027, and quotes an "as of" date.

Then type:

> Quiz me on SBA loan fees — don't explain first.

**`sensei-method` loaded if** Sensei gives you a scenario and asks for your answer and a confidence level (50/65/80/95%) before explaining anything.

If Claude answers normally but without that behaviour, the skill did not load. Check that the toggle is on (claude.ai) or the folder path is right (Claude Code), start a new conversation, and try again. If you're still stuck, see Troubleshooting in `README.md`.

---

## Updating or removing

- **claude.ai / desktop:** Settings → Capabilities → Skills → remove the old version, then upload the new ZIPs.
- **Claude Code:** delete the old folders from `~/.claude/skills/` (or `.claude/skills/`) and copy in the new ones.
