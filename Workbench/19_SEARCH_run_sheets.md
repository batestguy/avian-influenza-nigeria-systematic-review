# Search run sheets — execute one row at a time, log as you go

Freeze version: v1 (2026-09-16). Do not edit strings mid-run; amendments get new version + date.

## PubMed via NLM — run first

Paste block from `11_Phase1_search_rebuild_DRAFT.md` lines 1–7. Record per-line hits.
Date run: ____ | Filters: English, 2006/01/01–2026/09/30 | Total base (#4): ____ | Export file: ____

## Scopus via Elsevier

String: TITLE-ABS-KEY("avian influenza" OR AIV OR HPAI OR LPAI OR H5N1 OR H5N2 OR H5N6 OR H5N8 OR H9N2) AND TITLE-ABS-KEY(Nigeria OR Nigerian) AND PUBYEAR > 2005 AND PUBYEAR < 2027.
Date run: ____ | Hits: ____ | Export: ____

## Web of Science (API run recorded 2026-09-19; collection: `db=WOS`)

String: TS=("avian influenza" OR AIV OR HPAI OR LPAI OR H5N1 OR H9N2) AND TS=(Nigeria OR Nigerian) AND PY=(2006-2026).
Date run: 2026-09-19 | Hits: 175 total | Export: `.playwright-cli/response-1789793420726.json`, `.playwright-cli/response-1789794028954.json`, `.playwright-cli/response-1789794124393.json`, `.playwright-cli/response-1789794198378.json`
API pagination: limit 50; pages 1–4 = 50, 50, 50, 25; all HTTP 200; 175 unique UIDs. No English filter was recorded. This is the valid base query. A 2026-09-19 corrected facet rerun was attempted but returned HTTP 429 for molecular, epidemiological/spatial/temporal, and wild-bird facets; no facet totals are counted.

## ScienceDirect

Variant of Scopus string in title-abs-key; record filters + cap. Date: ____ | Hits: ____ | Export: ____

## Google Scholar (relevance-ranked, cap 200; supplementary only)

Queries: Q1 "avian influenza" Nigeria; Q2 H5N1 Nigeria; Q3 H9N2 Nigeria; Q4 poultry Nigeria wild birds. Date: 2026-09-17 | Years: 2006–2026 | Sort: relevance | Cap: 200/query | Retrieved: 140 | Cross-query unique: 99 | Persistent export: none | Status: supplementary, excluded from primary PRISMA snapshot.

## AJOL (free-text ×N; blocked/not run)

Queries recorded but not executed on-site: A1 avian influenza Nigeria; A2 H5N1 Nigeria; A3 H5N8 Nigeria; A4 H9N2 Nigeria; A5 HPAI Nigeria; A6 poultry Nigeria wild birds. Audit date: 2026-09-19 | Direct access: HTTP 403 | Hits: not claimed | Export: none. `site:ajol.info` results are discovery fallback only.

## Supplementaries

Backward/forward chasing per include; Kalonda + Akanbi lists checked. Added records: ____ with source each.
