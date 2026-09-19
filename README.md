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

## Current evidence state — 19 September 2026

`Workbench/53_CANONICAL_REGISTER.json` is the canonical identity register:

- 2,288 input rows;
- 1,845 canonical records;
- 443 collapsed duplicate rows;
- source counts: PubMed 140, OpenAlex/Crossref 1,744, Scopus 204,
  ScienceDirect 25, and Web of Science 175;
- all records remain provisional for screening; no final inclusion count is claimed.

Gate B is conditionally closed for the source audit, with explicit limitations recorded in
`Workbench/15_RUN_LOG.md` and `Workbench/19_SEARCH_run_sheets.md`. Gate C has a complete
identity register, but title/abstract screening and reconciliation remain open.

The valid Web of Science base retrieval is preserved as 175 records. Later facet experiments
are labelled exploratory or rate-limited; they must not be treated as protocol-valid facet
totals until rerun and logged. The next WoS retry should begin with one request after the
documented quota-reset time, then proceed at no more than one request per second.

## Repository map

| Path | Purpose | Version-control status |
|---|---|---|
| `AGENTS.md` | Project rules, scope lock, methods, and safety constraints | tracked |
| `Avian_review_paper_fellow.docx` | Single manuscript source of truth | tracked |
| `ScienceDirect_*.ris` | ScienceDirect citation export | tracked |
| `scopus_export_*.ris` | Scopus citation export | tracked |
| `Workbench/00_INDEX.md`–`53_*.json` | Protocol, methods, audit trail, search outputs, and canonical register | tracked |
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

1. Read `AGENTS.md` and `Workbench/49_NEXT_SESSION_HANDOFF.md`.
2. Treat `Workbench/53_CANONICAL_REGISTER.json` as the current identity source.
3. Complete/reconcile screening before extraction.
4. Rerun only the documented WoS facet queries after the rate-limit reset; save response files
   without credentials and update the run log.
5. Keep decisions provisional until the screening, duplicate reconciliation, and adjudication
   gates are complete.

No GitHub remote has been configured or pushed. This is a local repository only.

