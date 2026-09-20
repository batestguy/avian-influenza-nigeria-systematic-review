# Next-session handoff — Nigeria AIV systematic review

**Prepared:** 19 September 2026; **updated:** 20 September 2026
**Purpose:** resume import, canonical reconciliation, and screening without reopening settled methodological decisions.

**Master workplan:** `50_END_TO_END_WORKPLAN.md`. Use it for phase order, gates, deliverables and the conditional post-extraction pooling decision.

## 1. Repository and scope

- The only manuscript source of truth is `Avian_review_paper_fellow.docx`.
- The manuscript is frozen and must not be edited until a change is explicitly approved.
- Existing Workbench files are planning, search, and audit aids. Do not create new CSV, Markdown, figure, or log sidecars unless the user explicitly authorises them. Final tables and appendices belong inside the Word manuscript; screening guidance may remain in chat.
- Review question: emergence, temporal/geographic/host-range, molecular/clade, and reassortment dynamics of avian influenza viruses in Nigeria.
- Framework: CoCoPop/PEO, not PICO.
- Synthesis: SWiM narrative synthesis without meta-analysis.
- Registration: PROSPERO was skipped. Never use the obsolete prospective-registration wording in `14_METHODS_paste_ready.md`.

## 2. Current evidence state

Use `15_RUN_LOG.md` as the operational status reference. The status below distinguishes the locked
2026-09-16 library from the raw Web of Science update retrieved on 2026-09-19.

- **Cutoff:** the operational search-update date is now fixed at 20 September 2026. The 16 September library and 19 September WoS API retrieval remain historical imported layers. The former 30 September endpoint is superseded and must not appear as the completed cutoff.
- **PubMed:** v3 base search returned 140 records; 142 were screened after two v1-only checks; 73 main candidates, 4 supplementary/context candidates, 64 exclusions, and 1 full-text check.
- **OpenAlex/Crossref supplement:** 2,000 raw records became 1,876 merged records and 1,744 canonical records; 1,627 were novel against PubMed. The current aggregate reports 77 main candidates, 15 context candidates, 53 unclear, and 1,464 exclusions, but votes have not been remapped cleanly from the pre-collapse set.
- **Manual imports:** 204 Scopus plus 25 ScienceDirect records; 76 marked novel, with 10 main, 2 context, 13 unclear, and 51 excluded.
- **Upper-bound full-text queue:** 160 candidates (PubMed 73 + supplement 77 + manual 10). This is not a final included-study count.
- **Full-text assessment:** 0 completed.
- **Extraction/RoB:** no T1–T7 rows completed.
- **WoS:** the 175-record API layer from 19 September is canonicalised in file 53. On 20 September, a broader Core Collection browser search returned 206 base / 77 molecular / 154 epidemiology / 70 wild-bird results. Free View prevented a reliable complete record export, so these newer values are count-only and are not in file 53.
- **Google Scholar:** 140 retrieved/99 canonical groups in the dated supplement; not merged into the candidate register and no persistent export is present.
- **AJOL:** on-site run completed and corrected on 20 September: nine queries, 144 query rows,
  79 unique article URLs, 73 within 2006–2026, and six outside-window. File 55 preserves source
  lineage; file 53 contains all 79 links (47 existing identities plus 32 new). None is substantively screened.

## 3. Mandatory reconciliation before further screening

1. Use `53_CANONICAL_REGISTER.json` as the identity base for 2,367 imported source rows and 1,877
   identities. It remains incomplete only for the count-only WoS browser layer. Do not rely on raw
   pre-collapse votes. The 14 missing PubMed metadata records are repaired in
   `51_PUBMED_v3_metadata_repair.json`.
2. Independently verify the AJOL import in files 53 and 55, then remap and adjudicate screening decisions.
3. Independently screen and adjudicate the 24 corrected provisional WoS-new records in `52_WOS_PROVISIONAL_NEW.json`. Reviewer 2's record-linked title/metadata result is 2 `include_main`, 6 `background_only`, 14 `exclude`, and 2 `unclear`; do not promote these to final decisions.
4. Re-screen every candidate using the frozen all-criteria rule:
   - Nigeria-specific data;
   - avian AIV/HPAI/LPAI with laboratory confirmation and stated assay;
   - epidemiological, molecular/phylogenetic, spatial/temporal, or wild-bird evidence;
   - primary or extractable empirical data.
5. Correct the known error: PMID `27677611` is a study of backyard chickens in Iran and cannot be a Nigeria main inclusion (`48_PUBMED_FULLTEXT_LIST.md`).
6. Recheck KAP, worker, pig, policy, cost, and review papers. Unless they meet the strict avian laboratory-confirmation rule, classify them as background only or exclude them; they must not enter the main evidence synthesis.
7. Deduplicate the manual import queue. `47_MANUAL_IMPORT_candidates.json` contains repeated titles/DOIs, including a duplicated title with no DOI.
8. Maintain the operational role record: R1 primary reviewer, Epicurus as independent Reviewer 2, and the main Codex agent as arbiter.

Current identity-QA checkpoint: file 53 contains 1,877 canonical identities from 2,367 source rows
and 490 collapsed duplicates. AJOL added 79 source rows: 47 existing matches and 32 new identities.
The historical WoS layer still has 151 pre-existing matches and 24 provisional-new records.

