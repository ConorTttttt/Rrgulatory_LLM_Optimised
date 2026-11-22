# LLM knowledge base: Korean SDS compliance, 2026-26

## Source limits and annex availability

The original uploaded **main-body HWPX** contains the 2026-26 notice but does not embed its Annexes 1–7. All **seven annexes have since been uploaded separately** and text/derived review data is accessible under `annexes/`. Original HWP annex binaries, formula objects and pictogram images are not committed in this repository; official revision alignment and source layout require verification. Cross-referenced laws, up-to-date chemical data and product/SDS evidence remain necessary for defensible compliance verdicts.

**Do not treat the main-body knowledge base alone as a complete Annex 1–7 reference.** For detailed SDS checks, read `annexes/annex_4_sds_field_requirements.json`; for use-codes, `annexes/annex_5_use_categories.json`; and for Article 11 ingredient disclosure limits, `annexes/annex_6_concentration_limits.json`. Review source excerpts, scope and other legal materials before issuing PASS/FAIL.

## LLM instructions

# System prompt — Korean SDS compliance reviewer

Copy the following prompt to your SDS-evaluation LLM and attach the provided JSON source and rule files.

```text
You are a Korean MSDS/SDS preliminary compliance assessor. Apply the user-supplied Ministry of Employment and Labor Notice 2026-26, effective 2026-04-24, ONLY to the extent supported by the linked source provisions, and separately identified current official laws/annexes when provided. Annexes 1–7 are separately available in annexes/ as Korean source text and curated JSON. Treat these files as draft source-linked evidence: embedded pictograms, table geometry, formulas and effective-revision alignment are not independently verified. Never claim an unverified layout or externally dependent requirement has been conclusively checked.

INPUTS: (A) regulation_full_structured_ko.json, (B) compliance_rules_en_ko.json, (C) a product SDS (plain text/PDF extraction/structured intake), and optionally (D) label images, workplace evidence, approval decisions, and official annexes. Korean in the legal_sources fields is the primary legal evidence; English operationalised rules are secondary guidance.

ADDITIONAL ANNEX EVIDENCE:
- Annex 4: Read annexes/annex_4_sds_field_requirements.json (16 SDS sections, 97 detailed field/subfield records) and annex_4_sds_field_rules.jsonl before assessing section completeness. Verify actual SDS text/page locations, lawful nonapplicability and permitted "자료 없음" / "해당 없음" as appropriate. Annex 4 locates the MSDS number at the top of the first page, outside the 16 numbered items; verify submission-number applicability and actual page layout.
- Annex 5: Use annexes/annex_5_use_categories.json. Article 11(8): choosing at least one use category is optional in ordinary SDS preparation but required on the specified SDS submissions. Do not treat a selected category as an exemption.
- Annex 6: Use annexes/annex_6_concentration_limits.json ONLY for applicable Article 11(9) composition-information omissions, not directly as mixture GHS hazard-category cutoffs. If a component meets both referenced risk groups, apply the LOWER applicable disclosure threshold after verifying the implementing-rule classification.
- Annex 1/2/3/7: Consult the corresponding source chunks, draft classifications, H/P phrase catalogue, label-size rules and trade-secret evidence checklist, observing source layout/evidence limitations. Trade-secret evidence is not government approval.
- Always cross-check the linked Korean source wording, external statutes and technical data. Do not use missing original pictogram images, graphical equations or incomplete product evidence to infer PASS.

STRICT WORKFLOW:
1. Identify the product and your review boundary: SDS document only / SDS plus labels / full operations. Identify evidence missing from the request.
2. Establish scope under Articles 1–3 and any contextually applicable exclusions; if insufficient evidence, scope = UNCERTAIN. Do not declare an exemption on assumptions.
3. Extract SDS sections physically as presented, with location/page anchor. Check that exactly the required 16 conceptual sections exist IN ORDER, regardless of English/Korean heading variants. The actual section list follows Article 10(1).
4. Evaluate language and completeness (Art. 11(1),(2),(4),(7)), noting exceptional permitted English proper names, research reagent exemption, required original author/date when translated and prescribed placeholders 자료 없음 / 해당 없음 when relevant. Use the Annex 4 field inventory for all 16 sections, including nested fields; assess applicability and the quality of actual content. Do not assume a populated section contains every Annex 4 item, or treat a missing value as a confirmed FAIL without considering permitted absence explanations.
5. Compare Section 2 hazard information with Sections 3, 9, 11, 12, 15, and check composition representation and mixture logic (Art. 11(9)-(11), Art. 12). Apply general ingredient range ±5 percentage POINTS; do not use the special confidential-substitute ±10/±20 points unless Article 17(5) actually applies. Annex-6 limits can now be looked up, but composition accuracy depends on actual ingredient percentages, confirmed hazard classes and cross-referenced law. GHS classification, H/P selections and pictograms still require scientifically defensible evidence and original HWP visual verification. Do not derive hazard categories simply from CAS number or product name.
6. For confidential ingredient substitutions, verify official authorization result, number, validity, alternative info and any refusal/partial grant under Articles 16–18. If no approval evidence, never presume authorization.
7. Evaluate physical warning labels separately under Articles 5–9 and specific conditions; SDS-only evidence cannot prove affixing, color, size or workplace position. WARNING: Article 6-2(7) applies only specified simplifications to SDS Section 2; DO NOT apply its four-pictogram or 6-precautionary-statement label reduction to SDS Section 2.
8. Evaluate provision/retention, electronic worker access and training obligations only when user supplied operational evidence and requested this scope (Articles 13–15). Do not conflate an SDS defect with operational document-availability violation. A topic outside the requested review boundary is NOT ASSESSED and must be disclosed in the scope limitations; do not mark it NOT_APPLICABLE, which means a legal obligation genuinely does not apply.
9. Emit one finding for each checked rule. Use PASS only with adequate evidence and complete relevant legal criteria; FAIL only with concrete contradiction and no applicable exception; NEEDS_REVIEW for omitted facts, unavailable annex/cross-law, technical judgement or ambiguous document extraction; NOT_APPLICABLE where clear. Always include exact provision reference, quoted factual SDS evidence or explicit missing evidence, action to cure, and missing dependencies.
10. Overall SDS-document status: FAIL if any confirmed SDS-document critical/major defect; otherwise NEEDS_REVIEW when an applicable Annex-4 field, hazard verification, official HWP layout or other indispensable evidence remains unresolved; PASS only if all applicable document requirements actually verified. Whole-review status may remain NEEDS_REVIEW even when document section checks pass. Never claim official legal certification.
11. Output JSON matching compliance_report.schema.json; write summary, explanations and actions in Korean. Other-language explanatory synopsis is permitted only after the JSON if requested. Do not insert invented legal citations.

SPECIAL CAUTIONS: A blank SDS field does not by itself prove that information is obtainable; demand 자료 없음 / 해당 없음 where context calls for them. Absent hazard/physical data may need scientific review. An absent label photo means label rules are unverified, not failed. Source date is 2026-04-24; do not claim the text is current without separately verifying amendments.
```

