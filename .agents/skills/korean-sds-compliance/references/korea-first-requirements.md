# Korea-first MSDS requirement playbook

This playbook specifies **Korean legal checks**. Generic GHS scientific classification can support these checks; EU CLP, U.S. OSHA and other foreign rules are **not** alternative Korean legal authority.

## Scope and legal authority

**Start:** Confirm date and whether the review covers the SDS document only, the physical label, an official submission, confidentiality authorization, or workplace distribution. The default for an uploaded SDS alone is **SDS_DOCUMENT_ONLY**. Do not treat inaccessible records as proof of noncompliance, and do not present an unrequested workplace audit as an SDS failure.

**Primary Korean hierarchy:**
1. 산업안전보건법 (Industrial Safety and Health Act), particularly the applicable provisions governing MSDS preparation, submission, confidentiality and communication.
2. 산업안전보건법 시행령 and 시행규칙, including its relevant **별표 18** and provisions on MSDS filings and workplace obligations.
3. **고용노동부고시 제2026-26호 (시행 2026-04-24)**, the user-supplied main-body document.
4. Uploaded **별표 1–7** with the source manifest; do not silently assume annex artwork, formulas or version alignment is independently certified.
5. Government acceptance/approval records, Korean technical classifications, and actual product evidence.

**Official anchor:** National Law Information Center, https://www.law.go.kr/admRulLsInfoP.do?admRulSeq=2100000278320. Re-verify official legislation and any applicable historical amendment **on the relevant date** if the user needs a time-sensitive legal answer. A prior amendment's transitional rule is not automatically a new transitional rule of 2026-26.

## Priority 0 — core South Korean MSDS requirements

**KR-01: applicability and exemptions.** Confirm duties under the governing Act, Enforcement Decree and notice Articles 3 and 19. Research-use, intermediate and finished-article circumstances are *conditional* and require specific facts. Check the special-management-material exception where implicated. An assertion of "laboratory use" does not automatically excuse an SDS.

**KR-02: Korean language and translation (제11조제1·2·4항).** Check that SDS content is Korean where required; retain allowed names/foreign institutional identities in English. Consider the actual exception for foreign-language SDS of laboratory testing/research reagents. When translated, request the original authoring institution and original creation date, along with cited information sources. Do **not** apply blanket foreign-English SDS acceptance.

**KR-03: mandatory layout and missing-data terms (제10조, 제11조제7·12항, 별표 4).** Check **all sixteen sections in legal sequence** and **97 field/subfield identifiers**; verify substance, not just section labels. Source text provides prescribed `자료 없음` and `해당 없음` approaches; review their factual basis rather than automatically passing them. Flag evidence gaps. Annex 4 also places an applicable MSDS number at the first page's upper area outside numbered sections.

**KR-04: Korea-specific MSDS filing and use codes (산업안전보건법 제110조, 제11조제8항, 별표 4·5).** Determine manufacture/importer/submission context using the actual Act and implementing rules. An SDS number typed into a PDF is **not proof of submission**. For the covered submission scenario, verify at least one appropriate **Annex 5 use code** (48 main, 31 subcategories). Choosing one may be optional when merely preparing an SDS. The existing 60-rule index does **not** fully encode submission filing obligations; do not invent the gap.

**KR-05: Korean ingredient disclosures (제11조제9·10항, 시행규칙 별표 18, 별표 6).** For a claimed omission, verify that the component is in the legally specified hazard group and that its actual concentration is **below** the applicable 1% or Annex 6 limit. If the physical and health/environment categories overlap, the **lower** limit applies. This does **not** determine the mixture's GHS category. General concentration-range rules under Article 11(10) use **percentage points** rather than relative percent; separate these from confidentiality-specific Article 17(5) ranges. Missing composition cannot be reconstructed from publicly disclosed SDS alone.

**KR-06: confidential component substitute disclosure (제16–18조, 제20조, 별표 7).** Check excluded component categories, genuine ministry approval, approval number, validity, scope, permitted alternative name and range. Distinguish full, partial and refused decisions. An application or trade-secret declaration is **not** an approval. Do not publish confidential actual composition in user-facing summaries unless authorized.

