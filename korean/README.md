# Korean SDS / MSDS compliance — LLM-ready regulatory reference

**Regulatory basis:** 고용노동부고시 제2026-26호, effective 2026-04-24.  
**Source SHA-256:** `785aa6d6585f2b4276eef036ac028eca74f5bddcda9cbfc0a91b5d2712b4eb55` (uploaded HWPX).

This directory provides Korean legal source text, bilingual review rules, a retrieval index, a review prompt, and JSON contracts for preliminary Korean Safety Data Sheet (SDS/MSDS) compliance evaluation.

## Start here

For a simple LLM workflow, use **`SINGLE_FILE_LLM_KNOWLEDGE_BASE.md`** **alongside the separately uploaded Annexes 1, 2, 3 and 7 in [`annexes/`](annexes/README.md)**. Annexes 4, 5, 6 remain missing.

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
| `missing_annex_dependency_manifest.json` | Missing-annex and external-dependency manifest. |
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

**Do not infer an overall PASS merely because the required 16 SDS headings exist.** Complete field-by-field assessment depends on Annex 4 and other requirements.

## Important limits

The original notice **main-body HWPX** includes Articles 1–21 (including Article 6-2) and supplementary provisions, but not Annexes 1–7. **Separate HWP files for Annexes 1, 2, 3 and 7 have now been supplied**, and draft extracted text plus supporting files have been committed to [`annexes/`](annexes/README.md). Annexes **4, 5, 6 are still missing**. Hazard criteria, label details, Annex 4 SDS subfields, mixture concentration limits and trade-secret criteria require additional authoritative materials. The notice also cross-refers to other legislation and technical standards. None of these missing criteria should be guessed.

The first-party source files in this directory (`SINGLE_FILE_LLM_KNOWLEDGE_BASE.md`, `compliance_rules_en_ko.json`, and the extracted Markdown prompt/source/rulebook) were transferred from the original compliance conversion. Secondary machine-readable indexes here have been **regenerated from these primary artifacts**; their provenance, indexing structure and paragraph-offset metadata may differ from the original ZIP export. The supplied HWPX, rather than this repository, is the ultimate reference for the extracted language.

`build.py` validates this repository's snapshot; it is **not** the original HWPX extraction program.

A legal or regulatory expert should confirm actual product applicability, current amendments and final compliance judgments.

## Validation

Run `python korean/build.py --validate` at repository root. To regenerate retrieval chunks and the coverage matrix from the current source Markdown and rules JSON, run `python korean/build.py --refresh-index`.

## Newly added Annexes 1, 2, 3, 7

The `annexes/` directory now includes source-text extracts, source-located retrieval chunks, draft classification thresholds (Annex 1), H/P phrase codes (Annex 2), measurable label size rules (Annex 3), and trade-secret evidence questions (Annex 7). These are **draft review aids**, not certified annex transcriptions. Source HWP SHA-256 metadata is in [`annexes/annex_sources_manifest.json`](annexes/annex_sources_manifest.json).

Because HWP tables, pictograms and formulas can be lost in text extraction, confirm them against official source layout before automated final decisions. Confirm that each annex corresponds to the 2026-26 amendment. Annex 4 is still necessary for section-by-section SDS completion checks.