## Input example

At minimum provide the product SDS plus whether the review includes labels, approvals and workplace practices. For detailed mixture checks also supply actual formulation (if lawfully accessible) and government approval notices.

---

## Verbatim Korean provisions

# 화학물질의 분류·표시 및 물질안전보건자료에 관한 기준

**Source:** 고용노동부고시 제2026-26호; effective 2026-04-24. **Scope:** main body only. **Not included:** 별표 1–7.

> Korean source wording below is transcribed from the user-supplied HWPX. The source IDs support precise citations. Nested numbering is reconstructed from paragraph order; the legal text itself is not translated.

## 제1조 (목적)

**[A1-BODY] 제1조** — 이 고시는 「산업안전보건법」 제104조, 제110조부터 제116조까지, 같은 법 시행령 제86조, 같은 법 시행규칙 제141조, 제156조부터 제171조까지, 별표 18에 따른 화학물질의 분류, 물질안전보건자료, 대체자료 기재 승인, 경고표시 및 근로자에 대한 교육 등에 필요한 사항을 정함을 목적으로 한다.

## 제2조 (정의)

**[A2-C01] 제2조제1항** — 이 고시에서 사용하는 용어의 뜻은 다음 각 호와 같다.

**[A2-C01-I01] 제2조제1항제1호** — "화학물질"이란 원소ㆍ화합물 및 그에 인위적인 반응을 일으켜 얻어진 물질과 자연 상태에서 존재하는 물질을 화학적으로 변형시키거나 추출 또는 정제한 것을 말한다.

**[A2-C01-I02] 제2조제1항제2호** — "혼합물"이란 두 가지 이상의 화학물질로 구성된 물질 또는 용액을 말한다.

**[A2-C01-I03] 제2조제1항제3호** — "제조"란 다음 각 호의 어느 하나를 말한다.

**[A2-C01-I03-가] 제2조제1항제3호가목** — 직접 사용 또는 양도ㆍ제공을 목적으로 화학물질 또는 혼합물을 생산, 가공 또는 혼합 등을 하는 것

**[A2-C01-I03-나] 제2조제1항제3호나목** — 직접 사용 또는 양도ㆍ제공을 목적으로 화학물질 또는 혼합물을 직접 기획(성능ㆍ기능, 원재료 구성 설계 등)하여 다른 생산업체에 위탁해 자기명의로 생산하게 하는 것

**[A2-C01-I04] 제2조제1항제4호** — "수입"이란 직접 사용 또는 양도ㆍ제공을 목적으로 외국에서 국내로 화학물질 또는 혼합물을 들여오는 것을 말한다.

**[A2-C01-I05] 제2조제1항제5호** — "용기"란 고체, 액체 또는 기체의 화학물질 또는 혼합물을 직접 담은 합성강제, 플라스틱, 저장탱크, 유리, 비닐포대, 종이포대 등을 말한다. 다만, 레미콘, 콘테이너는 용기로 보지 아니한다.

**[A2-C01-I06] 제2조제1항제6호** — "포장"이란 제5호에 따른 용기를 싸거나 꾸리는 것을 말한다.

**[A2-C01-I07] 제2조제1항제7호** — "반제품용기"란 같은 사업장 내에서 상시적이지 않은 경우로서 공정간 이동을 위하여 화학물질 또는 혼합물을 담은 용기를 말한다.

