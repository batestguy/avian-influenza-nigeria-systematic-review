# Search run sheets — execute one row at a time, log as you go

## 2026-10-09 — W1 search rebuild (file 59). Final strings and counts for the re-run

**Where the strings live:** `D:\AvianInfluenzaSysRev_retrieval_20260927\w1_search_20261009\strings_final.md`
(verbatim per source, with facet rationale); raw responses in `raw\`; run metadata in `hits.json`.
To be transcribed into manuscript Appendix A at W9. The Scopus/ScienceDirect strings are unchanged
from this sheet (still pending D4 for a human export).

| Source | Status | Total | Notes |
|---|---|---:|---|
| PubMed (E-utilities) | ok | **209** | New PRESS-improved string; the old v3 string returned 140 — the old string missed about half the field (added `"Influenza in Birds"[Mesh]`, `"Influenza A virus"[tiab]`, `Nigerians[tiab]`, `Nigeria[ad]`). Record as a dated amendment. |
| OpenAlex (cursor, 54 pages × 200) | ok | 10,614 | No 1,000-record cap; `search` is a title/abstract/fulltext field — totals are not Boolean-comparable; spill-over expected. |
| Crossref (cursor, 6 pages × 1000) | ok | 6,000 of 16,292 | Relevance engine, non-Boolean; download stopped at 6 pages for wall-clock. PRISMA should say "6,000 of 16,292". |
| Web of Science Starter API | ok | 194 | Key live; **no date filter honoured by the API — window applied locally**; no abstracts returned by Starter. |
| AJOL | partial | 66 rows / 20 captured | `page=2..4` returned byte-identical page 1; 46 titles need a browser. |
| Google Scholar (SerpApi) | skipped | – | Quota spent (250/250 on 8 Oct). Refresh needs a new month or paid plan. |
| Scopus / ScienceDirect | skipped | – | No legal programmatic access; needs a human (D4). Strings: see the two rows below. |

- **Total downloaded:** 17,037. **Matched to register:** 2,270. **Corrected dedup (v3):** 48 candidates;
  **44 likely-new (43 in window)** after fuzzy probable-duplicate exclusion — the W3 screening queue.
  Scripts: `dedup_v3.py`, `abstracts_fetch.py`, `fix_openalex_abstracts.py`, `finalise_candidates.py`.
- **Methods and filters as executed:** PubMed/OpenAlex/Crossref date windows 2006-01-01 to 2026-10-09;
  no language filters (the review has none); rate limits respected (≤3/s PubMed, 0.15–0.2 s elsewhere).
- **Limitations (disclosed):** relevance for the WoS set and the OpenAlex/Crossref spill-over sets is
  title-only (no abstracts); OpenAlex/Crossref totals are not Boolean counts; the AJOL and Scholar gaps
  above. Independent PRESS peer review of the strings is still missing.
- **Reviewer outcome:** W1 reviewer pass found the dedup DOI/entity defects, now fixed (file 15 top).

---

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

Queries: Q1 "avian influenza" Nigeria; Q2 H5N1 Nigeria; Q3 H9N2 Nigeria; Q4 poultry Nigeria wild birds. Date: 2026-09-17 | Years: 2006–2026 | Sort: relevance | Cap: 200/query | Retrieved: 140 | Cross-query unique: 99 | Persistent export: none | Status: supplementary, excluded from primary PRISMA snapshot; superseded by the re-run below.

**Re-run 2026-09-28 (post-freeze update search; file 15 MAJOR amendment).** Same Q1–Q4, via SerpApi `engine=google_scholar`, `as_ylo=2006`, `as_yhi=2026`, `as_sdt=0` (no patents), `as_vis=1` (no citations), `hl=en`, relevance, `num=20`, pages start 0–180 (cap 200/query). Retrieved: 200 per query = 800 | Unique (normalised title): 519 | Matched register: 291 | New: 228 | Export: `D:\AvianInfluenzaSysRev_retrieval_20260927\scholar_rerun\raw_q1q4_20260928.json` (outside repo). Screening (2026-09-29): blind R1/R2 title/snippet votes plus adjudication → 36 retained for full text, 192 excluded; added to file 56 as CAN-1878 to CAN-2105.

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
