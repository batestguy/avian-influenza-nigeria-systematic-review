"""Workflow status and completion record - Nigeria avian influenza systematic review.

Operational record current to 10 October 2026. Replaces the 19 September 2026
"Workflow Status and Gate Roadmap" snapshot (created by tmp/pdfs/create_workflow_pdf.py,
which is left untouched).

Two outputs are built from exactly the same content:
  1. output/pdf/AvianInfluenzaSysRev.pdf                     - the clean record.
  2. output/pdf/AvianInfluenzaSysRev_AI_highlighted_20261010.pdf
     - identical content, but every whole-word token "AI" (case-sensitive; AIV, AIMS
       and similar words are not matched) is painted with a yellow background so the
       author can see every AI mention at a glance.

Every figure printed here is taken from the project's own records:
  Workbench/15_RUN_LOG.md (top), Workbench/57_NEXT_SESSION_HANDOFF_20260922.md (top),
  Workbench/56_SCREENING_RECONCILIATION.json (metadata.status / metadata.counts),
  Workbench/60_APPRAISAL_20261009.md, Workbench/59_IMPROVEMENT_PLAN_20261008.md
  (progress log), and manuscript/sections/03_methods.txt in the retrieval workspace.
No figure is invented, and nothing is attributed to a human that an AI agent did.
"""

import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    PageTemplate,
    PageBreak,
    Paragraph as _Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(r"D:\AvianInfluenzaSysRev")
OUT = ROOT / "output" / "pdf" / "AvianInfluenzaSysRev.pdf"
OUT_HIGHLIGHTED = ROOT / "output" / "pdf" / "AvianInfluenzaSysRev_AI_highlighted_20261010.pdf"

PAGE_W, PAGE_H = landscape(A4)
MARGIN_X = 14 * mm
MARGIN_TOP = 17 * mm
MARGIN_BOTTOM = 14 * mm
CONTENT_W = PAGE_W - 2 * MARGIN_X

NAVY = colors.HexColor("#17324D")
BLUE = colors.HexColor("#1E5F8A")
TEAL = colors.HexColor("#267A75")
GREEN = colors.HexColor("#2C7A56")
AMBER = colors.HexColor("#9A6200")
RED = colors.HexColor("#9A3030")
INK = colors.HexColor("#1F2933")
MUTED = colors.HexColor("#52606D")
GRID = colors.HexColor("#C6D0D9")
PALE_BLUE = colors.HexColor("#EAF2F8")
PALE_TEAL = colors.HexColor("#E8F4F1")
PALE_GREEN = colors.HexColor("#EAF5EE")
PALE_AMBER = colors.HexColor("#FFF4D6")
PALE_RED = colors.HexColor("#FDECEC")
PALE_GREY = colors.HexColor("#F4F6F8")

# Whole-word, case-sensitive "AI": not AIV, AIMS, SAID, AVIAN and so on.
AI_TOKEN = re.compile(r"(?<![A-Za-z0-9])AI(?![A-Za-z0-9])")
HIGHLIGHT = False


def hl(text):
    """Paint every whole-word AI token yellow when building the highlighted copy."""
    text = str(text)
    if not HIGHLIGHT:
        return text
    return AI_TOKEN.sub('<font backColor="#FFFF00">AI</font>', text)


def Paragraph(text, style, **kwargs):  # noqa: N802 - local wrapper for reportlab's class
    return _Paragraph(hl(text), style, **kwargs)


styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="TitleLarge", parent=styles["Title"], fontName="Helvetica-Bold",
    fontSize=23, leading=27, textColor=NAVY, alignment=TA_LEFT, spaceAfter=6,
))
styles.add(ParagraphStyle(
    name="Subtitle", parent=styles["Normal"], fontName="Helvetica",
    fontSize=11.2, leading=14.5, textColor=MUTED, spaceAfter=4,
))
styles.add(ParagraphStyle(
    name="Stamp", parent=styles["Normal"], fontName="Helvetica-Bold",
    fontSize=9.6, leading=12.5, textColor=TEAL, spaceAfter=4,
))
styles.add(ParagraphStyle(
    name="Section", parent=styles["Heading1"], fontName="Helvetica-Bold",
    fontSize=14.5, leading=18, textColor=NAVY, spaceBefore=0, spaceAfter=5,
))
styles.add(ParagraphStyle(
    name="Subsection", parent=styles["Heading2"], fontName="Helvetica-Bold",
    fontSize=10.3, leading=12.8, textColor=BLUE, spaceBefore=3, spaceAfter=2.5,
))
styles.add(ParagraphStyle(
    name="Body", parent=styles["BodyText"], fontName="Helvetica",
    fontSize=8.7, leading=11.2, textColor=INK, spaceAfter=3,
))
styles.add(ParagraphStyle(
    name="Small", parent=styles["BodyText"], fontName="Helvetica",
    fontSize=7.6, leading=9.4, textColor=INK, spaceAfter=2,
))
styles.add(ParagraphStyle(
    name="SmallMuted", parent=styles["BodyText"], fontName="Helvetica",
    fontSize=7.2, leading=9, textColor=MUTED, spaceAfter=2,
))
styles.add(ParagraphStyle(
    name="Table", parent=styles["BodyText"], fontName="Helvetica",
    fontSize=7.05, leading=8.7, textColor=INK,
))
styles.add(ParagraphStyle(
    name="TableTight", parent=styles["BodyText"], fontName="Helvetica",
    fontSize=6.5, leading=7.9, textColor=INK,
))
styles.add(ParagraphStyle(
    name="TableHead", parent=styles["BodyText"], fontName="Helvetica-Bold",
    fontSize=7.05, leading=8.6, textColor=colors.white,
))
styles.add(ParagraphStyle(
    name="TableHeadTight", parent=styles["BodyText"], fontName="Helvetica-Bold",
    fontSize=6.5, leading=7.8, textColor=colors.white,
))
styles.add(ParagraphStyle(
    name="Status", parent=styles["BodyText"], fontName="Helvetica-Bold",
    fontSize=6.8, leading=8.2, alignment=TA_CENTER, textColor=INK,
))
styles.add(ParagraphStyle(
    name="Callout", parent=styles["BodyText"], fontName="Helvetica-Bold",
    fontSize=9.1, leading=11.8, textColor=NAVY,
))


