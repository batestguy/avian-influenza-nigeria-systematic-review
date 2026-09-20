# Search run sheets — execute one row at a time, log as you go

Freeze version: v1 (2026-09-16). Execution amendment v2 (2026-09-20) is recorded below without
rewriting the historical strings. Do not edit strings mid-run; amendments get a new date/version.

## PubMed via NLM — run first

Paste block from `11_Phase1_search_rebuild_DRAFT.md` lines 1–7. Record per-line hits.
Date run: ____ | Filters: English, 2006/01/01–2026/09/30 | Total base (#4): ____ | Export file: ____

## Scopus via Elsevier

String: TITLE-ABS-KEY("avian influenza" OR AIV OR HPAI OR LPAI OR H5N1 OR H5N2 OR H5N6 OR H5N8 OR H9N2) AND TITLE-ABS-KEY(Nigeria OR Nigerian) AND PUBYEAR > 2005 AND PUBYEAR < 2027.
Date run: ____ | Hits: ____ | Export: ____

## Web of Science

Historical imported API layer (2026-09-19; collection `db=WOS`):
String: TS=("avian influenza" OR AIV OR HPAI OR LPAI OR H5N1 OR H9N2) AND TS=(Nigeria OR Nigerian) AND PY=(2006-2026).
Date run: 2026-09-19 | Hits: 175 total | Export: `.playwright-cli/response-1789793420726.json`, `.playwright-cli/response-1789794028954.json`, `.playwright-cli/response-1789794124393.json`, `.playwright-cli/response-1789794198378.json`
API pagination: limit 50; pages 1–4 = 50, 50, 50, 25; all HTTP 200; 175 unique UIDs. No English filter was recorded.

Browser update (2026-09-20; Web of Science Core Collection, Editions All; publication date
2006-01-01 to 2026-09-20):

- Base: `("avian influenza" OR "avian flu" OR "influenza A virus" OR "influenza A" OR H5N1 OR H5N2 OR H5N6 OR H5N8 OR H5Nx OR H7N1 OR H7N3 OR H7N4 OR H7N7 OR H9N2) AND (Nigeria OR Nigerian)` — **206**.
- Molecular: base AND `(molecular OR phylogen* OR sequence* OR genome* OR reassort* OR clade OR sublineage OR genotype)` — **77**.
- Epidemiology: base AND `(epidemiol* OR outbreak* OR surveillance OR prevalence OR incidence OR "risk factor*" OR spati* OR temporal OR spread)` — **154**.
- Wild-bird/host: base AND `("wild bird*" OR migratory OR waterfowl OR duck* OR goose* OR "live bird market*")` — **70**.

The interface suggested H7N9 for H7N4; the suggestion was not accepted. Free View supplied
authoritative displayed counts but no reliable full record-level export. These totals supersede
the 19 September HTTP-429 facet status for count documentation only; the 175 API UIDs remain the
only imported WoS records.

## ScienceDirect

Variant of Scopus string in title-abs-key; record filters + cap. Date: ____ | Hits: ____ | Export: ____

## Google Scholar (relevance-ranked, cap 200; supplementary only)

Queries: Q1 "avian influenza" Nigeria; Q2 H5N1 Nigeria; Q3 H9N2 Nigeria; Q4 poultry Nigeria wild birds. Date: 2026-09-17 | Years: 2006–2026 | Sort: relevance | Cap: 200/query | Retrieved: 140 | Cross-query unique: 99 | Persistent export: none | Status: supplementary, excluded from primary PRISMA snapshot.

## AJOL (on-site run completed 2026-09-20)

| Exact query | Displayed hits |
|---|---:|
| `+Nigeria +"avian influenza"` | 66 |
| `+Nigeria +"influenza A virus"` | 13 |
| `+Nigeria +"H5N1"` | 23 |
| `+Nigeria +"H5N8"` | 2 |
| `+Nigeria +"H9N2"` | 6 |
| `+Nigeria +"H7N7"` | 4 |
| `+Nigeria +"avian influenza" +molecular` | 8 |
| `+Nigeria +"avian influenza" +epidemiology` | 10 |
| `+Nigeria +"avian influenza" +"wild bird"` | 12 |

Raw query rows: **144**. URL-level deduplication: **79 unique article pages** (65 repeated rows
across queries). Initial metadata QA exposed 12 repeated navigation captures; the 12 missed URLs
were reopened and validated. Corrected public-page metadata QA: titles 79/79, dates 79/79, DOI
50/79; 73 records were dated 2006–2026 and six were outside the review window. Records and query
lineage are in file 55 and linked to file 53. No substantive screening decision was made.

## Supplementaries

Backward/forward chasing per include; Kalonda + Akanbi lists checked. Added records: ____ with source each.