**[A2-C02] 제2조제2항** — 그 밖에 이 고시에서 사용하는 용어의 정의는 이 고시에 특별한 규정이 없으면「산업안전보건법」(이하 "법"이라 한다), 같은 법 시행령(이하  "영"이라 한다) 및 같은 법 시행규칙(이하 "규칙"이라 한다)에서 정하는 바에 따른다.

## 제3조 (적용제외 물질)

**[A3-BODY] 제3조** — 영 제86조제18호의 "그 밖에 고용노동부장관이 독성ㆍ폭발성 등으로 인한 위해의 정도가 적다고 인정하여 고시하는 화학물질"이라 함은 다음 각 호의 물질을 말한다.

**[A3-I01] 제3조제1호** — 양도ㆍ제공받은 화학물질 또는 혼합물을 다시 혼합하는 방식으로 만들어진 혼합물. 다만, 다음 각 목의 어느 하나에 해당하는 경우는 제외한다.

**[A3-I01-가] 제3조제1호가목** — 해당 혼합물을 양도ㆍ제공하는 경우

**[A3-I01-나] 제3조제1호나목** — 화학적 반응을 통해 그 성질이 변화한 화학물질이 생성되는 경우

**[A3-I02] 제3조제2호** — 제19조에 따른 화학물질로서 연구개발 중간 단계에서 생성된 화학물질 또는 혼합물

**[A3-I03] 제3조제3호** — 완제품으로서 취급근로자가 작업 시 그 제품과 그 제품에 포함된 물질안전보건자료대상물질에 노출될 우려가 없는 화학물질 또는 혼합물(다만, 「산업안전보건기준에 관한 규칙」 제420조제6호에 따른 특별관리물질이 함유된 것은 제외한다)

## 제4조 (화학물질 등의 분류)

**[A4-C01] 제4조제1항** — 규칙 제141조 및 별표 18제1호에 따른 화학물질의 분류별 세부 구분기준은 별표 1과 같다.

**[A4-C02] 제4조제2항** — 화학물질의 분류에 필요한 시험의 세부기준은 국제연합(UN)에서 정하는「화학물질의 분류 및 표지에 관한 세계조화시스템(GHS)」지침을 따른다.

## 제5조 (경고표지의 부착)

**[A5-C01] 제5조제1항** — 물질안전보건자료대상물질을 양도ㆍ제공하는 자는 해당 물질안전보건자료대상물질의 용기 및 포장에 한글로 작성한 경고표지(같은 경고표지 내에 한글과 외국어가 함께 기재된 경우를 포함한다)를 부착하거나 인쇄하는 등 유해ㆍ위험 정보가 명확히 나타나도록 하여야 한다. 다만, 물질안전보건자료대상물질을 취급하는 근로자가 대한민국 국적을 가지지 않은 사람으로서 외국인근로자에 해당하는 경우에는 외국인근로자가 이해할 수 있는 언어로 작성된 경고표지를 추가로 작성하여 부착하거나 전단에 따른 경고표지에 병기하여 부착할 수 있다.

**[A5-C02] 제5조제2항** — 제1항 본문에도 불구하고 실험실에서 시험ㆍ연구목적으로 사용하는 시약으로서 외국어로 작성된 경고표지가 부착되어 있거나 수출하기 위하여 저장 또는 운반 중에 있는 완제품은 한글로 작성한 경고표지를 부착하지 아니할 수 있다.

**[A5-C03] 제5조제3항** — 제1항 본문에도 불구하고 국제연합(UN)의「위험물 운송에 관한 권고(RTDG)」에서 정하는 유해성ㆍ위험성 물질을 포장에 표시하는 경우에는 「위험물 운송에 관한 권고(RTDG)」에 따라 표시할 수 있다.

**[A5-C04] 제5조제4항** — 포장하지 않는 드럼 등의 용기에 국제연합(UN)의 「위험물 운송에 관한 권고(RTDG)」에 따라 표시를 한 경우에는 경고표지에 그림문자를 표시하지 아니할 수 있다.

**[A5-C05] 제5조제5항** — 용기 및 포장에 경고표지를 부착하거나 경고표지의 내용을 인쇄하는 방법으로 표시하는 것이 곤란한 경우에는 경고표지를 인쇄한 꼬리표를 달 수 있다.

**[A5-C06] 제5조제6항** — 물질안전보건자료대상물질을 사용ㆍ운반 또는 저장하고자 하는 사업주는 경고표지의 유무를 확인하여야 하며, 경고표지가 없는 경우에는 경고표지를 부착하여야 한다.

**[A5-C07] 제5조제7항** — 제6항에 따른 사업주는 물질안전보건자료대상물질의 양도ㆍ제공자에게 경고표지의 부착을 요청할 수 있다.

## 제6조 (경고표지의 작성방법)

**[A6-C01] 제6조제1항** — 규칙 제170조에 따른 경고표지의 그림문자, 신호어, 유해ㆍ위험 문구, 예방조치 문구는 별표 2와 같다.

**[A6-C02] 제6조제2항** — 물질안전보건자료대상물질의 내용량이 100그램(g) 이하 또는 100밀리리터(㎖) 이하인 경우에는 경고표지에 명칭, 그림문자, 신호어 및 공급자 정보만을 표시할 수 있다.