def p(text, style="Table"):
    return Paragraph(str(text), styles[style])


def bullet(text):
    return Paragraph("&#8226; " + str(text), styles["Small"])


def status(label, fill, text_color=INK, width=30):
    style = ParagraphStyle(
        name="StatusLocal" + label.replace(" ", "").replace("-", ""), parent=styles["Status"],
        textColor=text_color,
    )
    return Table([[Paragraph(label, style)]], colWidths=[width * mm], style=TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), fill),
        ("BOX", (0, 0), (-1, -1), 0.45, fill),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))


def table(rows, widths, header=True, row_bgs=None, tight=False):
    body_style = "TableTight" if tight else "Table"
    head_style = "TableHeadTight" if tight else "TableHead"
    rendered = []
    for i, row in enumerate(rows):
        rendered.append([
            cell if hasattr(cell, "wrap")
            else p(cell, head_style if header and i == 0 else body_style)
            for cell in row
        ])
    commands = [
        ("GRID", (0, 0), (-1, -1), 0.35, GRID),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]
    start = 0
    if header:
        commands.append(("BACKGROUND", (0, 0), (-1, 0), NAVY))
        start = 1
    if row_bgs:
        for row_index, fill in row_bgs.items():
            commands.append(("BACKGROUND", (0, row_index), (-1, row_index), fill))
    else:
        for row_index in range(start, len(rows)):
            if (row_index - start) % 2 == 1:
                commands.append(("BACKGROUND", (0, row_index), (-1, row_index), PALE_GREY))
    return Table(rendered, colWidths=widths, repeatRows=1 if header else 0,
                 hAlign="LEFT", style=TableStyle(commands))


def card(title, value, detail, fill, width=52):
    return Table(
        [[p(title, "SmallMuted")], [p(value, "Callout")], [p(detail, "Small")]],
        colWidths=[width * mm],
        style=TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), fill),
            ("BOX", (0, 0), (-1, -1), 0.6, GRID),
            ("LEFTPADDING", (0, 0), (-1, -1), 5),
            ("RIGHTPADDING", (0, 0), (-1, -1), 5),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ]),
    )


def band(text, label, fill, edge, width=30):
    return Table([[status(label, fill, width=width), p(text, "Body")]],
                 colWidths=[(width + 3) * mm, CONTENT_W - (width + 3) * mm],
                 style=TableStyle([
                     ("BACKGROUND", (1, 0), (1, 0), fill),
                     ("BOX", (0, 0), (-1, -1), 0.55, edge),
                     ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                     ("LEFTPADDING", (0, 0), (-1, -1), 5),
                     ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                     ("TOPPADDING", (0, 0), (-1, -1), 5),
                     ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                 ]))


def page_decor(canvas, doc):
    canvas.saveState()
    page = canvas.getPageNumber()
    canvas.setStrokeColor(GRID)
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN_X, PAGE_H - 10 * mm, PAGE_W - MARGIN_X, PAGE_H - 10 * mm)
    canvas.setFont("Helvetica-Bold", 7.2)
    canvas.setFillColor(NAVY)
    canvas.drawString(MARGIN_X, PAGE_H - 7.2 * mm, "NIGERIA AVIAN INFLUENZA SYSTEMATIC REVIEW")
    canvas.setFont("Helvetica", 7.1)
    canvas.setFillColor(MUTED)
    canvas.drawRightString(PAGE_W - MARGIN_X, PAGE_H - 7.2 * mm,
                           "WORKFLOW STATUS AND COMPLETION RECORD")
    canvas.line(MARGIN_X, 9 * mm, PAGE_W - MARGIN_X, 9 * mm)
    canvas.setFont("Helvetica", 7.1)
    canvas.setFillColor(MUTED)
    canvas.drawString(MARGIN_X, 5.3 * mm, "Current operational record: 10 October 2026")
    canvas.drawRightString(PAGE_W - MARGIN_X, 5.3 * mm, f"Page {page}")
    canvas.restoreState()


CLEAN_TITLE = ("Nigeria Avian Influenza Systematic Review - "
               "Workflow Status and Completion Record 2026-10-10")


def make_doc(out_path, title):
    doc = BaseDocTemplate(
        str(out_path), pagesize=landscape(A4), leftMargin=MARGIN_X, rightMargin=MARGIN_X,
        topMargin=MARGIN_TOP, bottomMargin=MARGIN_BOTTOM, title=title,
        author="Nigeria Avian Influenza Systematic Review",
    )
    frame = Frame(MARGIN_X, MARGIN_BOTTOM, CONTENT_W, PAGE_H - MARGIN_TOP - MARGIN_BOTTOM, id="main")
    doc.addPageTemplates([PageTemplate(id="all", frames=[frame], onPage=page_decor)])
    return doc


