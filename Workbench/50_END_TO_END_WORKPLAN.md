# End-to-end workplan — Nigeria AIV systematic review

**Prepared:** 17 September 2026  
**Purpose:** single operational plan from protocol truth through final manuscript audit.  
**Scope:** Nigeria avian influenza evidence, 2006–2026; CoCoPop/PEO; PRISMA 2020, PRISMA-S and SWiM.  
**Manuscript source of truth:** `Avian_review_paper_fellow.docx` only.

## Operating rules

1. Keep the `.docx` frozen until Gates A–F are passed and a paste-ready change is approved.
2. Keep screening, extraction and audit guidance in the Workbench or chat; final tables and appendices belong inside the `.docx`.
3. Do not treat RIS, JSON, titles or abstracts as full-text eligibility evidence.
4. Use `Not reported`, `Unclear` or `N/A`; never leave extraction fields blank.
5. Never conflate subtype, clade/lineage, reassortant, introduction or local evolution.
6. Do not force meta-analysis. The confirmed route is SWiM narrative synthesis without meta-analysis. Phase 7 may document whether a future, explicitly user-approved amendment could support narrow pooling; it does not authorise pooling automatically.
7. Never claim completion of WoS, Google Scholar or AJOL for the current snapshot unless a legitimate platform run, hit count and export are obtained.

## Current position

**Active phase:** Phase 2 screening reconciliation. Re-audited 20 September 2026.
**Completed:** protocol/search drafts, PubMed v3, OpenAlex/Crossref supplement, Scopus and ScienceDirect imports, preliminary title/abstract screening, and the Web of Science Starter API base retrieval (175 raw records, 19 September 2026).  
**Not completed:** final candidate-register reconciliation, full-text eligibility, extraction, risk of bias, certainty, synthesis and manuscript update.  
**Operational search layers:** locked library snapshot 16 September 2026; imported Web of Science
API layer dated 19 September; and AJOL plus WoS browser search updates dated 20 September. The
operational search-update date is 20 September 2026; the former 30 September endpoint is
superseded. Source-specific dates must be reported rather than implying a same-day rerun.

Evidence currently available:

- PubMed: 140 v3 records; 142 screened including two v1-only checks; 73 main candidates, 4 context candidates, 64 exclusions and 1 check.
- OpenAlex/Crossref supplement: 1,744 canonical records; 1,627 novel against PubMed; preliminary votes require remapping after canonicalisation.
- Manual imports: 204 Scopus and 25 ScienceDirect records; 76 marked novel before final reconciliation.
- Web of Science API: 175 raw records across four pages, canonicalised in file 53 but not finally
  screened or included in PRISMA flow counts.
- Web of Science browser update: 206 base / 77 molecular / 154 epidemiology / 70 wild-bird;
  count-only because Free View did not provide a reliable full export.
- AJOL browser update: 144 query rows, 79 unique article URLs, 73 dated 2006–2026; imported and
  canonicalised (47 existing matches, 32 new identities) but not substantively screened.
- WoS provisional-new queue: 24 records in `52_WOS_PROVISIONAL_NEW.json`; Reviewer 2 completed a provisional title/metadata pass: 2 `include_main`, 6 `background_only`, 14 `exclude`, and 2 `unclear`.
- PubMed metadata repair: 14 v3 IDs recovered from NCBI ESummary and retained in `51_PUBMED_v3_metadata_repair.json`; the original raw export was preserved unchanged.
- Upper-bound full-text queue: 160 candidates; this is not the final included-study count.
- Full-text assessment, extraction and RoB: zero completed.

Current identity-QA checkpoint: 2,367 source rows produce 1,877 provisional identity groups and
490 collapsed duplicates. AJOL contributes 79 rows across 79 identities; the WoS browser update
remains count-only. Screening reconciliation and full-text eligibility remain open.

## Roles and decision record

| Role | Named person | Responsibility |
|---|---|---|
| Reviewer 1 | Primary reviewer | Primary screening, extraction and synthesis lead |
| Reviewer 2 | Epicurus (independent Codex agent) | Independent verification pass and disagreement review |
| Arbiter | Main Codex agent | Resolves disagreements and approves final decisions |
| Methods reviewer | TBD | Reviews pooling decision, RoB and synthesis claims |

Reviewer 2 is an independent agent with a separate context and must receive the same evidence
packet as Reviewer 1. The main agent must adjudicate disagreements and verify that no agent
decision is promoted into T1–T7 without source evidence.

## Phase map

