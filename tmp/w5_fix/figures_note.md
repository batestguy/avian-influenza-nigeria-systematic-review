# Figures for the Nigeria avian influenza virus systematic review, 2006-2026

Draft dated 2026-10-09. Values are read at run time from the data files; no
range or date literal is typed into a drawing call. Figure 2 values come from
`synthesis/t2.json` and `synthesis/t1.json`. Figure 3 ranges come from
`fig3_ranges.json` in this folder, a curated file in which every range and date
carries the evidence it rests on (a `source` string, plus the study row(s) where
a row underpins it); `build_figures.py` stops if that file is missing or
malformed. The script prints a validation table to stdout and writes it to
`validation_table.txt`: the per-epoch counts recomputed from the cells, every
figure 3 range with its source, and the build date and the sha256 of each input.
It aborts before drawing, and does not write `validation_table.txt`, if the
per-epoch counts do not match the verified T2 counts or if `fig3_ranges.json` is
unusable. The data root is taken from the `AIV_RETRIEVAL_ROOT` environment
variable, falling back to the literal path recorded in the script (the same
pattern as `synthesis/syn_common.py`).

Environment: Python, matplotlib 3.10.9, numpy 2.4.6. No geo/spatial packages are
used: the GeoJSON is parsed and drawn as matplotlib `Polygon` patches.
Figures are deterministic in content (no random numbers are used anywhere): the
PNGs are byte-identical between runs, while the PDFs differ only in the creation
timestamp the PDF writer embeds. `validation_table.txt` additionally records the
build date and the input hashes.

## Outputs

| File | Note |
|---|---|
| `build_figures.py` | regenerates both figures from the source data |
| `fig3_ranges.json` | curated figure 3 ranges, each with its evidence and certainty rating |
| `fig2_states_epochs.pdf` / `.png` | state x epoch map, six panels |
| `fig3_timeline.pdf` / `.png` | detection timeline and clade turnover |
| `validation_table.txt` | the validation table printed at build time, stamped with the build date and input hashes |
| `geoBoundaries-NGA-ADM1.geojson` | Nigeria ADM1 boundaries, downloaded once and kept |

Both figures are 180 mm wide (double-column). The PDFs are true vector: the
files contain no raster image objects, and Times New Roman is embedded as a
Type-42/TrueType (CIDFontType2) subset. The PNGs are 600 dpi. A single-column
(90 mm) variant can be produced by setting `FIG_W_MM = 90.0` and re-running; six
map panels at 90 mm would need re-arranging, so only the double-column variant
is supplied.

---

## Figure 2. Laboratory-confirmed AIV evidence in Nigeria by state and epoch, 2006-2026

### Caption draft

**Figure 2.** Laboratory-confirmed avian influenza virus evidence in Nigeria by
state and epoch, 2006-2026. Four small multiples show E1 (2006-2010), E2
(2011-2014), E3 (2015-2020) and E4 (2021-2026); two further panels show rows
that cannot be placed in a single epoch ("multi-epoch") and rows with no stated
date ("date NR"). Dark blue denotes laboratory-confirmed evidence (sequence,
isolate, RNA, or a lab-confirmed case with the method not reported); light blue
denotes an official report only (the section sign, assay not stated), which is
not counted as confirmation; pale grey denotes no evidence in that epoch.
Hatching marks cells that carry antibody (cross) or antigen (double cross)
marker rows without laboratory-confirmed evidence; such a cell may still carry
an official report. Two-letter codes identify states; the Federal Capital
Territory is shown separately, and codes are drawn white on the dark blue fill
and dark grey on the light fills. Counts are named-state floors, so they record
where sequencing and reports exist rather than the true extent of infection.

### What the marks mean, and why

* **Dark blue (class 2)** - a `best_evidence` value of `sequence`, `isolate`,
  `RNA` or `lab-confirmed case (method NR)`. These four labels are the
  laboratory-confirmation tier defined in `synthesis/SWIM_NARRATIVE.md`
  ("Definitions used throughout") and in the T2 header in `synthesis/tables.md`.
* **Light blue (class 1)** - the cell holds an official report (the section
  sign; assay not stated). Official reports are explicitly *not* counted as
  confirmation, so they are shown but excluded from every panel count.
* **Pale grey (class 0)** - no evidence of any kind in that epoch. This includes
  jurisdictions absent from `t2.json` altogether.
