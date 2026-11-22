# Korean MSDS/SDS assessment procedure

The objective is an **auditable preliminary report**. Do not treat a file conversion or script run as compliance certification.

## A. Intake

1. Record `document_id`, original file, language, creation/revision dates, and whether the product SDS is Korean or translated.
2. Identify manufacturer's/importer's/supplier's role, product type, mixture status, intended uses, document-submission context and scope (document / label / operations).
3. Record whether original HWP/PDF page images are accessible; preserve evidence `page`, `section`, verbatim text, field ID, extraction confidence and any suspected extraction errors.
4. Determine applicable legal revision and any transitional arrangements from an **official** record. Do not silently treat 2026-26 as necessarily controlling for every past or future date.

## B. Detailed SDS completeness — Annex 4

- Locate 16 numbered sections in legal order. Match section semantics, not only English headings.
- Read `korean/annexes/annex_4_sds_field_requirements.json`; map each `field_id` to relevant SDS material.
- Distinguish **not found**, **present with content**, **explicit `자료 없음`**, **explicit `해당 없음`**, **unreadable** and **not applicable with legal basis**. These are observations, not verdicts.
- Inspect special entries: Section 1 Korean domestic contact for imports; Section 2 hazard and labelling; Section 3 chemical name, synonym, CAS/ID, concentration, conditional trade-secret approval; Section 8 PPE; Section 9 physical properties; Section 11 routes and toxicological endpoints; Section 14 marine pollutant label; Section 15 Korean laws; Section 16 dates and sources.
- Check MSDS submission-number presence/location on the first page, but only judge legal requirement after verifying submission applicability and supporting law.
- Check cross-section contradictions: Sections 2↔3, 2↔9, 2↔11/12; product ↔ label name; transport ↔ classification; exposure controls ↔ hazards. Flag scientific contradictions for expert review.

## C. Annex 5 use codes

Consult all 79 codes (`48 + 31`) in `annex_5_use_categories.json`. Test whether the SDS's stated use maps to an existing code. Do not guess a code for vague product uses; request intended use. At least one Annex 5 selection is a submission-specific duty under Article 11(8).

## D. Annex 6 composition information thresholds

1. Confirm applicability of Article 11(9), the implementing-rule hazard group and actual ingredient percentage; verify hazard type and category.
2. Retrieve matched Annex 6 entry (e.g. `KR-A6-04` respiratory sensitisation 0.1%; `KR-A6-06-2` germ-cell mutagenicity category 2, 1%).
3. If multiple relevant conditions apply, verify and use the lowest applicable threshold.
4. Comparison outcomes: `ABOVE_OR_EQUAL_DISCLOSURE_THRESHOLD`, `BELOW_THRESHOLD_REQUIRES_OTHER_HAZARDS_CHECK`, or `INSUFFICIENT_EVIDENCE`. These are **preliminary observations**, not legal PASS/FAIL and not hazard classification.

## E. Labels, trade secrets, and operations (as requested)

- Annex 2 maps chemical classifications to Korean hazard statements and physical label items; **pictogram mapping remains visually unverified**.
- Annex 3 relates actual physical container and pictogram size to minimum printed area; original label photo measurements are required.
- Annex 7 lists evidence supporting confidentiality/necessity; require separate actual government decision and valid approved substitute details.
- Storage, worker access and workplace SDS posting obligations need operational evidence and statutes; they cannot be inferred from an SDS attachment alone.

## F. Reporting

Read the exact `korean/compliance_report.schema.json` before producing JSON; don't invent missing required keys or enums. At a minimum provide:
- Document ID, legal/revision basis, requested review scope and scope result
- Summary (Korean if the user prefers)
- Per-check results and source citations with SDs page/section locations
- Missing input list and required external legal checks
- Explicit `annexes_not_provided=[]` only when **actual annex sources were accessible** for the assessment, not merely named in the repo
- `annex_review_summary` showing whether **each annex** was actually consulted, partial, or not assessed, and source-layout/revision verification flags
- `out_of_scope_checks` separate from `NOT_APPLICABLE`
- Conservative overall outcome and list of questions for qualified reviewer

## Worked scenarios for safety

- **All 16 headings present; Annex 4 subfields unreadable:** Report *structural heading presence* and `NEEDS_REVIEW`, not PASS.
- **Hazard class from CAS alone:** Report `NEEDS_REVIEW`; CAS is not hazard evidence.
- **0.05% respiratory sensitiser with no other hazard evidence:** Report below the 0.1% Annex 6 threshold **for that hazard only** and unresolved other hazards, not "composition lawful to omit".
- **No MSDS number printed:** Record observation; obtain relevant submission evidence/exemption before any regulatory FAIL.
- **Section 3 uses alternative component name without approval documentation:** Flag approval-evidence gap; do not assume trade-secret authorization.
