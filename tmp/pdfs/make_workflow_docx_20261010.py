# -*- coding: utf-8 -*-
"""Build the Word (.docx) versions of the workflow completion record.

Single source of truth: tmp/pdfs/create_workflow_status_20261010.py (the PDF
generator). This script imports that module, calls its make_story() twice
(clean, then with the AI-token highlight flag on), walks the resulting
reportlab flowables, and emits WordprocessingML. No text is retyped, so the
Word files cannot drift from the PDF content.

Outputs:
  output/docx/AvianInfluenzaSysRev_Workflow_Completion_Record_20261010.docx
  output/docx/AvianInfluenzaSysRev_Workflow_Completion_Record_AI_highlighted_20261010.docx

Run:  python -X utf8 make_workflow_docx_20261010.py
"""
import datetime
import importlib.util
import os
import re
import zipfile
from xml.sax.saxutils import escape

SRC = r"D:\AvianInfluenzaSysRev\tmp\pdfs\create_workflow_status_20261010.py"
OUTDIR = r"D:\AvianInfluenzaSysRev\output\docx"
OUT_CLEAN = os.path.join(OUTDIR, "AvianInfluenzaSysRev_Workflow_Completion_Record_20261010.docx")
OUT_HL = os.path.join(OUTDIR, "AvianInfluenzaSysRev_Workflow_Completion_Record_AI_highlighted_20261010.docx")

W_NS = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'
R_NS = 'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"'

# landscape A4, content width in twips
CONTENT_W_TW = 15250
GRID_HEX = "C6D0D9"
HL_TAG = '<w:highlight w:val="yellow"/>'

TAG_RE = re.compile(r"(<[^>]+>|&#[0-9]+;|&#x[0-9A-Fa-f]+;|&amp;|&lt;|&gt;|&quot;|&apos;)")
ENT_RE = re.compile(r"&#(\d+);|&#x([0-9A-Fa-f]+);|&(amp|lt|gt|quot|apos);")


def unescape_entities(s):
    def f(m):
        if m.group(1):
            return chr(int(m.group(1)))
        if m.group(2):
            return chr(int(m.group(2), 16))
        return {"amp": "&", "lt": "<", "gt": ">", "quot": '"', "apos": "'"}[m.group(3)]
    return ENT_RE.sub(f, s)


def colhex(c):
    try:
        return "#%02X%02X%02X" % (round(c.red * 255), round(c.green * 255), round(c.blue * 255))
    except Exception:
        return None


def luma(hexstr):
    try:
        h = hexstr.lstrip("#")
        r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
        return (0.299 * r + 0.587 * g + 0.114 * b) / 255.0
    except Exception:
        return 1.0


def parse_markup(text):
    """reportlab Paragraph markup -> [(text, fmt)] with fmt bold/italic/color/hl."""
    segs = []
    state = {"bold": False, "italic": False, "color": None, "hl": False}
    stack = []
    for tok in TAG_RE.split(str(text)):
        if not tok:
            continue
        if tok.startswith("<"):
            low = tok.lower()
            if low == "<b>":
                state["bold"] = True
            elif low == "</b>":
                state["bold"] = False
            elif low == "<i>":
                state["italic"] = True
            elif low == "</i>":
                state["italic"] = False
            elif low.startswith("<br"):
                segs.append(("\n", dict(state)))
            elif low.startswith("<font"):
                stack.append(dict(state))
                m = re.search(r'backcolor="([^"]+)"', low)
                if m:
                    state["hl"] = True
                m2 = re.search(r'(?<![a-zA-Z])color="([^"]+)"', low)
                if m2:
                    state["color"] = m2.group(1).lstrip("#")
            elif low.startswith("</font"):
                if stack:
                    state = stack.pop()
            # any other tag: ignore, keep text clean
        else:
            segs.append((unescape_entities(tok), dict(state)))
    return segs


