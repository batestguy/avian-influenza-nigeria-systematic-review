# Run log + gate checklists (update as you go)
## Expert audit and Scholar update search - 2026-09-28 (latest; session paused)
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
- 2026-09-28 MAJOR: Post-freeze update search. The 2026-09-17 Google Scholar supplement had no persistent export, so its 50 unmatched records could never be screened. It is replaced by a dated re-run of the same Q1–Q4 queries (28 Sept; parameters in the source table above), whose full raw output is saved. The 228 records not already in the register will be added as new canonical identities (CAN-1878 onward), screened by blind R1/R2 title/snippet votes on the file 18 form with main-session adjudication, and taken to full text where retained. They are reported under PRISMA 2020 "identification of studies via other methods", dated after the protocol freeze. Why: an unscreened set of search results is a PRISMA item 16 gap, and the re-run showed eligible Nigerian reports missing from the register. The 17 Sept record set itself is irrecoverable and must be described as such.
