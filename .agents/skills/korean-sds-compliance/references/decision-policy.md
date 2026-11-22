# Legal decision and evidence policy

## Separate observation from adjudication

An extracted heading, exact H-code match, threshold comparison, or visible MSDS number **is an observation**, not a legal PASS. Chemical hazard classification additionally depends on verified scientific data, methodology, and (where relevant) test/bridging criteria.

Use three distinct data levels:
1. **Observed:** What appears in the SDS, with location and verbatim excerpt.
2. **Validated:** Source and computation explicitly verified, plus applicability and exceptions considered.
3. **Determined:** Legal conclusion supported by applicable official law, independent evidence and reviewer approval where necessary.

Never upgrade Observed into Determined implicitly.

## Status definitions

| Status | Minimum evidence |
|---|---|
| `PASS` | Verified applicable legal criterion; unambiguous compliant SDS evidence; checked exceptions and relevant official-source version |
| `FAIL` | Specific demonstrated contravention; precise source basis; applicability confirmed; exceptions considered |
| `NEEDS_REVIEW` | Insufficient data, source not verified, calculation depends on missing inputs, conflicting classifications, trade-secret claim without approval, uncertain exemption |
| `NOT_APPLICABLE` | Documented facts plus legal authority show the rule does not apply |
| `NOT_ASSESSED` | Work outside agreed scope: record in scope limitations, **not** as `NOT_APPLICABLE` |

The current report schema has four rule-level statuses. Keep `NOT_ASSESSED` in `out_of_scope_checks` or review-scope limitations.

## No unsafe short-circuits

- **Annex 4:** Presence of a field label or a section heading is not proof the field is correctly populated. `자료 없음` (no data) and `해당 없음` (not applicable) need contextual examination under Article 11 rather than unconditional rejection.
- **Article 11(8):** Annex 5 use codes may be optional for ordinary SDS preparation and mandatory for the specified SDS submission scenario. Verify filing context.
- **Article 11(9):** Annex 6 0.1% or 1% values concern **whether certain ingredient information may be omitted** under specified legal conditions. Physical hazard provisions can require a 1% consideration under Enforcement Rule Annex 18. When both referenced group conditions apply, verify and use the **lower** threshold. **Never** infer the product's GHS classification from an Annex 6 disclosure threshold.
- **Annex 1:** Whole-mixture test evidence and bridging rules may supersede a naive ingredient threshold shortcut. Formulas may be encoded as HWP equation objects; do not guess them from missing characters.
- **Annex 2:** The H/P text catalogue is not a verified class→pictogram→precaution mapping. Check original visual tables before label adequacy conclusion.
- **Annex 3:** Measured capacity, available surface, printed label size and each pictogram area need real evidence. Label rules and SDS Section 2 restrictions are not identical.
- **Annex 7:** An application, confidentiality claim or confidentiality evidence does **not** prove Ministry approval; get decision identifier, expiry, scope and approved alternatives.
- **MSDS number:** Seeing a number on page 1 is not proof a government submission happened; check authority evidence and applicable exceptions.
- **CAS / names:** Correct-looking chemical IDs do not establish hazard categories or composition.

## Mandatory provenance in any finding

Each finding must include:
- `rule_id` or `field_id`
- exact legal provision and annex location
- verbatim Korean source or stable source reference
- location and quote of the SDS evidence, or what was missing
- facts required for applicability and any exemption review
- reproducible comparison or method, plus source-evidence limitations
- disposition and priority of corrective action
- uncertainty and reviewer status

Do not disclose unredacted trade-secret ingredient information in public-facing reports.

## Overall result aggregation

A confirmed critical or major SDS document violation may lead to SDS-document `FAIL`; unresolved essential checks produce `NEEDS_REVIEW`. Overall `PASS` is not available solely from these extracted, layout-unverified annexes, an H/P catalogue lookup or presence of 16 headings. Under the repository's current source-verification status, **issue only preliminary, explicitly qualified findings**.

If the user asks for guaranteed legal compliance or an official approval, explain the limitations and suggest review by qualified Korean regulatory personnel.
