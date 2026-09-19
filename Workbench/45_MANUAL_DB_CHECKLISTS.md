# 45 — Manual database checklists (human with library access) — v1 frozen 2026-09-16

Scope: Scopus / WoS / ScienceDirect / Google Scholar / AJOL manual runs only.
Out of scope: PubMed v3 140 (done) and supplement API pull (built separately) — do NOT re-run PubMed here.
Source strings: v1 verbatim from `19_SEARCH_run_sheets.md`. Do not amend strings mid-run; amendments get new version + date.
Standard: PRISMA-S loggable. Language of this sheet: British English (search strings themselves remain as frozen).

General logging rule (all databases): record platform, date run, exact string as pasted, filters applied, hits, number screened, number kept, export filename. Paste the completed log block back to the assistant for dedupe.

Dedupe baseline: PubMed v3 base 140 (`35_PUBMED_v3_base.txt`). Priority: DOI > PMID > normalised title + year.

---

## 1. Scopus (via Elsevier, library access) — copy-paste

Where: Scopus > Advanced search > enter query > Search.

Copy-paste string (v1 frozen):

```
TITLE-ABS-KEY("avian influenza" OR AIV OR HPAI OR LPAI OR H5N1 OR H5N2 OR H5N6 OR H5N8 OR H9N2) AND TITLE-ABS-KEY(Nigeria OR Nigerian) AND PUBYEAR > 2005 AND PUBYEAR < 2027
```

Steps:
1. Paste string above into Advanced search. Do not add extra terms.
2. Apply filters: Publication year 2006–2026 inclusive; Language English (record if filter unavailable).
3. Record hits as displayed before export.
4. Export: Select all > Export > RIS and BibTeX (both if available; RIS minimum). File name: `Scopus_YYYYMMDD_nNNN.ris` (replace NNN with hits).
5. If export is capped or truncated, note cap in log.

Log block (paste back):

```
Scopus | Date run: ____ | String: v1 as above (verbatim Y/N: __)
Filters: year 2006–2026, English: ____ | Hits: ____
Screened: ____ | Kept: ____ | Export file: ____ | Notes/cap: ____
```

---

## 2. Web of Science (library access) — copy-paste

Where: Web of Science Core Collection > Advanced Search.

Before running, record: Editions selected (tick and state): SCIE [ ] / SSCI [ ] / ESCI [ ] / other: ____.
Timespan: Custom date range 2006-01-01 to 2026-09-30.

Copy-paste string (v1 frozen):

```
TS=("avian influenza" OR AIV OR HPAI OR LPAI OR H5N1 OR H9N2) AND TS=(Nigeria OR Nigerian) AND PY=(2006-2026)
```

Steps:
1. Set collections and timespan first, then paste string.
2. Apply language filter English if available; record if not.
3. Record hits.
4. Export: Export > BibTeX and Tab-delimited (both if available; BibTeX minimum). File name: `WoS_YYYYMMDD_nNNN.bib`.
5. Export full record + cited references if offered; otherwise full record only — note choice.

Log block (paste back):

```
WoS | Date run: ____ | Collections: SCIE/SSCI/ESCI/other: ____
Timespan: 2006-01-01 to 2026-09-30 | String: v1 as above (verbatim Y/N: __)
Filters: ____ | Hits: ____ | Screened: ____ | Kept: ____
Export file: ____ | Notes/cap: ____
```

---

## 3. ScienceDirect (Elsevier) — advanced variant

Where: ScienceDirect > Advanced search > Title, abstract or author-specified keywords field.

Copy-paste variant (v1-adapted; ScienceDirect Boolean limits apply — run as one line, split only if rejected and log split):

```
("avian influenza" OR AIV OR H5N1 OR H9N2) AND (Nigeria OR Nigerian)
```

Steps:
1. Paste into Title/Abstract/Keywords field. Add Year range 2006–2026 via filters.
2. If the platform rejects the string (operator limit), run two splits and log both:
   - Split A: `("avian influenza" OR AIV OR H5N1) AND (Nigeria OR Nigerian)`
   - Split B: `(H9N2 OR H5N8 OR H5N6) AND (Nigeria OR Nigerian)`
3. Record filters applied (years, subject areas left at All unless noted).
4. Export: available export or e-mail/RIS capture per screen; if no bulk RIS, export page-by-page and note count. File name: `ScienceDirect_YYYYMMDD_nNNN.ris` or `.bib`.
5. ScienceDirect results are capped and relevance-ranked — always log displayed total vs exported total.

Log block (paste back):

```
ScienceDirect | Date run: ____ | String run: single-line / Split A+B (delete as applicable)
Exact string(s): ____ | Filters (years 2006–2026 + other): ____
Hits displayed: ____ | Exported: ____ | Screened: ____ | Kept: ____
Export file: ____ | Cap notes: ____
```

---

## 4. Google Scholar — 4 queries, cap 200 each, relevance sort

Where: Scholar (logged-in browser). Settings > Scholar: results per page 20; date range 2006–2026 via left filter "Since 2006" + "Custom range 2006–2026" where offered. Sort: relevance (default — do NOT switch to date sort).

Run each query separately. Copy-paste (include quotes where shown):

```
Q1: "avian influenza" Nigeria
Q2: H5N1 Nigeria
Q3: H9N2 Nigeria
Q4: poultry Nigeria wild birds
```

