# -*- coding: utf-8 -*-
"""
build_figures.py - W5 figures for the Nigeria avian influenza virus (AIV)
systematic review, 2006-2026.

Regenerates, from the verified synthesis data only:
  * FIGURE 2 - fig2_states_epochs.{pdf,png} : state x epoch small-multiple map
  * FIGURE 3 - fig3_timeline.{pdf,png}      : detection timeline, clade turnover

Design rules
------------
* No range or date is typed into a drawing call.  Figure 2 values are read at
  run time from synthesis/t2.json and synthesis/t1.json; figure 3 ranges are
  read from the curated fig3_ranges.json, in which every value carries the
  evidence (claim id or study row) it rests on.  Per-epoch counts and the shape
  of fig3_ranges.json are validated BEFORE any figure is drawn, and the script
  aborts on a mismatch.
* All six map panels share one explicit geographic extent, so the outline is
  identical in every panel.
* Times New Roman, British English, no emoji.
* PDF is true vector with embedded (Type-42) fonts; PNG is 600 dpi.
* Deterministic (no randomness is used anywhere).

Run:  python build_figures.py
"""
from __future__ import annotations

import hashlib
import json
import os
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MplPolygon, Patch

# --------------------------------------------------------------- paths ------
def _resolve(env_var, literal):
    # Environment override first, then the literal path recorded in this build;
    # the same pattern is used in synthesis/syn_common.py, so the pipeline can
    # be relocated with one environment variable.
    env = os.environ.get(env_var)
    if env:
        return Path(env)
    p = Path(literal)
    if p.exists():
        return p
    raise SystemExit(
        "%s is not set and the fallback path %s does not exist" % (env_var, literal)
    )


ROOT = _resolve("AIV_RETRIEVAL_ROOT",
                r"D:\AvianInfluenzaSysRev_retrieval_20260927")
SYN = ROOT / "synthesis"
OUT = ROOT / "manuscript" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

FIG3_RANGES = OUT / "fig3_ranges.json"
INPUTS_MANIFEST = ("t2.json", "t1.json", "fig3_ranges.json")

GEOJSON = OUT / "geoBoundaries-NGA-ADM1.geojson"
# geoBoundaries gbOpen, ADM1 for Nigeria.  Licence: CC BY 4.0.
# Attribution: geoBoundaries (www.geoboundaries.org), William & Mary geoLab.
GEOJSON_URL = (
    "https://github.com/wmgeolab/geoBoundaries/raw/9469f09/"
    "releaseData/gbOpen/NGA/ADM1/geoBoundaries-NGA-ADM1.geojson"
)

MM = 1.0 / 25.4
FIG_W_MM = 180.0  # double-column width; set 90.0 for a single-column variant

EPOCHS = ["E1", "E2", "E3", "E4"]
EPOCH_RANGE = {"E1": "2006-2010", "E2": "2011-2014",
               "E3": "2015-2020", "E4": "2021-2026"}
PANELS = EPOCHS + ["multi-epoch", "date NR"]

# best_evidence labels that count as laboratory confirmation, per
# synthesis/tables.md (T2 header) and synthesis/SWIM_NARRATIVE.md (definitions).
LAB_CONFIRMED = {"sequence", "isolate", "RNA", "lab-confirmed case (method NR)"}
OFFICIAL_ONLY = {"official confirmed report"}
NO_EVIDENCE_PREFIX = "none"

# Expected counts, read off synthesis/tables.md line 235 (verified upstream).
EXPECTED = {"E1": 27, "E2": 2, "E3": 22, "E4": 15, "multi-epoch": 0, "date NR": 5}