**[A6-C03] 제6조제3항** — 물질안전보건자료대상물질을 해당 사업장에서 자체적으로 사용하기 위하여 담은 반제품용기에 경고표시를 할 경우에는 유해ㆍ위험의 정도에 따른 "위험" 또는 "경고"의 문구만을 표시할 수 있다. 다만, 이 경우 보관ㆍ저장장소의 작업자가 쉽게 볼 수 있는 위치에 경고표지를 부착하거나 물질안전보건자료를 게시하여야 한다.

## 제6조의2 (경고표지 기재항목의 작성방법)

**[A6B2-C01] 제6조의2제1항** — 명칭은 제10조제1항제1호에 따른 물질안전보건자료 상의 제품명을 기재한다.

**[A6B2-C02] 제6조의2제2항** — 그림문자는 별표 2에 해당되는 것을 모두 표시한다. 다만 다음 각 호의 어느 하나에 해당되는 경우에는 이에 따른다.

**[A6B2-C02-I01] 제6조의2제2항제1호** — "해골과 Ⅹ자형 뼈" 그림문자와 "감탄부호(!)" 그림문자에 모두 해당되는 경우에는 "해골과 Ⅹ자형 뼈" 그림문자만을 표시한다.

**[A6B2-C02-I02] 제6조의2제2항제2호** — 부식성 그림문자와 피부자극성 또는 눈 자극성 그림문자에 모두 해당되는 경우에는 부식성 그림문자만을 표시한다.

**[A6B2-C02-I03] 제6조의2제2항제3호** — 호흡기 과민성 그림문자와 피부 과민성, 피부 자극성 또는 눈 자극성 그림문자에 모두 해당되는 경우에는 호흡기 과민성 그림문자만을 표시한다.

**[A6B2-C02-I04] 제6조의2제2항제4호** — 5개 이상의 그림문자에 해당되는 경우에는 4개의 그림문자만을 표시할 수 있다.

**[A6B2-C03] 제6조의2제3항** — 신호어는 별표 2에 따라 "위험" 또는 "경고"를 표시한다. 다만, 물질안전보건자료대상물질이 "위험"과 "경고"에 모두 해당되는 경우에는 "위험"만을 표시한다.

**[A6B2-C04] 제6조의2제4항** — 유해ㆍ위험 문구는 별표 2에 따라 해당되는 것을 모두 표시한다. 다만, 중복되는 유해ㆍ위험문구를 생략하거나 유사한 유해ㆍ위험 문구를 조합하여 표시할 수 있다.

**[A6B2-C05] 제6조의2제5항** — 예방조치 문구는 별표 2에 해당되는 것을 모두 표시한다. 다만 다음 각 호의 어느 하나에 해당되는 경우에는 이에 따른다.

**[A6B2-C05-I01] 제6조의2제5항제1호** — 중복되는 예방조치 문구를 생략하거나 유사한 예방조치 문구를 조합하여 표시할 수 있다.

**[A6B2-C05-I02] 제6조의2제5항제2호** — 예방조치 문구가 7개 이상인 경우에는 예방ㆍ대응ㆍ저장ㆍ폐기 각 1개 이상(해당문구가 없는 경우는 제외한다)을 포함하여 6개만 표시해도 된다. 이 때 표시하지 않은 예방조치 문구는 물질안전보건자료를 참고하도록 기재하여야 한다.

**[A6B2-C06] 제6조의2제6항** — 유해ㆍ위험문구 및 예방조치 문구는 해당 문구를 표시하되 코드 번호를 함께 표시할 수 있다.

**[A6B2-C07] 제6조의2제7항** — 제2항제1호부터제3호까지, 제3항, 제4항 및 제5항제1호의 규정은 물질안전보건자료 중 제10조제1항제2호에서 정한 항목을 작성할 때에 적용할 수 있다.

## 제7조 (경고표지의 양식 및 규격)

**[A7-BODY] 제7조** — 경고표지의 양식 및 규격은 별표 3과 같다.

## 제8조 (경고표지의 색상 및 위치)

**[A8-C01] 제8조제1항** — 경고표지전체의 바탕은 흰색으로, 글씨와 테두리는 검정색으로 하여야 한다.

**[A8-C02] 제8조제2항** — 제1항에도 불구하고 비닐포대 등 바탕색을 흰색으로 하기 어려운 경우에는 그 포장 또는 용기의 표면을 바탕색으로 사용할 수 있다. 다만, 바탕색이 검정색에 가까운 용기 또는 포장인 경우에는 글씨와 테두리를 바탕색과 대비색상으로 표시하여야 한다.

**[A8-C03] 제8조제3항** — 그림문자(GHS에 따른 그림문자를 말한다. 이하 이 조에서 같다.)는 유해성ㆍ위험성을 나타내는 그림과 테두리로 구성하며, 유해성ㆍ위험성을 나타내는 그림은 검은색으로 하고, 그림문자의 테두리는 빨간색으로 하는 것을 원칙으로 하되 바탕색과 테두리의 구분이 어려운 경우 바탕색의 대비 색상으로 할 수 있으며, 그림문자의 바탕은 흰색으로 한다. 다만, 1리터(ℓ)미만의 소량용기 또는 포장으로서 경고표지를 용기 또는 포장에 직접 인쇄하고자 하는 경우에는 그 용기 또는 포장 표면의 색상이 두 가지 이하로 착색되어 있는 경우에 한하여 용기 또는 포장에 주로 사용된 색상(검정색계통은 제외한다)을 그림문자의 바탕색으로 할 수 있다.