Steps per query:
1. Paste query, apply custom range 2006–2026, keep relevance sort.
2. Screen first 200 records maximum per query (cap 200). Stop at 200 even if more hits.
3. Capture via Publish-or-Perish: Source Google Scholar > paste query > Lookup > set Years 2006–2026, Max results 200 > Export CSV/BibTeX. File name: `Scholar_Q1_YYYYMMDD.*` through `Scholar_Q4_YYYYMMDD.*`.
4. If Publish-or-Perish is unavailable, use Scholar manual save (My Library) + log screened/kept counts per query.

Anti-CAPTCHA notes (mandatory):
- Use a logged-in browser session, normal institutional IP; do not run queries in parallel tabs.
- Leave 5–10 s delay between page advances and between queries.
- If a CAPTCHA or "unusual traffic" page appears: stop immediately, wait at least 30 min, resume with longer delays. Do not use automated scrapers or solve-loop scripts.
- Log any CAPTCHA stop with time and query position.

Log block per query (paste back — 4 rows):

```
Scholar Q1 "avian influenza" Nigeria | Date: ____ | Years filter 2006–2026 Y/N: __ | Hits stated: ____ | Screened (cap 200): ____ | Kept: ____ | Export file: ____ | CAPTCHA stop Y/N + notes: ____
Scholar Q2 H5N1 Nigeria | Date: ____ | Years filter 2006–2026 Y/N: __ | Hits stated: ____ | Screened (cap 200): ____ | Kept: ____ | Export file: ____ | CAPTCHA stop Y/N + notes: ____
Scholar Q3 H9N2 Nigeria | Date: ____ | Years filter 2006–2026 Y/N: __ | Hits stated: ____ | Screened (cap 200): ____ | Kept: ____ | Export file: ____ | CAPTCHA stop Y/N + notes: ____
Scholar Q4 poultry Nigeria wild birds | Date: ____ | Years filter 2006–2026 Y/N: __ | Hits stated: ____ | Screened (cap 200): ____ | Kept: ____ | Export file: ____ | CAPTCHA stop Y/N + notes: ____
```

---

## 5. AJOL (African Journals Online) — 6 free-text queries + Google fallback

Where: https://www.ajol.info advanced/site search, manual browser. AJOL blocks bots (HTTP 403 to automation); all AJOL runs are manual by design with this sheet as the PRISMA-S record.

Copy-paste queries (run one at a time, free-text/All fields):

```
A1: avian influenza Nigeria
A2: H5N1 Nigeria
A3: H5N8 Nigeria
A4: H9N2 Nigeria
A5: HPAI Nigeria
A6: poultry Nigeria wild birds
```

Google fallback variants (only if AJOL on-site search returns zero or errors; log as fallback):

```
site:ajol.info "avian influenza" Nigeria
site:ajol.info H5N1 Nigeria
site:ajol.info H5N8 Nigeria
site:ajol.info H9N2 Nigeria
site:ajol.info HPAI Nigeria
site:ajol.info poultry Nigeria wild birds
```

Steps:
1. Run A1–A6 on AJOL in order; record hits per query individually (do not pool at search stage).
2. Screen title/abstract on AJOL; download or note records kept per query.
3. Use site: variants only as fallback; label clearly.

Per-query log table (paste back):

```
| Query | Date | Source (AJOL on-site / Google site:) | Hits | Screened | Kept | Notes |
| A1 avian influenza Nigeria | ____ | ____ | ____ | ____ | ____ | ____ |
| A2 H5N1 Nigeria | ____ | ____ | ____ | ____ | ____ | ____ |
| A3 H5N8 Nigeria | ____ | ____ | ____ | ____ | ____ | ____ |
| A4 H9N2 Nigeria | ____ | ____ | ____ | ____ | ____ | ____ |
| A5 HPAI Nigeria | ____ | ____ | ____ | ____ | ____ | ____ |
| A6 poultry Nigeria wild birds | ____ | ____ | ____ | ____ | ____ | ____ |
Export files: ____
```

PRISMA-S wording (paste into manuscript methods supplement): "AJOL was searched manually (on-site free-text, six queries, [dates]) because automated retrieval returns HTTP 403 bot-block responses; Google site:ajol.info variants served as fallback only where stated. Per-query hits, screening counts, and exports are logged in Workbench file 45."

---

## 6. What to paste back for dedupe (assistant step — do not dedupe by hand)

Reply with, per database: date run, exact string version (v1 verbatim Y/N + any split noted), hits, export filename (attach file or state Workbench path). Example:

```
Scopus 2026-09-__ v1 verbatim, hits ___, file Scopus_202609___.ris
WoS SCIE+ESCI 2006-01-01–2026-09-30 v1 verbatim, hits ___, file WoS_202609___.bib
ScienceDirect single/split, hits ___, file ScienceDirect_202609___.ris
Scholar Q1–Q4 screened/kept + 4 export files
AJOL A1–A6 table + export files
```

Assistant dedupes against PubMed v3 140 by DOI first, then PMID, then normalised title + year; reports new uniques vs duplicates with match key per record. Human does not need to remove duplicates before sending.

---

Freeze: v1 2026-09-16. Source: file 19. PubMed untouched. Files 15, 33, 41–44 untouched by this sheet.
