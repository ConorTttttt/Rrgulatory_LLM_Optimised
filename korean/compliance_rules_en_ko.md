# Korean SDS compliance rules — 고용노동부고시 제2026-26호

**Interpretation:** Authoritative text is in `regulation_full_structured_ko.md`. Rules below are English operationalisations linked to exact Korean provisions. Missing annexes cannot be inferred. `FAIL` is not a substitute for `NEEDS_REVIEW`.

## CLASSIFICATION

### CLASS-001: Chemical and mixture classification must use Annex 1 detailed criteria

- **Source:** 제4조제1항, 제12조제1항제1호
- **Test:** Annex 1 text and curated examples are now available; verify against the original HWP classification tables, formula objects, mixture hierarchy, test data and exceptions before any product hazard categorization. Never infer from name/CAS alone.
- **When:** Material is within the scope of this provision.
- **Inputs:** classification_data, supporting_studies, annex_1_text
- **Method:** external
- **External sources required:** 별표 1, 규칙 별표 18

### CLASS-002: Testing standards for classification refer to UN GHS guidance

- **Source:** 제4조제2항
- **Test:** If test-based classification is disputed, request specific test reports and current referenced UN GHS guidance.
- **When:** Material is within the scope of this provision.
- **Inputs:** test_reports, un_ghs_reference
- **Method:** expert
- **External sources required:** UN GHS

## CONFIDENTIALITY

### CBI-001: Certain hazardous substances cannot use alternative-name/content protection.

- **Source:** 제16조제1호, 제16조제2호, 제16조제3호, 제16조제4호, 제16조제5호, 제16조제6호
- **Test:** Screen prohibited manufacture, permit-only, regulated hazardous agents, exposure monitoring, health exam and registration-rule categories before permitting confidential-substance substitution.
- **When:** Material is within the scope of this provision.
- **Inputs:** component_regulatory_categories, proposed_confidentiality_claim
- **Method:** external
- **External sources required:** 법 제117조, 법 제118조, 산업안전보건기준에 관한 규칙 제420조, 규칙 별표 21, 규칙 별표 22, 화학물질의 등록 및 평가 등에 관한 법률 시행규칙 제35조제3항

### CBI-002: Confidentiality application evidence and necessity judged under Annex 7.

- **Source:** 제17조제1항, 제17조제2항
- **Test:** Annex 7 trade-secret substantiation criteria are available as evidence prompts, but no legal approval or sufficiency can be inferred without actual case documents, approval decisions and applicable exceptions.
- **When:** Material is within the scope of this provision.
- **Inputs:** confidentiality_application, annex_7_text, approval_result
- **Method:** external
- **External sources required:** 별표 7

### CBI-003: Substitute chemical names must follow cited Environment Ministry method or KOSHA method where inapplicable.

- **Source:** 제17조제3항, 제17조제4항
- **Test:** Validate only with the referenced environmental notice and possibly KOSHA methods.
- **When:** Material is within the scope of this provision.
- **Inputs:** alternative_name, chemical_structure_available, external_naming_standard
- **Method:** external
- **External sources required:** 환경부 고시 (자료보호신청서...), 공단 기준

### CBI-004: Protected content concentration ranges have ±10pp when actual <25% and ±20pp when actual >=25%.

- **Source:** 제17조제5항, 제17조제5항제1호, 제17조제5항제2호
- **Test:** Apply ONLY to an approved/confidentiality-application substitute-content field; do not replace general §11(10) ±5pp rule. Compare bounds with actual concentration if evidence provided.
- **When:** Material is within the scope of this provision.
- **Inputs:** actual_ingredient_percent, alternative_concentration_range, approval_status
- **Method:** context

### CBI-005: SDS adequacy review for alternative disclosure focuses on sections 2,3,9,11,12,15 and credible external data.

- **Source:** 제17조제6항, 제17조제6항제1호, 제17조제6항제2호
- **Test:** For an approval assessment, request full corresponding sections and relevant independent scientific references.
- **When:** Material is within the scope of this provision.
- **Inputs:** sds_sections_2_3_9_11_12_15, approval_review_sources
- **Method:** expert