**[A8-C04] 제8조제4항** — 경고표지는 취급근로자가 사용 중에도 쉽게 볼 수 있는 위치에 견고하게 부착하여야 한다.

## 제9조 (경고표시 기재항목을 적은 자료의 제공)

**[A9-C01] 제9조제1항** — 법 제115조제1항 단서에 따른 경고표시 기재 항목을 적은 자료는 물질안전보건자료대상물질을 양도하거나 제공하는 때에 함께 제공하여야 한다. 다만, 경고표시 기재 항목이 물질안전보건자료에 포함되어 있는 경우에는 물질안전보건자료를 제공하는 방법으로 해당 자료를 제공할 수 있다.

**[A9-C02] 제9조제2항** — 같은 상대방에게 같은 물질안전보건자료대상물질을 2회 이상 계속하여 양도하거나 제공하는 경우에는 최초로 제공한 제1항에 따른 경고표시 기재 항목을 적은 자료의 기재 내용의 변경이 없는 한 추가로 해당 자료를 제공하지 아니할 수 있다. 다만, 상대방이 해당 자료의 제공을 요청한 경우에는 그러하지 아니하다.

## 제10조 (작성항목)

**[A10-C01] 제10조제1항** — 물질안전보건자료 작성 시 포함되어야 할 항목 및 그 순서는 다음 각 호에 따른다.

**[A10-C01-I01] 제10조제1항제1호** — 화학제품과 회사에 관한 정보

**[A10-C01-I02] 제10조제1항제2호** — 유해성ㆍ위험성

**[A10-C01-I03] 제10조제1항제3호** — 구성성분의 명칭 및 함유량

**[A10-C01-I04] 제10조제1항제4호** — 응급조치요령

**[A10-C01-I05] 제10조제1항제5호** — 폭발ㆍ화재시 대처방법

**[A10-C01-I06] 제10조제1항제6호** — 누출사고시 대처방법

**[A10-C01-I07] 제10조제1항제7호** — 취급 및 저장방법

**[A10-C01-I08] 제10조제1항제8호** — 노출방지 및 개인보호구

**[A10-C01-I09] 제10조제1항제9호** — 물리화학적 특성

**[A10-C01-I10] 제10조제1항제10호** — 안정성 및 반응성

**[A10-C01-I11] 제10조제1항제11호** — 독성에 관한 정보

**[A10-C01-I12] 제10조제1항제12호** — 환경에 미치는 영향

**[A10-C01-I13] 제10조제1항제13호** — 폐기 시 주의사항

**[A10-C01-I14] 제10조제1항제14호** — 운송에 필요한 정보

**[A10-C01-I15] 제10조제1항제15호** — 법적규제 현황

**[A10-C01-I16] 제10조제1항제16호** — 그 밖의 참고사항

**[A10-C02] 제10조제2항** — 제1항 각 호에 대한 세부작성 항목 및 기재사항은 별표 4와 같다. 다만, 물질안전보건자료의 작성자는 근로자의 안전보건의 증진에 필요한 경우에는 세부항목을 추가하여 작성할 수 있다.

## 제11조 (작성원칙)

**[A11-C01] 제11조제1항** — 물질안전보건자료는 한글로 작성하는 것을 원칙으로 하되 화학물질명, 외국기관명 등의 고유명사는 영어로 표기할 수 있다.

**[A11-C02] 제11조제2항** — 제1항에도 불구하고 실험실에서 시험ㆍ연구목적으로 사용하는 시약으로서 물질안전보건자료가 외국어로 작성된 경우에는 한국어로 번역하지 아니할 수 있다.

**[A11-C03] 제11조제3항** — 제10조제1항 각 호의 작성 시 시험결과를 반영하고자 하는 경우에는 해당국가의 우수실험실기준(GLP) 및 국제공인시험기관 인정(KOLAS)에 따라 수행한 시험결과를 우선적으로 고려하여야 한다.

**[A11-C04] 제11조제4항** — 외국어로 되어있는 물질안전보건자료를 번역하는 경우에는 자료의 신뢰성이 확보될 수 있도록 최초 작성기관명 및 시기를 함께 기재하여야 하며, 다른 형태의 관련 자료를 활용 하여 물질안전보건자료를 작성하는 경우에는 참고문헌의 출처를 기재하여야 한다.

**[A11-C05] 제11조제5항** — 물질안전보건자료 작성에 필요한 용어, 작성에 필요한 기술지침은 「한국산업안전보건공단법」에 따른 한국산업안전보건공단(이하 "공단"이라 한다)이 정할 수 있다.

**[A11-C06] 제11조제6항** — 물질안전보건자료의 작성단위는「계량에 관한 법률」이 정하는 바에 의한다.

**[A11-C07] 제11조제7항** — 각 작성항목은 빠짐없이 작성하여야 한다. 다만, 부득이 어느 항목에 대해 관련 정보를 얻을 수 없는 경우에는 작성란에 "자료 없음"이라고 기재하고, 적용이 불가능하거나 대상이 되지 않는 경우에는 작성란에 "해당 없음"이라고 기재한다.

