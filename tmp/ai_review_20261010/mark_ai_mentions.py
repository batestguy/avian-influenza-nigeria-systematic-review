# -*- coding: utf-8 -*-
"""Create a review copy of the manuscript with every whole-word 'AI' mention
highlighted yellow (w:highlight val="yellow" - the same marker the build uses).

Read-only with respect to the target: the target docx is never modified; this
script writes a copy plus a report of every occurrence in document order.

Run:  python -X utf8 mark_ai_mentions.py
"""
import os
import re
import zipfile

SRC = r"D:\AvianInfluenzaSysRev\Avian_review_paper_submission_ready.docx"
OUTDIR = r"D:\AvianInfluenzaSysRev\tmp\ai_review_20261010"
DST = os.path.join(OUTDIR, "Avian_review_paper_AI_mentions_marked_20261010.docx")
REPORT = os.path.join(OUTDIR, "AI_mentions_report.md")

PAT = re.compile(r"(?<![A-Za-z0-9])AI(?![A-Za-z0-9])")
HL = '<w:highlight w:val="yellow"/>'

# schema order of run properties relative to w:highlight
SET_A = set(("rStyle rFonts b bCs i iCs caps smallCaps strike dstrike outline shadow "
             "emboss imprint noProof snapToGrid vanish webHidden color spacing w kern "
             "position sz szCs").split())
SET_B = set(("u effect bdr shd fitText vertAlign rtl cs em lang eastAsianLayout "
             "specVanish oMath").split())

RUN_RE = re.compile(r"<w:r(?:\s[^>]*)?>.*?</w:r>", re.S)
PARA_RE = re.compile(r"<w:p(?:\s[^>]*)?>.*?</w:p>", re.S)
TEXTS_RE = re.compile(r"<w:t(?:\s[^>]*)?>([^<]*)</w:t>")


def insert_hl(rpr_xml):
    """Return rPr with <w:highlight/> inserted in schema-valid position."""
    m = re.match(r"(<w:rPr(?:\s[^>]*)?>)(.*)(</w:rPr>)$", rpr_xml, re.S)
    if not m:
        return rpr_xml
    open_tag, inner, close_tag = m.groups()
    if "<w:highlight" in inner:
        return rpr_xml
    spans = []
    i = 0
    while True:
        mm = re.search(r"<w:([A-Za-z]+)\b", inner[i:])
        if not mm:
            break
        start = i + mm.start()
        name = mm.group(1)
        j = i + mm.end()
        k = inner.find(">", j)
        if k == -1:
            break
        if inner[k - 1] == "/":
            end = k + 1
        else:
            ct = "</w:%s>" % name
            e2 = inner.find(ct, k)
            if e2 == -1:
                break
            end = e2 + len(ct)
        spans.append((name, start, end))
        i = end
    last_a = [s for s in spans if s[0] in SET_A]
    if last_a:
        idx = last_a[-1][2]
    else:
        first_b = [s for s in spans if s[0] in SET_B]
        idx = first_b[0][1] if first_b else len(inner)
    return open_tag + inner[:idx] + HL + inner[idx:] + close_tag


def split_run(run_xml):
    """Split one run so AI tokens carry a yellow highlight. Returns (xml, n)."""
    m = re.match(r"(<w:r(?:\s[^>]*)?>)(.*)(</w:r>)$", run_xml, re.S)
    if not m:
        return run_xml, 0
    open_run, inner, close_run = m.groups()
    rpr_m = re.search(r"<w:rPr(?:\s[^>]*)?>.*?</w:rPr>|<w:rPr(?:\s[^>]*)?/>", inner, re.S)
    rpr = rpr_m.group(0) if rpr_m else ""
    core = inner if not rpr_m else inner[:rpr_m.start()] + inner[rpr_m.end():]
    tm = re.match(r"^(.*?)(<w:t(?:\s[^>]*)?>.*?</w:t>)(.*)$", core, re.S)
    if not tm or core.count("<w:t") != 1:
        return run_xml, 0
    prefix, text_el, suffix = tm.groups()
    if "<w:t" in prefix or "<w:t" in suffix:
        return run_xml, 0
    tm2 = re.match(r"(<w:t(?:\s[^>]*)?>)(.*)(</w:t>)$", text_el, re.S)
    if not tm2:
        return run_xml, 0
    t_open, text, t_close = tm2.groups()
    if not PAT.search(text):
        return run_xml, 0
    rpr_hl = insert_hl(rpr) if rpr else "<w:rPr>" + HL + "</w:rPr>"

    def t_for(seg):
        if (seg[:1].isspace() or seg[-1:].isspace()) and "xml:space" not in t_open:
            return t_open[:-1] + ' xml:space="preserve">'
        return t_open

    segs = []
    pos = 0
    for mm in PAT.finditer(text):
        if mm.start() > pos:
            segs.append((False, text[pos:mm.start()]))
        segs.append((True, mm.group(0)))
        pos = mm.end()
    if pos < len(text):
        segs.append((False, text[pos:]))
    out = []
    for idx, (hl, seg) in enumerate(segs):
        pre = prefix if idx == 0 else ""
        r = rpr_hl if hl else rpr
        out.append("<w:r>" + r + pre + t_for(seg) + seg + t_close + "</w:r>")
    return "".join(out), sum(1 for hl, _ in segs if hl)


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    zf = zipfile.ZipFile(SRC, "r")
    xml = zf.read("word/document.xml").decode("utf-8")

    stats = {"runs": 0, "occ": 0}

    def repl(m):
        new, n = split_run(m.group(0))
        if n:
            stats["runs"] += 1
            stats["occ"] += n
        return new

    new_xml = RUN_RE.sub(repl, xml)

    # integrity guard: all visible text must be identical
    strip = lambda s: re.sub(r"<[^>]+>", "", s)
    if strip(new_xml) != strip(xml):
        raise SystemExit("ABORT: text changed during marking")
    if stats["occ"] == 0:
        raise SystemExit("ABORT: no 'AI' occurrences found - investigate")

    with zipfile.ZipFile(DST, "w", zipfile.ZIP_DEFLATED) as out:
        for info in zf.infolist():
            data = zf.read(info.filename)
            if info.filename == "word/document.xml":
                data = new_xml.encode("utf-8")
            out.writestr(info, data)
    zf.close()

    # report: every occurrence with context, in document order
    paras = PARA_RE.findall(new_xml)
    entries = []
    for p in paras:
        text = "".join(TEXTS_RE.findall(p))
        if not PAT.search(text):
            continue
        for mm in PAT.finditer(text):
            a = max(0, mm.start() - 130)
            b = min(len(text), mm.end() + 130)
            clip = " ".join(("\u2026" + text[a:b] + "\u2026").split())
            entries.append(clip)
    with open(REPORT, "w", encoding="utf-8") as f:
        f.write("# AI-mention review copy - 2026-10-10\n\n")
        f.write("Source (untouched): %s\n\n" % SRC)
        f.write("Marked copy: %s\n\n" % DST)
        f.write("Whole-word 'AI' occurrences marked: **%d** (runs changed: %d)\n\n"
                % (stats["occ"], stats["runs"]))
        f.write("## Contexts (document order)\n\n")
        for i, c in enumerate(entries, 1):
            f.write("%d. %s\n\n" % (i, c))

    print("raw 'AI' substrings in document.xml:", len(re.findall("AI", xml)))
    print("occurrences marked:", stats["occ"])
    print("runs changed:", stats["runs"])
    print("contexts listed:", len(entries))
    print("wrote:", DST)
    print("report:", REPORT)


if __name__ == "__main__":
    main()