def emit_runs(segs, font="Arial", size=None, bold=False, italic=False, color=None):
    out = []
    for text, fmt in segs:
        if text == "\n":
            out.append('<w:r><w:br/></w:r>')
            continue
        if not text:
            continue
        b = fmt["bold"] or bold
        i = fmt["italic"] or italic
        col = fmt["color"] or color
        if col:
            col = col.lstrip("#")
        rpr = ['<w:rFonts w:ascii="%s" w:hAnsi="%s" w:cs="%s"/>' % (font, font, font)]
        if b:
            rpr.append("<w:b/>")
        if i:
            rpr.append("<w:i/>")
        if col:
            rpr.append('<w:color w:val="%s"/>' % col)
        if fmt["hl"]:
            rpr.append(HL_TAG)
        if size:
            rpr.append('<w:sz w:val="%d"/><w:szCs w:val="%d"/>' % (size, size))
        out.append('<w:r><w:rPr>%s</w:rPr><w:t xml:space="preserve">%s</w:t></w:r>'
                   % ("".join(rpr), escape(text)))
    return "".join(out)


def emit_para(p, keep=False):
    st = p.style
    name = (st.name or "")
    size = max(2, round((st.fontSize or 9) * 2))
    fontname = st.fontName or "Helvetica"
    bold = "Bold" in fontname
    italic = ("Italic" in fontname) or ("Oblique" in fontname)
    color = colhex(st.textColor) if getattr(st, "textColor", None) else None
    align = getattr(st, "alignment", 0)
    jc = {1: "center", 2: "right", 4: "both"}.get(align)
    before = int(round((st.spaceBefore or 0) * 20))
    after = int(round((st.spaceAfter or 0) * 20))
    leading = getattr(st, "leading", None)
    fs = st.fontSize or 9
    ppr = []
    if keep or name in ("Section", "Subsection", "Stamp"):
        ppr.insert(0, "<w:keepNext/>")
    if before or after or leading:
        attrs = ' w:before="%d" w:after="%d"' % (before, after)
        if leading and 1.02 <= (leading / fs) <= 1.6:
            attrs += ' w:line="%d" w:lineRule="exact"' % int(round(leading * 20))
        ppr.append("<w:spacing%s/>" % attrs)
    if jc:
        ppr.append('<w:jc w:val="%s"/>' % jc)
    segs = parse_markup(p.text)
    body = emit_runs(segs, size=size, bold=bold, italic=italic, color=color)
    if not body:
        body = '<w:r><w:rPr><w:sz w:val="%d"/></w:rPr></w:r>' % min(size, 18)
    return "<w:p><w:pPr>%s</w:pPr>%s</w:p>" % ("".join(ppr), body)


def spacer_para(height_pt):
    tw = max(60, int(round(height_pt * 20)))
    return ('<w:p><w:pPr><w:spacing w:before="0" w:after="0" w:line="%d" w:lineRule="exact"/>'
            '</w:pPr></w:p>' % tw)


def hr_para(item):
    color = colhex(getattr(item, "color", None)) or GRID_HEX
    lw = getattr(item, "lineWidth", 1) or 1
    sz = max(2, int(round(lw * 8)))
    before = int(round((getattr(item, "spaceBefore", 0) or 0) * 20))
    after = int(round((getattr(item, "spaceAfter", 0) or 0) * 20))
    return ('<w:p><w:pPr>'
            '<w:pBdr><w:bottom w:val="single" w:sz="%d" w:space="1" w:color="%s"/></w:pBdr>'
            '<w:spacing w:before="%d" w:after="%d"/>'
            '</w:pPr></w:p>' % (sz, color.lstrip("#"), before, after))


def page_break_para():
    return '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'


def expand(coord, nrows, ncols):
    c, r = coord
    if c == -1:
        c = ncols - 1
    if r == -1:
        r = nrows - 1
    return c, r


def emit_cell_content(obj):
    if obj is None:
        obj = ""
    if hasattr(obj, "_cellvalues"):          # nested Table
        return emit_table(obj)
    if hasattr(obj, "text") and hasattr(obj, "style"):   # Paragraph
        return emit_para(obj)
    # plain string
    t = unescape_entities(str(obj))
    if not t:
        return '<w:p><w:pPr><w:spacing w:after="0"/></w:pPr></w:p>'
    return ('<w:p><w:pPr><w:spacing w:after="0"/></w:pPr>'
            '<w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:sz w:val="14"/>'
            '<w:szCs w:val="14"/></w:rPr><w:t xml:space="preserve">%s</w:t></w:r></w:p>'
            % escape(t))


