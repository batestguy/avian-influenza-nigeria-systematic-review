# GRADE certainty — prognosis logic (narrative, no fake grades)

**Status (2026-09-20):** certainty framework unchanged and inactive. No certainty grade is
claimable before study grouping, extraction, JBI appraisal, and the molecular transparency check.

Sources: Iorio et al., BMJ 2015;h870 (GRADE prognosis); JBI GRADE mapping (no formal GRADE-prevalence rule — prognosis/baseline-risk logic is acceptable, optional for prevalence).
Assess per synthesis grouping, not per paper. Two reviewers; document reasons.

## Starting point

Observational bodies start at **Low** (residual confounding/selection). Rate **down** and only rate **up** with explicit justification (large effect, dose–response, opposing residual confounding).

## Five downgrade domains

1. **Risk of bias** — serious JBI concerns across the body (sampling, assay validity, attrition).
2. **Inconsistency** — point estimates / directions disagree, CIs barely overlap, unexplained by epoch/host/region.
3. **Indirectness** — population/setting/assay does not match our question (e.g. neighbouring-country data used for Nigeria inference; LBM-only for national claim).
4. **Imprecision** — wide CIs, small n, decision would flip at CI bounds. Do NOT double-count inconsistency + imprecision from the same wide interval — judge once.
5. **Publication bias** — grey missed, small-study effects, AJOL/theses absent.

## Final labels (use narratively)

- High / Moderate / Low / Very low confidence + one-line reason per domain judged.
- If evidence too sparse: state "confidence not gradable — narrative confidence only" rather than inventing a grade.

## Output format for our draft

Per synthesis (temporal / geographic / host / molecular): `Rating: Low — downgraded for RoB (…​) + indirectness (…​). Not downgraded for …​ because …​`
