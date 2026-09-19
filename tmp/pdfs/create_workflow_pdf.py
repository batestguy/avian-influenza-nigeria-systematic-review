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
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(r"D:\AvianInfluenzaSysRev")
OUT = ROOT / "output" / "pdf" / "AvianInfluenzaSysRev.pdf"
OUT.parent.mkdir(parents=True, exist_ok=True)

PAGE_W, PAGE_H = landscape(A4)
MARGIN_X = 14 * mm
MARGIN_TOP = 17 * mm
MARGIN_BOTTOM = 14 * mm

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

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="TitleLarge", parent=styles["Title"], fontName="Helvetica-Bold",
    fontSize=24, leading=29, textColor=NAVY, alignment=TA_LEFT, spaceAfter=7,
))
styles.add(ParagraphStyle(
    name="Subtitle", parent=styles["Normal"], fontName="Helvetica",
    fontSize=11.5, leading=15, textColor=MUTED, spaceAfter=5,
))
styles.add(ParagraphStyle(
    name="Section", parent=styles["Heading1"], fontName="Helvetica-Bold",
    fontSize=15.5, leading=19, textColor=NAVY, spaceBefore=0, spaceAfter=6,
))
styles.add(ParagraphStyle(
    name="Subsection", parent=styles["Heading2"], fontName="Helvetica-Bold",
    fontSize=10.5, leading=13, textColor=BLUE, spaceBefore=4, spaceAfter=3,
))
styles.add(ParagraphStyle(
    name="Body", parent=styles["BodyText"], fontName="Helvetica",
    fontSize=8.9, leading=11.5, textColor=INK, spaceAfter=3,
))
styles.add(ParagraphStyle(
    name="Small", parent=styles["BodyText"], fontName="Helvetica",
    fontSize=7.6, leading=9.5, textColor=INK, spaceAfter=2,
))
styles.add(ParagraphStyle(
    name="SmallMuted", parent=styles["BodyText"], fontName="Helvetica",
    fontSize=7.2, leading=9, textColor=MUTED, spaceAfter=2,
))
styles.add(ParagraphStyle(
    name="Table", parent=styles["BodyText"], fontName="Helvetica",
    fontSize=7.05, leading=8.65, textColor=INK,
))
styles.add(ParagraphStyle(
    name="TableBold", parent=styles["BodyText"], fontName="Helvetica-Bold",
    fontSize=7.05, leading=8.65, textColor=INK,
))
styles.add(ParagraphStyle(
    name="TableHead", parent=styles["BodyText"], fontName="Helvetica-Bold",
    fontSize=7.05, leading=8.6, textColor=colors.white,
))
styles.add(ParagraphStyle(
    name="Status", parent=styles["BodyText"], fontName="Helvetica-Bold",
    fontSize=6.8, leading=8.2, alignment=TA_CENTER, textColor=INK,
))
styles.add(ParagraphStyle(
    name="Callout", parent=styles["BodyText"], fontName="Helvetica-Bold",
    fontSize=9.3, leading=12, textColor=NAVY,
))


def p(text, style="Table"):
    return Paragraph(str(text), styles[style])


def bullet(text):
    return Paragraph("&#8226; " + str(text), styles["Small"])


def status(label, fill, text_color=INK):
    style = ParagraphStyle(
        name="StatusLocal" + label.replace(" ", ""), parent=styles["Status"],
        textColor=text_color,
    )
    return Table([[Paragraph(label, style)]], colWidths=[28 * mm], style=TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), fill),
        ("BOX", (0, 0), (-1, -1), 0.45, fill),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))


def table(rows, widths, header=True, row_bgs=None):
    rendered = []
    for i, row in enumerate(rows):
        rendered.append([
            cell if hasattr(cell, "wrap") else p(cell, "TableHead" if header and i == 0 else "Table")
            for cell in row
        ])
    commands = [
        ("GRID", (0, 0), (-1, -1), 0.35, GRID),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
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
    return Table(rendered, colWidths=widths, repeatRows=1 if header else 0, hAlign="LEFT", style=TableStyle(commands))


def card(title, value, detail, fill):
    return Table([[p(title, "SmallMuted")], [p(value, "Callout")], [p(detail, "Small")]], colWidths=[42 * mm], style=TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), fill),
        ("BOX", (0, 0), (-1, -1), 0.6, GRID),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
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
    canvas.drawRightString(PAGE_W - MARGIN_X, PAGE_H - 7.2 * mm, "WORKFLOW STATUS AND GATE ROADMAP")
    canvas.line(MARGIN_X, 9 * mm, PAGE_W - MARGIN_X, 9 * mm)
    canvas.drawString(MARGIN_X, 5.3 * mm, "Current operational record: 19 September 2026")
    canvas.drawRightString(PAGE_W - MARGIN_X, 5.3 * mm, f"Page {page}")
    canvas.restoreState()