def maybe_flatten(tbl):
    """Detect the 'container of nested tables' pattern (cards row, bands) and
    return a flattened single-level description, or None if not applicable.
    Nested tables render unreliably in Word/LibreOffice, so containers are
    turned into one plain table with per-cell borders and shading."""
    cvs = tbl._cellvalues
    if len(cvs) != 1:
        return None
    row = cvs[0]
    if not any(hasattr(c, "_cellvalues") for c in row):
        return None
    col_data = []
    for c in row:
        if hasattr(c, "_cellvalues"):
            inner = c._cellvalues
            icols = max(len(r) for r in inner) if inner else 0
            if icols != 1:
                return None
            cells = [(r[0] if r else None) for r in inner]
            lines = list(getattr(c, "_linecmds", []) or [])
            bgs = list(getattr(c, "_bkgrndcmds", []) or [])
            col_data.append({"cells": cells, "lines": lines, "bgs": bgs})
        else:
            col_data.append({"cells": [c], "lines": [], "bgs": []})
    R = max(len(d["cells"]) for d in col_data)
    widths = list(getattr(tbl, "_colWidths", []) or [])
    if len(widths) < len(col_data):
        widths += [None] * (len(col_data) - len(widths))
    ncols = len(col_data)

    fills, borders = {}, {}

    def mark_borders(lines, ci, nrows, only_col=None):
        for entry in lines:
            tag = entry[0]
            (c1, r1), (c2, r2) = entry[1], entry[2]
            hx = colhex(entry[3]) if len(entry) > 3 and entry[3] is not None else GRID_HEX
            if not hx:
                hx = GRID_HEX
            hx = hx.lstrip("#")
            r1o = 0 if r1 < 0 else r1
            r2o = nrows - 1 if r2 < 0 else r2
            for r in range(max(0, r1o), min(nrows - 1, r2o) + 1):
                d = borders.setdefault((r, ci), {})
                if tag in ("BOX", "GRID", "INNERGRID"):
                    if r == r1o:
                        d["top"] = hx
                    if r == r2o:
                        d["bottom"] = hx
                    d["left"] = hx
                    d["right"] = hx
                elif tag == "LINEABOVE" and r == r1o:
                    d["top"] = hx
                elif tag == "LINEBELOW" and r == r2o:
                    d["bottom"] = hx

    for ci, d in enumerate(col_data):
        nrows = len(d["cells"])
        for entry in d["bgs"]:
            if entry and entry[0] == "BACKGROUND":
                (cc1, r1), (cc2, r2) = entry[1], entry[2]
                r1o = 0 if r1 < 0 else r1
                r2o = nrows - 1 if r2 < 0 else r2
                hx = colhex(entry[3])
                for r in range(r1o, r2o + 1):
                    fills[(r, ci)] = hx
        mark_borders(d["lines"], ci, nrows)

    outer_bgs = list(getattr(tbl, "_bkgrndcmds", []) or [])
    for entry in outer_bgs:
        if entry and entry[0] == "BACKGROUND":
            (c1, r1), (c2, r2) = entry[1], entry[2]
            c1o = 0 if c1 < 0 else c1
            c2o = ncols - 1 if c2 < 0 else c2
            r1o = 0 if r1 < 0 else r1
            r2o = R - 1 if r2 < 0 else min(r2, R - 1)
            hx = colhex(entry[3])
            for r in range(r1o, r2o + 1):
                for ci in range(c1o, c2o + 1):
                    fills[(r, ci)] = hx

    outer_lines = list(getattr(tbl, "_linecmds", []) or [])
    for entry in outer_lines:
        tag = entry[0]
        (c1, r1), (c2, r2) = entry[1], entry[2]
        hx = colhex(entry[3]) if len(entry) > 3 and entry[3] is not None else GRID_HEX
        if not hx:
            hx = GRID_HEX
        hx = hx.lstrip("#")
        c1o = 0 if c1 < 0 else c1
        c2o = ncols - 1 if c2 < 0 else c2
        for ci in range(c1o, min(c2o, ncols - 1) + 1):
            d = borders.setdefault((0, ci), {})
            if tag in ("BOX", "GRID", "INNERGRID"):
                d["top"] = hx
                d["bottom"] = hx
                if ci == c1o:
                    d["left"] = hx
                if ci == c2o:
                    d["right"] = hx
            elif tag == "LINEABOVE":
                d["top"] = hx
            elif tag == "LINEBELOW":
                d["bottom"] = hx

    return {"cols": col_data, "R": R, "widths": widths, "fills": fills, "borders": borders}


