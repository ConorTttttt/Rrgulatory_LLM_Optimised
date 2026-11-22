# Korean SDS Annexes 1–7 — extracted and structured review aids

All **seven separately uploaded HWP annexes** to `고용노동부고시 제2026-26호` now have Korean text extracts and retrieval chunks in this directory.

## Inventory

| Annex | Purpose | Main structured resource |
|---|---|---|
| **1** | Hazard classifications and mixture methods | [18 curated thresholds](annex_1_curated_thresholds.json) |
| **2** | H/P codes, warning-label statements and pictograms | [218 H/P phrase entries](annex_2_h_p_phrase_catalog.json) |
| **3** | Warning-label dimensions | [5 container capacity bands + 2 pictogram dimensions](annex_3_label_dimensions.json) |
| **4** | Required SDS content for Sections 1–16 | [97 field/subfield checks](annex_4_sds_field_requirements.json), [flat JSONL rules](annex_4_sds_field_rules.jsonl) |
| **5** | Product use vocabulary | [48 primary and 31 subordinate use categories](annex_5_use_categories.json) |
| **6** | Health/environment hazard concentration limits for Article 11 | [14 threshold entries](annex_6_concentration_limits.json) |
| **7** | Evidence of trade secrecy and justification of alternative disclosure | [18 evidence prompts](annex_7_trade_secret_evidence_checklist.json) |

Each annex also has `annex_N.extracted_ko.txt` (Korean text) and `annex_N_rag_chunks.jsonl` (retrieval chunks). The source hashes and exact extraction/verification status are in [`annex_sources_manifest.json`](annex_sources_manifest.json).

### Applicability and classification safeguards

- **Annex 4:** The MSDS submission number is identified at the top of the first page outside the numbered SDS items. Whether a submission-number obligation applies requires checking the underlying law, product role and relevant exceptions. Field presence and completeness are not chemical accuracy.
- **Annex 5:** Article 11(8) says selecting an Annex 5 category is optional for ordinary SDS preparation, but mandatory for the SDS submission context identified in that provision.
- **Annex 6:** Under Article 11(9), use the specified lower concentration threshold where relevant conditions overlap. **Do not conflate these disclosure-information thresholds with Annex 1 GHS mixture classification thresholds.**
- **Annex 1:** Mixture classification methods involve whole-mixture evidence, bridging principles and ingredient-based calculation; individual cutoff examples are not a complete classifier.
- **Annex 2:** Text extraction cannot preserve the pictogram images or reliably preserve wide table-cell alignments. The H/P code glossary is **not** a complete hazard-class-to-label mapping.
- **Annex 3:** Label size rules require measured container/label dimensions and checking any statutory exceptions.
- **Annex 7:** Trade-secret evidence is not proof of an approval decision.

### Verification status

**Uploaded annexes missing: none.** **Production-ready annexes: none have yet passed an independent source-layout/version check.**

The extracted-text copies are not HWP facsimiles. Original HWP binaries are **not committed to GitHub**. Equations, images, table boundaries, exact legal revision and cross-referenced legislation must be verified before production compliance decisions. Qualified reviewers should confirm scientific classifications and trade-secret authorisations.

If no sufficient evidence supports a check, use `NEEDS_REVIEW` rather than a fabricated PASS/FAIL. [View the manifest](annex_sources_manifest.json).