## 4. CLI retrieval plan

CLI work is authorised retrieval preparation, not an eligibility decision.

### Retrieval order

For each of the 160 candidates:

1. Confirm metadata through DOI, PMID, PubMed, Europe PMC, Crossref, or OpenAlex.
2. Resolve legitimate full text through PubMed Central, Europe PMC, publisher open-access links, institutional library access, or an authorised repository copy.
3. If a DOI is absent, search by PMID and exact title/year; manually verify possible matches.
4. Record one retrieval status: `full_text_obtained`, `library_required`, `unretrievable_after_protocol`, `duplicate`, or `metadata_problem`.
5. For authorised PDFs, use `pdftotext -layout`; use OCR only for image-only PDFs and visually verify all critical numbers, clades, accessions, and tables.
6. Keep downloaded files and extracted text in a temporary location outside the repository unless persistent storage is later authorised. Do not store credentials, cookies, proxy tokens, or private URLs in the workspace.

CLI must not bypass paywalls, CAPTCHA, publisher restrictions, or institutional authentication. RIS files provide metadata only; they do not establish full-text eligibility.

## 5. Agentic workflow

Use the following routing when agent tools are available:

1. `sol_planner`: read-only methods/eligibility gate audit and final decision rules.
2. `luna_worker`: mechanical metadata normalisation, authorised full-text resolution, and page-labelled text preparation.
3. Two independent `terra_executor` passes on the same five-record batch. Each receives the same title/abstract/full-text evidence and returns a structured decision without seeing the other pass.
4. Main session: adjudicate all disagreements, verify all inclusions and exclusions, and check at least 20% of clear agreements.
5. `terra_reviewer`: fresh review of extraction, RoB, synthesis claims, and manuscript alignment.

If subagents are unavailable, run the two passes sequentially in the main session and record that deviation. Agents are pre-readers; their outputs never enter T1–T7 without main-session verification.

## 6. Required record schemas

### Retrieval record

`record_id`, `doi`, `pmid`, `title`, `year`, `source`, `canonical_match`, `retrieval_status`, `source_url`, `file_type`, `page_count`, `text_quality`, and `notes`.

### Screening record

`record_id`, `reviewer_id`, `stage`, `decision` (`include_main`, `background_only`, `exclude`, `unclear`), `reason_code`, `evidence_quote_or_page`, `full_text_required`, and `decision_date`.

### Extraction record

Every included study must populate T1–T5 fields: design, sampling frame, period, state/zone, host/system, sample and denominator, assay, subtype, clade/lineage, sequencing details, phylogeny/support, accession, reassortment or mutation claim, spatial/temporal finding, and reference. Use `Not reported`, `Unclear`, or `N/A`; never leave blanks.

### RoB record

Apply the relevant JBI Prevalence, Cross-Sectional, or Cohort tool plus molecular checks M1–M7. Record signalling answers and supporting quotes. Do not calculate score sums. Overall status is `Include`, `Exclude`, or `Seek further info`.

## 7. Gates and acceptance criteria

- **Gate A — protocol truth:** current cutoff, non-registration, actual searched sources, and dated amendments are internally consistent.
- **Gate B — search execution/source audit:** complete with explicit Scholar/AJOL/WoS export limitations; no complete exported-record coverage claim is permitted.
- **Gate C — canonicalisation and screening reconciliation:** identity register complete in `53_CANONICAL_REGISTER.json`; record-level screening adjudication and replacement of the 160-record upper-bound queue remain open.
- **Gate D — full text:** every candidate must have an eligibility outcome, one full-text exclusion reason where applicable, and duplicate-dataset links.
- **Gate D — pilot extraction:** five diverse studies are independently extracted and reconciled before full extraction.
- **Gate E — RoB:** every included study has JBI and molecular appraisal evidence.
- **Gate F — synthesis:** every temporal, geographic, host, and molecular claim links to extraction rows and is qualified by surveillance intensity, assay limitations, and certainty.
- **Gate G — manuscript:** only after Gates A–F, edit the `.docx`; add the Abstract, Results, Discussion, limitations, PRISMA flow, T1–T7 tables, exact searches, and correct registration statement.

## 8. Final validation checklist

Before handoff or manuscript editing, check that:

- no phrase claims prospective PROSPERO registration;
- no phrase converts WoS count-only results, Scholar supplementary results, or AJOL retrieval candidates into screened/included studies before screening and PRISMA reconciliation;
- no “31 September 2026” date remains;
- no malformed `And Nigeria` search block remains;
- title/abstract, full-text, and included-study counts sum at every PRISMA transition;
- all main inclusions meet laboratory-confirmed avian AIV eligibility;
- clade, subtype, lineage, reassortant, introduction, and local evolution are not conflated;
- every accession, method, and molecular claim is traceable;
- no placeholder (`____`, `[X]`, `[CRD]`) remains in the manuscript;
- Word formatting remains Times New Roman, British English, numeric citations, and the required Abstract heading style.

Before any `.docx` edit, load the repository-required `thesis-to-journal` skill. Do not use the arXiv search script from the systematic-literature-review skill for this PubMed/Scopus/Nigeria review.