# Two-letter / short state codes for the map.  These are LABELS ONLY (not data);
# chosen to be unique across the 36 states and the FCT.
STATE_CODE = {
    "Abia": "AB", "Adamawa": "AD", "Akwa Ibom": "AK", "Anambra": "AN",
    "Bauchi": "BA", "Bayelsa": "BY", "Benue": "BE", "Borno": "BO",
    "Cross River": "CR", "Delta": "DE", "Ebonyi": "EB", "Edo": "ED",
    "Ekiti": "EK", "Enugu": "EN", "FCT": "FCT", "Gombe": "GO", "Imo": "IM",
    "Jigawa": "JI", "Kaduna": "KD", "Kano": "KN", "Katsina": "KT",
    "Kebbi": "KB", "Kogi": "KO", "Kwara": "KW", "Lagos": "LA",
    "Nasarawa": "NA", "Niger": "NI", "Ogun": "OG", "Ondo": "OD", "Osun": "OS",
    "Oyo": "OY", "Plateau": "PL", "Rivers": "RI", "Sokoto": "SO",
    "Taraba": "TA", "Yobe": "YO", "Zamfara": "ZA",
}
# The GeoJSON uses a long formal name for the Federal Capital Territory.
GEO_ALIAS = {"Abuja Federal Capital Territory": "FCT"}

# First-detection label placement (layout only, not data).
FIRST_LABEL = {
    "H5N1": dict(y=3.02, ha="left", dx=+0.18),
    "H5N8": dict(y=3.02, ha="right", dx=-0.18),
    "H5N6": dict(y=3.32, ha="left", dx=+0.14),
    "H9N2": dict(y=3.62, ha="right", dx=-0.14),
}

plt.rcParams.update({
    "pdf.fonttype": 42,      # embed TrueType subsets
    "ps.fonttype": 42,
    "figure.dpi": 600,
    "savefig.dpi": 600,
    "font.family": "serif",
    "font.serif": ["Times New Roman", "DejaVu Serif"],
    "axes.linewidth": 0.5,
    "hatch.linewidth": 0.35,
    "text.color": "black",
})

# Colour-blind-safe sequential palette (ColorBrewer "Blues"); never red/green.
PALETTE = {0: "#f2f2f2", 1: "#a6cee3", 2: "#08519c"}
EDGE = "0.40"


# --------------------------------------------------------------- helpers ----
def classify(cell):
    """Return (class, has_antibody_rows, has_antigen_rows).

    class 2 = laboratory-confirmed evidence
    class 1 = official report only (the section sign, assay not stated)
    class 0 = no evidence in this epoch (exposure/antigen rows only, or nothing)
    class None = the state has no cell at all for this epoch
    """
    if cell is None:
        return None, False, False
    ev = (cell.get("best_evidence") or "").strip()
    ab = bool(cell.get("antibody_marker_rows(\u2020)"))
    ag = bool(cell.get("antigen_marker_rows(\u2021)"))
    off = bool(cell.get("official_marker_rows(\u00a7)"))
    if ev in LAB_CONFIRMED:
        cls = 2
    elif ev in OFFICIAL_ONLY:
        cls = 1
    elif ev.startswith(NO_EVIDENCE_PREFIX) or ev == "":
        cls = 1 if off else 0
    else:
        raise SystemExit("unexpected best_evidence value: %r" % ev)
    return cls, ab, ag


def parts_of(geom):
    """Exterior rings of a Polygon or MultiPolygon geometry."""
    c = geom["coordinates"]
    rings = [c] if geom["type"] == "Polygon" else c
    return [np.asarray(r[0], dtype=float) for r in rings]


def area_centroid(ring):
    x, y = ring[:, 0], ring[:, 1]
    x1, y1 = np.roll(x, 1), np.roll(y, 1)
    cross = x * y1 - x1 * y
    a = cross.sum() / 2.0
    if abs(a) < 1e-12:
        return 0.0, (float(x.mean()), float(y.mean()))
    cx = float(((x + x1) * cross).sum() / (6.0 * a))
    cy = float(((y + y1) * cross).sum() / (6.0 * a))
    return abs(a), (cx, cy)


def label_point(geom):
    """Centroid of the largest ring - a stable label anchor."""
    rings = parts_of(geom)
    best = max(rings, key=lambda r: area_centroid(r)[0])
    return area_centroid(best)[1]


def add_geom(ax, geom, **kw):
    for ring in parts_of(geom):
        ax.add_patch(MplPolygon(ring, closed=True, **kw))


