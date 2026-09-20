# Nigeria Avian Influenza Systematic Review

Local evidence-synthesis workspace for the review of avian influenza emergence,
temporal and geographic distribution, host range, molecular/clade patterns, and
reassortment dynamics in Nigeria, 2006–2026.

## Authority and scope

- **Manuscript source of truth:** `Avian_review_paper_fellow.docx`.
- **Governing instructions:** `AGENTS.md`.
- **Review standard:** PRISMA 2020, PRISMA-S, and SWiM where meta-analysis is not justified.
- **Question framework:** CoCoPop/PEO, not PICO.
- **Eligibility anchor:** Nigeria-specific HPAI/LPAI evidence with epidemiological,
  molecular/phylogenetic, or spatial/temporal data.
- **Current work scope:** protocol/search audit, screening, extraction, risk of bias,
  and synthesis support. The manuscript remains unchanged in this repository state.

## Current evidence state — 20 September 2026

`Workbench/53_CANONICAL_REGISTER.json` is the canonical identity register:

- 2,367 input rows;
- 1,877 canonical records;
- 490 collapsed duplicate rows;
- source counts: PubMed 140, OpenAlex/Crossref 1,744, Scopus 204,
  ScienceDirect 25, Web of Science 175, and AJOL 79;
- all records remain provisional for screening; no final inclusion count is claimed.

This register represents the imported/canonicalised evidence layer through the 20 September
AJOL update. It still does **not** contain a record-level export of the broader 20 September Web
of Science browser search.

Gate B search execution is complete with documented export limitations. Gate C remains open:
the identity register is complete for all available record-level imports, but title/abstract
screening reconciliation and final candidate adjudication remain open.

Gate C is now operationally initialized in `Workbench/56_SCREENING_RECONCILIATION.json`. It contains
the 1,877 canonical screening identities, six deterministic outside-window date flags kept separate
from substantive eligibility decisions, and a 40-record stratified R1/R2 pilot. No final inclusion or
exclusion decisions have been made.

The historical Web of Science API retrieval remains 175 imported UIDs. A broader authenticated
Web of Science Core Collection browser run on 20 September returned 206 base results and valid
facet counts of 77 molecular, 154 epidemiology/spatial/temporal, and 70 wild-bird/host records.
The account was limited to Free View, so no complete record-level export was obtained; the
206/77/154/70 values are search-run counts, not imported records or PRISMA-ready denominators.

AJOL was searched on-site on 20 September with nine exact free-text queries. Their raw query
counts sum to 144; URL-level reconciliation yielded 79 unique article pages, of which 73 had
publication years in 2006–2026. Metadata completeness was 79/79 for title and date and 50/79 for
DOI. The 79 rows are now preserved in `Workbench/55_AJOL_CANDIDATES.json` and linked into the
canonical register: 47 matched existing identities and 32 formed new identities. They remain
unscreened retrieval candidates.

## Repository map

| Path | Purpose | Version-control status |
|---|---|---|
| `AGENTS.md` | Project rules, scope lock, methods, and safety constraints | tracked |
| `Avian_review_paper_fellow.docx` | Single manuscript source of truth | tracked |
| `ScienceDirect_*.ris` | ScienceDirect citation export | tracked |
| `scopus_export_*.ris` | Scopus citation export | tracked |
| `Workbench/00_INDEX.md`–`55_AJOL_CANDIDATES.json` | Protocol, methods, audit trail, search outputs, and canonical register | tracked |
| `Workbench/run_pubmed_*.py` | Existing PubMed retrieval helpers | tracked; historical helper files, not an application |
| `Workbench/wos_facet_*.json` | WoS facet retrieval artifacts; interpret only with the run log | tracked |
| `output/pdf/` | Existing rendered status PDF | tracked |
| `tmp/` | Existing local audit/PDF helper files and rendered pages | tracked except local virtual environment |
| `.playwright-cli/` | Browser snapshots and API-session material | ignored intentionally |
| `.playwright-mcp/` | Browser/session state | ignored intentionally |
| `woskey.txt` | Local API credential | ignored intentionally; never commit or paste |

For the exact tracked-file list, run `git ls-files`. For ignored paths, run
`git status --short --ignored`.

## Reproducibility and credential policy

Credentials are external to the repository. The local WoS key file is deliberately ignored,
and browser snapshots are deliberately excluded because they may contain API credentials,
cookies, or private session state. The key previously used in this workspace should be rotated
if it was exposed in chat, screenshots, logs, or snapshots.

Do not place credentials in `Workbench/`, the manuscript, README files, Git history, or command
output. Retrieval attempts, query strings, response totals, errors, and limitations belong in
`Workbench/15_RUN_LOG.md` and `Workbench/19_SEARCH_run_sheets.md` without secrets.

## Resume order

1. Read `AGENTS.md` and `Workbench/54_NEXT_SESSION_HANDOFF_20260919.md` (updated through
   20 September despite its historical filename).
2. Treat `Workbench/53_CANONICAL_REGISTER.json` as the current identity source.
3. Obtain a legitimate WoS record export if account access permits; otherwise retain the
   documented count-only limitation.
4. Complete/reconcile title/abstract screening against the 1,877-identity register before extraction.
5. Keep decisions provisional until screening, duplicate reconciliation, and adjudication
   gates are complete.

No GitHub remote has been configured or pushed. This is a local repository only.