### CBI-006: SDS must reflect full/partial/refused substitution decisions; when approved include approval ID, validity and alternative info.

- **Source:** 제18조제1항, 제18조제1항제1호, 제18조제1항제2호, 제18조제1항제3호
- **Test:** Compare each concealed ingredient against written approval result; full approval: number+term+substitute fields; partial: do so only for allowed and disclose denied; refusal: disclose non-substituted info.
- **When:** Material is within the scope of this provision.
- **Inputs:** sds_section_3, authority_approval_letter, approval_number, approval_validity, ingredient_decision_outcomes
- **Method:** context

### CBI-007: Applicant must reflect SDS adequacy review changes after approval notification.

- **Source:** 제18조제2항
- **Test:** Cross-check required alterations in official review result versus current SDS.
- **When:** Material is within the scope of this provision.
- **Inputs:** authority_review_outcome, sds_revision
- **Method:** context

### CBI-008: If authorised requester asks for underlying identity/content, provide it directly or by Art. 13(1) channel.

- **Source:** 제20조
- **Test:** Assess request and delivery record; cannot infer from published SDS alone.
- **When:** Material is within the scope of this provision.
- **Inputs:** authorised_request, underlying_ingredient_details, delivery_record
- **Method:** context
- **External sources required:** 법 제112조제10항

## DISTRIBUTION

### DISTR-001: Supplier provides warning label item data at transfer, potentially by SDS if included.

- **Source:** 제9조제1항
- **Test:** Review transfer event and transmission evidence; an SDS containing those items can satisfy delivery method.
- **When:** Material is within the scope of this provision.
- **Inputs:** delivery_records, label_information_delivered, sds_provided
- **Method:** context
- **External sources required:** 법 제115조제1항

### DISTR-002: Repeated supply of same material to same recipient does not require resending unchanged label information, unless requested.

- **Source:** 제9조제2항
- **Test:** Check first delivery, no changes, and no request for duplicate document.
- **When:** Material is within the scope of this provision.
- **Inputs:** recipient, product, first_delivery_record, content_changed, recipient_request
- **Method:** context

### DISTR-003: SDS may be delivered by registered mail or specified electronic channels; supplier confirms receipt.

- **Source:** 제13조제1항
- **Test:** Review dispatch mode, direct file/storage accessibility and recipient acknowledgement.
- **When:** Material is within the scope of this provision.
- **Inputs:** transfer_event, dispatch_channel, receipt_confirmation
- **Method:** context
- **External sources required:** 규칙 제160조제1항

### DISTR-004: Supplier of non-classified material issues written non-classification notice or SDS including that fact.

- **Source:** 제13조제2항
- **Test:** Applicability and classification require Rule Annex 18; check a written declaration or SDS statement.
- **When:** Material is within the scope of this provision.
- **Inputs:** classified_under_rule_annex_18, written_notice_or_sds
- **Method:** external
- **External sources required:** 규칙 별표 18제1호

### DISTR-005: Supplier and receiving party retain written non-classification notice onsite.

- **Source:** 제13조제3항
- **Test:** Check record-retention location when the Article 13(2) notice applies.
- **When:** Material is within the scope of this provision.
- **Inputs:** written_notice_record, onsite_retention
- **Method:** context

### DISTR-006: Principal contracting out manufacturing supplies submitted SDS or confidentiality approval outcome to contractor.

- **Source:** 제13조제4항
- **Test:** When Article 2(1)(3)(b) commissioning arrangement applies, confirm delivery of SDS or approval outcome.
- **When:** Material is within the scope of this provision.
- **Inputs:** is_contract_manufacturing, principal_submission_or_approval, contractor_delivery
- **Method:** context

## LABEL

### LABEL-001: Supplier-provided container/packaging warning labels are in Korean.