# ------------------------------------------------------------- validation ---
def validate(matrix, summary):
    """Compute per-epoch counts from the cells and check them three ways."""
    cls = {st: {p: classify(s.get("cells", {}).get(p))[0] for p in PANELS}
           for st, s in matrix.items()}
    marks = {st: {p: classify(s.get("cells", {}).get(p))[1:] for p in PANELS}
             for st, s in matrix.items()}

    conf = {p: sum(1 for st in matrix if cls[st][p] == 2) for p in PANELS}
    off = {p: sum(1 for st in matrix if cls[st][p] == 1) for p in PANELS}
    expo = {p: sum(1 for st in matrix if cls[st][p] == 0 and any(marks[st][p]))
            for p in PANELS}

    distinct = sorted({(c.get("best_evidence") or "").strip()
                       for s in matrix.values()
                       for c in s.get("cells", {}).values()})

    lines = ["=== validation table (computed from synthesis/t2.json) ===",
             "states/jurisdictions in matrix : %d" % len(matrix),
             "distinct best_evidence values  : %d" % len(distinct),
             "",
             "%-12s%9s%10s%11s%10s%12s  %s" % ("column", "lab-conf",
                                               "official", "expo-only",
                                               "expected", "t2 summary", "match")]
    ok = True
    for p in PANELS:
        exp = EXPECTED[p]
        upstream = summary.get(p, {}).get("n_states_confirmed")
        m = (conf[p] == exp) and (upstream == exp)
        ok &= m
        lines.append("%-12s%9d%10d%11d%10d%12s  %s"
                     % (p, conf[p], off[p], expo[p], exp, str(upstream),
                        "OK" if m else "MISMATCH"))
    lines += ["",
              "distinct best_evidence values found:",
              *["  - %s" % v for v in distinct]]
    return lines, {"cls": cls, "marks": marks, "conf": conf, "ok": ok}


# --------------------------------------------------- figure 3 range checks --
FIG3_REQUIRED = {
    "waves": list, "lull": dict, "clades": list, "onset": dict,
    "reassortment": dict, "turnover": dict, "first_detections": list,
    "wave_timing_rating": str,
}


def load_fig3_ranges(path):
    """Read and shape-check the curated figure 3 ranges.  Stop if unusable."""
    if not path.exists():
        raise SystemExit("STOP - %s is missing; figure 3 needs it." % path)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise SystemExit("STOP - %s is malformed: %s" % (path, exc))
    if not isinstance(data, dict):
        raise SystemExit("STOP - %s: top level must be an object." % path)
    for key, typ in FIG3_REQUIRED.items():
        if key not in data or not isinstance(data[key], typ):
            raise SystemExit("STOP - %s: key %r is missing or not %s"
                             % (path, key, typ.__name__))
    checks = [(w, "waves", ("label", "source")) for w in data["waves"]]
    checks += [(c, "clades", ("name", "rating", "source"))
               for c in data["clades"]]
    checks += [(data["lull"], "lull", ("label", "rating", "source"))]
    checks += [(data["onset"], "onset", ("rating", "source"))]
    checks += [(data["turnover"], "turnover", ("rating", "source"))]
    checks += [(data["reassortment"], "reassortment", ("rating", "source"))]
    checks += [(fd, "first_detections", ("subtype", "claim", "rating",
                                         "value_source"))
               for fd in data["first_detections"]]
    for entry, where, keys in checks:
        for k in keys:
            if k not in entry:
                raise SystemExit("STOP - %s: %s entry lacks %r" % (path, where, k))
        if where not in ("first_detections", "reassortment") and (
                "start" not in entry or "end" not in entry):
            raise SystemExit("STOP - %s: %s entry lacks start/end" % (path, where))
    for span in data["reassortment"]["spans"]:
        if "start" not in span or "end" not in span:
            raise SystemExit("STOP - %s: reassortment span lacks start/end" % path)
    return data