def make_story():
    story = []

    # ------------------------------------------------------------ page 1
    story += [
        Spacer(1, 6 * mm),
        Paragraph("Nigeria Avian Influenza Systematic Review", styles["TitleLarge"]),
        Paragraph("2006-2026 &#8226; all phases complete &#8226; operational record current to 10 October 2026",
                  styles["Subtitle"]),
        Paragraph("WORKFLOW STATUS AND COMPLETION RECORD &#8212; Current operational record: 10 October 2026",
                  styles["Stamp"]),
        HRFlowable(width="100%", thickness=2, color=TEAL, spaceBefore=2, spaceAfter=7),
        Paragraph("Purpose", styles["Subsection"]),
        Paragraph(
            "This report replaces the workflow-status snapshot of 19 September 2026, which still showed the "
            "review at its screening stage. It records the complete journey - protocol, search, register and "
            "screening, retrieval, extraction, risk of bias, synthesis, figures, the October 2026 update search, "
            "and the manuscript build and checks - together with the controls that held, the author-owned items "
            "that remain, and the source of every number quoted. The manuscript is the deliverable; the Workbench "
            "remains the operational audit record. No number below is carried over from the superseded snapshot.",
            styles["Body"],
        ),
        Paragraph("1. Status at a glance", styles["Section"]),
        Table(
            [[
                card("Register", "2,157", "Final. 1,803 title-excluded + 342 full-text candidates + 12 duplicates.", PALE_TEAL),
                card("Reports / studies", "127 / 113", "Retained reports, linked into 113 studies.", PALE_BLUE),
                card("Manuscript", "PASS",
                     "verify.py PASS; docx validation PASSED; 96-page render with Figures 2-3.", PALE_GREEN),
                card("Author items", "6 + 1", "Six highlighted placeholders and the journal choice remain.", PALE_AMBER),
                card("Deadline", "Sun 11 Oct", "Submission-ready package; author asked for Sunday 11 October 2026.", PALE_AMBER),
            ]],
            colWidths=[52 * mm, 52 * mm, 55 * mm, 52 * mm, 48 * mm],
            style=TableStyle([
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 3),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]),
        ),
        Spacer(1, 4 * mm),
        Paragraph(
            "Every phase of the review is complete and the register is final. The manuscript passes every check "
            "the project can run: 145 references (4 flagged and disclosed), 8,530 main-text words, a 290-word "
            "abstract, and a 96-page render including appendices. Nothing further can be added to the evidence "
            "base from the sources available. What remains is a short list of author-owned items, two agent-side "
            "checks, and the choice of journal.",
            styles["Body"],
        ),
    ]
    story.append(table(
        [
            ["Phase", "Status", "Current evidence"],
            ["0. Protocol and eligibility", "COMPLETE",
             "Frozen on 16 September 2026 and re-frozen as amendments were taken; amendments dated and graded; registration position recorded honestly, not backdated."],
            ["1. Search (all sources)", "COMPLETE",
             "Six original sources 16-19 September 2026; Google Scholar update search 28 September; strategies rebuilt with the caps removed and citation chasing closed 10 October 2026; every limitation disclosed."],
            ["2. Register and screening", "COMPLETE",
             "2,157 records final; two independent AI reviewers, blind, with a third AI agent as arbiter; agreement reported per stage."],
            ["3. Retrieval", "COMPLETE",
             "Legal open routes only; 98 reports not retrieved and disclosed with the direction of effect."],
            ["4. Extraction", "COMPLETE",
             "113 studies; dual blind extraction with adjudication against the source texts."],
            ["5. Risk of bias and certainty", "COMPLETE",
             "JBI checklists plus the seven-item molecular transparency check; 14 high-risk studies; 13 studies with molecular caps; item agreement 79.3%."],
            ["6. Synthesis", "COMPLETE",
             "SWiM groupings S1-S5; four sensitivity analyses (i)-(iv); all assertions PASS at coverage 113."],
            ["7. Figures", "COMPLETE",
             "State x epoch map and clade/wave timeline, both built by script with provenance-validated ranges."],
            ["8. October update search", "COMPLETE",
             "17,037 records retrieved by the rebuilt strategies; citation chasing closed at 88/123 seeds with 0 errors; 52-record packet screened blind; 4 studies retained abstract-only."],
            ["9. Manuscript build and checks", "COMPLETE",
             "145 references (4 flagged, disclosed); verify.py PASS; docx validation PASSED; 96-page render including appendices; Figures 2-3 embedded."],
        ],
        [52 * mm, 24 * mm, 193 * mm],
    ))
    story += [
        Spacer(1, 4 * mm),
        Paragraph("What remains", styles["Subsection"]),
        Paragraph(
            "Author-owned: the six highlighted placeholders - the declarations (funding, which also appears in the "
            "abstract, competing interests, author contributions, acknowledgements and data availability) plus the "
            "Reviewer 1 line - and the choice of journal. Agent-side and pending: re-running the reporting audits "
            "against the updated manuscript, and the reviewer blind re-score. The author asked for the commit; it "
            "was made on 10 October 2026 (nothing pushed). Sections 6 "
            "to 8 list each item with its owner and its state.",
            styles["Body"],
        ),
        Spacer(1, 2 * mm),
        band(
            "Sunday 11 October 2026 is the hard deadline the author set (\"I need this by sunday\"), read as the "
            "submission-ready manuscript package. The review work is the agent's job: only the final deliverable "
            "goes to the author.",
            "DEADLINE", PALE_AMBER, AMBER, width=30,
        ),
    ]

    # ------------------------------------------------------------ page 2
    story += [
        PageBreak(),
        Paragraph("2. The record: the phase-by-phase journey", styles["Section"]),
        Paragraph(
            "Dates are those of the dated run-log and handoff entries. Agreement figures describe agreement "
            "between AI agents, never between humans.",
            styles["Body"],
        ),
    ]
    story.append(table(
        [
            ["Phase (dates)", "Record", "State"],
            ["0. Protocol\n16 September 2026",
             "The protocol was frozen on 16 September 2026 and re-frozen as amendments were taken. It carries the "
             "dated eligibility anchor, the reviewer model, the screening form and the graded amendments; the freeze "
             "is consistent with the registration position and no backdating is claimed. Reviewer roles and the SWiM "
             "default were fixed here.",
             "COMPLETE"],
            ["1. Search\n16-20 September 2026;\nScholar update 28 September",
             "PubMed, OpenAlex/Crossref, Scopus and ScienceDirect were last run on 16 September 2026 and the Web of "
             "Science Starter API update on 19 September (the record-level export of 20 September is not recoverable). "
             "A Google Scholar update search was run through SerpApi on 28 September, after the protocol freeze, and is "
             "reported as identification by other methods. The October rebuild and its per-source audit are in section 3.",
             "COMPLETE"],
            ["2. Register and screening\n16 September - 10 October",
             "Records were de-duplicated by DOI, PMID or normalised title plus year. Screening was two-stage "
             "(title/metadata, then full text) by two large language model agents working independently and blind to "
             "each other, with a third AI agent (the coordinating session) adjudicating every disagreement against the "
             "protocol criteria; at the title stage a record retained by either reviewer proceeded to full text. "
             "Reviewer 2 was an independent Codex agent (Epicurus) from 19 to 27 September; from 27 September Reviewer 1 "
             "was an executor agent and Reviewer 2 a separate reviewer agent. Agreement: 97.0% (kappa 0.88) at "
             "title/metadata on 1,877 records; 86.6% (kappa 0.76) at full text on 216 reports; 94.3% (kappa 0.77) on 228 "
             "records for the Scholar update search; and 92.3% (kappa 0.85) on 52 records for the October update search, "
             "whose final packet numbers are the newest layer.",
             "COMPLETE"],
            ["3. Retrieval\nSeptember - 9 October",
             "Full texts were sought only through identifier resolution and legal open-access routes (Crossref, OpenAlex, "
             "Europe PMC, PubMed, Semantic Scholar, Unpaywall, institutional repositories and Google Scholar version "
             "clusters). No CAPTCHA was bypassed, no login or shadow library was used, and institutional access was not "
             "available to the review team. The September open-route re-sweep recovered a file for 18 of the 88 reports "
             "then outstanding (10 full texts, 8 conference abstracts); three files obtained after a browser auto-passed "
             "an anti-bot check were deleted. Of the 17 records advanced by the October packet, 1 full text and 6 "
             "abstracts were retrieved and 10 were not retrievable. Reports with no verified full text were recorded as "
             "not retrieved and were not assessed for eligibility: 98 in total (88 + 10), of which about 40 were judged "
             "likely relevant - disclosed as a limitation, not silently dropped.",
             "COMPLETE"],
            ["4. Extraction\n30 September - 10 October",
             "Reports were linked into studies before extraction: links proposed by one AI agent from the full texts, "
             "checked against the texts by a second, and adjudicated by the coordinating session. The extraction form was "
             "piloted blind by two extractors on the same 10 studies. Each study was then extracted independently and "
             "blind by two AI agents, with every value tied to a verbatim locator in the source text, and disagreements "
             "adjudicated against the texts by the coordinating session. Authors were not contacted for missing data. "
             "Coverage is 113 studies, including the October additions STU-113, STU-114 and STU-115 and the abstract-only "
             "set; CAN-2139 was linked as a companion report of STU-023 rather than as a new study.",
             "COMPLETE"],
            ["5. Risk of bias and certainty\n3 - 10 October",
             "Each study was appraised with the JBI checklist matching its design (Prevalence 55, Analytical "
             "Cross-sectional 5 and Case Series 30, the last added by a dated minor amendment on 3 October 2026), with a "
             "structured note instead of a checklist for 20 secondary or modelling studies, and the 37 studies with "
             "molecular data were also assessed with the seven-item molecular transparency check M1-M7 (a \"No\" on "
             "accession availability or phylogenetic support caps a study's molecular claims at \"suggestive\"). Two AI "
             "appraisers worked independently and blind, and the coordinating session adjudicated against the texts. "
             "Item-level agreement before adjudication was 868 of 1,094 items (79.3%). Scores were never summed. The "
             "October additions raised the high-risk count from 11 to 14; 13 studies carry molecular caps.",
             "COMPLETE"],
            ["6. Synthesis\n7 - 10 October",
             "Meta-analysis was not attempted: designs, units (birds, flocks, outbreaks, sequences) and assays were too "
             "heterogeneous to combine. Synthesis followed SWiM with five groupings matched to the review question - S1 "
             "temporal, S2 geographic, S3 host, S4 molecular, S5 exposure - over epochs 2006-2010, 2011-2014, 2015-2020 "
             "and 2021-2026. Four sensitivity analyses were run: (i) excluding high-risk studies; (ii) excluding grey "
             "literature report by report; (iii) as (ii) with four reports of uncertain peer-review status also treated "
             "as grey, added during synthesis before certainty rating; and (iv) restricting state counts to states with "
             "sequence or isolate evidence, added post hoc after certainty rating. After the October update search, "
             "coverage is 113 studies, all script assertions PASS, the Table 2 counts are unchanged (27/2/22/15/0/5) and "
             "S5 holds 110 rows / 72 independent; sensitivity (i) was updated and (ii)-(iv) are table-level unchanged.",
             "COMPLETE"],
            ["7. Figures\n9 October",
             "Figure 2 is the state x epoch map built from the synthesis tables; Figure 3 is the clade and wave timeline. "
             "Both are built by script from the synthesis outputs, with every drawn range moved into a cited provenance "
             "file and a validation table carrying input hashes and a build date. The fix round closed the 2.3.2.1c bar at "
             "its last evidenced point with an honest continuation treatment and closed 2.3.4.4b at 2026. Both figures are "
             "embedded in the manuscript and were visually inspected in the render.",
             "COMPLETE"],
            ["8. October update search\n8 - 10 October",
             "All search strategies were rebuilt and the record caps removed. 17,037 records were retrieved and "
             "de-duplicated against the register (2,270 matched; 44 likely-new, 43 in window, after the "
             "reviewer-corrected de-duplication). Citation chasing ran on 123 seed reports and closed on 10 October "
             "(88 resolved, 3 with no DOI, 0 errors): 2,195 candidates collapsed to 1,745 records new to the register, of "
             "which 11 were relevance-positive. Those joined the rebuild hits in a 52-record packet screened blind (row 2): "
             "35 title-excluded, 17 pursued, 10 not retrievable, 3 excluded (a news item, a negative-only survey and a "
             "conceptual GIS piece) and 4 retained as abstract-only studies. The register gained CAN-2106 to CAN-2157.",
             "COMPLETE"],
            ["9. Manuscript build and checks\n9 - 10 October",
             "The target manuscript was rebuilt with all counts updated across the abstract, Methods, Results, Discussion, "
             "Appendices A/B/C and the flow diagram, with a new Appendix A3 (October update search and PRESS "
             "self-assessment) and amendment rows for 8-9 October. Checks: 145 references, 4 flagged for genuinely "
             "incomplete metadata and disclosed (nothing invented); verify.py PASS (145 references listed and cited, "
             "first-citation order monotonic, all 113 studies cited, no stray study ids, 6 author placeholders, no "
             "replacement characters); docx validation PASSED with Figures 2-3 embedded; render 96 pages including "
             "appendices; abstract 290 words and main text 8,530 words. Backups were taken before the figure and "
             "update-search rebuilds.",
             "COMPLETE"],
        ],
        [40 * mm, 208 * mm, 21 * mm],
    ))

    # ------------------------------------------------------------ page 3
    story += [
        PageBreak(),
        Paragraph("3. Search-source audit, per source", styles["Section"]),
        Paragraph(
            "Source status combines the original layers of 16-19 September 2026 with the October 2026 rebuild, which "
            "removed the record caps. Where a limitation could not be repaired it is kept visible here rather than "
            "quietly dropped.",
            styles["Body"],
        ),
    ]
    story.append(table(
        [
            ["Source", "Layer", "Records and limitations", "Reporting control"],
            ["PubMed / MEDLINE",
             "Original 16 Sep 2026 (v3); rebuild 9 Oct",
             "Original string returned 140 records. The rebuilt string (adding \"Influenza in Birds\"[Mesh] and related "
             "terms) returned 209, about 49% more. Abstracts were fetched for the 51 unmatched PubMed records, which "
             "found 5 newly relevant records.",
             "Both strings and their counts are documented; the gain from the improved string is reported, not hidden."],
            ["OpenAlex",
             "Rebuild 9-10 Oct",
             "10,614 records (the 1,000-record cap was removed). The reviewer pass found that OpenAlex stores DOI/PMID as "
             "full URLs, so the first de-duplication produced zero DOI matches; the corrected de-duplication was rerun. "
             "The free daily budget was exhausted (HTTP 429), blocking 43 citation-chasing seeds until the 00:00 UTC "
             "reset, after which the re-chase closed at 88/123 seeds resolved with 0 errors.",
             "Per-source totals and the rate-limit interruption are recorded; citation chasing is now complete."],
            ["Crossref",
             "Rebuild 9 Oct",
             "6,000 records of 16,292 returned (the source cap was reached).",
             "The cap is stated wherever the count is used, and is not presented as coverage of the source."],
            ["Web of Science Starter API",
             "Original 19 Sep; rebuild 9 Oct",
             "Original 175 records across 4 pages (175 unique UIDs, HTTP 200). Rebuild 194, with the date filter applied "
             "locally because the Starter API ignores it. Starter returns no abstracts, so records are matched on title "
             "and metadata only. The corrected facet queries of 19 September returned HTTP 429 for all three facets and "
             "no corrected facet total is claimed.",
             "Base-query counts only; facet totals never claimed as complete."],
            ["AJOL",
             "Rebuild 9 Oct",
             "66 rows returned, but result pages 2-4 were byte-identical to page 1, so only 20 records were captured; the "
             "remaining 46 titles would need a browser. AJOL was not one of the original run sources.",
             "The pagination defect is stated wherever the count is used."],
            ["Google Scholar",
             "SerpApi; supplement 17 Sep; update search 28 Sep; rebuild skipped",
             "The 17 September supplement (140 retrieved) cannot be reconstructed and is not relied on. The 28 September "
             "update search is the operative layer: 228 records screened, 26 retained, 190 excluded, 12 duplicates "
             "removed. In the October rebuild the SerpApi quota was spent, so Scholar was skipped (8 of 10 source calls "
             "succeeded).",
             "Reported as supplementary identification by other methods, never as a primary database layer."],
            ["Scopus and ScienceDirect",
             "Not rebuilt (author decision not pursued)",
             "The 16 September strings and exports are undocumented and unrecoverable, so these sources are not part of "
             "the October rebuild and no rebuilt string exists for them.",
             "Disclosed as an unrecoverable limitation rather than repaired silently."],
        ],
        [34 * mm, 33 * mm, 132 * mm, 70 * mm],
    ))
    story += [
        Spacer(1, 4 * mm),
        Paragraph("Limitations of the search record, kept honest", styles["Subsection"]),
    ]
    for item in [
        "The original strategies were not peer reviewed with the PRESS checklist. The rebuilt October strings were "
        "self-assessed against PRESS and that assessment is reported in Appendix A3 of the manuscript, but no "
        "independent PRESS reviewer was available.",
        "Record caps (Crossref 6,000 of 16,292; OpenAlex and the earlier WoS layer) mean the returned sets are not "
        "exhaustive for those sources; the caps and their effect are stated wherever the counts are used.",
        "The Starter-tier Web of Science layer returns no abstracts, so relevance assessment on those records is "
        "title-and-metadata only.",
        "Google Scholar cannot be reconstructed for the 17 September supplement; only the 28 September update search is "
        "relied on, and it is reported as identification by other methods.",
        "No prospective registration exists: the protocol is available from the corresponding author on request, and the "
        "dated 16 September freeze is not backdated or upgraded after the fact.",
    ]:
        story.append(bullet(item))

    # ------------------------------------------------------------ page 4
    story += [
        PageBreak(),
        Paragraph("4. Final accounting", styles["Section"]),
        Paragraph(
            "The register closes at report level and at study level. Both lines are reproduced from the register and "
            "from the manuscript build, and they reconcile arithmetically.",
            styles["Body"],
        ),
        Paragraph("The register at closure (report level)", styles["Subsection"]),
    ]
    story.append(table(
        [
            ["Register line", "Number", "Basis"],
            ["Register, final", "2,157", "Canonical identities after the October integration (CAN-2106 to CAN-2157 added)."],
            ["Title/metadata excluded", "1,803", "1,768 from the original arms + 35 from the October packet."],
            ["Full-text candidates", "342", "325 from the original arms + 17 from the October packet (88 + 10, 123 + 4, 114 + 3 all reconcile)."],
            ["- retained (provisional full-text eligible)", "127", "123 from the original arms + 4 retained abstract-only in October."],
            ["- excluded at full text", "117", "114 from the original arms + 3 excluded in October (news item, negative-only survey, conceptual GIS piece)."],
            ["- not retrieved", "98", "88 from the original arms + 10 from the October packet; disclosed with the direction of effect."],
            ["Duplicates removed", "12", "Collapsed during de-duplication; retained in the audit trail, not as evidence records."],
            ["Check", "1,803 + 342 + 12 = 2,157", "And 342 = 127 + 117 + 98."],
        ],
        [80 * mm, 39 * mm, 150 * mm],
    ))
    story += [
        Spacer(1, 4 * mm),
        Paragraph("From reports to studies", styles["Subsection"]),
        Paragraph(
            "The 127 retained reports were linked into 113 studies: five reports carry more than one study, and companion "
            "reports were attached to the study they duplicate rather than counted again (CAN-2139 was linked to STU-023 "
            "on author evidence). Every data stream reused across reports is counted once, under one primary study. For "
            "continuity with the pre-October layer: the register held 2,105 records (1,768 title-excluded, 325 full-text "
            "candidates = 123 retained / 114 excluded / 88 not retrieved, 12 duplicates); the October integration added 52 "
            "records, of which 35 were title-excluded and 17 pursued.",
            styles["Body"],
        ),
        Spacer(1, 3 * mm),
        Paragraph("Manuscript numbers (verified on the 10 October build)", styles["Subsection"]),
    ]
    story.append(table(
        [
            ["Quantity", "Value", "Verification"],
            ["References", "145", "4 flagged and disclosed (incomplete metadata in the new records); verify.py PASS with 145 listed and all cited, first-citation order monotonic."],
            ["Abstract", "290 words", "Counted from the built document between the abstract and Introduction headings."],
            ["Main text", "8,530 words", "Introduction to Conclusions, excluding tables and captions."],
            ["Render", "96 pages", "Includes Appendices A-F; Figures 2-3 embedded and visually inspected."],
            ["Studies", "113 of 113 cited", "No uncited studies, no stray study ids, no replacement characters."],
            ["Author placeholders", "6", "Highlighted for the author's own words; drafts prepared but not applied."],
            ["Build checks", "verify.py PASS; docx validation PASSED", "Run against the submission-ready build after the October update search and the figure integration."],
        ],
        [50 * mm, 45 * mm, 174 * mm],
    ))

    # ------------------------------------------------------------ page 5
    story += [
        PageBreak(),
        Paragraph("5. Controls that held (honesty record)", styles["Section"]),
        Paragraph(
            "These controls constrained what the review could claim. They held to the end and each is recorded in the "
            "run log, the handoff or the improvement-plan progress log.",
            styles["Body"],
        ),
    ]
    story.append(table(
        [
            ["Control", "How it held"],
            ["Legal open routes only",
             "Retrieval used identifier resolution and legal open-access routes only. No CAPTCHA was bypassed, no login "
             "or shadow library was used, and no institutional access was claimed. Retrieval closed at what legal open "
             "routes yield; reports obtainable only otherwise were recorded as not retrieved and disclosed."],
            ["One attempt per bot gate",
             "Three reports whose files had been obtained after a browser auto-passed an anti-bot check were deleted and "
             "moved to the author-download list. From then on the rule was one attempt per bot gate, never retried and "
             "never auto-passed."],
            ["No author contact",
             "Author contact for unretrieved reports was not pursued, and authors were not contacted for missing data. "
             "This is reported as a limitation rather than worked around."],
            ["No shadow libraries",
             "Shadow libraries were excluded at every retrieval round, including after retrieval was re-opened."],
            ["No invented human checks",
             "No external human check of screening was performed this cycle, and none is claimed. The author's own "
             "verification is reported as author verification, with its transcription caveat, and never as an "
             "independent human screening; all agreement statistics are labelled as AI-to-AI agreement."],
            ["Registration honestly not backdated",
             "The dated 16 September 2026 protocol freeze stands as recorded. No prospective registration is claimed, "
             "and the absence of OSF or PROSPERO registration is stated in the manuscript."],
            ["Committed only when the author asked",
             "The author's rule is commit only when asked. The ledger, register, appraisal, plan and orientation "
             "files stayed uncommitted through every session until the author asked for the close-out commit on "
             "10 October 2026."],
        ],
        [52 * mm, 217 * mm],
    ))
    story += [
        Spacer(1, 5 * mm),
        Paragraph("6. Remaining before submission", styles["Section"]),
    ]
    story.append(table(
        [
            ["Item", "Owner", "State and next action"],
            ["Author declarations - the six highlighted placeholders: funding (which also appears in the abstract), "
             "competing interests, author contributions, acknowledgements, data availability, and the Reviewer 1 line",
             "Author",
             "Pending the author's own words. Drafts are prepared for approval and are not applied. The Reviewer 1 line "
             "exists because the identity of Reviewer 1 before 27 September 2026 is not recorded in the repository."],
            ["Target journal choice", "Author",
             "Pending. The main text is 8,530 words, so it may need trimming to the journal's limit."],
            ["Reporting audits re-run (PRISMA 2020, PRISMA-S, SWiM) against the updated manuscript", "Agent",
             "Pending on the Sunday path: the audits were written against the pre-update manuscript and must be re-run "
             "now that counts, Appendix A3 and the flow have changed."],
            ["Reviewer blind re-score of every domain (baseline: the 9 October appraisal)", "Agent",
             "Pending. The re-scoring agent must not see the improvement plan's targets."],
            ["4 flagged references", "Disclosed",
             "The new records carry genuinely incomplete metadata; they are flagged and disclosed rather than repaired "
             "by invention. No further repair is possible from the sources available."],
            ["Commit and hand over", "Author",
             "Done on the author's request: committed 10 October 2026 (nothing pushed). The final deliverable is "
             "handed over."],
        ],
        [105 * mm, 18 * mm, 146 * mm],
    ))

    # ------------------------------------------------------------ page 6
    story += [
        PageBreak(),
        Paragraph("7. Governance and roles", styles["Section"]),
        Paragraph(
            "The review was executed by AI agents under the author's decisions. The table states exactly who did what, "
            "so that no AI task is presented as human work.",
            styles["Body"],
        ),
    ]
    story.append(table(
        [
            ["Role", "Who", "Scope as recorded"],
            ["Author", "M.O. - the only human decision-maker",
             "Set the protocol and the three verification eligibility rules (secondary analyses, official outbreak "
             "records, reprinted tables); verified 429 AI screening decisions - all full-text inclusions and exclusions, "
             "all duplicate removals, a seeded 10% sample of title-stage exclusions and all adjudication overrides - "
             "changing 6 of the 107 priority decisions and later reconfirming all 107 without change; gave the final "
             "decisions at report-to-study linkage and extraction; owns the declarations, the Reviewer 1 line and the "
             "journal choice."],
            ["Reviewer 1", "An AI executor agent",
             "Primary screening, full-text assessment, extraction and appraisal decisions. From 27 September 2026 "
             "Reviewer 1 was an executor agent; the identity of Reviewer 1 before 27 September is the one open "
             "governance line and is marked for the author to confirm."],
            ["Reviewer 2", "An independent AI reviewer agent",
             "Second, blind decision at every stage. Reviewer 2 was an independent Codex agent (Epicurus) from 19 to 27 "
             "September 2026, and a separate reviewer agent thereafter (Claude Sonnet 5, and Claude Sonnet 5.5 from 29 "
             "September 2026)."],
            ["Arbiter", "The coordinating AI session",
             "Adjudicated every disagreement against the protocol criteria and the source texts; ran the register, the "
             "retrievals, the synthesis reruns and the manuscript rebuilds."],
            ["Appraisal", "Two independent AI appraiser agents",
             "Scored the completed review on 9 October 2026, blind to the improvement plan and its targets, with "
             "main-session verification of every material claim."],
        ],
        [30 * mm, 52 * mm, 187 * mm],
    ))
    story += [
        Spacer(1, 4 * mm),
        band(
            "Every screening, full-text, extraction, risk-of-bias, appraisal and synthesis decision in this review was "
            "made by AI agents. No human performed AI work and no human screening check is claimed; the agreement "
            "statistics are AI-to-AI agreement. The single human role is the author - protocol, eligibility rules, "
            "verification of the 429 AI decisions, and final decisions.",
            "DISCLOSURE", PALE_RED, RED, width=30,
        ),
        Spacer(1, 5 * mm),
        Paragraph("8. Provenance of the key numbers", styles["Section"]),
        Paragraph(
            "Every figure printed in this report, with the project file it is taken from. Where the files differ, the "
            "newest layer (the register summary and the top of the run log) is used.",
            styles["Body"],
        ),
    ]
    story.append(table(
        [
            ["Number(s)", "Source"],
            ["2,157 records; 1,803 / 342 / 12",
             "Workbench/15_RUN_LOG.md (top, \"W7 done\" entry); Workbench/56_SCREENING_RECONCILIATION.json (metadata.status)"],
            ["127 retained / 117 excluded / 98 not retrieved",
             "Workbench/15_RUN_LOG.md (top); Workbench/56_SCREENING_RECONCILIATION.json (metadata.status); "
             "Workbench/57_NEXT_SESSION_HANDOFF_20260922.md (top section)"],
            ["127 reports linked into 113 studies; STU-113/114/115; CAN-2139 as a companion of STU-023",
             "Workbench/15_RUN_LOG.md (top); Workbench/57_NEXT_SESSION_HANDOFF_20260922.md (top section)"],
            ["Title agreement 97.0%, kappa 0.88, 1,877 records",
             "manuscript/sections/03_methods.txt (Screening); Workbench/15_RUN_LOG.md (screening reconciliation entry)"],
            ["Full-text agreement 86.6%, kappa 0.76, 216 reports",
             "manuscript/sections/03_methods.txt (Screening); Workbench/60_APPRAISAL_20261009.md (verified flow counts)"],
            ["Scholar update search 94.3%, kappa 0.77, 228 records (26 retained / 190 excluded / 12 duplicates)",
             "manuscript/sections/03_methods.txt (Screening); Workbench/56_SCREENING_RECONCILIATION.json (metadata.counts)"],
            ["October packet 92.3%, kappa 0.85, 52 records; 35 title-excluded / 17 pursued / 4 retained abstract-only",
             "Workbench/15_RUN_LOG.md (W3 adjudication and top); "
             "Workbench/56_SCREENING_RECONCILIATION.json (metadata.w1w2_update_20261009); "
             "Workbench/57_NEXT_SESSION_HANDOFF_20260922.md (top section)"],
            ["14 high-risk studies; 13 molecular caps; item agreement 79.3% (868/1,094)",
             "Workbench/15_RUN_LOG.md (top, RoB entry); Workbench/60_APPRAISAL_20261009.md (extraction and RoB, verified)"],
            ["JBI Prevalence 55 / cross-sectional 5 / case series 30; 20 without a JBI tool; 37 molecular studies; "
             "sensitivity analyses (i)-(iv)",
             "manuscript/sections/03_methods.txt (Risk of bias; Heterogeneity and sensitivity analyses)"],
            ["17,037 records retrieved; 2,270 matched; 44 likely-new (43 in window)",
             "Workbench/15_RUN_LOG.md (W1 reviewer outcome and corrections)"],
            ["PubMed 140 original / 209 improved string; OpenAlex 10,614; Crossref 6,000 of 16,292; "
             "Web of Science Starter 175 original / 194 rebuild; AJOL 66 with 20 captured; Scholar quota spent",
             "Workbench/15_RUN_LOG.md (W1 search rebuild); Workbench/57_NEXT_SESSION_HANDOFF_20260922.md (top section)"],
            ["Citation chasing: 123 seeds, 88/123 resolved, 3 with no DOI, 0 errors; 2,195 candidates; 1,745 new; "
             "11 relevance-positive",
             "Workbench/15_RUN_LOG.md (W2 entry; overnight re-chase of 10 October, top entry)"],
            ["18 of 88 reports recovered in the September re-sweep; 3 bot-gated files deleted",
             "Workbench/59_IMPROVEMENT_PLAN_20261008.md (progress log, 8 October)"],
            ["429 AI decisions verified; 6 of 107 priority decisions changed; 423 agree / 6 disagree",
             "manuscript/sections/03_methods.txt (verification paragraph); Workbench/15_RUN_LOG.md (register "
             "verification entries); Workbench/57_NEXT_SESSION_HANDOFF_20260922.md (9 October section)"],
            ["145 references with 4 flagged; verify.py PASS; docx validation PASSED; 96-page render; Figures 2-3 embedded",
             "Workbench/15_RUN_LOG.md (top); Workbench/57_NEXT_SESSION_HANDOFF_20260922.md (top section); verify.py and "
             "manuscript/build_report.json (145 references, 4 flagged)"],
            ["Abstract 290 words; main text 8,530 words",
             "verify.py run against the 10 October submission-ready build (counted between the abstract and Introduction "
             "headings, and Introduction to Conclusions excluding tables and captions)"],
            ["Deadline Sunday 11 October 2026",
             "Workbench/15_RUN_LOG.md (\"Deadline (D7 answered) + Sunday critical path\" entry)"],
            ["Controls: legal routes only; one attempt per bot gate; no author contact; no shadow libraries; no invented "
             "human checks; not backdated; commit only on the author's request",
             "Workbench/15_RUN_LOG.md (author directive, 9 October); Workbench/57_NEXT_SESSION_HANDOFF_20260922.md "
             "(working rules); Workbench/59_IMPROVEMENT_PLAN_20261008.md (progress log); Workbench/60_APPRAISAL_20261009.md "
             "(registration ceiling)"],
        ],
        [83 * mm, 186 * mm],
        tight=True,
    ))
    story += [
        Spacer(1, 4 * mm),
        HRFlowable(width="100%", thickness=1, color=GRID, spaceBefore=2, spaceAfter=4),
        Paragraph(
            "Prepared from the current project records on 10 October 2026. This report replaces the workflow-status "
            "snapshot of 19 September 2026. It is an operational completion record, not the manuscript, and it makes no "
            "claim beyond the sources listed above; the manuscript remains the single source of truth for the review's "
            "findings.",
            styles["SmallMuted"],
        ),
    ]
    return story


def build(out_path, highlight, title):
    global HIGHLIGHT
    HIGHLIGHT = highlight
    doc = make_doc(out_path, title)
    doc.build(make_story())
    HIGHLIGHT = False
    return out_path


if __name__ == "__main__":
    print(build(OUT, False, CLEAN_TITLE))
    print(build(
        OUT_HIGHLIGHTED, True,
        CLEAN_TITLE + " (every whole-word AI token highlighted)",
    ))