- **Source:** 제5조제1항
- **Test:** Inspect the actual label on container and packaging; bilingual allowed, foreign-worker additional language allowed.
- **When:** Material is within the scope of this provision.
- **Inputs:** label_image_or_text, container_label, packaging_label, transfer_role
- **Method:** label
- **Exceptions:** Article 5(2), (3) exceptions

### LABEL-002: Foreign-language labels need not be translated for laboratory testing/research reagents and exports in storage/transit.

- **Source:** 제5조제2항
- **Test:** Require documented context before applying language exemption; export condition refers to finished products in storage/transport for export.
- **When:** Material is within the scope of this provision.
- **Inputs:** is_lab_test_research_reagent, is_finished_product_export_storage_transport, label_language
- **Method:** context

### LABEL-003: UN RTDG labeling may alter package/drum requirements.

- **Source:** 제5조제3항, 제5조제4항
- **Test:** Check if the regulated material is marked in accordance with RTDG and whether packaging vs unpackaged drums, then review icon requirements.
- **When:** Material is within the scope of this provision.
- **Inputs:** rtdg_marking_applied, packaging_type, container_label
- **Method:** external
- **External sources required:** UN RTDG

### LABEL-004: Printed tag may substitute where label affixing/printing is difficult.

- **Source:** 제5조제5항
- **Test:** Verify actual difficulty and attached printed tag rather than accepting no hazard communication.
- **When:** Material is within the scope of this provision.
- **Inputs:** difficult_to_attach_or_print, tag_image
- **Method:** context

### LABEL-005: Employer must verify and affix missing warning labels before use/transport/storage.

- **Source:** 제5조제6항
- **Test:** Check employer workflow or inspection record, not solely SDS content.
- **When:** Material is within the scope of this provision.
- **Inputs:** employer_receipt_inspection, actual_label_present
- **Method:** context

### LABEL-006: Pictograms, signal words, H/P statements are determined by Annex 2.

- **Source:** 제6조제1항
- **Test:** Annex 2 now provides Korean H/P code text, but its flattened visual tables/pictograms are unverified. Cross-check category-to-statement/pictogram mapping against authoritative original layout before a PASS/FAIL determination.
- **When:** Material is within the scope of this provision.
- **Inputs:** classification_data, label_text, annex_2_text
- **Method:** external
- **External sources required:** 별표 2

### LABEL-007: Very small contents <=100g or <=100mL may use reduced label fields.

- **Source:** 제6조제2항
- **Test:** If declared amount <=100g or <=100mL, permit product name, pictograms, signal word, and supplier details only; verify ALL these remain.
- **When:** Material is within the scope of this provision.
- **Inputs:** net_mass_g, net_volume_ml, label_elements
- **Method:** label

### LABEL-008: In-house intermediate process containers may display only Danger or Warning IF nearby label or posted SDS present.

- **Source:** 제6조제3항
- **Test:** Confirm vessel is intermediate non-permanent inter-process transfer in same workplace AND visible warning label at storage site OR posted SDS.
- **When:** Material is within the scope of this provision.
- **Inputs:** is_intermediate_process_container, process_context, site_posted_label_or_sds, label_elements
- **Method:** context

### LABEL-009: Label product name must match SDS Section 1.

- **Source:** 제6조의2제1항
- **Test:** Compare semantic product identifier exactly or document justified equivalent alias.
- **When:** Material is within the scope of this provision.
- **Inputs:** sds_section_1_name, label_product_name
- **Method:** deterministic

### LABEL-010: Display all required Annex 2 pictograms subject to precedence and >=5 rule.

- **Source:** 제6조의2제2항, 제6조의2제2항제1호, 제6조의2제2항제2호, 제6조의2제2항제3호, 제6조의2제2항제4호
- **Test:** Apply skull-over-exclamation; corrosion-over-skin/eye irritation; respiratory sensitizer-over-skin sensitization/skin/eye irritation; when >=5 applicable, 4 may be shown. Annex 2 remains necessary.
- **When:** Material is within the scope of this provision.
- **Inputs:** hazard_classifications, selected_pictograms, annex_2_text
- **Method:** external
- **External sources required:** 별표 2

