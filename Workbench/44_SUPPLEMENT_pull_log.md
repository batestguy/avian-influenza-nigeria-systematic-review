# Supplement pull log — OpenAlex + Crossref (API, no browser) — 2026-09-16

Browser-free run: all target sites return 403/429/captcha to Playwright; used public APIs instead.

## PRISMA-S entries

### OpenAlex
- Source: OpenAlex. Platform: api.openalex.org (REST, polite pool User-Agent, no key).
- Date run: 2026-09-16.
- Verbatim search string / URL: `https://api.openalex.org/works?search=avian%20influenza%20Nigeria&filter=from_publication_date:2006-01-01,to_publication_date:2026-09-30,language:en&per-page=200&select=id,doi,pmid,title,publication_year,authorships,primary_location&cursor=* (paged via next_cursor, capped at 1000)`
- Filters (API `filter` param): `from_publication_date:2006-01-01,to_publication_date:2026-09-30,language:en`. Search keywords: `avian influenza Nigeria` (`search=` = full-text search).
- Select requested: `id,doi,pmid,title,publication_year,authorships,primary_location`; API rejects top-level `pmid` in `select` (HTTP 400), so actual select run was `id,doi,ids,title,publication_year,authorships,primary_location` with PMID taken from `ids.pmid` — equivalent coverage, noted here for reproducibility.
- Hits returned: total matches reported by API = 6455; exported (cap) = 1000 (per-page 200, cursor paging, hard cap 1000 per review plan).
- Exported file: `41_OPENALEX_raw.json` (fields per record as selected + `total_count`, `returned_count`, `first_url`).
- Notes: broad full-text `search=` recall — most hits are off-topic at title level; title/abstract screening + dedupe vs PubMed 140 still required. No rate-limit errors this run (0.3 s between pages). Cap means ranks beyond 1000 (relevance order) were NOT screened — record as PRISMA-S limitation.

### Crossref
- Source: Crossref. Platform: api.crossref.org (REST, no key, polite User-Agent).
- Date run: 2026-09-16.
- Verbatim search string / URL: `https://api.crossref.org/works?query=avian+influenza+Nigeria&filter=from-pub-date%3A2006-01-01%2Cuntil-pub-date%3A2026-09-30%2Ctype%3Ajournal-article&rows=1000&offset=0&select=DOI%2Ctitle%2Cauthor%2Cpublished-print%2Cpublished-online%2Ccreated%2Ccontainer-title%2CURL%2CISSN`
- Filters (API `filter` param): `from-pub-date:2006-01-01,until-pub-date:2026-09-30,type:journal-article`. Query: `query=avian influenza Nigeria`.
- Hits returned: total-results reported by API = 299088; exported = 1000 (single call `rows=1000&offset=0`, relevance-ranked).
- Exported file: `42_CROSSREF_raw.json` (full item payloads + `total_results`, `returned_count`, `url`).
- Notes: `query=` is bibliographic+full-text ranked, hence very large total (299088); only top-1000 relevance ranks exported per plan — same PRISMA-S cap limitation as OpenAlex. No rate-limit errors this run. Crossref items carry no reliable PMID; dedupe used DOI then normalised title+year.

## Dedupe vs PubMed v3 base (140 PMIDs, `35_PUBMED_v3_base.txt`)
- PubMed record is master. Match order: (1) DOI lowercase-normalised (strip `https://doi.org/`, trailing `.`), (2) PMID where present (OpenAlex `ids.pmid`; Crossref none), (3) normalised title (lowercase, punctuation→space, collapse whitespace) + 4-digit year.
- PubMed metadata from `31_PUBMED_candidates.json` (126/140) + NCBI esummary refill for the 14 v3-only PMIDs missing from file 31.
- Output: `43_SUPPLEMENT_candidates.json` — one record per unique supplement work (internal OpenAlex↔Crossref merge on DOI else title+year; `source` = `openalex`, `crossref`, or `openalex;crossref`), fields `source, doi, pmid, title, year, venue, url, overlap_pubmed`.
- Counts this run: OpenAlex 117/1000 overlap PubMed-140; Crossref 56/1000 overlap; unique supplement records 1876 (overlap 124, novel 1752, in-both-sources 124).

## Dedupe audit + collapse (2026-09-16, verified by script)

- False overlap: `10.2807/esw.11.07.02898-en` had no DOI/PMID/title match — flipped to novel. Overlap 124→123 raw.
- Near-duplicates (normalised title+year): 128 groups / 132 extra records (journal vs preprint/digest-DOI, e.g. 10.3390/v11070620 vs preprints201906; PAMJ variants).
- Collapsed canonical: `46_DEDUP_COLLAPSED.json` — 1744 records (overlap 117, novel 1627). Six overlap records merged inside duplicate groups (123→117).
- Screening votes to date are pre-collapse (upper bound); remap to canonical before locking PRISMA flow.

## Corrected PRISMA identification (2026-09-16)

| Stage | n |
|---|---|
| PubMed v3 base | 140 |
| OpenAlex exported of 6,455 | 1,000 |
| Crossref exported of 299,088 | 1,000 |
| Supplement raw → canonical | 2,000 → 1,876 → 1,744 |
| PubMed ∩ supplement (canonical) | 117 |
| Unique for title screening | 1,767 (140 + 1,627) |
| Title-screen status | PubMed 142 done; supplement 1,752 raw-screened, remap to 1,627 pending |
- Next step: title screen the 1752 novel records with file 18 forms before full-text; do NOT re-edit PubMed strings mid-run.
