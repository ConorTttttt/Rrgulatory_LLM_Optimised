# Korean SDS / MSDS compliance — LLM-ready regulatory reference

**Regulatory basis:** 고용노동부고시 제2026-26호, effective 2026-04-24.  
**Source SHA-256:** `785aa6d6585f2b4276eef036ac028eca74f5bddcda9cbfc0a91b5d2712b4eb55` (uploaded HWPX).

This directory provides Korean legal source text, bilingual review rules, a retrieval index, a review prompt, and JSON contracts for preliminary Korean Safety Data Sheet (SDS/MSDS) compliance evaluation.

## Start here

For a simple LLM workflow, use **`SINGLE_FILE_LLM_KNOWLEDGE_BASE.md`** with the **complete Annexes 1–7 reference collection** in [`annexes/`](annexes/README.md). The single-file version preserves the main-body notice only; detailed Annex tables and structured rules reside in `annexes/`.

For a structured compliance pipeline:
1. Load `compliance_rules_en_ko.json` and `regulation_full_structured_ko.md` as evidence-linked references; optionally index `rag_source_chunks.jsonl`.
2. Read `LLM_SYSTEM_PROMPT.md` before evaluating a Korean SDS.
3. Extract SDS input to `sds_intake.schema.json`; use `sds_16_section_index.json` to check the required 16 sections in order.
4. Produce findings conforming to `compliance_report.schema.json`, with literal source provisions, SDS evidence, review limitations and recommended corrections.
5. Have a qualified reviewer check all evidence-dependent, scientific, legal and confidential-ingredient decisions.

## Files

| File | Purpose |
| --- | --- |
| `SINGLE_FILE_LLM_KNOWLEDGE_BASE.md` | Consolidated LLM instructions, Korean provisions, operational rules. |
| `compliance_rules_en_ko.json` | 60 structured bilingual compliance rules. |
| `compliance_rules_en_ko.md` | Human-readable rulebook derived from the single-file knowledge base. |
| `regulation_full_structured_ko.md` | Korean legal provisions with source IDs and citations. |
| `regulation_full_structured_ko.json` | Article/provision JSON index regenerated from the exact Korean provision lines. |
| `rag_source_chunks.jsonl` | 131 legal-provision chunks linked to rules for retrieval. |
| `coverage_matrix.json` | Article-to-rule coverage index. |
| `sds_16_section_index.json` | Article 10(1) required SDS section names. |
| `missing_annex_dependency_manifest.json` | Annex availability, extraction quality and other external-dependency manifest. |
| `LLM_SYSTEM_PROMPT.md` | Ready-to-use assessor instructions and guardrails. |
| `sds_intake.schema.json` | Suggested structured input format. |
| `compliance_report.schema.json` | Required output schema with evidence and decision statuses. |
| `SYNTHETIC_example_compliance_report.json` | Clearly fictional report demonstrating FAIL and NEEDS_REVIEW. |
| `build.py` | Local consistency validator and retrieval-index rebuild utility. |

## Decision statuses

- `PASS`: sufficient evidence and all applicable criteria actually verified.
- `FAIL`: positive evidence of a specific noncompliance with no established exception.
- `NEEDS_REVIEW`: unavailable legal references, insufficient evidence, scientific ambiguity or missing inputs.
- `NOT_APPLICABLE`: the requirement genuinely does not apply with documented justification.

**Do not infer an overall PASS merely because the required 16 SDS headings exist.** Annex 4's field inventory is now available, but chemical accuracy, exemptions, source-layout details, cross-laws and product evidence must still be verified.

## Important limits

The uploaded notice's original **main-body HWPX** does not embed Annexes 1–7, but **all seven annexes have now been uploaded separately** and their text and structured review aids are in [`annexes/`](annexes/README.md). This enables detailed draft SDS field, use-code and concentration-threshold checking. The HWP annexes' effective revision, embedded illustrations and formula/layout fidelity have not been independently verified; cross-referenced laws and scientific evidence remain additional dependencies.

The first-party source files in this directory (`SINGLE_FILE_LLM_KNOWLEDGE_BASE.md`, `compliance_rules_en_ko.json`, and the extracted Markdown prompt/source/rulebook) were transferred from the original compliance conversion. Secondary machine-readable indexes here have been **regenerated from these primary artifacts**; their provenance, indexing structure and paragraph-offset metadata may differ from the original ZIP export. The supplied HWPX, rather than this repository, is the ultimate reference for the extracted language.

`build.py` validates this repository's snapshot; it is **not** the original HWPX extraction program.

A legal or regulatory expert should confirm actual product applicability, current amendments and final compliance judgments.

## Validation

Run `python korean/build.py --validate` at repository root. To regenerate retrieval chunks and the coverage matrix from the current source Markdown and rules JSON, run `python korean/build.py --refresh-index`.


## Deterministic review engine (new)

The [`engine/preflight.py`](engine/preflight.py) program is an **offline preliminary reviewer**, not a legal decision-maker. It reads the existing Annex 3–6 structured files, checks section order and extracted field coverage, matches Annex 5 use codes, compares known Annex 6 thresholds, and checks label dimensions using measured evidence.

**Run from the repository root:**

```bash
python -m korean.engine.preflight korean/examples/SYNTHETIC_preflight_intake.json > preflight-output.json
python -m unittest discover -s korean/tests -p "test_*.py" -v
python korean/annexes/validate_annexes.py
```

The preflight output conforms to [`engine/preflight_report.schema.json`](engine/preflight_report.schema.json) and **always** marks `overall_status: NEEDS_REVIEW` and `legal_compliance_determined: false`. This is intentional: observed presence is not information quality, and concentration-cutoff matching does not imply regulatory permission or an accurate GHS mixture classification. Detailed usage is in [`engine/README.md`](engine/README.md).

An automated [GitHub Actions QA workflow](../.github/workflows/korean-validation.yml) has been added to run the main-body and annex validators, the synthetic regression suite and JSON/JSONL syntax checks. A CI badge is not evidence of legal validation, and actual runner availability must be confirmed separately.

Use `korean/private_sds/`, `korean/private_intake/` or `korean/private_reports/` for confidential local files (excluded by `korean/.gitignore`); never commit actual confidential formulations or trade-secret approval documents.

## Annexes 1–7 — complete source collection (draft extractions)

All seven user-supplied HWP annexes are now represented in [`annexes/`](annexes/README.md). Primary additions:

- **Annex 4:** [16-section, 97-field SDS checklist](annexes/annex_4_sds_field_requirements.json) and [one-rule-per-line data](annexes/annex_4_sds_field_rules.jsonl), including first-page MSDS-number placement and eight cross-section checks.
- **Annex 5:** [48 use categories and 31 subcategories](annexes/annex_5_use_categories.json), with Korean descriptions and original English terms preserved.
- **Annex 6:** [14 concentration-limit entries](annexes/annex_6_concentration_limits.json) covering 13 hazard headings and the separate mutagenicity categories. These are Article 11 composition-information thresholds, **not** general Annex 1 mixture-classification cutoffs.

The original 60-rule JSON remains the cross-referenced base and now points assessors to the newly available annex-derived datasets. Read [the annex source manifest](annexes/annex_sources_manifest.json) before making compliance claims.

**No annex is missing as an uploaded source; verification is still incomplete.** For legal-grade conclusions, verify the official version of each HWP and any diagrams, tabular alignment, formulas, effective dates, other governing laws, product facts and qualified scientific review.