### LABEL-011: Only Danger should be displayed if both Danger and Warning apply.

- **Source:** 제6조의2제3항
- **Test:** Compare hazard-specific Annex 2 signals to actual label; only Danger if mixed levels, else applicable signal word.
- **When:** Material is within the scope of this provision.
- **Inputs:** hazard_signals, label_signal_word, annex_2_text
- **Method:** external
- **External sources required:** 별표 2

### LABEL-012: All applicable hazard statements on label; duplicate may be omitted and similar may be combined.

- **Source:** 제6조의2제4항
- **Test:** Require mapping from classification to H statements; count equivalents and do not confuse permitted combination with arbitrary deletion.
- **When:** Material is within the scope of this provision.
- **Inputs:** hazard_statements_required, label_hazard_statements, annex_2_text
- **Method:** external
- **External sources required:** 별표 2

### LABEL-013: All relevant precautionary statements, with specific 7+ label reduction conditions.

- **Source:** 제6조의2제5항, 제6조의2제5항제1호, 제6조의2제5항제2호
- **Test:** If 7 or more, 6 may be displayed including >=1 from prevention, response, storage and disposal wherever those groups exist. Omitted statement(s) must be directed to the SDS. Duplicate/combinable statements exception allowed.
- **When:** Material is within the scope of this provision.
- **Inputs:** precautionary_statements_required, label_precautionary_statements, label_sds_reference, annex_2_text
- **Method:** external
- **External sources required:** 별표 2

### LABEL-014: H/P codes are optional alongside actual statements.

- **Source:** 제6조의2제6항
- **Test:** Never accept an H or P code alone as the written statement solely based on this clause.
- **When:** Material is within the scope of this provision.
- **Inputs:** label_hazard_statements, label_precautionary_statements, label_codes
- **Method:** label

### LABEL-015: Warning label format and size subject to Annex 3.

- **Source:** 제7조
- **Test:** Annex 3 dimensional thresholds are available as draft structured rules. Compare actual container capacity, measured label area and pictogram areas to the appropriate criteria; inspect applicable exceptions and source layout.
- **When:** Material is within the scope of this provision.
- **Inputs:** label_image, label_dimensions, annex_3_text
- **Method:** external
- **External sources required:** 별표 3

### LABEL-016: Label background white; font and border black unless specific exception.

- **Source:** 제8조제1항
- **Test:** Inspect label imagery or printable artwork, not just SDS text.
- **When:** Material is within the scope of this provision.
- **Inputs:** label_image
- **Method:** image
- **Exceptions:** Article 8(2) container/background exception

### LABEL-017: Label background may use container/packaging background if white impracticable; use contrast when very dark.

- **Source:** 제8조제2항
- **Test:** Assess actual background and readability.
- **When:** Material is within the scope of this provision.
- **Inputs:** label_image, white_impracticable, container_color
- **Method:** image

### LABEL-018: GHS symbol black, red border and white pictogram ground as a rule; specific small-container color exception.

- **Source:** 제8조제3항
- **Test:** Check actual symbol colors; <=1L with direct print and <=2 surface colors may use main nonblack packaging color as pictogram ground.
- **When:** Material is within the scope of this provision.
- **Inputs:** label_image, container_volume_l, direct_print, packaging_surface_color_count
- **Method:** image

### LABEL-019: Warning label fixed securely and visible to workers during use.

- **Source:** 제8조제4항
- **Test:** Verify actual container location and attachment.
- **When:** Material is within the scope of this provision.
- **Inputs:** site_photo, container_location, affixation_quality
- **Method:** context

## MIXTURE

### MIX-001: If whole-mixture physical hazard testing was not performed, single-substance data may be used to evaluate potential physical hazards.

- **Source:** 제12조제1항제2호
- **Test:** If mixture test absent, do not automatically fail; document component-level assessment and technical rationale.
- **When:** Material is within the scope of this provision.
- **Inputs:** mixture_whole_physical_tested, ingredient_physical_hazard_data, assessment_rationale
- **Method:** expert

