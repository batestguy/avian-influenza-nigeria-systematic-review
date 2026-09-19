# AvianInfluenzaSysRev

Single-manuscript systematic-review repo. Only source of truth:
`Avian_review_paper_fellow.docx` (~2,783 words). No code, build, test, lint, CI, package manager. Do not scaffold any.

## Scope lock (user-confirmed)
- Future work = screening + extraction help only.
- Keep single `.docx`. No CSV/MD/figure/log sidecars unless explicitly asked. Put tables/appendices inside the `.docx`; screening guidance otherwise goes in chat.
- References are manual in Word. Keep numbered order + DOI style. No BibTeX/Zotero.

## Review identity
- Question: emergence, temporal/geographic/host-range, molecular/clade/reassortment dynamics of AIVs in Nigeria, 2006–2026.
- Standard: PRISMA 2020 (27-item + 12-item abstract) + PRISMA-S (16-item search) + SWiM for synthesis without meta-analysis. Do not force meta-analysis.
- Framework is CoCoPop/PEO, not PICO (no intervention).
- Search as stated: PubMed/MEDLINE, Scopus, WoS, Google Scholar, ScienceDirect, AJOL; Sept 2026. Full line-by-line strings per database are still missing — treat current term blocks as drafts. Current blocks wrongly embed `And Nigeria` inside every facet; rebuild as `(AIV) AND (Nigeria) AND (2006–2026)` with molecular/epi/wild-bird facets as separate lines (PRISMA-S).
- Differentiate vs Akanbi & Lakes 2025 (Nigeria 2006–2025 broad narrative, PubMed+Scopus only) and Kalonda 2020 (SSA 2000–2019, 68 studies): this review's claim is integrated spatiotemporal + clade/reassortment synthesis, not another overview.

## Working with the manuscript
- Read via `.docx`-as-ZIP (`word/document.xml`) or `python-docx`. Preserve Times New Roman + numeric bracket citations + yellow `Abstract` heading style.
- Never conflate: subtype vs clade/sublineage vs reassortant vs new introduction. State names and date ranges must stay consistent (British English).
- Eligibility anchor: Nigeria-specific HPAI/LPAI with epi, molecular/phylogenetic, or spatial/temporal data. Exclude non-Nigeria work without Nigeria data and non-avian influenza work.
- RoB: JBI Prevalence / Cross-Sectional / Cohort + custom molecular check (sampling, assay/sequencing transparency, phylogeny method/support, accession, reassortment overclaim). No ROBINS-I/RCT tools, no score-sums. Certainty narratively (GRADE-prognosis logic); do not invent grades.

## Order matters
`protocol freeze → search strings → screening → extraction pilot → RoB → SWiM synthesis → reporting → PRISMA/SWiM/PRISMA-S audit.` Do not start screening until protocol/strings frozen or PROSPERO prospectiveness is lost.

## Skills
- Load `systematic-literature-review` only for search/synthesis method; it is arXiv-only, so do not use its script for this PubMed/Scopus review.
- Load `thesis-to-journal` before any `.docx` edit; `academic-paper-review` for critique.
