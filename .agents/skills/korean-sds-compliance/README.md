# Korean SDS Compliance Skill for Gemini 4 Hydrogen

This is a reusable, **evidence-first preliminary Korean SDS/MSDS review skill** built using the open Agent Skills `SKILL.md` format. It works in Google Antigravity or Gemini CLI when installed at the repository's `.agents/skills/` path; the `SKILL.md` can also be imported into a supported Gemini Skills interface.

**Main skill:** [`SKILL.md`](SKILL.md)  
**Installation and use:** [`references/installation.md`](references/installation.md)  
**Example tasks:** [`examples/prompts.md`](examples/prompts.md)

## Scope

- Korean MSDS Section 1–16 screening with **Annex 4's 97 field/subfield entries**
- Annex 1 hazard and mixture classification evidence review; Annex 2 H/P language and label guidance
- Annex 3 printed label and pictogram dimension checks, requiring genuine images/measurements
- Annex 5 product-use codes and their submission-specific use
- Annex 6 Article 11(9) ingredient-information thresholds (**not mixture GHS category cutoffs**)
- Annex 7 trade-secret substantiation and official approval evidence
- Cited findings using Korean primary sources and `korean/compliance_report.schema.json`

**Not** a government filing service, official chemical classification certificate, autonomous legal signoff or replacement for a qualified Korean SDS reviewer.

## Usage

From the root of `ConorTttttt/Rrgulatory_LLM_Optimised`:

```bash
python .agents/skills/korean-sds-compliance/scripts/check_sources.py --kb korean
python -m unittest discover -s .agents/skills/korean-sds-compliance/tests -v
```

The read-only checker reports whether all **seven annex extracts**, the **60 original rules**, **131 main-body chunks**, **16 SDS sections and 97 field IDs**, **79 use codes** and **14 concentration threshold records** are structurally accessible. **It does not verify source legal revision, figures/formulas, substance classifications or overall compliance.**

Start Gemini CLI from the repository root, use `/skills reload` then `/skills list`, and ask it to use `korean-sds-compliance` to review a Korean SDS with page-cited findings.

## Knowledge base dependency

This skill references `korean/` in the same private GitHub repository. Copying `SKILL.md` alone provides instructions but **not the legal annex contents**. For a Gemini app skill, upload the relevant Korean reference files separately; don't expect the app to fetch a private repository automatically.

## Confidentiality

Keep client SDSs, proprietary formulations, trade-secret approvals and chemical lists out of public repositories and untrusted logs. Run the included checker locally; it makes no network calls and reads no customer SDS.

## Status

- Skill format and linked repo sources: implemented.
- Read-only source integrity checker and local smoke tests: included.
- Legal source revision / image / HWP table and formula validation: **not independently completed**.
- Chemical-specific compliance decisions: require real product data and qualified regulatory review.