### MIX-002: One representative SDS can cover multiple mixture products only if all 3 Article 12(2) criteria are met.

- **Source:** 제12조제2항, 제12조제2항제1호, 제12조제2항제2호, 제12조제2항제3호
- **Test:** Require same ingredients (subject to limited fragrance/pigment exception), ingredient concentration changes <=10 percentage points, and similar hazards. Check ALL conditions, not any one.
- **When:** Material is within the scope of this provision.
- **Inputs:** grouped_product_sds, product_group_composition, concentration_delta_pp, hazard_profiles
- **Method:** context

### MIX-003: Fragrance/perfume/pigment exception to shared composition requires total <=5% and only those ingredients to change.

- **Source:** 제12조제2항제1호가목, 제12조제2항제1호나목
- **Test:** Check summed perfume/fragrance/pigment share <=5% and verify other component identities unchanged between products.
- **When:** Material is within the scope of this provision.
- **Inputs:** grouped_product_sds, fragrance_pigment_fraction, non_fragrance_composition_changed
- **Method:** context

### MIX-004: A representative SDS must distinguish product-specific components and product-specific hazards where needed.

- **Source:** 제12조제3항
- **Test:** For qualifying product groups, verify section 3 identifies per-product composition for fragrance exception and hazards differentiated per product under similar-hazard grouping.
- **When:** Material is within the scope of this provision.
- **Inputs:** grouped_product_sds, sds_section_3, product_specific_hazards
- **Method:** document

## SCOPE

### SCOPE-001: Determine whether the material can be excluded under Article 3.

- **Source:** 제3조
- **Test:** Do not claim exclusion for a mixture produced only by re-mixing received chemicals when the mixture is supplied to others OR a chemical reaction generates a changed chemical. Check the other listed exclusions separately.
- **When:** Material is within the scope of this provision.
- **Inputs:** product_lifecycle, mixture_manufacturing_process, transfer_to_others, chemical_reaction, exposure_potential, special_management_substance_flag
- **Method:** context
- **External sources required:** 영 제86조, 제19조, 산업안전보건기준에 관한 규칙 제420조

### SCOPE-002: Special conditions governing re-mixed product exclusion

- **Source:** 제3조제1호, 제3조제1호가목, 제3조제1호나목
- **Test:** Mark potentially excluded ONLY when created by mixing received substances again and neither transferred to another party nor chemically transformed.
- **When:** Material is within the scope of this provision.
- **Inputs:** is_remixed_from_received_materials, is_transferred, changes_via_reaction
- **Method:** context

### SCOPE-003: Research intermediate exclusion

- **Source:** 제3조제2호
- **Test:** Check whether intermediate chemical or mixture was generated during research/development per Art. 19; record evidence.
- **When:** Material is within the scope of this provision.
- **Inputs:** research_use, is_intermediate, article_19_context
- **Method:** context
- **External sources required:** 제19조

### SCOPE-004: Finished articles no-exposure exclusion

- **Source:** 제3조제3호
- **Test:** Review whether an article in its finished form entails no exposure during work; exemption is inapplicable where special management substances are contained.
- **When:** Material is within the scope of this provision.
- **Inputs:** is_finished_article, worker_exposure_foreseeable, special_management_substance_flag
- **Method:** context
- **External sources required:** 산업안전보건기준에 관한 규칙 제420조제6호

### RND-001: R&D chemical/product criteria given in 5 enumerated types.

- **Source:** 제19조, 제19조제1호, 제19조제2호, 제19조제3호, 제19조제4호, 제19조제5호
- **Test:** Use the article 19 examples when deciding regulatory R&D context; do not assume all commercial scale-up qualifies.
- **When:** Material is within the scope of this provision.
- **Inputs:** r_and_d_purpose, r_and_d_use_records
- **Method:** context
- **External sources required:** 영 제86조제17호

## SDS_COMPLETENESS

### SDS-006: No SDS writing field may be silently omitted; use prescribed Korean null expressions.