def emit_flat_table(flat):
    col_data, R, widths = flat["cols"], flat["R"], flat["widths"]
    ncols = len(col_data)
    widths_tw = [max(80, int(round(w * 20))) if w else 3000 for w in widths]
    rows_xml = []
    for r in range(R):
        cells_xml = []
        for ci in range(ncols):
            content = col_data[ci]["cells"][r] if r < len(col_data[ci]["cells"]) else ""
            bd = flat["borders"].get((r, ci), {})
            tcb = []
            for side in ("top", "left", "bottom", "right"):
                if side in bd:
                    tcb.append('<w:%s w:val="single" w:sz="4" w:space="0" w:color="%s"/>' % (side, bd[side]))
                else:
                    tcb.append('<w:%s w:val="nil"/>' % side)
            tcpr = ['<w:tcW w:w="%d" w:type="dxa"/>' % widths_tw[ci],
                    '<w:tcBorders>%s</w:tcBorders>' % "".join(tcb)]
            fill = flat["fills"].get((r, ci))
            if fill:
                tcpr.append('<w:shd w:val="clear" w:color="auto" w:fill="%s"/>' % fill.lstrip("#"))
            tcpr.append('<w:vAlign w:val="top"/>')
            cells_xml.append('<w:tc><w:tcPr>%s</w:tcPr>%s</w:tc>'
                             % ("".join(tcpr), emit_cell_content(content)))
        rows_xml.append("<w:tr>%s</w:tr>" % "".join(cells_xml))
    total_tw = sum(widths_tw)
    tblpr = ('<w:tblPr><w:tblW w:w="%d" w:type="dxa"/>'
             '<w:tblLayout w:type="fixed"/>'
             '<w:tblCellMar><w:top w:w="40" w:type="dxa"/><w:left w:w="60" w:type="dxa"/>'
             '<w:bottom w:w="40" w:type="dxa"/><w:right w:w="60" w:type="dxa"/></w:tblCellMar>'
             '</w:tblPr>' % total_tw)
    grid = "".join('<w:gridCol w:w="%d"/>' % w for w in widths_tw)
    return "<w:tbl>%s<w:tblGrid>%s</w:tblGrid>%s</w:tbl>" % (tblpr, grid, "".join(rows_xml))


