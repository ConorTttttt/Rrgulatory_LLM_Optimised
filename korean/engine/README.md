# Korean SDS/MSDS deterministic preflight

The preflight tool is a **conservative, offline, standard-library Python reviewer** for structured SDS evidence. It does **not** issue legal PASS/FAIL decisions.

## Quick start

From the repository root:

```bash
python -m korean.engine.preflight korean/examples/SYNTHETIC_preflight_intake.json > /tmp/sds_preflight.json
python -m unittest discover -s korean/tests -v
python korean/annexes/validate_annexes.py
```

The engine reads the actual committed Annex 3–6 JSON datasets. It **does not** parse PDFs, extract HWP/HWPX, retrieve chemical identities, verify government submissions, or establish an SDS’s legal status. Supply already extracted structured input conforming to `korean/sds_intake.schema.json` (additional optional input keys are documented below).

Checks are deterministic:
- **Annex 4:** all 16 numbered sections, their physical order, and 97 referenced field/subfield IDs. An extracted text value demonstrates only that text was found, **not** that its content is legally or scientifically adequate. Missing fields require review. Explicit `자료 없음` and `해당 없음` placeholders are flagged for review rather than rejected categorically.
- **Annex 5:** use-code membership in the 79 published entries; whether use-code selection is required depends on Article 11(8) submission context.
- **Annex 6:** known ingredient hazard/category matching, 0.1% versus 1% concentration boundaries, and the lowest *known* applicable threshold, optionally including the Article 11(9) 1% physical-hazard group. Threshold matching is **not** itself a mixture GHS classification or permission to suppress ingredient disclosure.
- **Annex 3:** label size from measured container capacity and side area; pictogram minimum of both 0.5 cm² and 1/40 of label area. Physical evidence and any relevant exceptions remain necessary.
- **Annex 4 / MSDS number:** presence and user-reported first-page placement; actual first-page location and government submission have **not** been verified by code.

### Suggested optional input keys

These extend the intake JSON schema:
- `sds.extraction_complete`: boolean asserting that every page and section was successfully extracted and checked. If absent, missing headings/fields mean **NOT_ASSESSED**, not a confirmed omission.
- `sds.section_fields`: array of `{field_id, section_no, source_text, source_page?}`; IDs must match `annex_4_sds_field_requirements.json` exactly.
- `product.is_submission_context`: Boolean provided by a reviewer, not inferred by this script.
- `product.annex_5_use_codes`: array of selected codes as strings (e.g. `["8.1"]`).
- `components[].actual_pct`: numeric mass percentage known from authorised product evidence (not merely an SDS range).
- `components[].confirmed_hazard_categories`: array of `{hazard_name_ko, category, classification_source?}` with hazard names from Annex 6.
- `components[].physical_hazard_group_under_rule_annex_18_1a`: Boolean only after reviewer verification of the external implementing-rule hazard group.
- `label.container_capacity_liters`, `printed_label_area_cm2`, `exterior_side_surface_area_cm2`, `pictogram_areas_cm2`: actual measurements.
- `msds_submission.submission_number` and `document_number_on_first_page`: claimed submission number and observed location.

## Output and legal safeguards

The JSON report **always** contains `overall_status: NEEDS_REVIEW` and `legal_compliance_determined: false`. Its `observation` codes are evidence-check results, not legal compliance grades. A human reviewer must examine applicability, approval documents, authoritative full HWP tables/graphics, scientifically validated classification data and any legislative amendments before a formal compliance conclusion.

### Data security

Do not commit proprietary SDS data, complete formulas, confidential ingredient lists, or trade-secret approval files to the repository or synthetic tests. The CLI processes local files offline without transmitting input to external services.

### Testing

The automated GitHub Actions workflow runs the existing main-body and annex structural validators plus the synthetic regression tests. The regression tests cover missing/duplicate/out-of-order sections, placeholders, unknown use codes, the Annex 6 thresholds at exact 0.1% and 1% boundaries, overlapping hazards, label-size boundaries and unsupported final-PASS prevention.

**Remaining quality gates:** independently verify the uploaded annex HWP revisions, reconstruct and visually check formulas and pictograms, obtain cross-referenced legal provisions, and benchmark using regulator-reviewed real SDS examples.