doc = BaseDocTemplate(
    str(OUT), pagesize=landscape(A4), leftMargin=MARGIN_X, rightMargin=MARGIN_X,
    topMargin=MARGIN_TOP, bottomMargin=MARGIN_BOTTOM,
    title="Nigeria Avian Influenza Systematic Review - Workflow Status 2026-09-19",
    author="Nigeria Avian Influenza Systematic Review",
)
frame = Frame(MARGIN_X, MARGIN_BOTTOM, PAGE_W - 2 * MARGIN_X, PAGE_H - MARGIN_TOP - MARGIN_BOTTOM, id="main")
doc.addPageTemplates([PageTemplate(id="all", frames=[frame], onPage=page_decor)])

story = []

# Page 1: executive status
story += [
    Spacer(1, 9 * mm),
    Paragraph("Nigeria Avian Influenza Systematic Review", styles["TitleLarge"]),
    Paragraph("Current workflow status, evidence controls, and completion roadmap", styles["Subtitle"]),
    HRFlowable(width="100%", thickness=2, color=TEAL, spaceBefore=2, spaceAfter=8),
    Paragraph("Purpose", styles["Subsection"]),
    Paragraph(
        "This report is the current project-control snapshot for the Nigeria avian influenza review. It records what is complete, what remains provisional, and the controlled order required before final screening, extraction, synthesis, and manuscript reporting. The manuscript DOCX remains the single source of truth and is unchanged.",
        styles["Body"],
    ),
]

cards = [[
    card("Gate A", "PASSED", "Protocol truth and amendment control", PALE_GREEN),
    card("Gate B", "CONDITIONAL", "Source audit closed with limitations", PALE_AMBER),
    card("Gate C", "OPEN", "Identity register complete; screening reconciliation open", PALE_BLUE),
    card("Gate D onward", "NOT STARTED", "Full text, extraction, RoB, synthesis, reporting", PALE_GREY),
]]
story.append(Table(cards, colWidths=[45 * mm, 45 * mm, 50 * mm, 55 * mm], style=TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ("TOPPADDING", (0, 0), (-1, -1), 0),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
])))
story += [Spacer(1, 6 * mm), Paragraph("Evidence and identity checkpoint", styles["Subsection"])]
metric_cards = [[
    card("Input rows", "2,288", "PubMed, supplement, manual imports, WoS", PALE_BLUE),
    card("Canonical groups", "1,845", "Provisional identity groups", PALE_TEAL),
    card("Collapsed duplicates", "443", "DOI / PMID / title-year matching", PALE_GREEN),
    card("WoS base retrieval", "175", "Raw records; not yet PRISMA counted", PALE_AMBER),
    card("Full-text assessed", "0", "Eligibility stage has not begun", PALE_RED),
]]
story.append(Table(metric_cards, colWidths=[39 * mm] * 5, style=TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 3),
    ("TOPPADDING", (0, 0), (-1, -1), 0),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
])))
story += [Spacer(1, 6 * mm), Paragraph("Controlling sequence", styles["Subsection"])]
story.append(Paragraph(
    "Protocol truth -> search closure -> canonicalisation -> screening -> full-text eligibility -> extraction pilot -> full extraction -> risk of bias and certainty -> SWiM synthesis -> manuscript reporting -> PRISMA / PRISMA-S / SWiM audit.",
    styles["Callout"],
))
story += [Spacer(1, 4 * mm), Paragraph(
    "Current stop point: do not promote provisional votes or the 160-record upper-bound queue into final PRISMA counts. Complete record-level screening reconciliation from the canonical register first.",
    styles["Body"],
)]