def emit_table(tbl):
    flat = maybe_flatten(tbl)
    if flat is not None:
        return emit_flat_table(flat)
    cvs = tbl._cellvalues
    nrows = len(cvs)
    ncols = max(len(r) for r in cvs) if nrows else 0
    widths = list(getattr(tbl, "_colWidths", []) or [])
    if len(widths) < ncols:
        widths += [None] * (ncols - len(widths))
    known = sum(w for w in widths if w)
    missing = [i for i, w in enumerate(widths) if not w]
    if missing:
        fill = (762.52 - known) / len(missing)   # content width in pt
        for i in missing:
            widths[i] = fill
    widths_tw = [max(80, int(round(w * 20))) for w in widths]

    # backgrounds
    bg = {}
    for entry in getattr(tbl, "_bkgrndcmds", []) or []:
        if entry and entry[0] == "BACKGROUND":
            c1, r1 = expand(entry[1], nrows, ncols)
            c2, r2 = expand(entry[2], nrows, ncols)
            hx = colhex(entry[3])
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    bg[(r, c)] = hx

    # spans
    span_at, covered = {}, set()
    for entry in getattr(tbl, "_spanCmds", []) or []:
        if entry and entry[0] == "SPAN":
            c1, r1 = expand(entry[1], nrows, ncols)
            c2, r2 = expand(entry[2], nrows, ncols)
            span_at[(r1, c1)] = (r2 - r1 + 1, c2 - c1 + 1)
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    if (r, c) != (r1, c1):
                        covered.add((r, c))

    header_row = bool(bg.get((0, 0))) and luma(bg.get((0, 0))) < 0.5 and nrows > 1

    rows_xml = []
    for r in range(nrows):
        trpr = ""
        if r == 0 and header_row:
            trpr = "<w:trPr><w:tblHeader/></w:trPr>"
        cells_xml = []
        c = 0
        while c < len(cvs[r]):
            if (r, c) in covered:
                c += 1
                continue
            rs, cs = span_at.get((r, c), (1, 1))
            wtw = sum(widths_tw[c:c + cs]) if c + cs <= len(widths_tw) else widths_tw[c]
            tcpr = ['<w:tcW w:w="%d" w:type="dxa"/>' % wtw]
            if cs > 1:
                tcpr.append('<w:gridSpan w:val="%d"/>' % cs)
            if rs > 1:
                tcpr.append('<w:vMerge w:val="restart"/>')
            elif (r - 1, c) in span_at and span_at[(r - 1, c)][0] > 1:
                tcpr.append('<w:vMerge/>')
            fill = bg.get((r, c))
            if fill:
                tcpr.append('<w:shd w:val="clear" w:color="auto" w:fill="%s"/>' % fill.lstrip("#"))
            tcpr.append('<w:vAlign w:val="top"/>')
            content = cvs[r][c] if c < len(cvs[r]) else ""
            cells_xml.append('<w:tc><w:tcPr>%s</w:tcPr>%s</w:tc>' % ("".join(tcpr), emit_cell_content(content)))
            c += cs
        rows_xml.append("<w:tr>%s%s</w:tr>" % (trpr, "".join(cells_xml)))

    total_tw = sum(widths_tw)
    borders = "".join(
        '<w:%s w:val="single" w:sz="4" w:space="0" w:color="%s"/>' % (side, GRID_HEX)
        for side in ("top", "left", "bottom", "right", "insideH", "insideV"))
    tblpr = ('<w:tblPr><w:tblW w:w="%d" w:type="dxa"/>'
             '<w:tblBorders>%s</w:tblBorders>'
             '<w:tblLayout w:type="fixed"/>'
             '<w:tblCellMar><w:top w:w="40" w:type="dxa"/><w:left w:w="80" w:type="dxa"/>'
             '<w:bottom w:w="40" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tblCellMar>'
             '</w:tblPr>' % (total_tw, borders))
    grid = "".join('<w:gridCol w:w="%d"/>' % w for w in widths_tw)
    return "<w:tbl>%s<w:tblGrid>%s</w:tblGrid>%s</w:tbl>" % (tblpr, grid, "".join(rows_xml))


def iter_paragraphs(story):
    for item in story:
        cls = item.__class__.__name__
        if cls == "Paragraph":
            yield item
        elif cls == "Table":
            for row in item._cellvalues:
                for cell in row:
                    if hasattr(cell, "_cellvalues"):
                        yield from iter_paragraphs([cell])
                    elif hasattr(cell, "text") and hasattr(cell, "style"):
                        yield cell


def walk(story):
    out = []
    for item in story:
        cls = item.__class__.__name__
        if cls == "Paragraph":
            out.append(emit_para(item))
        elif cls == "Table":
            out.append(emit_table(item))
            out.append(spacer_para(6))
        elif cls == "Spacer":
            h = getattr(item, "height", 0) or 0
            if h * 20 >= 60:
                out.append(spacer_para(h))
        elif cls == "PageBreak":
            out.append(page_break_para())
        elif cls == "HRFlowable":
            out.append(hr_para(item))
        else:
            # unknown flowable; note it for the run report
            out.append('<!-- skipped flowable: %s -->' % cls)
    return "".join(out)


