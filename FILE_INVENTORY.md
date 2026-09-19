# File inventory

Inventory of the local systematic-review workspace at the initial Git commit,
19 September 2026. Files containing credentials or browser session state are intentionally
excluded from Git and are listed below for transparency.

## Tracked root files

| File | Role |
|---|---|
| `AGENTS.md` | Binding project instructions and review scope lock |
| `README.md` | Repository orientation, evidence state, and operating rules |
| `FILE_INVENTORY.md` | This inventory |
| `Avian_review_paper_fellow.docx` | Manuscript source of truth |
| `ScienceDirect_citations_1789537860130.ris` | ScienceDirect export |
| `scopus_export_Sep 16-2026_5089c145-dbeb-4bdb-ac77-8e6913ca52bc.ris` | Scopus export |

## `Workbench/`

### Methods, protocol, and forms

- `00_INDEX.md`
- `01_scoring_PRISMA2020.md`, `02_scoring_PRISMA_S.md`, `03_scoring_PRISMA_P.md`,
  `04_scoring_SWiM.md`, `05_scoring_JBI_RoB.md`, `06_scoring_GRADE_prognosis.md`,
  `07_scoring_molecular_check.md`, `08_formats_for_our_draft.md`
- `10_Phase0_protocol_freeze_DRAFT.md`, `11_Phase1_search_rebuild_DRAFT.md`,
  `12_PROSPERO_submission_READY.md`, `13_WORKFLOW_prospective.md`,
  `14_METHODS_paste_ready.md`, `16_PRE_PROSPERO_inputs_needed.md`,
  `17_SKIPPED_PROSPERO_note.md`
- `18_SCREENING_forms.md`, `20_EXTRACTION_T1_T5_shells.md`,
  `21_ROB_T6_T7_shells.md`, `22_FLOW_audit_shell.md`

### Operations and audit trail

- `15_RUN_LOG.md` — chronological retrieval and decision log
- `19_SEARCH_run_sheets.md` — database-by-database search documentation
- `23_AGENT_OPS.md`, `24_AGENT_BATCH_SEED1.md`, `25_AGENT_CALIBRATION_SEED1.md`
- `33_SEARCH_execution_log.md`, `36_PUBMED_improvement_log.md`
- `38_SCREEN_ROUND2.md`, `39_SCREEN_ROUND3.md`, `44_SUPPLEMENT_pull_log.md`
- `45_MANUAL_DB_CHECKLISTS.md`, `48_PUBMED_FULLTEXT_LIST.md`
- `49_NEXT_SESSION_HANDOFF.md`, `50_END_TO_END_WORKPLAN.md`

### Search inputs and candidate data

- `30_PUBMED_idlist.txt`
- `31_PUBMED_candidates.json`, `32_PUBMED_title_relevant.json`
- `34_PUBMED_v2_base.txt`, `34_PUBMED_v2_dropped.txt`, `34_PUBMED_v2_epi.txt`,
  `34_PUBMED_v2_gained.txt`, `34_PUBMED_v2_mol.txt`, `34_PUBMED_v2_wild.txt`
- `35_PUBMED_v3_base.txt`, `35_PUBMED_v3_mol.txt`, `37_MOL_titles.txt`
- `41_OPENALEX_raw.json`, `42_CROSSREF_raw.json`, `43_SUPPLEMENT_candidates.json`,
  `46_DEDUP_COLLAPSED.json`, `47_MANUAL_IMPORT_candidates.json`
- `51_PUBMED_v3_metadata_repair.json`
- `52_WOS_PROVISIONAL_NEW.json`
- `53_CANONICAL_REGISTER.json` — canonical identity register and provisional decisions

### Web of Science retrieval artifacts

- `wos_facet_molecular_20260919_page*.json` — exploratory molecular facet responses;
  the initial query omitted the AIV block and is not protocol-valid.
- `wos_facet_epi_spatial_temporal_20260919_page*.json` — exploratory/rate-limited
  epi-spatial-temporal responses; interpret only through the run log because retries produced
  incomplete or repeated page artifacts.
- `wos_facet_wild_bird_20260919_page1.json` — exploratory wild-bird facet response.

The validated base WoS retrieval and the failed corrected-facet retries are documented in
`15_RUN_LOG.md` and `19_SEARCH_run_sheets.md`. Do not infer corrected facet totals from the
exploratory files.

### Existing helper scripts

- `run_pubmed_v2.py`
- `run_pubmed_v3.py`

These are retained historical retrieval helpers. This project has no application, package
manager, test suite, build system, or CI pipeline.

## Other tracked folders

- `output/pdf/AvianInfluenzaSysRev.pdf` — existing rendered status document.
- `tmp/c_drive_audit.py`, `tmp/c_profile_childaudit.py`, `tmp/c_profile_subaudit.py` — existing
  local audit helpers.
- `tmp/pdfs/create_status_pdf.py`, `tmp/pdfs/render_pdf.py`, and `tmp/pdfs/rendered/page-*.png`
  — existing PDF-generation helpers and rendered pages.
- `tmp/pdfs/.venv/` is not tracked because it is a generated local Python environment.

## Intentionally ignored files

- `woskey.txt` — local WoS API credential; never commit.
- `.playwright-cli/` — browser snapshots and API/session material; may contain secrets.
- `.playwright-mcp/` — browser/session state.
- `tmp/pdfs/.venv/` — generated environment.
- Python caches, editor metadata, and environment files matched by `.gitignore`.