**[A11-C08] 제11조제8항** — 제10조제1항제1호에 따른 화학제품에 관한 정보 중 용도는 별표 5에서 정하는 용도분류체계에서 하나 이상을 선택하여 작성할 수 있다. 다만, 법 제110조제1항 및 제3항에 따라 작성된 물질안전보건자료를 제출할 때에는 별표 5에서 정하는 용도분류체계에서 하나 이상을 선택하여야 한다.

**[A11-C09] 제11조제9항** — 혼합물 내 함유된 화학물질 중 규칙 별표 18제1호가목에 해당하는 화학물질의 함유량이 한계농도인 1% 미만이거나 동 별표 제1호나목에 해당하는 화학물질의 함유량이 별표 6에서 정한 한계농도 미만인 경우 제10조제1항 각호에 따른 항목에 대한 정보를 기재하지 아니할 수 있다. 이 경우 화학물질이 규칙 별표18 제1호가목과 나목 모두 해당할 때에는 낮은 한계농도를 기준으로 한다.

**[A11-C10] 제11조제10항** — 제10조제1항제3호에 따른 구성 성분의 함유량을 기재하는 경우에는 함유량의 ± 5퍼센트포인트(%P) 내에서 범위(하한 값 ~ 상한 값)로 함유량을 대신하여 표시할 수 있다.

**[A11-C11] 제11조제11항** — 제10조제1항제15호에 따라 물질안전보건자료에 혼합물의 법적규제 현황을 기재하는 경우 제10조제1항제3호에 따른 개별 구성성분의 명칭 및 함유량 기재 여부와 관계없이 혼합물 전체로서 적용되는 법령상 규제사항을 기재하여야 한다.

**[A11-C12] 제11조제12항** — 물질안전보건자료를 작성할 때에는 취급근로자의 건강보호 목적에 맞도록 성실하게 작성하여야 하고, 기재된 내용이 최신의 과학적ㆍ기술적 정보 및 관련 법령에 부합하도록 지속적으로 관리하여야 한다.

## 제12조 (혼합물의 유해성ㆍ위험성 결정)

**[A12-C01] 제12조제1항** — 물질안전보건자료를 작성할 때에는 혼합물의 유해성ㆍ위험성을 다음 각 호와 같이 결정한다.

**[A12-C01-I01] 제12조제1항제1호** — 혼합물에 대한 유해성ㆍ위험성의 결정을 위한 세부 판단기준은 별표 1에 따른다.

**[A12-C01-I02] 제12조제1항제2호** — 혼합물에 대한 물리적 위험성 여부가 혼합물 전체로서 시험되지 않는 경우에는 혼합물을 구성하고 있는 단일화학물질에 관한 자료를 통해 혼합물의 물리적 잠재유해성을 평가할 수 있다.

**[A12-C02] 제12조제2항** — 혼합물인 제품들이 다음 각 호의 요건을 모두 충족하는 경우에는 해당 제품들을 대표하여 하나의 물질안전보건자료를 작성할 수 있다.

**[A12-C02-I01] 제12조제2항제1호** — 혼합물인 제품들의 구성성분이 같을 것. 다만, 향수, 향료 또는 안료(이하 "향수등"이라 한다) 성분의 물질을 포함하는 제품으로서 다음 각 목의 요건을 모두 충족하는 경우에는 그러하지 아니하다.

**[A12-C02-I01-가] 제12조제2항제1호가목** — 제품의 구성성분 중 향수등의 함유량(2가지 이상의 향수등 성분을 포함하는 경우에는 총함유량을 말한다)이 5퍼센트(%) 이하일 것

**[A12-C02-I01-나] 제12조제2항제1호나목** — 제품의 구성성분 중 향수등 성분의 물질만 변경될 것

**[A12-C02-I02] 제12조제2항제2호** — 각 구성성분의 함유량 변화가 10퍼센트포인트(%P) 이하 일 것

**[A12-C02-I03] 제12조제2항제3호** — 유사한 유해성을 가질 것

**[A12-C03] 제12조제3항** — 제2항에 따라 하나의 물질안전보건자료를 작성하는 제품들이 제2항제1호 단서에 해당하는 경우는 제10조제1항제3호에 따른 항목에 제품별로 구성성분을 알 수 있도록 기재하여야 하고 제2항제3호에 해당하는 경우는 제품별로 유해성을 구분하여 기재하여야 한다.

## 제13조 (양도 및 제공)

**[A13-C01] 제13조제1항** — 물질안전보건자료대상물질을 양도하거나 제공하는 자는 규칙 제160조제1항에 따라 다음 각 호의 어느 하나에 해당하는 방법으로 물질안전보건자료를 제공할 수 있다. 이 경우 물질안전보건자료대상물질을 양도하거나 제공하는 자는 상대방의 수신 여부를 확인하여야 한다.

**[A13-C01-I01] 제13조제1항제1호** — 등기우편

**[A13-C01-I02] 제13조제1항제2호** — 공단에서 운영하는 물질안전보건자료시스템을 포함한 「정보통신망 이용촉진 및 정보보호 등에 관한 법률」 제2조제1항에 따른 정보통신망 및 전자문서(물질안전보건자료를 직접 첨부하거나 저장하여 제공하는 것에 한한다)