def header_xml():
    right_tab = CONTENT_W_TW
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            '<w:hdr %s %s><w:p><w:pPr>'
            '<w:pBdr><w:bottom w:val="single" w:sz="4" w:space="2" w:color="%s"/></w:pBdr>'
            '<w:tabs><w:tab w:val="right" w:pos="%d"/></w:tabs>'
            '<w:spacing w:after="0"/></w:pPr>'
            '<w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/><w:b/>'
            '<w:color w:val="17324D"/><w:sz w:val="14"/><w:szCs w:val="14"/></w:rPr>'
            '<w:t xml:space="preserve">NIGERIA AVIAN INFLUENZA SYSTEMATIC REVIEW</w:t></w:r>'
            '<w:r><w:rPr><w:sz w:val="14"/></w:rPr><w:tab/></w:r>'
            '<w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/>'
            '<w:color w:val="52606D"/><w:sz w:val="14"/><w:szCs w:val="14"/></w:rPr>'
            '<w:t xml:space="preserve">WORKFLOW STATUS AND COMPLETION RECORD</w:t></w:r>'
            '</w:p></w:hdr>' % (W_NS, R_NS, GRID_HEX, right_tab))


def footer_xml():
    right_tab = CONTENT_W_TW
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            '<w:ftr %s %s><w:p><w:pPr>'
            '<w:pBdr><w:top w:val="single" w:sz="4" w:space="2" w:color="%s"/></w:pBdr>'
            '<w:tabs><w:tab w:val="right" w:pos="%d"/></w:tabs>'
            '<w:spacing w:after="0"/></w:pPr>'
            '<w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/>'
            '<w:color w:val="52606D"/><w:sz w:val="14"/><w:szCs w:val="14"/></w:rPr>'
            '<w:t xml:space="preserve">Current operational record: 10 October 2026</w:t></w:r>'
            '<w:r><w:rPr><w:sz w:val="14"/></w:rPr><w:tab/></w:r>'
            '<w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/>'
            '<w:color w:val="52606D"/><w:sz w:val="14"/><w:szCs w:val="14"/></w:rPr>'
            '<w:t xml:space="preserve">Page </w:t></w:r>'
            '<w:r><w:fldChar w:fldCharType="begin"/></w:r>'
            '<w:r><w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>'
            '<w:r><w:fldChar w:fldCharType="separate"/></w:r>'
            '<w:r><w:t>1</w:t></w:r>'
            '<w:r><w:fldChar w:fldCharType="end"/></w:r>'
            '</w:p></w:ftr>' % (W_NS, R_NS, GRID_HEX, right_tab))


def styles_xml():
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            '<w:styles %s><w:docDefaults><w:rPrDefault><w:rPr>'
            '<w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/>'
            '<w:sz w:val="18"/><w:szCs w:val="18"/><w:lang w:val="en-GB"/>'
            '</w:rPr></w:rPrDefault><w:pPrDefault><w:pPr/></w:pPrDefault></w:docDefaults>'
            '<w:style w:type="paragraph" w:default="1" w:styleId="Normal">'
            '<w:name w:val="Normal"/><w:qFormat/></w:style></w:styles>' % W_NS)


def core_xml(title):
    now = "2026-10-10T00:00:00Z"
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            '<cp:coreProperties '
            'xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
            'xmlns:dc="http://purl.org/dc/elements/1.1/" '
            'xmlns:dcterms="http://purl.org/dc/terms/" '
            'xmlns:dcmitype="http://purl.org/dc/dcmitype/" '
            'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
            '<dc:title>%s</dc:title>'
            '<dc:creator>Nigeria Avian Influenza Systematic Review</dc:creator>'
            '<cp:lastModifiedBy>Nigeria Avian Influenza Systematic Review</cp:lastModifiedBy>'
            '<dcterms:created xsi:type="dcterms:W3CDTF">%s</dcterms:created>'
            '<dcterms:modified xsi:type="dcterms:W3CDTF">%s</dcterms:modified>'
            '</cp:coreProperties>' % (escape(title), now, now))