* **Hatching** - the cell carries `antibody_marker_rows(†)` or
  `antigen_marker_rows(‡)` and has no laboratory-confirmed evidence; it may
  still carry an official report (true for the two hatched multi-epoch cells,
  Bauchi and Gombe). Antibody evidence shows exposure only, and H5 antibody in
  poultry can reflect vaccination. In these data only antibody-marker cells
  trigger hatching - no cell carries antigen rows without laboratory-confirmed
  evidence - so the legend has a single hatch key and the double-cross hatch is
  retained in the code but not drawn.

### Provenance of every number shown

Per-epoch counts, computed from `synthesis/t2.json`
(`matrix[<state>].cells[<epoch>].best_evidence`) and identical to
`synthesis/t2.json` `summary_per_column[<epoch>].n_states_confirmed` and to
`synthesis/tables.md` line 235:

| Panel | Count shown | Composition (source: `t2.json` summary / `tables.md` L235) |
|---|---|---|
| E1 2006-2010 | 27 | 26 states + FCT |
| E2 2011-2014 | 2 | Kano, Oyo |
| E3 2015-2020 | 22 | 21 states + FCT |
| E4 2021-2026 | 15 | 14 states + FCT |
| multi-epoch | 0 | no jurisdiction has confirmed evidence in this column |
| date NR | 5 | Bauchi, Borno, Gombe, Jigawa, Plateau |

Rows behind the composition:

* E2 Kano - `STU-004#3` (H5N1 isolate; the entry rests on deaths of 24 Dec 2014,
  specimens received 2015-01, per the `t2.json` notes). Oyo - `STU-049` LPAI
  H5N2 in live-bird-market ducks.
* date NR - `STU-014#4` (H5, N not determined) in Bauchi and Gombe; `STU-106#0`
  and `STU-106#1` (type A / subtype not reported) in Borno; `STU-009#1` (H5N1
  isolate) in Jigawa; `STU-007#0` (type A / subtype not reported; high-risk
  study) in Plateau.
* multi-epoch - 35 jurisdictions each carry `STU-043#0` (a single WAHIS row
  dated 2006-01 to 2023-06). It is an official-report marker only and therefore
  contributes **no** confirmed count anywhere.
* FCT is a separate key in `t2.json` (`"FCT"`), and the boundary file names it
  `Abuja Federal Capital Territory`; the script maps the two names.

Exposure/antigen-only (hatched) jurisdictions per panel, computed from the
marker fields and equal to `t2.json`
`summary_per_column[<epoch>].states_with_exposure_or_antigen_only`:

| Panel | Hatched jurisdictions |
|---|---|
| E1 | Kogi |
| E2 | Bauchi, Gombe, Kaduna, Kogi, Plateau |
| E3 | Kwara |
| E4 | none |
| multi-epoch | Bauchi, Gombe |
| date NR | Kaduna, Kogi, Ogun, Osun, Oyo |

One deliberate difference from `t2.json`'s own summary: in the multi-epoch
column the summary's `states_with_exposure_or_antigen_only` list is empty, but
Bauchi and Gombe do carry antibody rows (`STU-041#0`, `STU-041#1`) alongside
their official-report marker. The figure hatches those two, because the
underlying marker rows exist; the summary lists only cells that have antibody or
antigen rows *and no* official marker.

Jurisdictions drawn with no evidence at all: Cross River and Ondo (absent from
`t2.json`, consistent with the narrative's statement that only those two lack
both laboratory and official evidence), plus, per epoch, the states whose cells
are empty.

---

## Figure 3. Detection timeline and clade turnover, 2006-2026

### Caption draft

**Figure 3.** Detection timeline and clade turnover of avian influenza virus in
Nigeria, 2006-2026. Hatched bands show the two epizootic waves (2006-2008 and
2015-2017) and the lull in reported highly pathogenic avian influenza from 2009
to November 2014 (the band closes at 2014.83, the decimal-year position of
November 2014 under the month-start convention recorded in `fig3_ranges.json`).
The existence of the two waves is of low certainty; their boundaries and the
lull are of very low certainty, because an absence of reports is not an absence
of virus and H5 RNA and antibody were both found in the interval. Horizontal
bars show successive clades: 2.2 (2006-2008), 2.3.2.1c from 2015 and 2.3.4.4b
(2021-2026). The 2.3.2.1c bar is solid only over the interval its evidence
supports (2015 to 2016; the last retrieved 2.3.2.1c evidence is `STU-023#1`,
2016-01 to 2016-06), and continues to 2026 as a lighter, dashed band labelled
"no later evidence retrieved", to show that the claim runs to the present
without further 2.3.2.1c evidence. The separate dashed segment marks the very
low certainty claim about the onset of 2.3.4.4 in 2019 (or 2016). The lower bars
show intra-clade reassortment. Triangles mark the first detections of H5N1
(2006, low certainty), H5N8 (2016), H5N6 (2019) and H9N2 (2019, month not
reported); the non-H5N1 first detections are of very low certainty.