# Page 2: phase workflow
story += [PageBreak(), Paragraph("1. Formal workflow and exit gates", styles["Section"]), Paragraph(
    "The review follows the phase order below. Each phase has a defined output and a stop condition; unresolved source access or identity decisions must remain visible rather than being silently treated as complete.",
    styles["Body"],
)]
workflow_rows = [
    ["Phase", "Required output", "Current evidence", "Exit gate / next decision"],
    ["0. Protocol truth", "Dated protocol, eligibility, dates, roles, registration status, and amendment boundary.", "Passed 19 Sep. Operational cutoff fixed at 19 Sep 2026; R1 primary, Epicurus as R2, main agent as arbiter; SWiM default.", "Gate A passed. Keep the manuscript frozen until the downstream evidence gates are complete."],
    ["1. Search closure", "Exact strings, dates, filters, caps, exports, and access outcomes for every named source.", "PubMed, Scopus, ScienceDirect, OpenAlex/Crossref and WoS base query completed; Scholar supplementary; AJOL blocked/not run; corrected WoS facets rate-limited.", "Gate B conditionally closed for source audit. Preserve source-specific dates and limitations."],
    ["2. Canonicalisation", "One candidate identity with source lineage, duplicate links, and remapped decisions.", "Register complete: 2,288 input rows -> 1,845 provisional identity groups; 443 collapsed duplicates; all final statuses deliberately non-final.", "Gate C identity subgate repaired, but screening reconciliation remains open."],
    ["3. Screening", "Calibrated title/abstract decisions, full-text retrieval register, and fixed exclusion reasons.", "PubMed and supplement pilot decisions exist; they have not been fully remapped to the canonical register. Full-text assessment: 0.", "Replace the 160-record upper-bound queue with a reconciled candidate queue before definitive screening."],
    ["4-6. Extraction and RoB", "T1-T5 extraction, JBI/custom molecular RoB, and narrative certainty.", "Not started. No final included set exists.", "Begin only after Gate D full-text eligibility and extraction pilot criteria are met."],
    ["7. Synthesis", "SWiM narrative synthesis; quantitative pooling only if separately justified.", "Not started. No final study-level evidence table.", "Do not force meta-analysis; keep subtype, clade, reassortant, introduction, and local evolution distinct."],
    ["8-9. Reporting and audit", "Updated DOCX, PRISMA flow, PRISMA-S appendix, SWiM report, references, and final audit.", "Not started. Manuscript remains unchanged.", "All counts and claims must trace to the locked library and extraction/RoB records."],
]
story.append(table(workflow_rows, [29 * mm, 69 * mm, 91 * mm, 80 * mm]))
story += [Spacer(1, 5 * mm), Paragraph("Non-negotiable controls", styles["Subsection"])]
for item in [
    "Eligibility anchor: Nigeria-specific avian influenza evidence with epidemiological, molecular/phylogenetic, or spatial/temporal data.",
    "Use CoCoPop/PEO; do not recast the question as PICO.",
    "Use JBI prevalence/cross-sectional/cohort tools plus the custom molecular check; do not use score-sums or ROBINS-I/RCT tools.",
    "Keep `Not reported`, `Unclear`, and `N/A` explicit; never infer missing study facts from metadata alone.",
    "Final tables and appendices belong inside the single DOCX; the Workbench remains the operational audit record.",
]:
    story.append(bullet(item))