| Phase | Name | Main output | Exit gate |
|---|---|---|---|
| 0 | Protocol truth and amendment control | Dated protocol truth record | Gate A |
| 1 | Search closure and source audit | Reproducible source table and raw-library inventory | Gate B |
| 2 | Canonicalisation and screening reconciliation | One candidate register with traceable decisions | Gate C |
| 3 | Full-text retrieval and eligibility | Included set plus T6 exclusions | Gate D |
| 4 | Extraction pilot | Reconciled five-study pilot and revised form | Gate E |
| 5 | Full extraction | T1–T5 plus quantitative-data fields | Gate F |
| 6 | Risk of bias and certainty | T7, molecular checks and certainty notes | Gate G |
| 7 | Synthesis decision and analysis | SWiM synthesis or narrowly justified pooling | Gate H |
| 8 | Manuscript reporting | Paste-ready Results, Discussion and tables | Gate I |
| 9 | Final audit and handoff | PRISMA/PRISMA-S/SWiM-complete manuscript | Gate J |

---

## Phase 0 — Protocol truth and amendment control

### Tasks

- Confirm the frozen question, four objectives, CoCoPop/PEO framework and strict avian laboratory-confirmation eligibility rule.
- Record the 2026-09-20 amendment fixing the operational search-update date at 20 September 2026; retain the 16 and 19 September layers as historical imported layers.
- Confirm that PROSPERO was skipped and retain the non-registration wording.
- Maintain the named roles: R1 primary reviewer, Epicurus as independent Reviewer 2, and the main Codex agent as arbiter.
- Confirm the current default: SWiM without meta-analysis; no post hoc pooling unless Phase 7 passes.
- Confirm the exact database strings and the status of each source. A blocked or unavailable source is logged as not run, not silently treated as searched.

### Deliverables

- Approved and dated protocol truth note.
- Dated amendment in `15_RUN_LOG.md`.
- Named review roles.
- Decision record for the default SWiM route and conditional pooling gate.

### Gate A — pass criteria

- Question, eligibility, date scope, registration status and source status are internally consistent.
- Roles and independence/verification plan are recorded.
- No screening or extraction decision relies on an unresolved protocol contradiction.

**If failed:** stop. Repair the protocol truth record before further screening.

## Phase 1 — Search closure and source audit

### Tasks

- Freeze the 16 September operational snapshot and preserve all existing exports.
- Reconcile the Gate 1 source table: PubMed, Scopus, ScienceDirect, OpenAlex and Crossref completed; WoS API retrieval completed 19 September; Google Scholar remains a dated unmerged supplement; AJOL and WoS browser searches completed 20 September with the export limitations in files 15 and 19.
- Record the WoS API collection (`db=WOS`), exact string, date, pagination, 175 hits, four raw JSON exports, and absence of a recorded English filter. Do not count it in PRISMA until canonicalised.
- Treat the nine AJOL on-site query counts as the executed search record. Do not substitute earlier `site:ajol.info` discovery estimates.
- Do not use a scraper, proxy rotation, CAPTCHA solver or unauthorised full-text route.
- Inventory every raw and derived file, recording source, date, query version, cap and known limitations.

### Deliverables

- Completed source/hit/export table in `15_RUN_LOG.md`.
- Raw-library inventory with source lineage.
- Search limitations paragraph for eventual Methods/limitations text.

### Gate B — pass criteria

- Every source is labelled `completed`, `not run`, `blocked` or `supplementary`.
- Exact strings, dates, filters, caps and exports are traceable.
- The search snapshot is not described as covering dates or databases that were not actually searched.

**Current decision (2026-09-20): Gate B search execution is complete with export limitations.**
AJOL has a verified on-site run and WoS has verified browser counts, but AJOL lacks a durable
project export and WoS Free View lacks a complete record-level export. This does not convert
count-only results into PRISMA identification records or screened studies.

## Phase 2 — Canonicalisation and screening reconciliation

### Tasks

- Create one canonical identity for each record using DOI first, then PMID, then normalised title plus year.
- Remap all preliminary votes from raw records to canonical identities; do not carry pre-collapse votes across records without verification.
- Deduplicate the manual import queue, including repeated title/DOI records.
- Correct the known false Nigeria candidate: PMID `27677611` is an Iran study and cannot be a Nigeria main inclusion.
- Separate primary empirical records from reviews, KAP, worker, pig, policy, cost, vaccine-only and other context records.
- Establish duplicate-dataset links and retain the most complete report for extraction.
- Complete the title/abstract pilot and record independent votes, dates and reasons for uncertainty.
- Re-screen the 160 upper-bound main candidates using all frozen criteria.

### Deliverables

- Canonical candidate register.
- Source-lineage and duplicate links.
- Independent screening decisions with reviewer IDs.
- Fixed full-text queue.

### Gate C — pass criteria

- Every candidate has one canonical identity and a traceable source.
- All preliminary votes are remapped or discarded with a reason.
- Duplicate datasets and obvious non-avian/non-Nigeria records are flagged.
- PRISMA identification and screening counts reconcile.