**KR-07: Korean warning labels (제5–8조, 별표 2·3).** Assess actual Korean label content, H/P full Korean phrases, symbol precedence, Danger/Warning precedence, reduced-content rules for qualifying **≤100g/≤100mL** packages, the **7+ P-statement** condition for a six-statement label, and original label/pictogram dimensions, colors and placement. Record whether RTDG or research reagent exceptions apply. Do **not** apply the physical label's blanket four-pictogram or six-P-statement reductions to SDS Section 2: Article 6-2(7) cross-references only specified exceptions. Distinguish a label from the MSDS itself.

## Priority 1 — important additional Korean differences

**KR-08: mixtures and representative SDS (제4조, 제12조, 별표 1).** A representative SDS across related products requires all applicable conditions, including component identity allowances, concentration differences and similar hazards. Review the specific ≤5% fragrance/pigment exception and ≤10 percentage-point group-difference condition only under the cited provision. Confirm science and original Annex 1 formulas before hazard calculations.

**KR-09: Section 15 Korean regulatory status (제10조제1항제15호, 제11조제11항, 별표 4).** Check legal status under *each* listed Korean law as applicable (산업안전보건법; 화학물질관리법; 화학물질의 등록 및 평가 등에 관한 법률; 위험물안전관리법; 폐기물관리법; other applicable law). Rule §11(11) addresses mixture-wide obligations regardless of whether a specific component appears in Section 3. Do not claim "not regulated" without authoritative regulatory list checks. Preserve applicable historical rules if reviewing older SDSs.

**KR-10: supply communication (제9·13조).** Assess delivery methods, confirmation of receipt, non-classification written notices, duplicate-supply conditions and contractor communications **only with transfer/distribution evidence**.

**KR-11: Korean worker access (제14·15조).** Assess equipment, access instructions, worker education and actual ability to retrieve SDS **only if requested in scope**. An online link alone may not establish the required workplace measures.

**KR-12: source and units rules (제11조제3·6항).** Trace testing information and preference for suitable accredited results, and apply Korean unit legislation as referenced; do not guess technical equivalencies or tolerances.

## Report format and escalation

For each obligation: `module_id`, `rule_id`, exact `한국 법령 근거`, `적용여부`, `SDS 페이지/증거`, `검토결과`, `누락된 증빙`, `조치 제안`. Preserve exact Korean citations. Reports may explain in English if asked, but legal source remains Korean.

Use `NEEDS_REVIEW` for unclear source revision, missing referenced statutes, unavailable label photos, incomplete composition, absent approval decision or unreadable table/formula. Use `NOT_ASSESSED` for out-of-scope compliance topics. **A machine-readable count, a found Korean phrase, or an H/P code match is never an automatic legal PASS.**

### Route by the actual user task

- Uploaded SDS or request for "Korean compliance" → start KR-01 through KR-06 and KR-09 as supported by document evidence; assess other modules only if scope/evidence supports them.
- "MSDS 제출" or "제출번호" → KR-04 first; require the Act/rules and official filing proof.
- "경고표지" → KR-07; request package photograph/capacity and Annex 2/3 verified layout.
- "영업비밀" or "대체자료" → KR-06; request genuine ministry decision.
- "혼합물" or "함유량" → KR-05 and KR-08; verify component data and enforce separation of disclosure limits and classification methods.
- "법적 규제현황" → KR-09 with the appropriate current Korean regulatory lists.
- Workplace handling or employer access → KR-10 and KR-11 only if asked.

For structured routing, see `assets/korean-requirement-matrix.json`: its twelve modules collectively map every one of the 60 curated base rule IDs **exactly once**. It is an assessment map, **not a second legal source**.

## Version and interpretation safeguards

- The main notice is marked effective **2026-04-24**. Its own supplied HWPX supplementary provision says it takes effect on issuance.
- Earlier amendments can have separate transitional rules. A previously indexed Annex 4 transitional provision can appear in historical amendment notes, so always identify *which amendment* actually established it; never re-label a historical provision as a 2026 transitional rule without proof.
- Official source says Annex text should be cross-checked against the legal version relevant to the SDS's creation/revision. This project's annex extract manifest still flags lack of independent source-layout and exact amendment-alignment verification.
- Changes in current Korean law, chemical control lists, and product-specific approvals must be checked against the correct date. Do not use current foreign hazard classifications as Korean regulatory evidence.