# Page 3: source audit
story += [PageBreak(), Paragraph("2. Search-source audit", styles["Section"]), Paragraph(
    "Source status is separated into completed, supplementary, blocked, and not-run states. The WoS base retrieval is valid for the executed query, but the later facet experiments are exploratory or rate-limited and must not be counted as corrected facet totals.",
    styles["Body"],
)]
source_rows = [
    ["Source", "Run / status", "Current evidence", "Control for reporting"],
    ["PubMed / MEDLINE", "16 Sep 2026; v3", "140 base records; 53 molecular subset; 142 preliminary screens including two v1 checks.", "Completed source. Preserve v3 strings and export provenance; do not mix v1 and v3 without a recorded reason."],
    ["Scopus", "16 Sep 2026; manual export", "204 imported records.", "Completed source. Reconcile DOI/PMID/title-year identity before PRISMA counting."],
    ["ScienceDirect", "16 Sep 2026; manual export", "25 displayed/exported records.", "Completed source. Retain date, filters, wording, and export."],
    ["OpenAlex / Crossref", "16 Sep 2026; supplement", "1,744 canonical supplement records after local processing.", "Supplementary layer. Do not present as a replacement for a locked database search without an amendment."],
    ["Web of Science", "19 Sep 2026; Starter API", "175 raw records across 4 pages (50/50/50/25), HTTP 200, 175 unique UIDs. Not merged or screened.", "Valid base query only. Corrected molecular, epi/spatial/temporal, and wild-bird facets returned HTTP 429; no facet totals claimed."],
    ["Google Scholar", "17 Sep 2026; SerpApi supplement", "140 retrieved; 99 cross-query unique; 49 matched current library and 50 unmatched. No persistent export.", "Supplementary only. Keep separate from the primary PRISMA snapshot until provenance and reconciliation are complete."],
    ["AJOL", "19 Sep 2026; blocked/not run", "Direct access returned HTTP 403; no hit count or export claimed.", "Do not imply AJOL was searched. Record compliant manual search if later available or retain the limitation."],
]
story.append(table(source_rows, [34 * mm, 42 * mm, 90 * mm, 103 * mm]))
story += [Spacer(1, 5 * mm), Paragraph("Gate B decision", styles["Subsection"]), Table([[status("CONDITIONALLY CLOSED", PALE_AMBER), p(
    "The source-audit subgate is closed with explicit limitations: completed sources are traceable; Scholar is supplementary; AJOL is blocked/not run; and WoS facet retries are rate-limited. This does not claim complete database coverage or authorize final PRISMA counts before Gate C reconciliation.",
    "Body",
)]], colWidths=[39 * mm, 230 * mm], style=TableStyle([
    ("BACKGROUND", (1, 0), (1, 0), PALE_AMBER),
    ("BOX", (0, 0), (-1, -1), 0.55, AMBER),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
]))]

# Page 4: canonicalisation
story += [PageBreak(), Paragraph("3. Canonical identity and screening reconciliation", styles["Section"]), Paragraph(
    "The canonical register is the current identity source. It is complete as a register, but decisions remain non-final because full-text assessment has not occurred and pre-collapse votes require explicit remapping or discard reasons.",
    styles["Body"],
)]
identity_rows = [
    ["Audit item", "Current result", "Interpretation"],
    ["Input rows", "2,288", "PubMed 140 + OpenAlex/Crossref 1,744 + Scopus 204 + ScienceDirect 25 + WoS 175."],
    ["Canonical identity groups", "1,845", "Symmetric DOI / PMID / normalized title-year matching; provisional identity groups."],
    ["Collapsed duplicate rows", "443", "Rows collapsed across the source layers; retain source lineage and title/year variants."],
    ["WoS cross-source QA", "151 matched; 24 provisional-new", "The 24-record queue is preserved separately for reconciliation; correction-parent linkage is recorded."],
    ["Decision distribution", "1,695 needs adjudication; 75 main candidate needs adjudication; 10 background provisional; 3 unclear; 62 exclude provisional", "All 1,845 final statuses remain non-final by design."],
    ["Upper-bound full-text queue", "160", "Historical upper bound only. It must be replaced by the reconciled candidate queue before PRISMA accounting."],
    ["Full-text / extraction / RoB", "0 / 0 / 0", "Downstream gates have not started."],
]
story.append(table(identity_rows, [52 * mm, 56 * mm, 161 * mm]))
story += [Spacer(1, 5 * mm), Paragraph("Required Gate C repairs", styles["Subsection"])]
for item in [
    "Remap every preliminary vote from raw records to canonical IDs; discard pre-collapse aggregate votes with a recorded reason where remapping is not defensible.",
    "Manually adjudicate the 31 title/year discrepancy groups and the 52 supplement, 33 Scopus, and 19 WoS rows lacking both DOI and PMID.",
    "Link WoS correction record WOS:000255508300044 to its parent article; do not treat it as an independent evidence record.",
    "Keep PMID 27677611 in the audit trail as a non-Nigeria Iran record; do not delete it silently.",
    "Rebuild the full-text queue from the canonical register and only then freeze the screening denominator.",
]:
    story.append(bullet(item))