**If failed:** do not begin extraction. Return to canonicalisation or adjudication.

**Current decision (2026-09-19): Gate C remains open for screening reconciliation.** The identity register is now complete in `53_CANONICAL_REGISTER.json`, but record-level adjudication of the pre-collapse supplement/manual screens and replacement of the 160-record upper-bound queue are still required.

## Phase 3 — Full-text retrieval and eligibility

### Tasks

- Retrieve full text through PubMed Central, Europe PMC, publisher open access, institutional library access or authorised repositories.
- Record retrieval status: `full_text_obtained`, `library_required`, `unretrievable_after_protocol`, `duplicate` or `metadata_problem`.
- Verify Nigeria-specific data, avian host, AIV laboratory confirmation, assay, empirical design and extractable outcomes.
- Use one fixed full-text exclusion reason per record and complete T6.
- Link companion reports to the retained primary dataset.
- Record page/section evidence for every included study and every uncertain decision.

### Deliverables

- Retrieval register.
- Dual full-text decisions and adjudications.
- Completed T6 excluded-study table.
- Final included-study list and duplicate-dataset map.

### Gate D — pass criteria

- Every candidate has a retrieval outcome and eligibility decision.
- Every exclusion has one fixed reason and supporting evidence.
- Every inclusion meets the strict avian laboratory-confirmation rule.
- PRISMA flow counts reconcile from identification through inclusion.

## Phase 4 — Extraction pilot

### Tasks

- Select five diverse included studies: early H5N1, outbreak/spatiotemporal, LBM or wild-bird, molecular/clade, and recent H5/H9 study.
- Independently extract the same five studies using the T1–T5 shells.
- Add quantitative-readiness fields during the pilot without changing eligibility: outcome definition, positive numerator, tested denominator, sampling unit, sampling frame, period, location, assay, CI/SE/SD, adjusted estimate, comparator and duplicate-data flag.
- Compare extraction field by field; record disagreements and revise the form once.
- Re-pilot if a major form change affects eligibility, outcome definition or molecular interpretation.

### Deliverables

- Reconciled five-study pilot.
- Dated extraction-form amendment, if needed.
- Quantitative-readiness field specification.

### Gate E — pass criteria

- Pilot disagreements are adjudicated.
- No essential field is blank.
- Outcome definitions and study-unit rules are stable.
- The team can distinguish study, report, dataset, sample, isolate and event.

## Phase 5 — Full extraction

### Tasks

- Complete T1 first-detection chronology.
- Complete T2 state × epoch matrix.
- Complete T3 host-range table.
- Complete T4 clade-transition evidence table.
- Complete T5 accession and molecular-methods audit.
- Extract design, sampling frame, period, state/zone, host/system, sample size, denominator, assay, subtype, clade/lineage, sequencing, phylogeny/support, accession, reassortment/mutation claims and limitations.
- Extract quantitative fields only when the outcome and denominator are defined sufficiently for interpretation.
- Record `Not reported`, `Unclear` or `N/A` rather than infer missing values.
- Verify all inclusions and a prespecified sample of clear exclusions against the source text.

### Deliverables

- Completed T1–T5 tables.
- Study-level extraction register.
- Candidate quantitative-data register.
- Claim-to-study traceability map.

### Gate F — pass criteria

- Every included study has complete T1–T5 fields.
- Every temporal, geographic, host and molecular claim is traceable to a source page/table/figure.
- No duplicate dataset contributes more than once to a given synthesis unless explicitly justified.

## Phase 6 — Risk of bias and certainty

### Tasks

- Apply the relevant JBI Prevalence, Cross-Sectional or Cohort tool.
- Apply molecular checks M1–M7: sampling, assay, sequencing, accession, phylogeny/support, nomenclature and reassortment discipline.
- Record signalling answers and evidence quotes; do not calculate score sums.
- Classify each study as `Include`, `Exclude` or `Seek further info` for synthesis use.
- Draft narrative certainty using prognosis-style GRADE logic without inventing grades.
- Identify studies whose sampling intensity, assay sensitivity, missing accessions or overlapping data limit interpretation.

### Deliverables

- Completed T7 table.
- Per-study JBI and molecular evidence notes.
- Certainty notes for each synthesis grouping.
- High-risk and unclear-information list.

### Gate G — pass criteria

- Every included study has RoB evidence.
- Molecular claims are downgraded where methods/support/accessions are inadequate.
- Certainty language matches the evidence and does not overstate causality or emergence.

## Phase 7 — Synthesis decision and analysis

### Default route: SWiM narrative synthesis

Group evidence by epoch, subtype/clade, host system and geography. Present structured tables, chronology, state matrix, host-range synthesis and qualified molecular/clade narrative. Explain surveillance intensity and assay differences as alternative explanations for apparent emergence or geographic variation.