### Every range drawn, with its source

These ranges live in `fig3_ranges.json` (one entry per range, each with its
`source` and any study rows); the script reads them from there, draws them, and
prints them with their sources into `validation_table.txt`. Claim ids are those
in `synthesis/SWIM_NARRATIVE.md`; ratings are the adjudicated certainty ratings.

| Element | Range drawn | Claim | Rating | Source |
|---|---|---|---|---|
| Epizootic wave 1 | 2006-2008 | (b1) existence; (b2) boundaries | Low (existence); Very low (timing) | SWIM S1 (b1), (b2) |
| Epizootic wave 2 | 2015-2017 | (b1); (b2) | Low; Very low | SWIM S1 (b1), (b2) |
| Lull in reported HPAI | 2009 to Nov 2014 (drawn to 2014.83) | (b2) | Very low | SWIM S1 (b2) |
| Clade 2.2 | 2006-2008 | (h) | Low | SWIM S4 (h); `t1.json` clade `2.2` earliest 2006-03, `STU-108#2` |
| Clade 2.3.2.1c | 2015-2016 solid, dashed continuation to 2026 | (i) | Low | SWIM S4 (i) "from 2015"; last evidenced point `STU-023#1` (2016-01 to 2016-06); `t1.json` clade `2.3.2.1c` earliest 2015-01, `STU-066#0`, `STU-067#0` |
| Clade 2.3.4.4b | 2021-2026 | (j1) | Low | SWIM S4 (j1) |
| Onset of 2.3.4.4 (dashed) | 2019-2021 | (j2) | Very low | SWIM S4 (j2); `t1.json` clade `2.3.4.4b` earliest 2019-06, `STU-071#1` |
| Clade-level turnover | 2006 to 2026 | (l1) | Low | SWIM S4 (l1) |
| Intra-clade reassortment | 2006-2007 and 2015-2016 | (k1) | Low | SWIM S4 (k1) |
| First detection H5N1 | 2006-01 | (a) | Low | `t1.json` `subtype.H5N1.earliest.start_ym = [2006, 1]` |
| First detection H5N8 | 2016-11 | (c) | Very low | `t1.json` `subtype.H5N8.earliest.start_ym = [2016, 11]`, `STU-033#2` |
| First detection H5N6 | 2019-06 | (c) | Very low | `t1.json` `subtype.H5N6.earliest.start_ym = [2019, 6]`, `STU-071#1` |
| First detection H9N2 | 2019 (month not reported) | (c) | Very low | `t1.json` `subtype.H9N2.earliest.start_ym = [2019, null]`, `STU-071#0` |

How certainty is drawn: low-certainty items are solid; very-low-certainty items
are lighter or dashed. The first-detection markers use a filled triangle for low
certainty and an open triangle with a dashed leader for very low certainty. The
solid part of a clade bar covers only the interval its evidence supports; where
the claim runs on without later evidence (2.3.2.1c), the bar continues as a
lighter dashed band labelled "no later evidence retrieved".