- **Source:** 제11조제7항
- **Test:** For an unfilled field: if unavailable despite efforts, require 자료 없음; if inapplicable, require 해당 없음. Do not confuse absence with a justified exception.
- **When:** Material is within the scope of this provision.
- **Inputs:** sds_fields, field_applicability, information_availability
- **Method:** document

## SDS_COMPOSITION

### SDS-008: Low-concentration component information may be omitted from Article 10 sections only within applicable thresholds.

- **Source:** 제11조제9항
- **Test:** Use Annex 6 concentration limits under Art. 11(9) for potential omission of information on components that meet the implementing-rule hazard group. For implementing-rule Annex 18 §1(a) use the 1% criterion referenced by Art. 11(9); for §1(b) use the appropriate Annex 6 threshold. Where both groups apply, use the LOWER limit. These are composition-information omission limits, not Annex 1 mixture GHS category thresholds. Check actual ingredient concentration, classified hazards, context, exceptions and implementing-rule source before deciding.
- **When:** Material is within the scope of this provision.
- **Inputs:** mixture_component_composition, ingredient_classifications, annex_6_text, enforcement_rule_annex_18
- **Method:** external
- **External sources required:** 규칙 별표 18제1호, 별표 6

### SDS-009: Declared component concentrations may be stated as ranges within ±5 percentage points of real values.

- **Source:** 제11조제10항
- **Test:** For each normal-disclosure concentration range, compare to actual composition if available; bounds should be within actual±5 percentage points. Do not use relative ±5% or apply the separate trade-secret alternative range thresholds.
- **When:** Material is within the scope of this provision.
- **Inputs:** reported_component_range, real_component_concentration
- **Method:** context

## SDS_CURRENCY

### SDS-011: SDS information must be accurate and maintained against current science, technology and law.

- **Source:** 제11조제12항
- **Test:** Request revision history, source dates, and known change triggers; a revision date alone does not establish current scientific accuracy.
- **When:** Material is within the scope of this provision.
- **Inputs:** sds_revision_date, technical_source_dates, regulatory_change_review
- **Method:** expert

## SDS_HAZARDS

### SDS-014: Specific label statement simplifications may be applied to SDS Section 2.

- **Source:** 제6조의2제7항
- **Test:** May apply the pictogram precedences (items 1–3), Danger-over-Warning, duplicate/combined hazard statements and duplicate/combined precautionary statements, but NOT blanket 4-pictogram or six-P-phrase reductions.
- **When:** Material is within the scope of this provision.
- **Inputs:** sds_section_2, hazard_classifications, annex_2_text
- **Method:** external
- **External sources required:** 별표 2

## SDS_INTENDED_USE

### SDS-007: Use category selected from Annex 5 is mandatory when formally submitting the SDS.

- **Source:** 제11조제8항
- **Test:** For the SDS submission scenario in Art. 11(8), require at least one legitimate Annex 5 use code. Outside the specified submission context, the same clause permits optional category selection when preparing the SDS. Do not presume an exemption from product use alone.
- **When:** Material is within the scope of this provision.
- **Inputs:** sds_section_1_use, is_sds_submitted, annex_5_text
- **Method:** external
- **External sources required:** 별표 5, 법 제110조제1항 및 제3항

## SDS_LANGUAGE

### SDS-003: SDS is in Korean as a rule; certain proper names can remain in English.

- **Source:** 제11조제1항
- **Test:** Check main narrative, hazard phrases, safety procedures and sections are in Korean; allow chemical names and foreign organisation names in English.
- **When:** Material is within the scope of this provision.
- **Inputs:** sds_text, sds_language_detected
- **Method:** document
- **Exceptions:** Article 11(2) foreign-language lab testing/research reagent

### SDS-004: Foreign-language laboratory test/research reagent SDS need not be translated.

- **Source:** 제11조제2항
- **Test:** Apply only when evidence shows a reagent used for laboratory testing/research and the SDS was prepared in a foreign language.
- **When:** Material is within the scope of this provision.
- **Inputs:** is_lab_test_research_reagent, sds_original_language
- **Method:** context

