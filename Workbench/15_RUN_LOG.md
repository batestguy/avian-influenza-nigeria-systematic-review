# Run log + gate checklists (update as you go)
## Phase D: extraction batch 04 - 2026-10-02 (latest)
- **Scope.** STU-038 to 048 and 050 to 053 (15 studies). Both reviewers were stopped by the session limit and resumed from their per-study files.
  - Both outputs validated. R1's quote check: 177 quotes, 0 missing. R2: 0 failures.
  - No email or personal identifier was sent (brief item 7). PMC's proof-of-work browser check on the CAN-0654 supplement was not bypassed.
- **Consensus.** `extraction/consensus_batch04.json` has 15 studies, 54 rows and 11 logged adjudications (`adjudication_batch04.json`).
  - STU-041: H5 HI split by state (Bauchi 6/200, Gombe 2/200).
  - STU-042: ELISA split by state (Oyo 19/315, Osun 4/95, Ondo 0/110). H3N8 HI positives are 22, not 18.
  - STU-043: 499 WAHIS reports covering 1,230 outbreaks.
  - STU-045: hotspot-state subset rows.
  - STU-047: national 299/1,675 row; year rows coded lab-confirmed (method NR); introduction NA.
  - STU-053: introduction "hypothesised only".
  - STU-040: JBI case series (new genomes).
- **Cross-study overlaps to settle at synthesis (count once).**
  - STU-040 and STU-053 share the same 21 Nigerian 2006-07 genomes (CY016276-91, CY016907-54, CY017179-86, EU148356-451). The register does not flag this yet.
  - The NVRI "299" appears three ways: STU-051 (farms out of 1,006 submitting farms), STU-047 (cases out of 1,675 suspected), and STU-025/110 (233 farms + 66 LBMs).
  - STU-048 and STU-052 sequence sets overlap CAN-0654, CAN-0863 and CAN-0541.
  - STU-043, 044 and 045 national records overlap.
- **Access.** Every report was read in full. Not obtained: the CAN-0654 supplement (Table S1, per-isolate state and date).

## Phase D: extraction batch 03 - 2026-10-02
- **Scope.** STU-021 to 024, 026, 027 and 029 to 037 (15 studies).
  - Both reviewers were stopped by the 1 Oct session limit and resumed from their per-study files. R1 was finished by a fresh executor session (STU-027, 029, 037).
  - Validation: R1 and R2 were both structurally valid. R2's quote check had 0 failures. R1 had 141 quotes, with 11 misses that are checker false alarms (column splits, non-ASCII decimals), all confirmed by hand.
- **Consensus.** `extraction\consensus_batch03.json` has 15 studies, 48 rows and 13 logged adjudications (`adjudication_batch03.json`).
  - STU-021: pooled Nigeria + Egypt markets (75 + 80), recorded as lab-confirmed with method NR.
  - STU-024: control-farm row added (by selection, do not add).
  - STU-027: 106 Nigerian HA sequences.
  - STU-031: Table 1 state rows, with the Fig 3 reading in estimate.
  - STU-033: own versus public sequences (R-e); H5N8 introduction "no" (R-k).
  - STU-035: introduction "no" (R-k).
  - STU-036: R1's full text used (legal Wetlands International copy).
- **Abstract only** (no legal full text; no CAPTCHA bypass): CAN-0191, CAN-0282 and CAN-0330. CAN-0539 was abstract only for R2, but R1 found the legal full text.
- **Eligibility queries to the author** (study IDs not renumbered while pending):
  - STU-032 (CAN-0356): its Nigerian content is a single narrative sentence plus a map.
  - STU-035 (CAN-0527): its Nigerian content is 19 H9N2 sequences reused from STU-071 in a regional phylogeography.
- **Author decisions (2026-10-02, yes/no in chat):**
  - STU-032 / CAN-0356 is **excluded** (reason "non-Nigeria no Nigeria-data"; `linkage/exclude_0356.py`). STU-032 is retired and the other study IDs are not renumbered.
  - STU-035 / CAN-0527 is **kept**, with an overlap flag to STU-071 (CAN-0491/1484/1585), so its sequences are counted once.
  - Flow recomputed by `prisma_flow.py`: databases arm 219 assessed, 107 excluded (non-Nigeria 53), 112 included. **Total 124 reports = 111 studies.** File 22 and the file 14 Methods sentence were updated.
- **Privacy incident.** An R1 session sent the user's email once as the Unpaywall `email=` parameter, without being asked. Later calls did not. A privacy rule was added to the brief (item 7), and the author has been told.

## Phase D: extraction batch 02 - 2026-10-01
- **Scope.** STU-006 to 020 (15 studies). After the session-limit stop, R1 and R2 were relaunched at about 09:30. They extracted blind, and both outputs validated with no structural errors.
- **Consensus.**
  - `extraction\consensus_batch02.json` has 15 studies, 54 findings rows and 16 logged adjudications (`adjudication_batch02.json`).
  - Every study uses R1 as the base except STU-019, which uses R2 because only R2 opened the PMC supplement (Tables S1/S2: Nigerian sequences H5N1 280, H5N2 3, H5N6 1, H5N8 5, of 289).
- **Main fixes.**
  - STU-008: R2's host classification (the production system is not stated for 3 flocks), with flock counts. The NVRI result for case 10345 is coded RNA H5N1.
  - STU-013: LBM surveillance split into 25 infected states (13,884 samples) and 11 non-infected states (5,807).
  - STU-014: wild and captive serology rows added, marked "subset; do not add".
  - STU-007 and STU-012: subtype "type A" (not subtyped).
  - STU-006: host system NR.
- **Form v2.2 rules R-i to R-n** added:
  - host_system = sampling setting
  - "NR (abstract only)" for introductions
  - "introduction" = into Nigeria or into a new zone
  - subtype "NA" only for serology
  - no template text as a value
  - open the supplement tables before recording NR
- **Access gaps.** CAN-0129 (STU-015) and CAN-0147 (STU-014) were available as abstracts only (Springer; the ResearchGate copies returned 403, with no bypass). The full text of CAN-0209 was not retrieved.
- **Notable source errors**, logged per study, for RoB and synthesis:
  - CAN-0087: its Table 1 total double-counts 2006 (1,893,708 vs 1,250,345).
  - CAN-0155: labels the 2015-16 genomes clade 2.3.2.1f, but the primary reports use 2.3.2.1c.
  - CAN-0114: altitude P = 0.000, but a recomputation gives P ≈ 0.17.

## Phase D: extraction batch 01 - 2026-10-01
- **Scope.** 15 studies: the 10 pilot studies re-done under form v2, plus STU-001 to 005.
  - R1 and R2 extracted blind. R1 was resumed after the 30 Sept interruption from its per-study files; R2 was rebuilt from its cached texts.
  - Quote checks: R1 169/173 matched (4 false alarms confirmed by eye); R2 202/202.
- **Agreement.**
  - Period and design agreed in 15/15 studies; headline counts agreed in most.
  - Differences were mainly labels: evidence type for records versus lab-confirmed cases, "hypothesised" versus NA introductions, and NA conventions.
- **Consensus.**
  - `extraction\consensus_batch01.json` is R1 as the base, with 18 logged adjudications (`adjudication_batch01.json`) and R2's inconsistency findings merged in.
  - Numbers fixed: STU-004 542/1,137; STU-057 228 screening denominator; STU-025 299/1,654; STU-003 157.
  - Classifications fixed: STU-071 H5N6 is an inherited reassortant; STU-100 rows are official reports; STU-110 rows are lab-confirmed cases with method NR.
- **Form v2.1 rules R-a to R-h** added to `EXTRACTION_FORM_v2.md`:
  - NA conventions for introduction and reassortment
  - `n_tested` is the first screening denominator
  - authors' own sequences are evidence type "sequence"
  - records with no assay are "official confirmed report"
  - subset rows are allowed, marked "do not add"
  - sub-state counts go in `estimate`
