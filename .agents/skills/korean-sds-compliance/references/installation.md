# Install and use with Gemini 4 Hydrogen

A Skill configures an **agent host**, not the model binary itself. The same `SKILL.md` works with compatible Gemini 4 Hydrogen experiences when skills are supported by that host.

## Gemini CLI or Google Antigravity (recommended)

**Workspace installation:** The GitHub repo already contains this folder at:
`<repo>/.agents/skills/korean-sds-compliance/SKILL.md`.

Both current Gemini CLI and Antigravity document workspace discovery under `.agents/skills/`. Run Gemini CLI or Antigravity from the cloned repository root (authentication required because the source repo is private). No copy is necessary.

**CLI commands:**
```sh
# Open a terminal in the cloned repository root
gemini
# In interactive Gemini CLI:
/skills reload
/skills list
```

The skill should appear as `korean-sds-compliance`. If activation requires consent, allow it only after verifying what scripts it will access. Run the standalone integrity check:
```sh
python .agents/skills/korean-sds-compliance/scripts/check_sources.py --kb korean
```

Ask Gemini 4 Hydrogen:
> Use the korean-sds-compliance skill to review this Korean MSDS against the supplied 2026-26 notice. Inspect all applicable Annex 4 fields, Annex 5 submission-use codes and Annex 6 information-omission limits. Cite the Korean source and SDS page for every issue, distinguish findings from evidence gaps and do not issue an overall PASS without independent legal and scientific validation.

**Global skills:** Follow Google Antigravity's documented `~/.gemini/config/skills/<skill-name>/` location or Gemini CLI's `~/.gemini/skills/`. The skill still needs `korean/` legal source files available locally or set `KOREAN_SDS_KB` to the directory.

## Gemini app skills

Google's Gemini skills experience may allow creating/importing a `skill.md` file directly. If your account offers **Skills**, use its Create/Import skill flow and paste/upload this `SKILL.md`. The app **does not automatically obtain private GitHub repository content**; upload the relevant legal reference files as additional context or use the agent-host workspace method.

The app experience may not support local Python scripts or repository file access. In that case treat the skill as a careful evidence-review prompt, not a fully automated compliance engine. Report any missing legal files.

## Security

Keep confidential customer SDS and formulations outside public repositories. Do not ask Gemini to publish ingredient lists, government approvals or proprietary recipes. The skill validator is local and does not make network requests.

## References

- Official Gemini CLI Skills documentation: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/using-agent-skills.md
- Official Google Antigravity Skills documentation: https://antigravity.google/docs/skills
- Official Google Gemini Skills guide: https://services.google.com/fh/files/misc/gemini_skills_guide.pdf