The 9 low / 14 very low / 1 not-gradable rating counts quoted above were
cross-checked against the manuscript: `manuscript/sections/06_results_c.txt`
line 11 ("Nine claims were rated low certainty and fourteen very low certainty;
species-level host range was not gradable") and `manuscript/sections/03_methods.txt`
line 61 (the rating convention). No rating is invented here.

---

## Review cross-checks performed

1. **Per-epoch counts, three ways.** The script recomputes every panel count from
   the per-cell `best_evidence` values and compares each against (a) the expected
   values in the brief and (b) `t2.json` `summary_per_column.n_states_confirmed`.
   All six columns printed `OK` (27/2/22/15/0/5). The build aborts before drawing
   on any mismatch, and `validation_table.txt` is written only after the guard
   passes.
2. **Evidence-tier vocabulary.** The script raises an error on any
   `best_evidence` value it does not recognise. The five values present in the
   file are `RNA`, `isolate`, `lab-confirmed case (method NR)`,
   `none (exposure/antigen/official only)` and `sequence` - all mapped.
3. **Exposure/antigen-only sets.** The hatched jurisdictions per panel were
   compared with `t2.json`
   `summary_per_column[<epoch>].states_with_exposure_or_antigen_only` for E1-E4
   and the date-NR column; they agree. The one deliberate difference (Bauchi and
   Gombe in the multi-epoch column) is documented above.
4. **Geography coverage.** All 35 jurisdictions in `t2.json` were matched to an
   ADM1 feature; the script stops if any is unmatched. The boundary file has 37
   features, so Cross River and Ondo are drawn as "no evidence".
5. **Visual inspection.** The rendered PNGs were opened and inspected, including
   a crop of the E1 panel, to confirm that the hatching is confined to the
   correct state (Kogi) and that no polygon is drawn off-canvas.
6. **First-detection values** are read live from `t1.json` and echoed by the
   script at build time, so the printed log and the figure cannot diverge.
7. **Vector output.** Both PDFs were inspected: no `/Subtype /Image` objects
   (true vector), and Times New Roman is embedded as a Type-42/TrueType
   (`FontFile2`, CIDFontType2) subset. Only one font is embedded, so the section
   sign, cross, double cross, arrow and en-dash all resolved from Times New
   Roman rather than falling back.
8. **Figure 3 ranges.** Every range and date drawn in Figure 3 is read from
   `fig3_ranges.json`, and the script aborts if the file is missing, malformed or
   missing a required field. Each range is printed with its source into
   `validation_table.txt`. The first-detection claim, rating and month-reported
   flag come from the same file, and the flag is checked against `t1.json`
   `start_ym` before the value is used.

## Could not verify, or deliberately omitted

* **Projection.** The boundaries are unprojected WGS84 longitude/latitude drawn
  with an equal aspect ratio, so shapes are slightly distorted east-west
  relative to a projected map. No scale bar is drawn for this reason; distances
  read from Figure 2 would not be accurate.
* **Wave boundaries are years, not months.** The source states the waves as
  2006-2008 and 2015-2017, so the bands are drawn on calendar-year edges; the
  underlying monthly evidence is not precise enough to place them better.
* **2.3.4.4b onset.** The figure draws the 2019 onset only (from `t1.json`,
  `STU-071#1`) and labels it very low certainty, with the dashed 2019-2021
  segment distinct from the low-certainty 2021-2026 presence. The alternative
  2016 onset (`STU-033#2`, labelled "2.3.4.4 group B" in the source and mapped
  to 2.3.4.4b by the review) is described in the caption but not drawn as a
  second marker, so as not to imply two separate onsets.
* **H9N2 month.** The first H9N2 detection is dated 2019 with the month not
  reported; it is plotted at the start of 2019, and its position within the year
  is not evidenced. Both the marker label and the caption say "month not
  reported".
* **Lull end convention.** The source states the lull as "2009 to Nov 2014"; the
  band is drawn to 2014.83, the decimal-year position of November 2014 under the
  month-start convention recorded in `fig3_ranges.json`.
* **Unused double-cross (‡) hatch.** No cell in `t2.json` carries antigen rows
  without laboratory-confirmed evidence, so the `...` antigen hatch is retained
  in the code but never drawn; the legend therefore carries one hatch key, for
  both marker types.
* **Flats for "no evidence".** Cross River and Ondo are drawn as no evidence in
  every panel. That is an absence of *retrieved* evidence, not a demonstrated
  absence of infection; the narrative rates this class of claim very low.
* **Underlying studies.** The study rows (`STU-xxx#i`) were not re-checked
  against the primary papers in this task. The validation is against
  `synthesis/t2.json` (including its own summary block), `synthesis/t1.json`,
  `synthesis/tables.md`, and the curated `fig3_ranges.json`, whose entries carry
  their own citations to the narrative claims and `t1.json`.
* **Single-column variant** is not supplied; see Outputs above.

## Geography attribution and licence

Nigeria administrative level 1 boundaries from geoBoundaries (gbOpen),
downloaded once and kept as `geoBoundaries-NGA-ADM1.geojson`:

* URL: `https://github.com/wmgeolab/geoBoundaries/raw/9469f09/releaseData/gbOpen/NGA/ADM1/geoBoundaries-NGA-ADM1.geojson`
* Pinned commit: `9469f09`
* Licence: **CC BY 4.0**. Attribution: geoBoundaries (www.geoboundaries.org),
  William & Mary geoLab.
