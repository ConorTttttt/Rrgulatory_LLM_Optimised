# Korean SDS regulatory annexes

This directory contains **four separately uploaded annexes** to *화학물질의 분류·표시 및 물질안전보건자료에 관한 기준*, prepared for LLM retrieval and controlled review.

**Received:** 별표 1, 2, 3, 7.  
**Still required:** **별표 4, 5, 6**. Of these, Annex 4 is the priority for detailed requirements inside SDS Sections 1–16.

## Files and status

| Annex | Extracted Korean text | Retrieval | Initial machine-readable checks |
|---|---|---|---|
| 1 — classification criteria | `annex_1.extracted_ko.txt` | `annex_1_rag_chunks.jsonl` | `annex_1_curated_thresholds.json` (18 draft thresholds) |
| 2 — hazard label elements | `annex_2.extracted_ko.txt` | `annex_2_rag_chunks.jsonl` | `annex_2_h_p_phrase_catalog.json` (218 H/P code entries) |
| 3 — label dimensions | `annex_3.extracted_ko.txt` | `annex_3_rag_chunks.jsonl` | `annex_3_label_dimensions.json` (5 container size ranges, 2 pictogram size rules) |
| 7 — trade-secret evidence | `annex_7.extracted_ko.txt` | `annex_7_rag_chunks.jsonl` | `annex_7_trade_secret_evidence_checklist.json` (18 evidence prompts) |

See `annex_sources_manifest.json` for source SHA-256 hashes and legal-version alignment status.

## Important extraction and interpretation restrictions

1. The **original HWP binaries are user-provided source material, not committed in GitHub**. The extracted Korean texts are not facsimiles.
2. HWP table geometry is flattened in text extraction. Some formulas and all pictogram images are not retained as authoritative structured data in these files. In particular, do not assume Annex 2's class-by-class hazard/pictogram table is correctly machine-readable from `.txt` alone.
3. Annex 1 criteria for mixture classification use a hierarchy of whole-mixture testing, bridging principles, and ingredient-based methods; do not apply isolated threshold rules without checking method applicability.
4. The Annex 3 dimensions are objective draft validation rules, but require measured label/container evidence and examination of Article 7 and applicable exceptions.
5. Annex 7 criteria concern **evidence of trade secrecy and need for alternative disclosure**, not proof of regulatory approval. Never infer an approval from a written claim or a missing ingredient name.
6. Uploaded annex filenames do not, by themselves, prove that the files correspond exactly to the **2026-04-24 amended** text. Confirm source revision against the official promulgated record before production use.
7. Annexes **4, 5, 6 remain missing**, and these incomplete extractions do not support an unconditional SDS compliance `PASS`.

## Suggested LLM retrieval order

1. Retrieve the main-body provision and its cross-reference to an Annex.
2. Retrieve the corresponding `annex_N_rag_chunks.jsonl` chunk and check extracted Korean wording.
3. Use the curated machine-readable rules only where their preconditions and evidence can be confirmed.
4. Request exact official HWP/PDF table or image and qualified regulatory review whenever layout, formula, scientific interpretation, or legal exemptions matter.
5. Mark unresolved checks as `NEEDS_REVIEW`, not `PASS`.

**Annex 2 phrase catalogue:** H/P phrases are useful for language checking, not sufficient to determine which symbols or statements a product must display; that mapping requires exact hazard class, category, additional rules and visual verification.
