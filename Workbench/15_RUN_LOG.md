# Run log + gate checklists (update as you go)

**Re-audited:** 2026-09-20. Historical entries are retained for auditability; the latest dated
re-audit below is the current operational status. The manuscript remains frozen.

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
| Scholar | Google via SerpApi | 2026-09-17 update supplement | Q1–Q4; relevance; cap 200/query | 2006–2026; patents/citations excluded | 140 retrieved; 99 cross-query unique | supplementary run; no persistent export; excluded from primary PRISMA snapshot |
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