## SDS_REGULATION

### SDS-010: Mixture-wide legal requirements must be reported regardless of what components are listed in Section 3.

- **Source:** 제11조제11항
- **Test:** Check section 15 considers regulations applying to whole mixture; do not accept omitted regulatory obligations merely because component identity is absent.
- **When:** Material is within the scope of this provision.
- **Inputs:** sds_section_15, mixture_level_legal_requirements
- **Method:** expert
- **External sources required:** applicable sector legislation

## SDS_SOURCES

### SDS-005: Translated SDS must identify original authoring institution and date; related materials need citations.

- **Source:** 제11조제4항
- **Test:** If translated from a foreign-language SDS, check original issuing institution AND time are given; if other related references are used in authoring, check references are cited.
- **When:** Material is within the scope of this provision.
- **Inputs:** translated_from_foreign_sds, original_authoring_institution, original_creation_date, supporting_references_used, bibliographic_sources
- **Method:** document

### SDS-012: GLP/KOLAS test results should be preferentially considered.

- **Source:** 제11조제3항
- **Test:** When test results used for preparation are submitted, look for GLP/KOLAS basis and explain if others were preferred.
- **When:** Material is within the scope of this provision.
- **Inputs:** supporting_test_reports, test_accreditation
- **Method:** expert
- **External sources required:** GLP, KOLAS

## SDS_STRUCTURE

### SDS-001: SDS must include 16 sections in the prescribed order.

- **Source:** 제10조제1항, 제10조제1항제1호, 제10조제1항제2호, 제10조제1항제3호, 제10조제1항제4호, 제10조제1항제5호, 제10조제1항제6호, 제10조제1항제7호, 제10조제1항제8호, 제10조제1항제9호, 제10조제1항제10호, 제10조제1항제11호, 제10조제1항제12호, 제10조제1항제13호, 제10조제1항제14호, 제10조제1항제15호, 제10조제1항제16호
- **Test:** Normalize section headings based on their meaning, not English numbering alone. The sixteen sections must be identifiable in the given sequence.
- **When:** Material is within the scope of this provision.
- **Inputs:** sds_sections
- **Method:** deterministic

### SDS-002: Detailed subsection and field requirements come from Annex 4.

- **Source:** 제10조제2항
- **Test:** Annex 4 is now available as a draft structured 16-section/97-field checklist. Compare each field and nested subfield with SDS evidence, apply Article 11 treatment of unavailable/not applicable entries and any relevant exceptions; validate source layout and version before production. Additional worker-safety subitems may be included.
- **When:** Material is within the scope of this provision.
- **Inputs:** sds_sections, annex_4_text
- **Method:** external
- **External sources required:** 별표 4

## SDS_UNITS

### SDS-013: SDS measurement units follow applicable Korean measurement law.

- **Source:** 제11조제6항
- **Test:** Review units for consistency and verify with the cited units law if supplied; do not guess legal tolerances.
- **When:** Material is within the scope of this provision.
- **Inputs:** sds_units
- **Method:** external
- **External sources required:** 계량에 관한 법률

## WORKPLACE

### WORK-001: Employer providing electronic SDS access must place reachable active equipment, train users and post lookup instructions.

- **Source:** 제14조제1호, 제14조제2호, 제14조제3호
- **Test:** Verify all three conditions rather than treating an online SDS link alone as sufficient.
- **When:** Material is within the scope of this provision.
- **Inputs:** equipment_location_and_status, worker_training, posted_lookup_instructions
- **Method:** context
- **External sources required:** 규칙 제167조제1항, 법 제114조제2항, 규칙 제168조제1항

### WORK-002: Employer verifies exposed workers can retrieve SDS using the equipment.

- **Source:** 제15조
- **Test:** Request practical validation or training/confirmation records.
- **When:** Material is within the scope of this provision.
- **Inputs:** worker_lookup_proficiency, validation_record
- **Method:** context