**[A13-C02] 제13조제2항** — 규칙 별표 18제1호에 따른 분류기준에 해당하지 아니하는 화학물질 또는 혼합물을 양도하거나 제공할 때에는 해당 화학물질 또는 혼합물이 규칙 별표 18제1호에 따른 분류기준에 해당하지 않음을 서면으로 통보하여야 한다. 이 경우 해당 내용을 포함한 물질안전보건자료를 제공한 경우에는 서면으로 통보한 것으로 본다.

**[A13-C03] 제13조제3항** — 제2항에 따른 화학물질 또는 혼합물을 양도하거나 제공하는 자와 그 양도ㆍ제공자로부터 해당 화학물질 또는 혼합물이 규칙 별표 18제1호에 따른 분류기준에 해당되지 않음을 서면으로 통보받은 자는 해당 서류(제2항 후단에 따라 물질안전보건자료를 제공한 경우에는 해당 물질안전보건자료를 말한다)를 사업장내에 갖추어 두어야 한다.

**[A13-C04] 제13조제4항** — 제2조제1항제3호 나목의 위탁자가 물질안전보건자료를 제출하거나 비공개 승인을 신청하여 그 결과를 통지받은 경우, 제출한 물질안전보건자료 또는 통지받은 승인 결과를 수탁자에게 제공하여야 한다.

## 제14조 (전산장비 조치사항)

**[A14-BODY] 제14조** — 규칙 제167조제1항 단서의 ‘고용노동부장관이 정하는 조치’란 다음 각 호의 조치를 말한다.

**[A14-I01] 제14조제1호** — 물질안전보건자료를 확인할 수 있는 전산장비를 취급근로자(화학물질에 노출되는 근로자를 모두 포함한다. 이하 같다)가 작업 중 쉽게 접근할 수 있는 장소에 설치하여 가동하고 있을 것

**[A14-I02] 제14조제2호** — 해당 화학물질 취급근로자에게 물질안전보건자료의 프로그램 작동 방법, 제품명 입력 및 물질안전보건자료 확인 방법 등을 교육할 것

**[A14-I03] 제14조제3호** — 법 제114조제2항 및 규칙 제168조제1항에 따른 관리요령에 물질안전보건자료 검색방법을 포함하여 게시하였을 것

## 제15조 (교육내용의 주지)

**[A15-BODY] 제15조** — 사업주는 규칙 제167조제1항제3호에 따라 전산장비를 갖추어 둔 경우에는 취급근로자가 그 장비를 이용하여 물질안전보건자료를 확인할 수 있는지 여부를 확인하여야 한다.

## 제16조 (대체자료 기재 제외물질)

**[A16-BODY] 제16조** — 법 제112조제1항 단서에 따른 ‘근로자에게 중대한 건강장해를 초래할 우려가 있는 화학물질로서 「산업재해보상보험법」 제8조제1항에 따른 산업재해보상보험및예방심의위원회의 심의를 거쳐 고용노동부장관이 고시하는 것’이란 다음 각 호의 어느 하나에 해당하는 물질을 말한다.

**[A16-I01] 제16조제1호** — 법 제117조에 따른 제조등금지물질

**[A16-I02] 제16조제2호** — 법 제118조에 따른 허가대상물질

**[A16-I03] 제16조제3호** — 「산업안전보건기준에 관한 규칙」제420조에 따른 관리대상 유해물질

**[A16-I04] 제16조제4호** — 규칙 별표 21의 작업환경측정 대상 유해인자

**[A16-I05] 제16조제5호** — 규칙 별표 22의 특수건강진단 대상 유해인자

**[A16-I06] 제16조제6호** — 「화학물질의 등록 및 평가 등에 관한 법률」시행규칙 제35조제3항 단서에서 정하는 화학물질

## 제17조 (대체자료 기재 승인 및 연장승인 기준 등)

**[A17-C01] 제17조제1항** — 규칙 제161조제1항제1호에 따른 ‘영업비밀에 해당함을 입증하는 자료로서 고용노동부장관이 정하여 고시하는 자료’란 별표 7제1호에서 정한 자료를 말한다. 이 경우 신청인은 제2항에서 정한 판단기준에 부합하는 정보를 기재하여 제출하여야 한다.

**[A17-C02] 제17조제2항** — 규칙 제162조제5항에 따른 ‘대체 필요성에 대한 판단기준’은 별표 7제2호와 같다.

**[A17-C03] 제17조제3항** — 규칙 제162조제5항에 따른 ‘대체자료 중 대체명칭의 적합성에 대한 판단기준’은 환경부 고시 「자료보호신청서의 작성방법 및 보호자료 관리방법 등에 관한 규정」의 별표를 준용한다.

**[A17-C04] 제17조제4항** — 제3항에도 불구하고 화학식과 구조를 특정할 수 없거나 제3항 에 따른 방법만으로는 대체명칭을 특정하기 곤란한 경우에는 공단이 정하는 방법을 따른다.

**[A17-C05] 제17조제5항** — 규칙 제162조제5항에 따른 ‘대체자료 중 대체함유량의 적합성에 대한 판단기준’은 다음 각 호와 같다.

**[A17-C05-I01] 제17조제5항제1호** — 비공개하고자 하는 구성성분의 원래 함유량이 25퍼센트(%) 미만인 경우 ±10퍼센트포인트(%P) 내에서 범위로 기재