story += [Spacer(1, 4 * mm), Table([[status("GATE C OPEN", PALE_RED), p(
    "Identity reconciliation is reproducible and the register is complete. Screening reconciliation remains open; no final inclusion count or final PRISMA screening count is claimable.",
    "Body",
)]], colWidths=[31 * mm, 238 * mm], style=TableStyle([
    ("BACKGROUND", (1, 0), (1, 0), PALE_RED),
    ("BOX", (0, 0), (-1, -1), 0.55, RED),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
]))]

# Page 5: next work and governance
story += [PageBreak(), Paragraph("4. Controlled completion roadmap", styles["Section"]), Paragraph(
    "The immediate objective is not to enlarge the provisional queue. It is to close the identity and screening controls so that every later result can be traced to a stable denominator and a source-backed decision.",
    styles["Body"],
)]
roadmap_rows = [
    ["Order", "Action", "Deliverable", "Stop condition"],
    ["1", "Close Gate B records", "Final source-disposition table, exact strings, source dates, export paths, and limitations.", "Every named source is completed, supplementary, blocked, or not run; no silent coverage claim."],
    ["2", "Close Gate C reconciliation", "Canonical screening denominator, source-lineage table, duplicate links, and remapped decisions.", "Every candidate has one identity and an explicit provisional/final screening state."],
    ["3", "Calibrate screening", "R1/R2 pilot decisions, disagreement memo, frozen operational rules.", "R2 verification and all-excludes recheck are completed before full screening."],
    ["4", "Complete full-text eligibility", "Retrieval register, T6 exclusions, included-study list, and duplicate-dataset map.", "Every candidate has a retrieval outcome and one evidence-based full-text decision."],
    ["5", "Pilot and complete extraction", "Reconciled five-study pilot, then T1-T5 study-level extraction.", "No essential field is blank; missing information is explicitly coded."],
    ["6", "Complete RoB and certainty", "JBI/custom molecular assessments and narrative certainty notes.", "Judgments are domain-based, traceable, and not score-summed."],
    ["7", "Synthesize with SWiM", "Temporal, geographic, host, molecular, clade, and reassortment synthesis.", "Subtypes, clades, reassortants, introductions, and local evolution remain distinct."],
    ["8", "Update the DOCX", "Methods, Results, PRISMA flow, tables/appendices, limitations, Discussion, and conclusions.", "Every claim traces to locked extraction and RoB evidence."],
    ["9", "Final audit", "PRISMA 2020, PRISMA-S, SWiM, DOI, reference, terminology, and reproducibility checks.", "Counts agree across text, tables, flow, appendices, and source records."],
]
story.append(table(roadmap_rows, [13 * mm, 55 * mm, 91 * mm, 108 * mm]))
story += [Spacer(1, 5 * mm), Paragraph("Reviewer governance", styles["Subsection"])]
roles = [
    ["Role", "Owner", "Control"],
    ["Reviewer 1", "Primary reviewer", "Primary screening, extraction, and synthesis lead."],
    ["Reviewer 2", "Epicurus independent Codex agent", "Independent verification pass and disagreement review; no credential access; no final promotion of decisions."],
    ["Arbiter", "Main Codex agent", "Resolves disagreements, checks source evidence, and approves gate transitions."],
    ["Methods reviewer", "TBD", "Reviews pooling decision, RoB, certainty, and synthesis claims."],
]
story.append(table(roles, [35 * mm, 58 * mm, 174 * mm]))
story += [Spacer(1, 5 * mm), Paragraph("Immediate next session", styles["Subsection"])]
for item in [
    "Read AGENTS.md, Workbench/49_NEXT_SESSION_HANDOFF.md, Workbench/15_RUN_LOG.md, and Workbench/53_CANONICAL_REGISTER.json.",
    "Rebuild and freeze the canonical screening queue; do not start extraction.",
    "Keep the manuscript DOCX unchanged until Gates A-F are passed and a paste-ready amendment is approved.",
]:
    story.append(bullet(item))

story += [Spacer(1, 4 * mm), HRFlowable(width="100%", thickness=1, color=GRID, spaceBefore=2, spaceAfter=5), Paragraph(
    "Prepared from the current Workbench records on 19 September 2026. This report separates verified, provisional, supplementary, blocked, and not-started work; it is not a final PRISMA flow diagram or final evidence synthesis.",
    styles["SmallMuted"],
)]

doc.build(story)
print(OUT)

