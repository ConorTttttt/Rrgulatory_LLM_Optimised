# Korean SDS knowledge-base source map

**Korean-specific routing:** Start at [`korea-first-requirements.md`](korea-first-requirements.md) and `assets/korean-requirement-matrix.json` before reading general hazard-classification data. The official anchor for the Korean notice is https://www.law.go.kr/admRulLsInfoP.do?admRulSeq=2100000278320. The notice cites the Industrial Safety and Health Act, its Enforcement Decree and Enforcement Rule, which are **additional mandatory legal evidence when the assessment depends on those provisions**. Do not invent their text if missing.



Use this guide to locate the **actual Korean evidence**. Do not treat the skill itself as legal source text.

## Required primary files (workspace-root relative)

| Purpose | Source path | Notes |
|---|---|---|
| Notice main-body text | `korean/regulation_full_structured_ko.md` | 22 indexed article headings and 131 provision entries; original Korean |
| Source-index JSON | `korean/regulation_full_structured_ko.json` | Derived; original paragraph offsets may be absent |
| Base compliance rules | `korean/compliance_rules_en_ko.json` | 60 rules; English descriptions secondary to Korean source |
| Review instruction compatibility | `korean/LLM_SYSTEM_PROMPT.md` | Additional project guidance; obey this skill's stricter evidence guardrails |
| Annex source manifest | `korean/annexes/annex_sources_manifest.json` | **All seven uploaded**, but each is still `layout_and_math_validated=false` |
| Pre-existing manifest | `korean/missing_annex_dependency_manifest.json` | Historical name; now indicates annexes supplied, not production-ready |
| Report schema | `korean/compliance_report.schema.json` | Output status enum: PASS / FAIL / NEEDS_REVIEW / NOT_APPLICABLE |
| Intake schema | `korean/sds_intake.schema.json` | Extracted SDS evidence contract; input fields may be null or incomplete |

## Annexes

| Annex | Regulatory role | Read first | Special cautions |
|---|---|---|---|
| **별표 1** | Hazard and mixture classification | `korean/annexes/annex_1.extracted_ko.txt`; `annex_1_curated_thresholds.json` | Curated thresholds are incomplete; formulas/whole-mixture decision trees require original visuals |
| **별표 2** | Label elements, pictograms, H/P text | `annex_2.extracted_ko.txt`; `annex_2_h_p_phrase_catalog.json` | 218 text-code entries; images and wide-table associations unverified |
| **별표 3** | Warning label dimensions | `annex_3_label_dimensions.json` | Five capacity bands, two pictogram criteria; measured label images needed |
| **별표 4** | SDS Section 1–16 field inventory | `annex_4_sds_field_requirements.json` | 16 sections; 97 fields/subfields; eight cross-section suggestions; field presence alone insufficient |
| **별표 5** | Product-use vocabulary | `annex_5_use_categories.json` | 48 main plus 31 subcategories; Article 11(8) submission context |
| **별표 6** | Ingredient information concentration limits | `annex_6_concentration_limits.json` | 14 values across 13 hazard headings; **not** GHS mixture classification cutoffs |
| **별표 7** | Trade-secret substantiation | `annex_7_trade_secret_evidence_checklist.json` | 18 prompts; does not constitute trade-secret approval |

For **every annex** also retrieve `korean/annexes/annex_N_rag_chunks.jsonl`, whose chunks are useful for focused text retrieval but are not original HWP facsimiles.

## Source precedence and provenance

- Regulation basis in repository: `고용노동부고시 제2026-26호` dated 2026-04-24.
- The original user-provided notice HWPX included the main body; the Annex HWP files arrived separately.
- Do not assert that all annexes correspond exactly to the promulgated 2026 amendment: **revision alignment has not been independently established**.
- Do not claim to have verified the binary HWP source integrity just because a SHA-256 appears in metadata; original binaries are not committed to the repository.
- Annex 2 pictograms, Annex 1 graphical equations, source table geometry and actual SDS visuals may require separate image/layout review.
- External OSH Act, enforcement rules (especially Rule Annex 18), regulatory lists and product data are needed when referenced. Absence -> `NEEDS_REVIEW` for dependent findings.
- Legal citations: prefer `legal_sources[].verbatim_ko`, exact subsection from notice and `source_text_ko` from the annex. Do not cite filenames as substitutes for a legal provision.

## Work without repository access

If installed in a different folder or Gemini app, supply `KOREAN_SDS_KB` (local agents) or upload the actual Korean source files (Gemini app). A remote URL to a private GitHub repo is **not proof** the agent can read those files. Tell the user which exact sources you need.