**[A17-C05-I02] 제17조제5항제2호** — 비공개하고자 하는 구성성분의 원래 함유량이 25퍼센트(%) 이상인 경우 ±20퍼센트포인트(%P) 내에서 범위로 기재

**[A17-C06] 제17조제6항** — 규칙 제162조제5항에 따른 ’물질안전보건자료의 적정성에 대한 승인기준’은 다음 각 호와 같다.

**[A17-C06-I01] 제17조제6항제1호** — 제10조제1항제2호, 제3호, 제9호, 제11호, 제12호 및 제15호를 검토대상으로 한다.

**[A17-C06-I02] 제17조제6항제2호** — 제1호에 따른 정보는 사업주가 승인 신청시 제출한 자료 뿐만 아니라 국내외 관련 기관 등에서 제공하고 있는 정보를 바탕으로 하여 그 적정성을 판단한다. 이 경우 국내외 관련 기관 등에 대한 정보는 공단이 정할 수 있다.

## 제18조 (대체자료 기재 승인 결과의 반영)

**[A18-C01] 제18조제1항** — 규칙 제162조제6항 및 제163조제3항에 따라 승인 결과를 통보받은 신청인은 다음 각 호에 따른 결과를 물질안전보건자료에 반영하여야 한다.

**[A18-C01-I01] 제18조제1항제1호** — 승인: 승인번호, 유효기간 및 대체자료를 기재

**[A18-C01-I02] 제18조제1항제2호** — 부분승인: 세부 승인결과에 따라 승인된 화학물질에 대하여만 제1호의 정보를 기재하고 불승인된 화학물질은 제3호의 정보를 기재

**[A18-C01-I03] 제18조제1항제3호** — 불승인: 제11조에 따라 화학물질의 정보를 기재

**[A18-C02] 제18조제2항** — 제1항에 따라 승인 결과를 통보받은 신청인은 물질안전보건자료의 적정성 검토 결과 그 내용이 달라진 경우 물질안전보건자료에 반영하여야 한다.

## 제19조 (연구ㆍ개발용 화학물질 또는 화학제품)

**[A19-BODY] 제19조** — 영 제86조제17호에 따른 ‘고용노동부장관이 정하여 고시하는 연구ㆍ개발용 화학물질 또는 화학제품’이란 다음 각 호의 어느 하나에 해당하는 것을 말한다.

**[A19-I01] 제19조제1호** — 시약 등 과학적 실험ㆍ분석 또는 연구를 위한 경우

**[A19-I02] 제19조제2호** — 화학물질 또는 화학제품 등을 개발하기 위한 경우

**[A19-I03] 제19조제3호** — 생산공정을 개선ㆍ개발하기 위한 경우

**[A19-I04] 제19조제4호** — 사업장에서 화학물질의 적용분야를 시험하기 위한 경우

**[A19-I05] 제19조제5호** — 화학물질의 시범제조 또는 화학제품 등의 시범생산을 위한 경우

## 제20조 (대체자료의 제공 방법)

**[A20-BODY] 제20조** — 법 제112조제10항에 따라 대체자료로 적힌 화학물질의 명칭 및 함유량 정보의 제공을 요구받은 자는 이를 요구한 자에게 직접 제공하거나 제13조제1항에서 정한 방법으로 제공하여야 한다.

## 제21조 (재검토기한)

**[A21-BODY] 제21조** — 고용노동부장관은 「행정규제기본법」 및 「훈령ㆍ예규 등의 발령 및 관리에 관한 규정」에 따라 이 고시에 대하여 2021년 1월 1일 기준으로 매 3년이 되는 시점(매 3년째의 12월 31일까지를 말한다)마다 그 타당성을 검토하여 개선 등의 조치를 하여야 한다.

## 부칙

부칙 <제2026-26호, 2026. 4. 24.>



---

## Linked operational rules

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

---

## Annexes 1–7: supplementary structured compliance references (uploaded separately)

The following references extend this single-file **main-body** transcription. Each retains its Korean source text in `annexes/annex_N.extracted_ko.txt` and retrieval chunks in `annexes/annex_N_rag_chunks.jsonl`:

| Annex | Structured review artifact | Use |
|---|---|---|
| 1 | `annexes/annex_1_curated_thresholds.json` | Partial hazard-class examples, not a complete classifier |
| 2 | `annexes/annex_2_h_p_phrase_catalog.json` | Korean H/P glossary, not verified pictogram mapping |
| 3 | `annexes/annex_3_label_dimensions.json` | Physical label size checks |
| 4 | `annexes/annex_4_sds_field_requirements.json` | **16 sections, 97 field/subfield checks, eight consistency checks** |
| 5 | `annexes/annex_5_use_categories.json` | **48 main uses and 31 subcategories**, for Article 11(8) context |
| 6 | `annexes/annex_6_concentration_limits.json` | **14 threshold entries** for Article 11(9) composition-information disclosure conditions |
| 7 | `annexes/annex_7_trade_secret_evidence_checklist.json` | Confidentiality evidence; not approval proof |

**Source integrity:** The original main-body notice and the annexes are distinct user-supplied files; source hashes are recorded in `annexes/annex_sources_manifest.json`. Unverified source diagrams, table layouts, formulas and other applicable statutes must not be silently inferred. For the complete workflow, prefer `LLM_SYSTEM_PROMPT.md` over the historical main-body rule notes embedded below.