def range_lines(ranges):
    """One line per drawn range, each with the evidence it rests on."""
    def fmt(x0, x1):
        return "%.2f-%.2f" % (x0, x1)

    lines = ["=== figure 3 ranges (curated in fig3_ranges.json, with evidence) ===",
             "%-26s%16s  %-22s  %s"
             % ("element", "range drawn", "rating", "source")]
    for w in ranges["waves"]:
        lines.append("%-26s%16s  %-22s  %s"
                     % (w["label"], fmt(w["start"], w["end"]),
                        w["rating"], w["source"]))
    lull = ranges["lull"]
    lines.append("%-26s%16s  %-22s  %s"
                 % (lull["label"], fmt(lull["start"], lull["end"]),
                    lull["rating"], lull["source"]))
    for cl in ranges["clades"]:
        rng = fmt(cl["start"], cl["end"])
        if "continuation_to" in cl:
            rng += " (+ dashed to %.2f: %s)" % (cl["continuation_to"],
                                                 cl.get("continuation_label", ""))
        src = cl["source"]
        if cl.get("rows"):
            src += "; rows " + ", ".join(cl["rows"])
        lines.append("%-26s%16s  %-22s  %s"
                     % ("clade %s" % cl["name"], rng, cl["rating"], src))
    on = ranges["onset"]
    lines.append("%-26s%16s  %-22s  %s; rows %s"
                 % ("2.3.4.4 onset (dashed)", fmt(on["start"], on["end"]),
                    on["rating"], on["source"], ", ".join(on["rows"])))
    re_ = ranges["reassortment"]
    for sp in re_["spans"]:
        lines.append("%-26s%16s  %-22s  %s; rows %s"
                     % ("intra-clade reassortment", fmt(sp["start"], sp["end"]),
                        re_["rating"], re_["source"], ", ".join(re_["rows"])))
    tr = ranges["turnover"]
    lines.append("%-26s%16s  %-22s  %s"
                 % ("clade-level turnover", fmt(tr["start"], tr["end"]),
                    tr["rating"], tr["source"]))
    for fd in ranges["first_detections"]:
        extra = "" if fd["month_reported"] else "  <- %s" % fd.get("note", "")
        lines.append("%-26s%16s  %-22s  %s%s"
                     % ("first detection %s" % fd["subtype"], "from t1.json",
                        "%s (claim %s)" % (fd["rating"], fd["claim"]),
                        fd["value_source"], extra))
    return lines


def _sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


# --------------------------------------------------------------- figure 2 ---
def figure2(matrix, cls, marks, geoms, bounds):
    x0, x1, y0, y1 = bounds
    fig, axes = plt.subplots(2, 3, figsize=(FIG_W_MM * MM, 124 * MM))
    for ax, p in zip(axes.ravel(), PANELS):
        for st, geom in geoms.items():
            k = cls.get(st, {}).get(p)
            k = 0 if k is None else k          # absent state = no evidence
            add_geom(ax, geom, facecolor=PALETTE[k], edgecolor=EDGE,
                     linewidth=0.12, zorder=1)
            ab, ag = marks.get(st, {}).get(p, (False, False))
            if k < 2 and (ab or ag):
                add_geom(ax, geom, facecolor="none", edgecolor="0.30",
                         hatch="..." if ag else "///", linewidth=0.12, zorder=2)
        for st, geom in geoms.items():
            x, y = label_point(geom)
            # White code on the dark class-2 fill (black would be only ~2.7:1);
            # dark code on the light classes 0 and 1.
            k = cls.get(st, {}).get(p)
            k = 0 if k is None else k
            ax.text(x, y, STATE_CODE.get(st, st[:2].upper()), ha="center",
                    va="center", fontsize=3.0,
                    color="white" if k == 2 else "0.10", zorder=3)
        n = sum(1 for st in matrix if cls[st][p] == 2)
        ax.set_title("%s  %s   (n = %d)" % (p, EPOCH_RANGE.get(p, "").strip(), n),
                     fontsize=5.8, pad=2.0)
        ax.set_xlim(x0, x1)
        ax.set_ylim(y0, y1)
        ax.set_aspect("equal", adjustable="box")
        ax.set_xticks([])
        ax.set_yticks([])
        for s in ax.spines.values():
            s.set_visible(False)

    handles = [
        Patch(facecolor=PALETTE[2], edgecolor=EDGE,
              label="Laboratory-confirmed evidence (sequence, isolate, RNA or "
                    "lab-confirmed case, method not reported)"),
        Patch(facecolor=PALETTE[1], edgecolor=EDGE,
              label="Official report only (\u00a7; assay not stated, not counted "
                    "as confirmation)"),
        Patch(facecolor=PALETTE[0], edgecolor=EDGE,
              label="No evidence in this epoch"),
        Patch(facecolor="white", edgecolor="0.30", hatch="///",
              label="No laboratory-confirmed evidence, but marker rows present "
                    "(\u2020 antibody or \u2021 antigen; not infection)"),
    ]
    fig.legend(handles=handles, loc="lower center", ncol=2, frameon=False,
               fontsize=5.2, bbox_to_anchor=(0.5, 0.058),
               handlelength=1.4, handleheight=0.9, labelspacing=0.4,
               columnspacing=1.4)
    fig.text(0.5, 0.008,
             "Panel counts are states (plus the Federal Capital Territory) with "
             "laboratory-confirmed evidence in that epoch.\n"
             "Rows that cannot be placed in one epoch are shown as 'multi-epoch'; "
             "rows with no stated date as 'date NR'. Codes are two-letter state "
             "abbreviations.",
             ha="center", va="bottom", fontsize=5.0, linespacing=1.25)
    fig.subplots_adjust(left=0.010, right=0.990, top=0.955, bottom=0.175,
                        wspace=0.01, hspace=0.02)
    for ext in ("pdf", "png"):
        fig.savefig(OUT / ("fig2_states_epochs.%s" % ext))
    plt.close(fig)