### Conditional quantitative-pooling check — inactive unless the protocol is reopened

Consider pooling only when all conditions below are met for a specific outcome and subgroup:

1. A common estimand is defined in advance—for example, laboratory-confirmed prevalence in a specified host/system and period.
2. At least two independent datasets report compatible outcome definitions, numerator/denominator or effect estimate, and uncertainty.
3. Sampling frames, assay definitions, host categories and time windows are sufficiently comparable.
4. Duplicate datasets, clustering, repeated sampling and multiple subtypes are handled without double counting.
5. Risk of bias and missingness can be incorporated into interpretation.
6. A dated amendment records the rationale, effect measure, model, zero-event/missing-data rules and sensitivity analyses before looking at pooled results.

### If a future amendment is explicitly approved and pooling is defensible

- Define the effect measure and transformation.
- Extract or calculate effect estimates and standard errors.
- Prespecify fixed/random-effects rationale; do not choose solely from an I² test.
- Report heterogeneity, confidence/prediction intervals where appropriate, influential studies and sensitivity analyses.
- Avoid pooling molecular clade, reassortment, first-detection or chronology claims as if they were common effects.

### If the protocol remains unchanged, or pooling is not defensible

- Use SWiM: structured tables, effect/estimate ranges where meaningful, evidence-direction summaries only where justified, and transparent reasons for non-pooling.
- Do not use a forest plot or pooled estimate merely because some numbers exist.

### Deliverables

- Synthesis eligibility matrix.
- SWiM narrative synthesis or approved narrow meta-analysis output.
- Heterogeneity and sensitivity notes.
- Claim-to-extraction-to-reference audit trail.

### Gate H — pass criteria

- Every synthesis has a defined evidence set and rationale.
- The synthesis method matches the estimand and data structure.
- No pooled result combines incomparable designs, hosts, assays or molecular claims.
- All limitations and certainty qualifications are visible.

## Phase 8 — Manuscript reporting

### Tasks

- Only after Gates A–H, obtain explicit paste approval before editing the `.docx`.
- Update Methods: eligibility, actual sources and dates, exact strings, screening, extraction, RoB, certainty and synthesis method.
- Update Results: PRISMA flow, included studies, T6 exclusions, study characteristics, T1–T5/T7 tables and synthesis results.
- Update Discussion: main findings, surveillance/assay limitations, molecular uncertainty, source limitations and implications.
- State that the review was not prospectively registered.
- State the actual source layers: WoS API retrieval on 2026-09-19 is canonicalised in file 53;
  Google Scholar is an unmerged supplementary run; AJOL and WoS browser updates on 2026-09-20
  are documented but not fully imported. Do not describe retrieval candidates as eligible studies
  until screening and PRISMA accounting are complete.
- Write the Abstract last and preserve the required yellow `Abstract` heading, Times New Roman, British English and numeric bracket citations.

### Deliverables

- Paste-ready manuscript revision.
- In-manuscript tables and appendices only.
- Corrected reference order and DOI formatting.

### Gate I — pass criteria

- Every manuscript number traces to a final register or table.
- Methods, Results, Discussion and Abstract agree on dates, sources, counts and synthesis type.
- No prospective-registration claim, future-date claim or unsupported molecular claim remains.

## Phase 9 — Final audit and handoff

### Tasks

- Run PRISMA 2020 27-item plus abstract audit.
- Run PRISMA-S 16-item audit.
- Run SWiM nine-item audit if no meta-analysis; if pooling occurred, audit the quantitative synthesis method and amendment.
- Check PRISMA count arithmetic and duplicate handling.
- Check all citations, DOI styles, table references and accession numbers.
- Check no placeholders remain: `____`, `[X]`, `[CRD]`, `31 September 2026`.
- Check the manuscript opens and retains formatting.
- Record final limitations and unresolved evidence gaps.

### Gate J — final readiness

The review is submission-ready only when every mandatory audit item is `Yes` or has a documented justification and owner. A passed audit does not upgrade weak evidence; it demonstrates that the evidence and uncertainty are reported honestly.

## Immediate next actions

1. Use this plan as the master route; stop relying on stale phase status in older files.
2. Use `56_SCREENING_RECONCILIATION.json` as the sole controlled screening queue: 1,877 identities,
   six date flags held separately, and a 40-record stratified dual-review pilot.
3. Independently verify the AJOL source-to-canonical links and deterministic date flags; the source
   and identity QA are complete, but record-level screening remains provisional.
4. Remap and verify all preliminary screening decisions against the canonical identities; do not
   inherit precollapse aggregate votes silently.
5. Complete the R1/R2 pilot and adjudication before expanding title/abstract screening.
6. Only then begin full-text retrieval and T6 eligibility decisions.
7. Do not edit the manuscript or run a meta-analysis yet.