- **Scope note.** STU-110 is now thesis Study 1 + CAN-0714/1845/0039. The FFPE work counts under STU-005 and the mixed-species work under STU-104, per `also_reports_on`.
- **Batch 02** (STU-006 to 020) launched.
## Phase D: extraction pilot and form v2 - 2026-09-30
- **Pilot.** Two extractors worked blind on the same 10 studies with per-study form v1:
  - R1 = `executor` (Opus 5.5); R2 = `reviewer` (Sonnet 5.5).
  - The 10: STU-025, 028, 049, 057, 063, 069, 071, 072, 100 and 110.
  - They cover molecular, serology, official-records, secondary, wild-bird, thesis, LPAI, national surveillance and spatial studies.
  - The unit is one record per study, drawn from all its reports.
  - Workspace: `D:\AvianInfluenzaSysRev_retrieval_20260927\extraction\` (`EXTRACTION_FORM_v1.md`/`v2.md`, `BATCH_BRIEF.md`, `R1_pilot.json`, `r2_scratch\R2_pilot.json`).
- **Agreement.** High on design, period, states, subtypes, headline counts and reassortment/introduction calls. Differences came mainly from the form:
  - findings-row granularity
  - pathotype basis
  - no "inherited reassortant" or "hypothesised introduction" options
  - one citation field for multi-report studies
  - RoB tool choice for records reviews and secondary studies
- **Adjudicated:**
  - STU-071: the Nigerian H5N8 is "inherited" (its reassortant genotype was shown elsewhere). The H9N2 19 genomes go in one row.
  - STU-110: introduction is "hypothesised only".
  - STU-028: Jema'a is recorded as printed, with the inconsistency logged.
  - STU-025 shares the NVRI 2006-08 dataset (299 cases) with STU-110 and is counted once.
- **Access gaps.** CAN-0244 (the only report of STU-025) and CAN-0329 could be read only as abstracts, because of paywall or CAPTCHA blocks; no bypass was attempted.
- **Internal inconsistencies found in reports:**
  - CAN-1796: 304 cases vs 287 positive farms; birds 889,980 / 825,000 / 836,031.
  - CAN-1785: four LGAs, not five; 0.8% printed for 5/250.
  - CAN-0782: "H5N2" applied to H5-only RT-PCR positives.
  - CAN-2033: "all clade 2.2" from a 154-nt BLAST, one clone best matching Vietnam 2005; OR 3.02 is a mortality contrast, not infection risk.
  - CAN-1602: 13 H5N8 genomes vs 12 outbreaks.
- **Form v2.** Adds:
  - per-report access level
  - the row rule (evidence × subtype × host × state × year)
  - `pathotype_basis`, `n_characterised` and `report` per row
  - reassortment "inherited" and introduction "hypothesised only"
  - `molecular` as a per-subtype list
  - `inconsistencies` and `other_outcomes`
  - a RoB-tool mapping rule
- **Full extraction.** 112 studies, in batches of about 15, with dual blind R1/R2 per the protocol (dual for outcome fields). Batch 01 is the 10 pilot studies re-done under v2, plus STU-001 to 005. Each batch is compared and adjudicated by the main session.
## Phase B addendum: the author's second pass over the 107 priority rows - 2026-09-30
- **Why.** No second human screener is available, so the author chose to recheck the 107 priority rows themselves before Phase D.
- **Tool.** A private page, https://claude.ai/artifact/9jhGWfFgZtxun9p8HnfEqS.
  - It shows one row per screen: the current register decision, the reviewers' evidence and the author's first-check answer.
  - The author answered each row directly (Correct / Change it / Not sure); nothing was transcribed by the AI.
  - Answers are stored in the page's db collection `recheck`.
- **Result.** 107/107 marked correct: no changes, no "not sure" rows, no notes.
  - Recorded in file 58 (new columns `recheck_decision` and `recheck_at`) and in file 56 (`human_verification.recheck` per record, plus `metadata.human_verification.recheck`).
- **Timing.** All answers were entered between 01:01:20 and 01:04:51 UTC, about 2 seconds per row. Report this pass as a reconfirmation, not an independent re-review. File 14 says so.
- **Next:** Phase D.
## Phase C: report-to-study linkage and PRISMA 2020 flow - 2026-09-30
- **Method.**
  - R1 (`executor`, Opus 5.5) proposed links for the 126 retained reports from full texts (legal routes only) and OpenAlex/Crossref author metadata. It started from 21 candidate clusters and reported 205 pairwise relations.
  - The `reviewer` agent (Sonnet 5.5) checked the links against the texts. The main session adjudicated.
  - A study is a set of reports sharing samples, animals or outbreaks (Cochrane Handbook ch. 5), not merely authors. Separate studies that reuse the same data are flagged `overlapping_data` so synthesis counts those data once.
  - Workspace: `D:\AvianInfluenzaSysRev_retrieval_20260927\linkage\`. Files: `R1_linkage.json`, `linkage_final.json`, `adjudicate_linkage.py`, `apply_linkage.py`, `prisma_flow.py`.
- **Reviewer fixes applied.**
  - R1's STU-101 (Fasanmi thesis) and STU-104 (Fasina thesis) bundled sibling papers that share no samples. Both were split: CAN-0174 and CAN-0266 are separate studies, and so is CAN-0339.
  - In the Akanbi thesis study, CAN-1907 (a different case definition) and CAN-0031 (FFPE sub-study) became separate studies.
  - CAN-1730 is now `overlapping_data` with CAN-0114 at specimen level: count the shared Bauchi/Gombe sera once.
  - Not-retrieved companions CAN-0204 and CAN-1939 are marked possible, unverified.
  - R1's checker forced same_study labels onto sibling pairs through transitivity; those labels were corrected.
- **Result.** **126 reports = 113 studies**, then **125 reports = 112 studies** after the author excluded CAN-1610 (below). Study IDs below are the post-exclusion numbering. 10 studies have more than one retained report:
  - STU-004: CAN-0025 + 1902 (NVRI 2015 resurgence).
  - STU-008: CAN-0060 + 1711 (Zaria case 10345).
  - STU-014: CAN-0114 + 0147 (Bauchi/Gombe survey); CAN-0209 not retrieved.
  - STU-022: CAN-0191 + 1882 (preprint and article).
  - STU-028: CAN-0329 + 1785 (the same 480 Kaduna sera).
  - STU-071: CAN-1585 + 0491 + 1484 (2019 national LBM surveillance; keep H9N2, H5N6 and H5N8 separate).
  - STU-084: CAN-1712 + 1453 (the same Gombe duck isolates).
  - STU-086: CAN-1715 + 0058 (the same article recorded twice).
  - STU-108: CAN-2005 thesis + 0337 (the same 35 isolates).
  - STU-110: CAN-2033 thesis + 0039, 0714, 1845 (NVRI 2006-08 submissions, 233 farms).
- **Written to file 56.** `report_linkage` fields study_id, study_role, study_reports, study_basis and overlapping_data_with on all retained reports (125 after the exclusion), plus `metadata.report_study_linkage`.
- **Not verified in full text.** CAN-0031, 0058, 0066, 0129, 0147, 0191, 0243, 0244, 0282, 0329, 0330 and 1662; their links rest on register evidence and metadata.
- **Author decision (2026-09-30): CAN-1610 excluded** (retain → exclude, rule Q1, reason "no primary data"; `human_override` in file 56, file 58 row 174 set to disagree; script `linkage/exclude_1610.py`). CAN-1610 is Cui et al. 2025 (Viruses), a compilation of 658 pigeon sequences from 21 countries. Its only Nigerian datum is one 2006 isolate, which is already in CAN-2005/0337. The register R1 evidence misnamed its journal.
- **Extraction flags.**
  - CAN-0114: 950 vs 1,000 sera.
  - CAN-0266 vs thesis: 465 vs 840 outbreaks.
  - CAN-1785: "five LGAs" but four tabulated.
  - CAN-0058: register year 2017; the article is 2020/21.
  - CAN-1796 is the umbrella for Plateau outbreak counts (it covers CAN-2009 and CAN-1719).
  - CAN-0745 embeds the Kano and Enugu records.
- **PRISMA 2020 flow** (`prisma_flow.py`; all reconciliation asserts pass).
  - **Databases arm:**
    - Identified: 2,367 (OpenAlex/Crossref 1,744, PubMed 140, Scopus 204, WoS 175, ScienceDirect 25, AJOL 79).
    - Duplicates removed: 490. Screened: 1,877.
    - Excluded on title/metadata: 1,578, of which 6 were outside the date window.
    - Sought: 299. Not retrieved: 80. Assessed: 219.
    - Excluded: 106 (non-Nigeria 52, no lab-confirmed avian AIV 19, no avian-host field data 17, no primary data 13, no epi/molecular/spatial-temporal data 2, duplicate dataset 1, non-AIV 1, experimental only 1).
    - Reports included: 113.
  - **Other methods** (Google Scholar dated update search, 2026-09-28):
    - 800 rows; 519 unique; 291 already identified; 228 new, of which 12 were later found to be duplicates. Screened: 216.
    - Excluded on title/snippet: 190. Sought: 26. Not retrieved: 8. Assessed: 18.
    - Excluded: 6 (non-Nigeria 2, no primary data 2, no lab-confirmed avian AIV 1, experimental only 1).
    - Reports included: 12.
  - **Total: 125 reports of 112 studies** (after the CAN-1610 exclusion; before it, 126 and 113).
- **Register note corrected.** `metadata.human_verification` still said "429/429 confirmed; 0 overturned" (from the blanket stage). It now records 423 agree / 6 disagree and both stages.
## Phase B: row-level check of the 107 priority decisions - 2026-09-29 (supersedes the blanket-only note below)
- **How it was done.** The author (MO) went through all 107 `must_check` rows in chat, in three batches.
  - The AI assistant prepared a one-line summary of each row, gave its own read (flagged as not independent, since it adjudicated these decisions), and raised three consistency questions.
  - The author answered each batch; the AI transcribed the answers. Script: `votes/apply_human_review.py`. Decisions: `votes/human_review_20260929.json`.
  - Rows in file 58 now read "Row-level assisted review" (107 rows) or "Blanket confirmation" (322 rows).
- **Rules set by the author** (also stored in `metadata.human_verification.rules`):
  - **Q1 A:** secondary or global analyses that reuse Nigerian data are eligible if they produce Nigeria-specific analytic results. Narrative compilations, reprinted tables and model predictions are not.
  - **Q2 A:** official outbreak records described as confirmed are eligible even without a named assay; they are flagged for sensitivity analysis.
  - **Q3 A:** reports that only reprint official outbreak tables (CAN-0055, CAN-2082) stay excluded.
- **Changes (6 of 107).** Everything else was confirmed.
  - CAN-1535 and CAN-1558: exclude → retain (Q1).
  - CAN-1672 and CAN-2009: exclude → retain (Q2; CAN-2009 is the weakest, since it states neither "confirmed" nor an assay).
  - CAN-0343 and CAN-0345: title exclusion → full text. Both reviewers had retained them, and the adjudication override had no recorded reason.
- **CAN-0343 and CAN-0345 at full text.** Both open-access publisher PDFs were obtained and identity-verified. Blind R1 (Opus 5.5) and R2 (Sonnet 5.5) both excluded them as "non-Nigeria no Nigeria-data".
  - CAN-0343: Poyang Lake, China.
  - CAN-0345: 7 Central/West African countries, not including Nigeria. Its Nigerian citations (Joannis 2008; Nwankwo, Sokoto) are already retained as CAN-1357 and CAN-0086.
- **Process note.** R1 and R2 wrote text extracts to the same scratch folder, so one overwrote the other's extracts. Votes and blinding were unaffected. From now on, give each reviewer its own scratch subfolder.
- **Register.**
  - 2,105 records = **1,768 title/metadata excluded + 325 full-text candidates + 12 duplicate records removed**.
  - 325 = **126 provisional retain + 111 excluded + 88 not retrieved**.
- File 14's Methods and Limitations now describe the row-level assisted check accurately.
## Phase B: human verification - 2026-09-29
- **The sheet.** `Workbench/58_HUMAN_VERIFICATION.csv` is the user-approved sidecar, built by `votes/build_human_verification.py` from file 56.
  - 429 decisions: 122 full-text retains, 113 full-text excludes, 12 duplicate removals, and 182 title exclusions (seeded 10% sample of 1,770, seed 20260929, plus 5 adjudication overrides).
  - 107 rows are flagged must-check (batches 5-6, the Scholar full-text screen, borderline cases, R1/R2 disagreements, overrides and duplicates).
  - A `reviewer` agent audited it against the register: 0 mismatches over all 429 rows. Its should-fix items (unusable punctuation-stripped DOIs, HTML in titles, mid-word truncation) were fixed.
- **Verification.** The author, **Mayowa Olabode (MO)**, confirmed all AI decisions in the session chat ("I agree with all AI decisions").
  - Because of physical limitations, the author asked the AI assistant to enter the confirmation on their behalf. All 429 rows read `agree`, MO, 2026-09-29, with a note stating this.
  - The register now has a `human_verification` field on each of the 429 records and a `metadata.human_verification` summary. 0 decisions were overturned.
- **Caveat.** This is a blanket confirmation transcribed by the AI, not a row-level independent check. The 100% human-AI agreement **must not** be reported as an agreement statistic.
- **Methods and Limitations.** Draft text was added to file 14. Before submission, the author must confirm how the accessibility wording should read. A second human screener checking the 107 priority rows would materially strengthen the review.
## Reviewer audit corrections - 2026-09-29 (supersedes counts below)
- An independent `reviewer` agent (Claude Sonnet 5.5) audited today's register changes. There were no blocking findings. All counts, κ values and 10 duplicate calls reproduced; 19 PDFs were identity-checked; no shadow-library or login-gated source URL was found.
- **False claim corrected.** The retrieval section below says the looser re-check "found no others". That was wrong.
  - The auditor found CAN-2073 = CAN-1687 (same DOI 10.4161/viru.26360; both title-excluded).
  - **Root cause:** older register records store DOIs with punctuation stripped (e.g. `104161viru26360`), so DOI matching against Scholar DOIs never fired.
  - A normalised-DOI re-check of all 228 then found **CAN-1941 = CAN-0835**: same DOI 10.12834/VetIt.870.4301.3, the bilingual Veterinaria Italiana article, both retained. No others were found.
  - Both are now `duplicate_record_removed`. CAN-1941's full-text votes are kept for audit only.
- **Linked for Phase C:**
  - CAN-2044 (2009 poster) ↔ CAN-0061 (the same case-control study; not retrieved).
  - CAN-2040 (French report) → CAN-0359 (Nature 2006, Ducatez et al.).
  - CAN-1939 remains a not-retrieved companion of the retained CAN-1778.
- **Consistency flag.** The line between retained records-based outbreak reports (CAN-1914, CAN-1719, CAN-1347) and excluded ones (CAN-2009: confirmation not stated; CAN-2082: official tables reproduced without analysis) is thin. CAN-1914, 2009, 2082 and 1806 are marked `phase_b_must_check`.
  - The CAN-1914 basis now describes chapter 6 (economic-impact chapter; epidemic curves from official RT-PCR-confirmed records) and chapter 5 (hotspot map) precisely. It no longer says "original analyses".
- **Register metadata.** Stale fields are updated or marked superseded (`retrieval_summary`, `last_update`, `scholar_rerun_20260928.result`).
- **Corrected register.**
  - 2,105 records = **1,770 title/metadata excluded + 323 full-text candidates + 12 duplicate records removed** (2,093 unique identities).
  - 323 = **122 provisional retain + 113 excluded + 88 not retrieved**.
  - The Scholar re-run's 228 = 12 duplicates + 190 title-excluded + 26 to full text (11 retained, 7 excluded, 8 not retrieved). CAN-1806, advanced from the original screen, was excluded.
  - Full-text agreement on the 20 screened reports stays 19/20 (κ 0.90).
## Scholar re-run full-text screen - 2026-09-29 (full-text gate closed again)
- **Screen.** 20 reports were screened: the 19 obtained non-duplicates, including CAN-1806 via the CAN-1974 copy, plus CAN-2026 obtained on retry.
  - Reviewers: R1 was the executor agent (Claude Opus 5.5) and R2 the reviewer agent (Claude Sonnet 5.5, blind; first R2 batch on 5.5 per the MINOR amendment).
  - Decision agreement: 19/20. There were two reason-only disagreements.
  - Votes: `votes/R1_scholar_ft.json` and `R2_scholar_ft.json`; script `votes/adjudicate_scholar_ft.py`.
- **Adjudication (main session).**
  - **CAN-1914 retained** (R1 retain / R2 exclude). Chapter 6 (an economic-impact chapter; PDF pp.160-162) gives epidemic curves for 2006-08 and 2015-17 from official RT-PCR-confirmed NVRI/FDL/OIE outbreak records (840 confirmed outbreaks, Dec 2014 to May 2017). Chapter 5 gives a hotspot map. This is consistent with CAN-1719 and CAN-1347. It is flagged as records-based, for sensitivity analysis and as a Phase B must-check.
  - **CAN-2044:** "no primary data" (poster of a planned study).
  - **CAN-2068:** "experimental only no field relevance" (H9 assay validation; Nigerian content is a reference strain only).
  - **CAN-2009 and CAN-2082:** concordant excludes kept, after a main-session check. CAN-2009 does not state laboratory confirmation. CAN-2082 is a desk review reproducing official tables without analysis.
  - **CAN-1995:** kept as a weak retain (egg-yolk antibody in captive quails).
- **Result.** 12 retained: CAN-1882, 1884, 1902, 1907, 1914, 1919, 1941, 1995, 2005, 2033, 2038, 2056. 8 excluded: CAN-1806, 1948, 2009, 2026, 2044, 2068, 2082, 2094.
- **Overlap for Phase C.**
  - The 2006-07 NVRI outbreak dataset underlies CAN-1907, CAN-1941 and CAN-2033 (and likely CAN-2038/2056).
  - CAN-2005 (Fasina MSc) overlaps the Fasina papers.
  - CAN-1902 overlaps the 2015 outbreak reports.
  - CAN-1882 is the preprint of CAN-0191.
- **Register.**
  - 2,105 records = 1,771 title/metadata excluded + 324 full-text candidates + 10 duplicate records removed.
  - 324 = **123 provisional retain + 113 excluded + 88 not retrieved**. None are pending.
  - These are report counts; study counts await Phase C.
## Scholar re-run full-text retrieval - 2026-09-29
- **Retrieval.** The executor agent ran the legal sweep for the 36 retains.
  - Routes: Scholar links, publisher/DOI, Unpaywall, OpenAlex, the PMC open-access copy on AWS (used where PMC or MDPI showed a reCAPTCHA), repositories (UP, UI, UILSpace, CGSpace, NVRI, SVEPM), and 23 SerpApi Scholar version look-ups. No shadow library, CAPTCHA bypass, login or author contact was used; the source URLs were audited in the main session.
  - Result: 26 full texts obtained and identity-verified (CAN-2038 and CAN-2056 by Tesseract OCR); 10 not obtained.
  - Route log: `D:\AvianInfluenzaSysRev_retrieval_20260927\work\scholar36_retrieval.json`, now copied into each record's `retrieval` field.
- **Correction: 10 duplicate records.** Once the full texts were in hand, 10 of the 228 "new" records turned out to be existing identities. The 2026-09-28 title matching (threshold 0.90; Scholar titles truncated, garbled or mis-titled) had missed them.
  - The 10 pairs: CAN-1879→1585, 1910→1602, 1922→0642, 1942→1716, 1969→0191, 1974→1806, 2046→1734, 2067→0046, 2070→1778, 2079→1357.
  - A looser re-check of all 228 (similarity ≥0.75 plus substring match, each hit judged by hand) was run. [Corrected by the audit above: it missed CAN-2073 and CAN-1941, found later by normalised DOI.]
  - They are now `duplicate_record_removed`, with the evidence in `report_linkage`, and are counted as duplicates removed rather than as screened identities.
  - Companion preprints are linked for Phase C: CAN-1882 → CAN-0191 and CAN-1939 → CAN-1778.
- **CAN-1806 advanced to full text.** It was excluded at title stage in the original screen, but its duplicate CAN-1974 was retained by the fresh blind screen. Conservative union across the two screens moves it to full text, using the copy obtained under CAN-1974. The previous decision is kept in `title_rescreen`.
- **Register.**
  - 2,105 records = 2,095 unique identities + 10 duplicate records removed.
  - 1,771 title/metadata excluded.
  - 324 full-text candidates = 111 provisional retain + 105 excluded + **89 not retrieved** (80 + 9) + **19 pending R1/R2 full-text screen**.
  - The 9 new not-retrieved were CAN-1881, 1909, 1920, 1931, 1939, 2023, 2026, 2040 and 2095. **Update, same day:** CAN-2026 was obtained on one retry via the WHO IRIS REST API, which was reachable again (Wkly Epidemiol Rec No. 42, 15 Oct 2010, PMID 20949701).
  - Net for the Scholar re-run: **20 pending R1/R2 full-text screen, 8 not retrieved**.
  - Full-text candidates are now 324 = 111 + 105 + 88 not retrieved + 20 pending.
## Phase A checkpoint - 2026-09-29
- **A1 Scholar re-run screened.** The 228 new records went into a blinded packet (SCH-001 to SCH-228: title, year, venue line, Scholar snippet, link). They were screened on the file 18 form by R1 (executor agent, Claude Opus 5.5) and R2 (reviewer agent, Claude Sonnet 5, blind to R1).
  - **Votes:** R1 20 include / 9 unsure / 199 exclude; R2 22 include / 14 unsure / 192 exclude.
  - **Agreement (retain = include or unsure):** 215/228 (94.3%), Cohen's κ 0.77.
  - **Adjudication (main session):** conservative union, with three overrides to exclude:
    - SCH-090: human isolate only (no avian-host field data)
    - SCH-211: human bird handlers only (no avian-host field data)
    - SCH-192: correspondence (no primary data)
  - **Result:** 36 retained for full text and 192 excluded. They were added to file 56 as CAN-1878 to CAN-2105; the SCH→CAN map is in `metadata.scholar_rerun_20260928`. Seven possible duplicate pairs are flagged in `report_linkage` (e.g. SCH-092/SCH-005 and SCH-193/SCH-062, both retained).
  - **Register now:** 2,105 identities; 1,773 title/metadata excluded; 332 full-text candidates = 111 provisional retain + 105 excluded + 80 not retrieved + **36 pending retrieval**. The full-text gate is reopened for the 36.
  - **Files:** votes in `D:\AvianInfluenzaSysRev_retrieval_20260927\votes\R1_scholar.json` and `R2_scholar.json`; adjudication script `adjudicate_scholar.py`.
- **A2 Reviewer agreement: all R1/R2 pairs are AI agents** (Codex, then Claude). These figures are AI-AI agreement, not human-AI agreement (see Phase B).
  - **Title/metadata (1,877 original identities):** 1,821/1,877 agree (97.0%), κ 0.88. Of the 56 disagreements, 31 were R1 exclude / R2 retain and 25 the reverse. In 2 further records both reviewers retained and adjudication excluded.
  - **Full text (216 assessed):** votes were normalised to retain / exclude / unsure (`exclude_recommended` = exclude; `uncertain`, `unclear` and `seek_further_info` = unsure).
    - Three-category agreement: 187/216 (86.6%), κ 0.76.
    - Where both reviewers gave a definitive vote: 181/190 (95.3%), κ 0.90.
    - Batches 5-6 (current R1/R2 pairing): 42/46 (91.3%), κ 0.83.
    - Concordant exclusions with the same fixed reason: 32/43.
  - **Scholar re-run title stage:** see A1 above.
- **A3 The 80 not-retrieved reports.**
  - **By period:** 2006-10 27; 2011-15 23; 2016-20 15; 2021-26 15.
  - **Identifiers:** 66 have a DOI, 19 a PMID, and 12 neither.
  - **Sources:** 40 are OpenAlex/Crossref only; the rest came from at least one bibliographic database.
  - **Likely relevance (main-session title-level judgement, provisional):** about 33 look like Nigerian avian laboratory or epidemiological reports: CAN-0014, 0015, 0017, 0027, 0032, 0048, 0051, 0061, 0064, 0089, 0122, 0189, 0204, 0205, 0208, 0209, 0359, 0575, 0576, 0608, 0609, 0612, 0619, 0632, 0655, 0742, 1143, 1179, 1180, 1254, 1291, 1843, 1870. Three of these have their study represented by a retained report: CAN-1179 (by CAN-1152), CAN-0204 (by CAN-0008) and CAN-1291 (by CAN-1602).
  - **The other ~47** appear to be human-, mammal- or non-Nigeria-only, risk/biosecurity/economic reports without laboratory data, or reviews.
  - **Possible duplicate:** CAN-0014 and CAN-0015 share a title (2019/2020 records) and may be one report counted twice; resolve in Phase C.
  - This profile feeds the manuscript appendix and the Limitations text (risk of missing studies).
## Expert audit and Scholar update search - 2026-09-28
- **Expert audit against PRISMA 2020 / Cochrane ch. 4-5 / 2025 AI-in-evidence-synthesis guidance.** Process documentation judged strong (dated freeze, graded amendments, dual votes + adjudication, one fixed reason, per-record access routes, honest not-retrieved handling). Seven gaps: (1) no human reviewer recorded at any screening stage (R1/R2/arbiter all AI agents); (2) most of the 1,581 exclusions are title/metadata-only (OpenAlex/Crossref records lack abstracts); (3) the 17 Sept Scholar supplement was never screened; (4) 80/296 (27%) reports not retrieved, which must be characterised; (5) no agreement statistics and no PRESS search peer review; (6) no PROSPERO registration and sources added 17-20 Sept around the freeze (already dated; report clearly); (7) report-to-study linkage and PRISMA study counts not done. Remediation plan (Phases A-D) is in file 57.
- **Phase A1 started.** The 17 Sept SerpApi Scholar run had no persistent export, so its 50 unmatched records cannot be reconstructed. The same Q1-Q4 queries were re-run on 28 Sept via SerpApi with the same parameters (`as_ylo=2006`, `as_yhi=2026`, `as_sdt=0` no patents, `as_vis=1` no citations, relevance, 20/page, cap 200/query; 40 API searches). Result: 800 rows (200 per query) → 519 unique titles; 291 matched register identities (DOI, title similarity ≥0.90, or a unique substring match for Scholar-truncated titles); **228 are not in the 1,877-identity register**. Spot checks confirmed genuine absences, including in-scope Nigerian reports (e.g. Ifende et al. 2015 NVRI overview of the 2015 HPAI outbreaks; Yakubu et al. 2025 exotic/zoo birds; Balami et al. 2025 pigeons, Maiduguri; Akanbi et al. 2016 mixed-species farms; Akintule et al. 2026 commercial farms) and the comparator review Kalonda et al. 2020. Raw pages, scripts and the reconciliation output are outside the repo at `D:\AvianInfluenzaSysRev_retrieval_20260927\scholar_rerun\` (`run_q1q4.py`, `raw_q1q4_20260928.json`, `reconcile.py`, `reconciled_20260928.json`).
- **Not yet done:** the blinded packet (SCH-001 to SCH-228) was not written because of a tool outage; the 228 are unscreened and file 56 is unchanged (1,877 identities; 1,581 / 111 / 105 / 80). See file 57 for resume steps.
## Retrieval and screening checkpoint - 2026-09-28
- The 32 candidates from 27 Sept were identity-verified (six scanned PDFs were checked by Tesseract OCR) and screened as batch 5 (independent R1/R2 plus main adjudication): 13 retained and 19 excluded (commit `15c316e`). CAN-1627 and CAN-1672 were decided on the text as published (no laboratory-confirmed results reported). R2's quoted "confirmed positive" phrase for CAN-1672 was not found in the text, so the adjudication relied on the verified passages.
- Sweeps 3-4 and the browser pass obtained 14 more full texts; the remaining 80 open reports are `report_not_retrieved` (commit `2087a50`). Route logs and scripts are in `D:\AvianInfluenzaSysRev_retrieval_20260927\`. Batch 6 (the 14; independent R1/R2 plus main adjudication): 6 retained (CAN-0835, CAN-1716, CAN-1717, CAN-1719, CAN-1731, CAN-1735) and 8 excluded. Pig/horse-only serology (CAN-0062, CAN-1725, CAN-1871) was excluded as no avian-host field data.
- **Full-text gate closed.** Register: 1,581 title/metadata excluded; 296 full-text candidates = 216 assessed (111 provisional retain + 105 excluded) + 80 reports not retrieved. These are report counts; study counts await overlap resolution.
## Retrieval checkpoint - 2026-09-27 (session paused)
- Register eligibility counts are unchanged (170 adjudicated: 92 retain / 78 exclude; 126 open). The 28 stale `full_text_status` values were normalised (commit `8d68ad2`). Protocol amendments for the unretrievable rule and the reviewer identities are in the Amendments section below.
- A legal open-access retrieval sweep of the 126 open records was stopped partway because of the usage limit. It did not write to file 56. Of 32 downloaded candidates, none has been verified yet; they and the route logs are kept outside the repo at `D:\AvianInfluenzaSysRev_retrieval_20260927\`. See file 57 for the resume steps.
## Full-text checkpoint - 2026-09-27 (fourth batch)
- Another 32-record original-publication access audit yielded nine independent R1/R2 adjudications: CAN-0244, CAN-0282, CAN-0329 and CAN-0330 provisionally retained; CAN-0416, CAN-0483, CAN-0485, CAN-0499 and CAN-0570 excluded. The register now has **170 adjudicated reports (92 provisional retain; 78 exclude)** and **126 open candidates (125 unassessed; CAN-1627 seek further info)**, reconciling to 296 full-text candidates. These are report counts, not final included studies or PRISMA counts.
- CAN-0244's 2006–08 NVRI outbreak series overlaps the source period for CAN-0070 and other national reports. CAN-0282 reanalyses 106 Nigerian HA sequences; do not infer new field isolates. CAN-0329 and CAN-0330 report H5 or influenza A antibodies, which indicate exposure only; CAN-0330's virus isolation was negative. Twenty-three further records had original access routes documented without a full-text vote. CAN-0215's indexed excerpts and CAN-0541's single-reviewer copy were insufficient for adjudication. No author contact occurred and the manuscript `.docx` was not edited.

## Full-text checkpoint - 2026-09-27 (latest; third batch)
- A further independent R1/R2 batch adjudicated four original publications: CAN-0070 and CAN-0129 provisional retain; CAN-0097 excluded for no Nigerian data; CAN-0187 excluded for no primary data. Current counts are **161 adjudicated reports (88 provisional retain; 73 exclude)** and **135 open candidates (134 unassessed; CAN-1627 seek further info)**, reconciling to 296 full-text candidates. CAN-0070's 2006–07 NVRI outbreak records may overlap later spatial reports; compare line lists. CAN-0129's 14 Nigerian 2015 HA accessions KU971602–KU971615 need overlap matching before study counting.
- Original-publication routes were attempted for eleven further records without verified full text. CAN-0207's accessible 2021 JALSI article is a different publication from the canonical 2016 IJID abstract; it was correctly left unassessed. CAN-0204/0205/0206 are indexed conference abstracts with empirical leads, but no matching full publication was verified. No decisions were inferred from their abstracts. Access attempts and the CAN-0207 identity warning are in file 56. No author contact occurred; the manuscript `.docx` was not edited.

## Full-text checkpoint - 2026-09-27 (latest; second batch)
- Independent R1/R2 review and main adjudication closed eight more original full texts: six provisional retains (CAN-0031, CAN-0033, CAN-0053, CAN-0058, CAN-0065, CAN-0066) and two exclusions (CAN-0046, CAN-0063). The controlling register now has **157 adjudicated reports (86 provisional retain; 71 exclude)** and **139 open candidates (138 unassessed; CAN-1627 seek further info)**. The 296 full-text candidates reconcile as 157 + 139. These remain report counts, not a final included-study or PRISMA count.
- CAN-0033 is a secondary HA1 sequence reanalysis with extractable Nigerian phylogenetic results; link its GenBank sequences to original sources and do not count new Nigerian field isolates. CAN-0063 tested bird sera against human seasonal H3N2 and influenza B antigens, without an avian AIV-specific result. CAN-0046 models hypothetical risk without observed laboratory-confirmed avian AIV outcomes. The four serology/assay studies retained in this batch require careful separation of exposure from active infection, subtype and pathotype; CAN-0053's H5N1 attribution and CAN-0065's internal arithmetic require extraction QA. Original URLs and reviewer evidence are recorded in file 56.
- Seventeen other records in this 25-record batch remain unassessed because original full text was unavailable or unverified; their access leads and search attempts are in file 56. Continue original-source retrieval and independent assessment. No author contact occurred and the manuscript `.docx` was not edited.

## Full-text checkpoint - 2026-09-27 (latest)
- A second independent full-text batch added four provisional retains: CAN-1347, CAN-1501, CAN-1637 and CAN-1737. Current counts are **149 adjudicated reports (80 provisional retain; 69 exclude)** and **147 open candidates (146 unassessed; CAN-1627 seek further info)**. The 296 full-text candidates reconcile as 149 + 147. CAN-1731 and CAN-1870 remain unassessed after failed legitimate PDF routes.
- CAN-1737 was a reviewer disagreement: R2 proposed exclusion because its Oyo duck results were antibody-only; R1 retained. The arbiter retained it under the frozen file 10 criterion, which expressly permits a stated serological assay in avian hosts. Its 85/200 ELISA-positive result is exposure evidence only, not active virus detection, subtype, pathotype or current circulation. CAN-1501 reports 17/28 matrix-gene RT-PCR-positive Maiduguri ducks, without subtype/pathotype; site counts need extraction QA. CAN-1637 documents six laboratory-confirmed Jos farm events in 2021 (four H5N1, two H5N8); check overlap with other Plateau reports. CAN-1347 analyses 67 confirmed Rivers outbreak reports in 2015-2022; its affected-bird totals and conclusion have internal inconsistencies, and source-line-list overlap remains to check.
- The first 27 September independent R1/R2 batch provisionally retained CAN-0147, CAN-0744, CAN-0745, CAN-0746 and CAN-1630. All counts above remain report counts, not final study or PRISMA counts.
- CAN-0147 reports Nigerian Bauchi/Gombe RT-PCR-positive AIV bird swabs. CAN-0744 and CAN-0745 analyse laboratory-confirmed poultry surveillance/outbreak records, with overlap against national line lists still to check. CAN-0746 documents one NVRI-confirmed H5N1 poultry event at an Ebonyi live-bird market (VPD 172-A/22). CAN-1630 supports H5 RNA in a Kaduna layer flock, while its H9 evidence is antibody-only and H9 PCR is negative; its title's H9N2 co-infection and molecular claims are not established by the reported assays. Original full-text URLs and page/section evidence are in file 56.
- CAN-1627's original Ogun surveillance-system PDF was opened, but its 99,923 affected-bird total is not linked to an explicit positive laboratory-confirmed avian AIV result. Both reviewers and the arbiter left it `seek_further_info`; do not count it as included or excluded yet. CAN-0129, CAN-0189, CAN-0089, CAN-0006 and CAN-0017 still led only to abstracts, previews or failed original-article routes. Access attempts were logged; none was excluded as unretrievable.
- Next: continue original-source retrieval and independent full-text assessment for the 146 untouched candidates; resolve CAN-1627 laboratory source evidence and report/dataset overlap before a final study count. The original manuscript `.docx` was not edited.

## Current full-text checkpoint - 2026-09-26 (latest)
- The controlling register has 1,877 unique title/metadata identities: 1,581 excluded and 296 retained for full-text assessment. **140 reports now have independent two-reviewer adjudications** (71 provisionally eligible; 69 excluded). **156 reports have no full-text assessment.** No R1-first-pass report is awaiting R2. These are report counts, not a final included-study or PRISMA count.
- Today independent R2 and main-agent adjudication closed 132 new reports beyond the eight prior adjudications. The final 22-record R2 batch produced ten provisional retains and twelve exclusions, all from original full texts. CAN-0423 was independently verified through the versioned HAL accepted-manuscript PDF; it reports a 2006 Kaduna mixed-bird outbreak with laboratory investigation, but its authors could not establish the virus entry route. The accepted manuscript is a version of the original article, not another study.
- R1 original-source work covered CAN-1610, CAN-0423, CAN-0191, six AJOL publisher PDFs, 19 open-access records, and CAN-0146 from a University of Ilorin repository PDF. CAN-1679 was uncertain at R1 but retained after R2 verified the original spatial analysis; its source outbreak case definition remains for extraction QA. CAN-1662's reported serology denominators need checking. Serology indicates exposure and must not be treated as proof of active infection or pathotype.
- CAN-0113 was corrected from a prior provisional retain to exclusion because its questionnaire contains no sampled avian hosts or avian AIV assay; the earlier decision remains in adjudication history. CAN-1610 is eligible as a secondary genomic reanalysis with an extractable Nigerian pigeon sequence, not a new field detection. CAN-0056/CAN-1446 are confirmed as the same Monne et al. 2008 report; CAN-0056 was excluded as a duplicate report, but the 1,877 title-identity denominator has not yet been formally re-deduplicated. CAN-0008/CAN-0204, CAN-1291/CAN-1602, and CAN-1152/CAN-1179 remain possible report/version overlaps. Dataset overlap across distinct reports remains unresolved.
- CAN-1734 publication year was corrected to 2021 in the register and reconciliation file. The fixed exclusion reason `no laboratory-confirmed avian AIV` is an operational label under the existing frozen avian-laboratory criterion; no eligibility rule changed.
- Next: retrieve original full texts and perform independent R1/R2 assessment for the 156 untouched candidates; reconcile report identity and dataset overlap before any final study count; then extraction pilot, RoB, SWiM synthesis and reporting. Unretrievable exclusion requires the frozen two-attempt-plus-author-contact process. No author contact occurred. The original manuscript `.docx` was not edited. The session ended at this verified checkpoint; the next-session handoff gives the resume queue.

## Current full-text proceedings — 2026-09-26
- Register QA corrected 91 stale `retrieval.eligibility_status=not_assessed` labels where first-pass eligibility decisions already existed. This was status synchronisation only; no underlying vote changed.
- Original Europe PMC full text for CAN-1610 was verified: Methods and Table 1 include `A/pigeon/Nigeria/VRD370/2006` (H5N1). R1 first-pass retain was recorded because Nigerian sequence data are extractable. The 2025 global reanalysis must be linked to the original isolate source before study-level counting; subtype and cleavage motif do not establish a new Nigerian introduction.
- Current register arithmetic after that assessment: 1,877 title/metadata records; 296 full-text candidates; 108 with eligibility records (eight previously adjudicated, 100 awaiting independent second review); 188 without eligibility assessment. These are report counts, not final included-study counts.
- Identity QA found CAN-0056 and CAN-1446 are the same Monne et al. 2008 report (DOI 10.3201/eid1404.071178, PMID 18394282, PMC2570913). Other likely report/version overlaps under investigation are CAN-0008/CAN-0204, CAN-1291/CAN-1602, and CAN-1152/CAN-1179. Do not double count these as independent studies. The 1,877 denominator has not yet been re-deduplicated.
- Independent R2 full-text review is in progress; preliminary R2 messages must be integrated and adjudicated record by record before any final PRISMA or included-study tally.

## Current full-text proceedings — 2026-09-24
- The controlling screening register is `56_SCREENING_RECONCILIATION.json`. It contains 1,877 screened canonical records: 296 full-text candidates and 1,581 title/metadata exclusions. Earlier gate text below is historical.
- Full-text eligibility is documented for 107 reports: eight earlier two-reviewer adjudications (five provisional eligible, three excluded) and 99 first-pass assessments awaiting an independent second decision. Another 189 candidates remain without a full-text eligibility assessment. No final included-study count or PRISMA full-text exclusion distribution is yet supportable.
- Newly assessed CAN-0056: original Emerging Infectious Diseases article, pp. 637–640, The Study/Table 1, reports twelve Nigerian 2007 H5N1 poultry genomes (ten 2:6 reassortants). First-pass retain; accession overlap with the 2006–2008 genome group remains to be checked. Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC2570913/ .
- Newly assessed CAN-0039: original Journal of World's Poultry Research article, pp. 109–110, Methods, reports seventeen turkey-flock submissions in Nigeria confirmed by virus isolation/RT-PCR; its 299 NVRI outbreak coordinates may reuse national surveillance data. First-pass retain. Source: https://jwpr.science-line.com/attachments/article/34/J%20World%27s%20Poult%20Res%205%284%29%20109-114%2C%20December%2025%2C%202015.pdf .
- Newly assessed CAN-0025: Nigerian Veterinary Journal 37(3) original PDF is indexed, and the author-posted Results describe 2015 Kano poultry investigations, eight necropsies and 542 H5N1 farm-premises cases across twenty states. First-pass retain, with diagnostic-method and outbreak-line-list verification due at extraction. The journal PDF returned 403 in the available browser. Sources: https://www.ajol.info/index.php/nvj/article/download/147399/136905 and https://www.researchgate.net/publication/309722832_Epidemiology_and_Clinicopathological_Manifestation_of_Resurgent_Highly_Pathogenic_Avian_Influenza_H5N1_Virus_in_Nigeria_2015 .
- Newly assessed CAN-1724: original Sokoto Journal of Veterinary Sciences PDF, pp. 40–42, Methods and Results, analyses 32 affected and 32 unaffected Kano poultry farms. First-pass retain with laboratory case-definition verification and an internal consistency caution for several odds-ratio confidence intervals. Source: https://sokvetjournal.net/wp-content/uploads/2012/10/8.pdf .
- Newly assessed CAN-0007 and CAN-0008 through the African Union publisher's DSpace API original issue PDFs. CAN-0007 (Bulletin 61(2), pp. 121–124) is a Jigawa live-bird-market H5 serosurvey of 396 birds, with 48 positive; H5 antibodies do not establish active infection or HPAI pathotype. CAN-0008 (Bulletin 62(2), pp. 183–187) is Kaduna wild-bird surveillance with influenza A antibody positivity in 157 tested birds, while H5/H7 serology and AIV PCR antigen tests were negative. Both first-pass retain with these distinctions. Sources: https://repository.au-ibar.org/server/api/core/bitstreams/71d86e32-916d-4ee7-9686-85d1edacb196/content and https://repository.au-ibar.org/server/api/core/bitstreams/f452f064-4703-4882-b42d-407aa4281d0f/content .
- Newly assessed CAN-0339 and CAN-1678 by opening the recorded publisher PDFs directly. CAN-0339 (Epidemiology and Infection 138, pp. 192–195) maps 113 2006 H5N1-affected poultry farms against road proximity; first-pass retain, with national line-list overlap and causal-claim caution. CAN-1678 (Geospatial Health 3(1), pp. 9–11) combines November–December 2007 FAO field interviews with FAO/OIE outbreak maps; first-pass retain, with overlap caution. Its proposed 2005 introduction remains a hypothesis, not a confirmed detection. Sources: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/3EB2E35E4499AF2D5B16F017597BF952/S0950268809990495a.pdf/div-class-title-lessons-from-nigeria-the-role-of-roads-in-the-geo-temporal-progression-of-avian-influenza-h5n1-virus-div.pdf and https://geospatialhealth.net/index.php/gh/article/download/227/227 .
- CAN-0061's Métras conference presentation was linked as a possible earlier report of peer-reviewed CAN-0608; CAN-1724 may involve a separate Kano farm sample. The three are on an overlap watchlist, not declared duplicates. The presentation source and attempted retrieval are recorded in the register.
- Additional exact-title retrieval attempts are recorded for CAN-0007 (journal abstract and matching conference poster; full article unverified), CAN-0008 (African Union publisher issue confirms article; repository fetch failed), CAN-0017 (Europub listing returned 403), and CAN-0032 (conference abstract linked for comparison with Aiki-Raji et al. 2008 full article). These remain pending eligibility; no exclusion was inferred from access failure.
- MINOR operational clarification: the screening form now names `no avian-host field data`, a reason already implied by the frozen avian-host inclusion criterion. First-pass exclusion recommendations CAN-0098, CAN-0388, CAN-1534 and CAN-1567 use this reason; CAN-1720 uses the existing experimental-only/no-field-relevance reason. All five still await independent second review; eligibility criteria were not changed.
- Four previously recorded free routes remain unassessed because the original full text could not be verified through the available browser or document reader: CAN-0191 (publisher 403), CAN-0423 (publisher PDF unavailable), CAN-0485 (publisher/CiteSeerX PDF unavailable), and CAN-1610 (MDPI 429 and Europe PMC blocked). Their prior retrieval attempts remain in the register; a listed free route alone is not proof that a report was assessed.
- Retrieval statuses across the 296 candidates: 107 recorded free routes, 24 metadata/subscription only, 122 identifier unresolved and 35 identifier missing, plus the eight earlier adjudicated cases. These access categories do not determine eligibility.
- The frozen protocol requires independent second screening and report/dataset reconciliation before extraction. The current main-agent first pass is identified as such; it has not been relabelled as an independent reviewer vote. T1–T5 extraction shells remain unfilled because full-text eligibility and study overlap are unresolved.
- No manuscript text or final PRISMA numbers changed in this session. The original manuscript remains frozen; the working submission-ready file remains provisional.

**Re-audited:** 2026-09-24. Historical entries are retained for auditability; the 24 September
full-text proceedings above are the current screening status. The original manuscript remains frozen.

## Controlling status — 2026-09-20

- AJOL on-site search completed and corrected: nine exact queries, 144 raw query rows, 79 unique
  article URLs, 73 dated within 2006–2026, 0 missing titles, 0 missing dates, and 29 missing DOIs.
  All rows are in file 55 and linked to file 53; they remain unscreened retrieval candidates.
- Web of Science Core Collection browser search completed for counts: 206 base, 77 molecular,
  154 epidemiology/spatial/temporal, and 70 wild-bird/host. The exact publication-date window was
  2006-01-01 to 2026-09-20. The suggested substitution of H7N9 for H7N4 was rejected.
- Web of Science Free View did not provide a reliable complete record-level export. The older
  175-UID API dataset remains the only imported WoS layer; do not equate it with the broader
  206-result browser run.
- Gate B search execution is complete with export limitations. Gate C is open: obtain/export WoS
  records if legitimately available, then reconcile title/abstract screening.
- Preliminary PubMed and supplement screening remains valid as provisional evidence; final
  screening, full-text eligibility, extraction, and RoB are not complete.

## Gate 0 — Protocol re-frozen (date: 2026-09-19; passed for protocol truth)

- [x] Historical decision recorded: Phase 0 text (file 10 v1), Phase 1 strings (file 11 v1), and the unregistered path (file 17) were treated as approved on 2026-09-16. The reviewer design was recorded as R1 primary, R2 independent 20% verification plus all-excludes recheck, and R1 arbitration.
- [x] Amendment accepted: operational search-update date fixed at 20 September 2026; the 16 and
  19 September imported layers remain separately dated and the former 30 September endpoint is
  superseded.
- [x] Reviewer roles assigned: R1 = primary reviewer; R2 = independent Reviewer-2 Codex agent (Epicurus); Arbiter = main Codex agent. R2 decisions remain independent until adjudication.
- Gate 0 is closed for protocol truth. Gate 1/source audit is conditionally closed with limitations; Gate 2 identity reconciliation is complete but screening reconciliation remains open. No final eligibility decision is yet claimable.
- Screening cleared to start ONLY via files 18 + 19 forms/logs.

## PROSPERO

- SKIPPED per file 17 (2026-09-16). Use "not prospectively registered" sentence. File 12 retained for reference.

## Gate 1 — Searches and source audit (re-audited 2026-09-19)

| Source | Platform | Date run | String version | Filters | Hits | Export file |
|---|---|---|---|---|---|---|
| PubMed | NLM E-utilities | 2026-09-16 | v3 (v1 188 superseded) | EN 2006/01/01–2026/09/30 | 140 base; MOL 53 | 35_PUBMED_v3_base.txt / 35_PUBMED_v3_mol.txt |
| Scopus | Elsevier | 2026-09-16 (manual, file 45) | v1 file 19 verbatim | EN 2006–2026 | 204 | scopus_export_Sep 16-2026_5089c145-dbeb-4bdb-ac77-8e6913ca52bc.ris |
| WoS | Clarivate Web of Science Starter API | 2026-09-19 | v1 file 19; API base query | `db=WOS`; limit 50; pages 1–4; no English filter recorded; 2006–2026 publication-year query | 175 (50+50+50+25) | `.playwright-cli/response-1789793420726.json` through `response-1789794198378.json` |
| WoS browser update | Clarivate Web of Science Core Collection, Free View | 2026-09-20 | expanded base + three separate facets; exact strings in file 19 | Publication date 2006-01-01–2026-09-20; Editions All | 206 base; 77 molecular; 154 epidemiology; 70 wild-bird | no reliable full export; count-only audit |
| ScienceDirect | Elsevier | 2026-09-16 (manual, file 45) | v1-adapted single-line | 2006–2026 | 25 displayed/exported | ScienceDirect_citations_1789537860130.ris |
| Scholar | Google via SerpApi | 2026-09-17 update supplement | Q1–Q4; relevance; cap 200/query | 2006–2026; patents/citations excluded | 140 retrieved; 99 cross-query unique | supplementary run; no persistent export; excluded from primary PRISMA snapshot; superseded by the 2026-09-28 re-run |
| Scholar re-run | Google via SerpApi | 2026-09-28 dated update search (post-freeze) | Q1–Q4 verbatim; relevance; 20/page; cap 200/query | `as_ylo=2006`, `as_yhi=2026`, `as_sdt=0` (no patents), `as_vis=1` (no citations), `hl=en` | 800 rows (4 × 200); 519 unique; 291 matched register; 228 new | `D:\AvianInfluenzaSysRev_retrieval_20260927\scholar_rerun\raw_q1q4_20260928.json` (outside repo); PRISMA "other methods" |
| AJOL | AJOL on-site | 2026-09-20 | nine exact mandatory-term queries; file 19 | No site date filter; year QA applied after metadata capture | 144 query rows; 79 unique URLs; 73 dated 2006–2026 | `55_AJOL_CANDIDATES.json`; integrated into file 53 |
| OpenAlex (supplement) | api.openalex.org | 2026-09-16 | search avian influenza Nigeria | EN 2006/01/01–2026/09/30 | 6,455 total, 1,000 exported | 41_OPENALEX_raw.json |
| Crossref (supplement) | api.crossref.org | 2026-09-16 | query avian influenza Nigeria | 2006–2026 journal-article | 299,088 total, 1,000 exported | 42_CROSSREF_raw.json |

Deduped: supplement raw 2,000 → 1,876 → canonical 1,744 (file 46); PubMed ∩ supplement 117; unique for title screening 1,767 (140 + 1,627). WoS update added 175 raw records on 2026-09-19; symmetric cross-source QA is complete provisionally, while the final canonical-register rerun remains pending.
PubMed title-screen complete: 142 screened (140 v3 + 2 v1-only). See file 33 for R1–R5. Supplement raw-screen 1,752 done (64→86 main after KAP/abstract fixes); remap to canonical 1,627 pending.

### Gate B closure decision — 2026-09-19 (historical; superseded above)

- **Gate B passed with documented limitations.** Every planned source is now assigned an auditable status: PubMed, Scopus, ScienceDirect, OpenAlex/Crossref and the WoS base query are completed; Google Scholar is a dated supplementary run; AJOL is blocked/not run and has no claimed hit count.
- Exact strings, dates, caps, filters and available exports are recorded in this file and `19_SEARCH_run_sheets.md`; the six AJOL strings are preserved in files 11/45 and are explicitly marked unexecuted.
- Cutoff wording is source-specific: PubMed, OpenAlex/Crossref, Scopus and ScienceDirect were last run on 2026-09-16 (their date filters extend to 2026-09-30); only the WoS update was run on 2026-09-19. The review must not imply that every source was rerun on 2026-09-19.
- The primary operational snapshot therefore covers only the completed sources and the 2026-09-19 WoS base update. It does not claim a completed AJOL search, a complete Google Scholar export, or WoS facet coverage.
- Gate B does not authorise PRISMA counting of the WoS, Scholar or AJOL layers until the Gate C reconciliation and source-status caveats are carried into the final flow record.
- Reviewer 2 advised retaining Gate B as open because Scholar lacks a persistent export and AJOL was not run. The arbiter closes the **source-audit** subgate conditionally because the workflow explicitly permits `supplementary`, `blocked` and `not run` source statuses; the review must not describe this as complete database coverage.

### Current WoS import status

- The API retrieval is genuine and complete for the executed base query: 175 records, 175 unique Web of Science UIDs, HTTP 200 on all four pages.
- The four JSON files are raw source exports only. They have not yet been merged into the canonical identity register or screened.
- The WoS result set contains substantial candidate noise (meeting records, abstracts, reviews, news and non-Nigeria records); 19 records lack both DOI and PMID and require title–year identity checks.
- No separate molecular, epidemiological/spatial/temporal, or wild-bird WoS facet query has been run.
- The query used `PY=(2006-2026)` and was executed on 2026-09-19. It represents evidence available through the operational cutoff, not evidence after 2026-09-19.

### WoS facet retrieval attempt — 2026-09-19

- The external key file supplied by the user was read without being displayed or copied into the workspace.
- A broad exploratory molecular query (without the required AIV block) returned 1,995 records across 40 pages and was retained as exploratory only; it is not a PRISMA search result.
- Broad exploratory epidemiology/spatial/temporal and wild-bird requests returned metadata totals of 17,254 and 427 respectively, but were not fully exported and are not counted.
- Corrected protocol queries using `AIV block AND Nigeria block AND facet block` returned HTTP 429 rate-limit responses for all three facets. No corrected facet total is claimed. The existing 175-record base export remains the only valid WoS search layer until the quota permits corrected facet retrieval.

### Phase 2 — provisional WoS-new candidate queue

- Symmetric cross-source identity matching identified 24 WoS records provisionally new relative to the repaired PubMed v3, canonical supplement, Scopus, and ScienceDirect layers.
- The records are preserved in `52_WOS_PROVISIONAL_NEW.json` with WoS UID, title, year, identifiers, type, and source date.
- Reviewer 2 independently screened this corrected queue at title/metadata stage: 2 `include_main`, 6 `background_only`, 14 `exclude`, and 2 `unclear`. These are provisional decisions only; no record is a final inclusion or exclusion.
- Twelve of the 24 records lack both DOI and PMID and require title–year/manual reconciliation. WoS correction record `WOS:000255508300044` must be linked to its parent article rather than treated as an independent evidence record.

### Cross-source identity QA — provisional, not PRISMA counts

- Inputs checked: 140 PubMed v3 records (including the repair file `51_PUBMED_v3_metadata_repair.json`), 1,744 supplement records, 204 Scopus records, 25 ScienceDirect records, and 175 WoS records: 2,288 rows.
- Symmetric DOI/PMID/normalised-title + year matching produced 1,845 provisional identity groups and collapsed 443 duplicate rows across these inputs.
- 201 groups contained more than one source. Of the 175 WoS rows, 151 matched a pre-existing source group and 24 were provisionally new; four apparent WoS-new records were removed after the symmetric cross-source match.
- 31 identity groups showed title/year discrepancies requiring manual review; missing DOI and PMID occurred in 52 supplement, 33 Scopus, and 19 WoS rows.
- The 14 PubMed v3 IDs previously missing from the retained 188-record metadata file were repaired from NCBI ESummary and preserved separately; the original raw file remains unchanged.
- These figures are QA diagnostics only. They do not replace the final canonical register, screening decisions, or PRISMA flow counts.

### Gate re-audit — 2026-09-17

- **Gate A not passed:** the operational search snapshot is 2026-09-16 while the frozen protocol endpoint is 2026-09-30; reviewer/arbiter roles remain TBD.
- **Gate B not passed:** WoS was not run (Clarivate Free View/Documents disabled); direct Google Scholar returned HTTP 429; AJOL returned HTTP 403. A dated SerpApi Scholar supplement was completed (140 retrieved; 99 cross-query unique), but executed-string/filter reconciliation and canonical merge are incomplete.
- **Gate C not passed:** the reported 160 queue is provisional and cannot be used for PRISMA or retrieval. A read-only cross-match found 115 supplement records matching PubMed candidates by DOI/title-year and 118 manual records matching PubMed candidates, despite contradictory stored overlap flags. The SerpApi run adds 99 canonical Scholar groups: 49 match the current library and 50 remain unmatched candidates pending title/abstract verification. No eligibility decisions were changed.
- PMID `27677611` remains an audit-trail error and must be classified as non-Nigeria, not deleted.
- Safe next operation: complete canonical DOI/PMID/title-year reconciliation and remap votes before full-text retrieval or further screening.

### Gate re-audit — 2026-09-19

- **Gate A passed with amendment:** the operational cutoff is 19 September 2026, R2 is assigned to an independent Codex agent, and the main agent is the arbiter.
- **Gate B conditionally closed for source audit:** WoS base retrieval is complete (175), AJOL remains explicitly blocked/not run, and Scholar remains supplementary without a persistent export; these limitations are now recorded in the source table.
- **Gate C identity subgate repaired but screening reconciliation remains open:** the 1,845-record canonical register exists, while the 160-record queue remains provisional and must be replaced by record-level adjudication. Full-text assessment remains 0.
- **Gate D onward not started:** extraction, RoB, certainty and synthesis remain 0/not started.
- **Security hold:** 11 Playwright snapshot files contain the API key in rendered Swagger/Curl content. Do not share those snapshots. Key rotation and local-artifact cleanup require a separate approved security action.
- **Current safe state:** no manuscript edit, full-text eligibility decision, extraction decision or RoB decision was made during this re-audit.

### Reviewer-2 calibration pilot — 2026-09-19

- Independent agent: Epicurus (Reviewer 2); read-only, no credential access, no file edits.
- Pilot: first five WoS records from the 2026-09-19 API export.
- Provisional decisions: 1 `include_main`, 1 `background_only`, 2 `exclude`, 1 `unclear`.
- Calibration status: suitable for provisional title/metadata calibration, not final screening because the Starter export lacks abstracts and substantive full-record fields.

### Reviewer-2 repair verification — 2026-09-19 (historical pre-AJOL snapshot)

- Epicurus independently verified the 14-record PubMed repair: 14 unique PMIDs, NCBI ESummary provenance, raw-export preservation, and the revised QA arithmetic.
- Verified arithmetic: 140 + 1,744 + 204 + 25 + 175 = 2,288 input rows; 2,288 − 443 collapsed duplicate rows = 1,845 provisional identity groups; 151 pre-existing WoS matches + 24 provisional WoS-only groups = 175 WoS rows.
- Corrected Reviewer-2 queue result: 2 `include_main`, 6 `background_only`, 14 `exclude`, and 2 `unclear` among the 24 provisional WoS-new records. These decisions remain provisional pending canonical reconciliation and full-text assessment.
- Remaining high-impact issue: Google Scholar is not a persistent primary export, AJOL is blocked/not run, and the 160-record full-text queue must be rebuilt from the canonical register before PRISMA accounting.

## Gate 2 — Screening and canonical reconciliation (Gate C remains open)

Title/abs: PubMed 142 (main 73, supp 4, excl 64, check 1). Supplement canonical novel 1,609 screened in 4 slices (A 407: 55/4/22/326; B 389: 8/9/9/363; C 407: 11/2/17/377; D 406: 3/0/5/398) = main 77, supp 15, unsure 53, excl 1,464. Combined 1,751: main 150, supp 19, checks 54, excl 1,528. 18/1,627 novel pending reconciliation (overlap interspersion). Manual imports 2026-09-16: Scopus 204 (66 novel: 10 main/2 supp/11 unsure/43 excl) + ScienceDirect 25 (10 novel: 0/0/2/8) = file 47; combined manual novel 76: 10 main, 2 supp, 13 unsure, 51 excl.
Library LOCKED 2026-09-16 (amendment above): identification = PubMed 140 + supplement canonical 1,744 + Scopus 204 + ScienceDirect 25. Title mains locked: PubMed 73 (file 48 retrieval list) + supplement canonical 77 + manual 10 = 160 (upper bound, duplicate-group secondaries flagged at full-text). Full-text: T6 table next, assessed 0.
Next: remap/adjudicate the remaining canonical screening records → rebuild and freeze the corrected full-text queue → full-text T6 → extraction pilot T1–T5.

### Gate C repair status — updated 2026-09-20

- Identity reconciliation is reproducible: 2,367 input rows yielded 1,877 provisional identity
  groups and 490 collapsed duplicate rows using symmetric compact DOI/PMID/normalised-title plus
  year matching; source lineage is retained.
- AJOL contributed 79 source rows: 47 matched existing identities (34 DOI, 13 exact title-year)
  and 32 formed new identities. Of the new identities, 26 are in-window and need adjudication;
  six carry a deterministic outside-2006–2026 flag. No prior disposition changed.
- The persistent register is `53_CANONICAL_REGISTER.json`; AJOL source records and all nine-query
  memberships are in `55_AJOL_CANDIDATES.json`. Every `final_status` remains non-final.
- Four apparent WoS-new records were removed by the symmetric match. The remaining 24-record queue is preserved in `52_WOS_PROVISIONAL_NEW.json`; Reviewer 2 returned 2 `include_main`, 6 `background_only`, 14 `exclude` and 2 `unclear` at title/metadata stage.
- Known identity corrections are recorded: PubMed `27677611` is Iran, not Nigeria; WoS correction `WOS:000255508300044` is linked to its parent article; 12 WoS queue records lack DOI and PMID and require manual title–year review.
- Preliminary vote handling is now explicit: PubMed PMID-level decisions are retained; the six WoS background decisions and two WoS main decisions are record-linked; and pre-collapse supplement/manual aggregates are marked `precollapse_vote_discarded` with a reason rather than being silently inherited.
- **Gate C remains open for screening reconciliation:** 1,799 records are tagged as needing
  adjudication/screening (`needs_adjudication`, `main_candidate_needs_adjudication`, or
  `unclear_needs_adjudication`); all 1,877 records remain non-final. The 160-record upper-bound
  queue has not been replaced, and no final PRISMA screening count is claimed.

## Gate 3 — Extraction + RoB

Pilot studies: ____. T1–T5 rows: ____. T7 RoB done: ____. Certainty paras done: ____.

## Amendments (date + what + why + minor/major)

- 2026-09-16 MAJOR: Drop WoS / Google Scholar / AJOL as run sources for this version (no institutional export obtained; Scholar 429 + AJOL/ScienceDirect 403 to automation; user ran Scopus + ScienceDirect only). Library locked to PubMed v3 140 + OpenAlex/Crossref canonical 1,744 + Scopus 204 + ScienceDirect 25. WoS/Scholar/AJOL move to pre-submission update search (file 45 retained). PRISMA flow + methods must state this limitation vs Akanbi & Lakes 2026-09-16 (PubMed+Scopus).
- 2026-09-17 MINOR: Authenticated CLI session reached Clarivate Web of Science Free View, but the Documents tab remained disabled and the account exposed only Researcher Search. No WoS query, hit count, or export was obtained; no change to the locked search library.
- 2026-09-17 MINOR: Google Scholar supplemental search completed through SerpApi using Q1–Q4, relevance sorting, 2006–2026 year limits, patent/citation exclusion, and pagination up to the 200-record/query cap. 140 records were retrieved and 99 were unique across queries. Results remain unmerged pending canonical DOI/PMID/title-year reconciliation; no eligibility decisions changed.
- 2026-09-17 MINOR: SerpApi reconciliation rerun with normalized title–year grouping to prevent result-ID inflation. The 140 Scholar rows collapsed to 99 canonical groups; 49 matched the locked library and 50 remained unmatched. Unmatched records are not yet eligible studies and remain outside the locked library pending screening.
- 2026-09-17 MINOR: Mechanical identity audit across PubMed (188), canonical supplement (1,744), and manual imports (229) found 2,161 input rows, 1,869 canonical components, and 174 cross-source components using DOI → PMID → normalized title–year matching; no identifier conflicts were found under that rule. Independent PubMed matching found 124 supplement rows (113 DOI, 11 PMID; 117 stored true flags) and 127 manual rows (115 DOI, 12 title–year; 0 stored true flags). Stored overlap fields must not be used for PRISMA counts until remapped.
- 2026-09-17 MINOR: Operational decision recorded: the 2026-09-16 search set is the current snapshot; the 2026-09-17 SerpApi Google Scholar run is a separately dated update supplement and must not be backdated into the snapshot. Solo-review safeguards are R1 primary screening, R2 independent 20% verification plus all-excludes recheck, and R1 arbitration.
- 2026-09-17 MINOR: Web of Science Starter API Free Trial subscription requested for the registered application `avian-influenza-nigeria-sysrev`; Clarivate status is “Subscription approval is pending”. No API key, query, hit count or export is available; WoS remains unsearched for this supplement.
- 2026-09-19 MINOR (superseded later the same day): Clarivate Developer Portal account `Jerry Bannister` registered confidential server-side application `avian-influenza-nigeria-sysrev-jb2026` for this review. At that point the subscription was still shown as pending and no API result was available.
- 2026-09-19 MAJOR: Web of Science Starter API access was confirmed for application `avian-influenza-nigeria-sysrev-jb2026`. The frozen base query returned 175 records across four pages (50/50/50/25), all HTTP 200, and the raw JSON exports were retained under `.playwright-cli`. This is a source update, not a final eligible-study count; canonical DOI/PMID/title-year reconciliation and screening are pending.
- 2026-09-19 MAJOR: The operational search snapshot now has two dated layers: the locked 2026-09-16 library and the WoS API update on 2026-09-19. The protocol endpoint, source table, and manuscript wording must be amended before the update can enter PRISMA counts.
- 2026-09-19 MAJOR: User fixed the operational cutoff at 2026-09-19. Reviewer 2 is now an independent Codex agent (Epicurus); the main Codex agent is arbiter. The five-record agent calibration is provisional and does not replace full-text screening.
- 2026-09-20 MAJOR: AJOL on-site searching completed with nine exact queries (144 query rows;
  79 unique article URLs; corrected metadata show 73 dated 2006–2026 and six outside-window).
  Twelve initially missed pages were recovered after QA found repeated navigation captures. The
  79 rows now map to 47 existing plus 32 new canonical identities. Web of Science browser searching
  completed with 206 base, 77 molecular, 154 epidemiology, and 70 wild-bird/host results for
  2006-01-01 to 2026-09-20. AJOL source metadata is now persistent in file 55; WoS Free View did
  not provide a complete export. Gate C therefore remains open for screening reconciliation.
- …​
- 2026-09-27 MAJOR: Unretrievable-report rule changed by user decision for deadline reasons. The frozen rule (two documented retrieval attempts plus author contact) is replaced by: (a) automated identifier resolution and legitimate open-access search (Crossref, OpenAlex, Europe PMC, PubMed, Semantic Scholar, Unpaywall, repositories); (b) one time-boxed institutional-access attempt through the reviewer's ATBU affiliation; (c) no author contact and no waiting period. Reports still without verified full text after (a) and (b) are recorded as "reports not retrieved" in the PRISMA 2020 flow diagram and not assessed for eligibility. They are not labelled as exclusions on content. The Methods and Limitations sections must state this deviation.
- 2026-09-27 MINOR: Independent full-text reviewers changed. R1 is now an executor agent (Claude Opus 5.5) and R2 is a separate reviewer agent (Claude Sonnet 5) that does not see R1's vote; the main session adjudicates. This replaces the Codex agent (Epicurus) as R2 for the remaining 126 candidates. The 170 existing adjudications are unchanged.
- 2026-09-28 MAJOR (modifies the 2026-09-27 rule): step (b), the ATBU institutional-access attempt, was dropped because institutional access was not available to the review team. The legal open-access sweep was extended instead: OpenAlex (all locations), Europe PMC, Semantic Scholar and Crossref title searches; Google Scholar via SerpApi, including the "All versions" cluster; long-timeout repository retries; and a browser pass (Chrome DevTools) for author-posted or repository copies. ResearchGate (DataDome bot check), AgEcon Search (human verification) and Academia.edu (login needed for the full PDF) were blocked; no CAPTCHA was bypassed, no login was used and no shadow library was used. Outcome: 14 further full texts were obtained and 80 reports were recorded as "reports not retrieved". The Methods and Limitations sections must state that institutional access was unavailable and that no authors were contacted.
- 2026-09-29 MINOR: R2 model changed from Claude Sonnet 5 to Claude Sonnet 5.5 (released 2026-09-28, same price tier) for all R2 votes from the full-text screen of the 36 Scholar re-run retains onward. R2 is still the separate `reviewer` agent, blind to R1; R1 remains the `executor` agent (Claude Opus 5.5); the main session still adjudicates. All earlier R2 votes (including the 228-record Scholar title screen on 2026-09-29) were cast by Sonnet 5 and are unchanged. Why: the newer model is faster and stronger on agentic tasks at the same cost. Each R2 vote's `method` field records the model used.
- 2026-09-28 MAJOR: Post-freeze update search. The 2026-09-17 Google Scholar supplement had no persistent export, so its 50 unmatched records could never be screened. It is replaced by a dated re-run of the same Q1–Q4 queries (28 Sept; parameters in the source table above), whose full raw output is saved. The 228 records not already in the register will be added as new canonical identities (CAN-1878 onward), screened by blind R1/R2 title/snippet votes on the file 18 form with main-session adjudication, and taken to full text where retained. They are reported under PRISMA 2020 "identification of studies via other methods", dated after the protocol freeze. Why: an unscreened set of search results is a PRISMA item 16 gap, and the re-run showed eligible Nigerian reports missing from the register. The 17 Sept record set itself is irrecoverable and must be described as such.