# --------------------------------------------------------------- figure 3 ---
def figure3(firsts, ranges):
    # ---- every range drawn is read from fig3_ranges.json (validated in main);
    # no range or date literal is typed here.
    waves = ranges["waves"]
    lull = ranges["lull"]
    clades = ranges["clades"]
    onset = ranges["onset"]
    reassort = ranges["reassortment"]["spans"]
    turnover = ranges["turnover"]

    fig, ax = plt.subplots(figsize=(FIG_W_MM * MM, 92 * MM))
    fig.subplots_adjust(left=0.045, right=0.995, top=0.985, bottom=0.250)
    ymax = 4.55

    # (a) the two epizootic waves and (b) the lull, as background bands
    for i, w in enumerate(waves):
        x0, x1 = w["start"], w["end"]
        ax.axvspan(x0, x1, 0, 1, facecolor="0.90", hatch="///", alpha=0.85,
                   edgecolor="0.72", linewidth=0.0, zorder=0,
                   label="Epizootic wave (existence b1, Low; timing b2, %s)"
                   % ranges["wave_timing_rating"] if i == 0 else None)
        ax.text((x0 + x1) / 2, ymax - 0.02, w["label"], ha="center", va="top",
                fontsize=4.2, color="0.30")
    ax.axvspan(lull["start"], lull["end"], 0, 1, facecolor="0.985",
               hatch="\\\\\\\\\\", alpha=1.0, edgecolor="0.87", linewidth=0.0,
               zorder=0, label="%s, %s to Nov 2014 (b2, %s)"
               % (lull["label"], int(lull["start"]), lull["rating"]))
    ax.text((lull["start"] + lull["end"]) / 2, ymax - 0.02, lull["label"],
            ha="center", va="top", fontsize=4.2, color="0.40")

    # (c) clade bands.  Each bar is solid over the interval the evidence
    # supports; where the source records no later evidence, a lighter dashed
    # continuation carries the bar to the end of the claim window.
    for j, cl in enumerate(clades):
        y = 2.42 - j * 0.42
        x0, x1 = cl["start"], cl["end"]
        cont = cl.get("continuation_to")
        ax.barh(y, x1 - x0, left=x0, height=0.28, facecolor=PALETTE[2],
                edgecolor="white", linewidth=0.4, zorder=3)
        lab = "clade %s  (%s)" % (cl["name"], cl["rating"])
        if x1 - x0 > 4.5:                       # label fits inside the bar
            ax.text(x0 + 0.20, y, lab, va="center", ha="left", fontsize=4.4,
                    color="white", zorder=4)
        elif cont is not None:                  # narrow bar with a continuation:
            ax.text((x0 + x1) / 2.0, y + 0.20, lab, va="bottom", ha="center",
                    fontsize=4.4, color="0.15", zorder=4)   # above it, clear
        else:                                   # place to the right
            ax.text(x1 + 0.15, y, lab, va="center", ha="left", fontsize=4.4)
        if cont is not None:
            ax.barh(y, cont - x1, left=x1, height=0.28, facecolor="#dbe9f6",
                    edgecolor=PALETTE[2], linewidth=0.4,
                    linestyle=(0, (1.6, 1.2)), zorder=3)
            ax.text((x1 + cont) / 2.0, y - 0.22, cl["continuation_label"],
                    va="top", ha="center", fontsize=3.6, color="0.45", zorder=4)
    # (j2) the 2.3.4.4 onset is a separate, Very low claim - shown broken
    y_onset = 2.42 - 2 * 0.42
    ax.barh(y_onset, onset["end"] - onset["start"], left=onset["start"],
            height=0.28, facecolor="white", edgecolor=PALETTE[2], linewidth=0.5,
            linestyle=(0, (1.6, 1.4)), zorder=3)
    ax.text(onset["start"] - 0.15, y_onset,
            "onset %d (%s)" % (int(onset["start"]), onset["rating"]),
            va="center", ha="right", fontsize=4.0, color="0.25", zorder=4)

    # (c) clade-level turnover
    ax.annotate("", xy=(turnover["end"], 4.14), xytext=(turnover["start"], 4.14),
                arrowprops=dict(arrowstyle="-|>", lw=0.6, color="0.35",
                                shrinkA=0, shrinkB=0), zorder=4)
    ax.text((turnover["start"] + turnover["end"]) / 2.0, 4.22,
            "Clade-level turnover: 2.2 \u2192 2.3.2.1c \u2192 2.3.4.4b  (%s)"
            % turnover["rating"], ha="center", va="bottom", fontsize=4.6)

    # (c) intra-clade reassortment
    for sp in reassort:
        ax.barh(0.95, sp["end"] - sp["start"], left=sp["start"], height=0.20,
                facecolor="#6baed6", edgecolor="white", linewidth=0.4, zorder=3)
    # label anchored in the gap between the two spans (derived, not typed)
    gap = (reassort[0]["end"] + reassort[1]["start"]) / 2.0
    ax.text(gap, 0.95, "intra-clade reassortment  (%s)"
            % ranges["reassortment"]["rating"], va="center",
            ha="center", fontsize=4.0, color="0.25")

    # (d) first-detection markers
    for sub, x, claim, rating, month_rep in firsts:
        solid = rating == "Low"
        ax.plot([x, x], [0.42, 2.90], color="0.30", lw=0.55,
                ls="-" if solid else (0, (2.0, 1.6)), zorder=2.5)
        ax.plot([x], [2.90], marker="v", ms=3.4,
                mfc=PALETTE[2] if solid else "white", mec=PALETTE[2],
                mew=0.7, zorder=6, clip_on=False)
        cfg = FIRST_LABEL[sub]
        lab = "%s %d (%s%s)" % (sub, int(np.floor(x)), rating,
                                "" if month_rep else ", month not reported")
        ax.text(x + cfg["dx"], cfg["y"], lab,
                ha=cfg["ha"], va="center", fontsize=4.0, color="0.15", zorder=6)

    ax.set_xlim(2005.7, 2026.7)
    ax.set_ylim(0.25, ymax)
    ax.set_yticks([])
    ax.set_xticks(range(2006, 2027, 2))
    ax.set_xticklabels([str(y) for y in range(2006, 2027, 2)], fontsize=5.0)
    ax.tick_params(axis="x", length=2.0, pad=1.5)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.set_xlabel("Year", fontsize=5.4, labelpad=1.5)
    ax.grid(axis="x", color="0.93", lw=0.4, zorder=-1)
    ax.set_axisbelow(True)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.135), ncol=2,
              frameon=False, fontsize=5.0, handlelength=1.6, handleheight=0.9,
              columnspacing=1.6)
    for ext in ("pdf", "png"):
        fig.savefig(OUT / ("fig3_timeline.%s" % ext))
    plt.close(fig)