def app_xml():
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            '<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" '
            'xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">'
            '<Application>Microsoft Office Word</Application>'
            '<AppVersion>16.0000</AppVersion></Properties>')


def content_types_xml():
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
            '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
            '<Default Extension="xml" ContentType="application/xml"/>'
            '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
            '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
            '<Override PartName="/word/header1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml"/>'
            '<Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>'
            '<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>'
            '<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>'
            '</Types>')


def rels_root_xml():
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
            '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>'
            '<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>'
            '</Relationships>')


def rels_document_xml():
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
            '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/header" Target="header1.xml"/>'
            '<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/>'
            '</Relationships>')


def sectpr_xml():
    return ('<w:sectPr>'
            '<w:headerReference w:type="default" r:id="rId2"/>'
            '<w:footerReference w:type="default" r:id="rId3"/>'
            '<w:pgSz w:w="16838" w:h="11906" w:orient="landscape"/>'
            '<w:pgMar w:top="964" w:right="794" w:bottom="794" w:left="794" '
            'w:header="397" w:footer="340" w:gutter="0"/>'
            '</w:sectPr>')


def build_docx(out_path, body_xml, title):
    document = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
                '<w:document %s %s><w:body>%s%s</w:body></w:document>'
                % (W_NS, R_NS, body_xml, sectpr_xml()))
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types_xml())
        z.writestr("_rels/.rels", rels_root_xml())
        z.writestr("docProps/core.xml", core_xml(title))
        z.writestr("docProps/app.xml", app_xml())
        z.writestr("word/document.xml", document)
        z.writestr("word/_rels/document.xml.rels", rels_document_xml())
        z.writestr("word/styles.xml", styles_xml())
        z.writestr("word/header1.xml", header_xml())
        z.writestr("word/footer1.xml", footer_xml())


def main():
    os.makedirs(OUTDIR, exist_ok=True)

    spec = importlib.util.spec_from_file_location("wfgen_20261010", SRC)
    if spec is None or spec.loader is None:
        raise SystemExit("ABORT: cannot load generator module from %s" % SRC)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    setattr(mod, "HIGHLIGHT", False)
    story_clean = mod.make_story()
    setattr(mod, "HIGHLIGHT", True)
    story_hl = mod.make_story()
    setattr(mod, "HIGHLIGHT", False)

    # expected token count: whole-word AI tokens across the clean story text
    token_re = re.compile(r"(?<![A-Za-z0-9])AI(?![A-Za-z0-9])")
    n_tokens = sum(len(token_re.findall(p.text)) for p in iter_paragraphs(story_clean))

    body_clean = walk(story_clean)
    body_hl = walk(story_hl)

    n_hl = body_hl.count(HL_TAG)
    n_hl_clean = body_clean.count(HL_TAG)
    if n_hl != n_tokens:
        raise SystemExit("MISMATCH: highlighted tokens %d != expected %d" % (n_hl, n_tokens))
    if n_hl_clean != 0:
        raise SystemExit("MISMATCH: clean story contains %d highlight tags" % n_hl_clean)

    build_docx(OUT_CLEAN, body_clean, mod.CLEAN_TITLE)
    build_docx(OUT_HL, body_hl, mod.CLEAN_TITLE + " (every whole-word AI token highlighted)")

    n_tables = sum(1 for i in story_clean if i.__class__.__name__ == "Table")
    n_paras = sum(1 for i in story_clean if i.__class__.__name__ == "Paragraph")
    n_skip = sum(1 for i in story_clean if i.__class__.__name__ not in
                 ("Paragraph", "Table", "Spacer", "PageBreak", "HRFlowable"))
    print("story items: %d paragraphs, %d top-level tables (plus nested), %d unknown"
          % (n_paras, n_tables, n_skip))
    print("AI tokens (whole-word) in story:", n_tokens)
    print("highlight tags -> clean: %d | highlighted: %d" % (n_hl_clean, n_hl))
    for p in (OUT_CLEAN, OUT_HL):
        print("wrote: %s (%d bytes)" % (p, os.path.getsize(p)))


if __name__ == "__main__":
    main()