# ------------------------------------------------------------------ main ----
def main():
    t2 = json.loads((SYN / "t2.json").read_text(encoding="utf-8"))
    t1 = json.loads((SYN / "t1.json").read_text(encoding="utf-8"))
    ranges = load_fig3_ranges(FIG3_RANGES)
    matrix = t2["matrix"]

    # (1) per-epoch count guard, recomputed from the cells
    lines, v = validate(matrix, t2.get("summary_per_column", {}))
    # (2) figure 3 ranges, each printed with the evidence it rests on
    lines += [""] + range_lines(ranges)
    if not v["ok"]:
        print("\n".join(lines))
        raise SystemExit(
            "STOP - computed per-epoch counts do not match the verified T2 counts "
            "(see table above).  No figure was drawn and validation_table.txt "
            "was not written."
        )

    # first detections, t1.json -> decimal year (month mid-point when stated).
    # The claim id, rating and month-reported flag come from fig3_ranges.json,
    # and the flag is checked against t1.json before the value is used.
    firsts = []
    by_sub = {fd["subtype"]: fd for fd in ranges["first_detections"]}
    for sub in ("H5N1", "H5N8", "H5N6", "H9N2"):
        meta = by_sub[sub]
        node = t1["subtype"][sub]["earliest"]
        y, m = node["start_ym"]
        if bool(meta["month_reported"]) != (m is not None):
            raise SystemExit(
                "STOP - fig3_ranges.json says month_reported=%s for %s, but "
                "t1.json start_ym is %s" % (meta["month_reported"], sub,
                                            node["start_ym"])
            )
        x = float(y) if m is None else y + (m - 0.5) / 12.0
        firsts.append((sub, x, meta["claim"], meta["rating"],
                       meta["month_reported"]))
        print("[first detection] %-5s %-70s -> x=%.3f (claim %s, %s)"
              % (sub, node["date"], x, meta["claim"], meta["rating"]))

    # provenance-stamped validation table, written only now that every guard
    # above has passed (build date + sha256 of each input)
    stamp = ["", "=== build provenance ===",
             "build date (UTC)   : %s"
             % datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
             "build script       : build_figures.py"]
    for name in INPUTS_MANIFEST:
        path = FIG3_RANGES if name == "fig3_ranges.json" else SYN / name
        stamp.append("sha256 %-16s: %s" % (name, _sha256(path)))
    stamp.append("guards: per-epoch counts OK; fig3_ranges.json shape OK")
    table = "\n".join(lines + stamp)
    print(table)
    (OUT / "validation_table.txt").write_text(table + "\n", encoding="utf-8")

    # geography
    if not GEOJSON.exists():
        print("[geo] downloading %s" % GEOJSON_URL)
        urllib.request.urlretrieve(GEOJSON_URL, GEOJSON)
    geo = json.loads(GEOJSON.read_text(encoding="utf-8"))
    geoms = {}
    for f in geo["features"]:
        nm = f["properties"]["shapeName"]
        geoms[GEO_ALIAS.get(nm, nm)] = f["geometry"]
    unnamed = [s for s in matrix if s not in geoms]
    print("[geo] ADM1 features: %d | matrix states without geometry: %s"
          % (len(geoms), unnamed))
    if unnamed:
        raise SystemExit("STOP - no geometry for: %s" % unnamed)

    pts = np.vstack([p for g in geoms.values() for p in parts_of(g)])
    bx0, bx1 = float(pts[:, 0].min()), float(pts[:, 0].max())
    by0, by1 = float(pts[:, 1].min()), float(pts[:, 1].max())
    px, py = 0.015 * (bx1 - bx0), 0.015 * (by1 - by0)
    bounds = (bx0 - px, bx1 + px, by0 - py, by1 + py)
    print("[geo] extent lon %.3f..%.3f  lat %.3f..%.3f" % (bx0, bx1, by0, by1))

    figure2(matrix, v["cls"], v["marks"], geoms, bounds)
    figure3(firsts, ranges)
    print("[done] wrote fig2_states_epochs.{pdf,png} and fig3_timeline.{pdf,png}")


if __name__ == "__main__":
    main()
