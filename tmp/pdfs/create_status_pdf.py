from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, HRFlowable
)

ROOT = Path(r"D:\AvianInfluenzaSysRev")
OUT = ROOT / "output" / "pdf" / "AvianInfluenzaSysRev_Project_Status_Roadmap_2026-09-17.pdf"
OUT.parent.mkdir(parents=True, exist_ok=True)

PAGE_W, PAGE_H = landscape(A4)
MARGIN_X = 14 * mm
MARGIN_TOP = 18 * mm
MARGIN_BOTTOM = 14 * mm

NAVY = colors.HexColor("#16324F")
BLUE = colors.HexColor("#1F5F8B")
TEAL = colors.HexColor("#287D78")
GREEN = colors.HexColor("#2E7D5B")
AMBER = colors.HexColor("#A56700")
RED = colors.HexColor("#9B2C2C")
INK = colors.HexColor("#1F2933")
MUTED = colors.HexColor("#52606D")
PALE_BLUE = colors.HexColor("#EAF2F8")
PALE_TEAL = colors.HexColor("#E8F4F1")
PALE_GREEN = colors.HexColor("#EAF5EE")
PALE_AMBER = colors.HexColor("#FFF4D6")
PALE_RED = colors.HexColor("#FDECEC")
PALE_GREY = colors.HexColor("#F4F6F8")
GRID = colors.HexColor("#C7D0D9")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="CoverTitle", parent=styles["Title"], fontName="Helvetica-Bold",
    fontSize=25, leading=30, textColor=NAVY, alignment=TA_LEFT, spaceAfter=8
))
styles.add(ParagraphStyle(
    name="CoverSub", parent=styles["Normal"], fontName="Helvetica",
    fontSize=12, leading=17, textColor=MUTED, spaceAfter=6
))
styles.add(ParagraphStyle(
    name="Section", parent=styles["Heading1"], fontName="Helvetica-Bold",
    fontSize=16, leading=20, textColor=NAVY, spaceBefore=2, spaceAfter=7
))
styles.add(ParagraphStyle(
    name="Subsection", parent=styles["Heading2"], fontName="Helvetica-Bold",
    fontSize=11.5, leading=14, textColor=BLUE, spaceBefore=5, spaceAfter=4
))
styles.add(ParagraphStyle(
    name="BodySmall", parent=styles["BodyText"], fontName="Helvetica",
    fontSize=8.3, leading=10.5, textColor=INK, spaceAfter=3
))
styles.add(ParagraphStyle(
    name="Body", parent=styles["BodyText"], fontName="Helvetica",
    fontSize=9.2, leading=12.2, textColor=INK, spaceAfter=4
))
styles.add(ParagraphStyle(
    name="TableText", parent=styles["BodyText"], fontName="Helvetica",
    fontSize=7.45, leading=9.15, textColor=INK
))
styles.add(ParagraphStyle(
    name="TableTextBold", parent=styles["BodyText"], fontName="Helvetica-Bold",
    fontSize=7.45, leading=9.15, textColor=INK
))
styles.add(ParagraphStyle(
    name="TableHead", parent=styles["BodyText"], fontName="Helvetica-Bold",
    fontSize=7.5, leading=9.1, textColor=colors.white
))
styles.add(ParagraphStyle(
    name="Status", parent=styles["BodyText"], fontName="Helvetica-Bold",
    fontSize=7.2, leading=8.8, alignment=TA_CENTER, textColor=INK
))
styles.add(ParagraphStyle(
    name="SmallMuted", parent=styles["BodyText"], fontName="Helvetica",
    fontSize=7.3, leading=9.2, textColor=MUTED
))
styles.add(ParagraphStyle(
    name="Callout", parent=styles["BodyText"], fontName="Helvetica-Bold",
    fontSize=10, leading=13, textColor=NAVY
))

def P(text, style="TableText"):
    return Paragraph(str(text), styles[style])

def bullet(text):
    return Paragraph("&#8226; " + text, styles["BodySmall"])

def status(text, fill):
    return Table([[P(text, "Status")]], colWidths=[28 * mm], style=TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), fill),
        ("BOX", (0, 0), (-1, -1), 0.4, fill),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))

def data_table(rows, widths, header=True, row_bgs=None, font_size=None):
    rendered = []
    for r, row in enumerate(rows):
        rendered.append([x if hasattr(x, "wrap") else P(x, "TableHead" if header and r == 0 else "TableText") for x in row])
    cmds = [
        ("GRID", (0, 0), (-1, -1), 0.35, GRID),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]
    if header:
        cmds += [("BACKGROUND", (0, 0), (-1, 0), NAVY), ("TEXTCOLOR", (0, 0), (-1, 0), colors.white)]
        start = 1
    else:
        start = 0
    if row_bgs:
        for idx, bg in row_bgs.items():
            cmds.append(("BACKGROUND", (0, idx), (-1, idx), bg))
    else:
        for idx in range(start, len(rows)):
            if (idx - start) % 2 == 1:
                cmds.append(("BACKGROUND", (0, idx), (-1, idx), PALE_GREY))
    return Table(rendered, colWidths=widths, repeatRows=1 if header else 0, hAlign="LEFT", style=TableStyle(cmds))

def page_decor(canvas, doc):
    canvas.saveState()
    page = canvas.getPageNumber()
    canvas.setStrokeColor(GRID)
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN_X, PAGE_H - 10 * mm, PAGE_W - MARGIN_X, PAGE_H - 10 * mm)
    canvas.setFont("Helvetica-Bold", 7.4)
    canvas.setFillColor(NAVY)
    canvas.drawString(MARGIN_X, PAGE_H - 7.2 * mm, "AVIAN INFLUENZA NIGERIA SYSTEMATIC REVIEW")
    canvas.setFont("Helvetica", 7.2)
    canvas.setFillColor(MUTED)
    canvas.drawRightString(PAGE_W - MARGIN_X, PAGE_H - 7.2 * mm, "PROJECT STATUS AND COMPLETION ROADMAP")
    canvas.line(MARGIN_X, 9 * mm, PAGE_W - MARGIN_X, 9 * mm)
    canvas.setFont("Helvetica", 7.2)
    canvas.setFillColor(MUTED)
    canvas.drawString(MARGIN_X, 5.3 * mm, "As of 17 September 2026 | Prepared from the Workbench status record")
    canvas.drawRightString(PAGE_W - MARGIN_X, 5.3 * mm, f"Page {page}")
    canvas.restoreState()

doc = BaseDocTemplate(
    str(OUT), pagesize=landscape(A4), leftMargin=MARGIN_X, rightMargin=MARGIN_X,
    topMargin=MARGIN_TOP, bottomMargin=MARGIN_BOTTOM, title="Avian Influenza Nigeria Systematic Review - Project Status and Completion Roadmap",
    author="Avian Influenza Nigeria Systematic Review"
)
frame = Frame(MARGIN_X, MARGIN_BOTTOM, PAGE_W - 2 * MARGIN_X, PAGE_H - MARGIN_TOP - MARGIN_BOTTOM, id="main")
doc.addPageTemplates([PageTemplate(id="all", frames=[frame], onPage=page_decor)])

story = []

# Cover / executive status
story.append(Spacer(1, 12 * mm))
story.append(Paragraph("Avian Influenza Nigeria Systematic Review", styles["CoverTitle"]))
story.append(Paragraph("Formal project status, evidence position, and completion roadmap", styles["CoverSub"]))
story.append(Spacer(1, 3 * mm))
story.append(HRFlowable(width="100%", thickness=2, color=TEAL, spaceBefore=2, spaceAfter=10))
story.append(Paragraph("Purpose", styles["Subsection"]))
story.append(Paragraph(
    "This document records the formal workflow required to complete the review, distinguishes completed work from provisional or pending work, and sets out the controlled path from the current search/reconciliation stage to final reporting. It is a project-control document, not a substitute for the manuscript or the final PRISMA flow diagram.",
    styles["Body"]
))
summary = [
    [P("Current position", "TableTextBold"), P("Search and candidate-reconciliation stage. The evidence library is not yet locked for screening.", "TableText")],
    [P("Formal gates", "TableTextBold"), P("Gate A: operational snapshot recorded, but exact-string/source reconciliation remains open. Gate B: not passed. Gate C: not passed. Gates D onward: not started.", "TableText")],
    [P("Evidence available", "TableTextBold"), P("PubMed v3, Scopus, ScienceDirect, OpenAlex/Crossref supplement, and a separately dated SerpApi Google Scholar supplement. WoS and AJOL remain unresolved for the current snapshot.", "TableText")],
    [P("What has not begun", "TableTextBold"), P("Final deduplicated screening set, full-text eligibility, extraction, risk of bias, certainty assessment, SWiM synthesis, manuscript update, and final PRISMA/PRISMA-S audit.", "TableText")],
]
story.append(data_table(summary, [38 * mm, 218 * mm], header=False, row_bgs={0: PALE_BLUE, 1: PALE_AMBER, 2: PALE_TEAL, 3: PALE_RED}))
story.append(Spacer(1, 8 * mm))
story.append(Paragraph("Status key", styles["Subsection"]))
legend = [[status("COMPLETE", PALE_GREEN), P("Formally recorded and supported by an identified project artifact or run-log entry.", "BodySmall"),
           status("IN PROGRESS", PALE_BLUE), P("Work exists, but the gate or evidence set is not yet final.", "BodySmall")],
          [status("PENDING", PALE_AMBER), P("Requires a defined action before the next formal gate can pass.", "BodySmall"),
           status("BLOCKED / WAITING", PALE_RED), P("Dependent on external access, approval, or a source response.", "BodySmall")]]
story.append(Table(legend, colWidths=[31 * mm, 91 * mm, 37 * mm, 97 * mm], style=TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("LEFTPADDING", (0, 0), (-1, -1), 3),
    ("RIGHTPADDING", (0, 0), (-1, -1), 4), ("TOPPADDING", (0, 0), (-1, -1), 2),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
])))
story.append(Spacer(1, 5 * mm))
story.append(Paragraph("Controlling principle: protocol freeze -> search strings -> screening -> extraction pilot -> risk of bias -> SWiM synthesis -> reporting -> PRISMA / PRISMA-S / SWiM audit.", styles["Callout"]))

# Formal workflow
story.append(PageBreak())
story.append(Paragraph("1. Formal workflow: completed, pending, and gate position", styles["Section"]))
story.append(Paragraph("The sequence below is the authoritative project order. Screening must not start from the provisional queue until the search and canonical-reconciliation gate is closed.", styles["Body"]))
workflow_rows = [
    ["Phase / gate", "Required formal step", "Completed / evidenced", "Pending or blocker", "Status"],
    ["0 / Gate A", "Freeze question, scope, framework, eligibility, outcomes, review roles, and reporting standard.", "Question and scope locked: Nigeria AIV, 2006-2026; CoCoPop/PEO; PRISMA 2020, PRISMA-S, SWiM; no forced meta-analysis. Role design recorded: R1 primary, R2 independent 20% plus all-excludes recheck, R1 arbiter.", "Reconcile the protocol endpoint with the dated 16 September operational snapshot and record the amendment boundary clearly.", status("IN PROGRESS", PALE_BLUE)],
    ["1 / Gate B", "Freeze and execute database-specific search strings; preserve exact strings, dates, limits, exports, and exceptions.", "PubMed v3 and manual Scopus/ScienceDirect searches recorded. OpenAlex/Crossref supplement recorded. SerpApi Scholar supplement recorded separately.", "Exact-string/source reconciliation remains open. WoS has no query/export because documents are disabled pending subscription. AJOL automation returned 403. Direct Scholar returned 429.", status("PENDING", PALE_AMBER)],
    ["2 / Gate C", "Create the canonical library; deduplicate; reconcile DOI, PMID, and title-year identities; lock the screening denominator.", "Mechanical audit completed across 2,161 input rows and 1,869 canonical components; 174 cross-source components under DOI -> PMID -> normalized title-year rule. No identifier conflicts under that rule.", "Stored overlap fields need remapping. The provisional upper-bound queue is not the final screening denominator. Current set must be frozen after source decisions and unresolved matches are adjudicated.", status("PENDING", PALE_AMBER)],
    ["3 / Gate D", "Pilot title/abstract screening and calibrate inclusion/exclusion rules.", "Preliminary title/abstract decisions exist for the PubMed v3 working set; these are not yet a locked, full multi-source screening set.", "Apply the frozen rules to the canonical library; run R2 verification on the defined 20% sample and all exclusions; resolve disagreements before full screening.", status("NOT STARTED", PALE_GREY)],
    ["4 / Gate E", "Complete title/abstract screening and retrieve full texts.", "No final multi-source screening denominator or final full-text set has been locked.", "Screen all records; log reasons for exclusion at full text; preserve inaccessible or awaiting-classification records in the audit trail.", status("NOT STARTED", PALE_GREY)],
    ["5 / Gate F", "Pilot and complete structured data extraction.", "Extraction has not begun. The planned extraction domains are defined conceptually in the project workflow.", "Pilot the form on a small set; extract study design, setting, host, dates, sampling, positivity, subtype, clade, reassortment, phylogeny, geography, and surveillance context.", status("NOT STARTED", PALE_GREY)],
    ["6 / Gate G", "Assess risk of bias and certainty without score-summing.", "No final RoB or certainty assessments have been completed.", "Use JBI prevalence/cross-sectional/cohort tools plus the custom molecular checks; provide narrative certainty using prognosis-style logic and identify evidence gaps.", status("NOT STARTED", PALE_GREY)],
    ["7 / Gate H", "Synthesize evidence using SWiM; use meta-analysis only if the data justify it.", "No synthesis has been performed.", "Build study-level evidence tables; synthesize temporal, geographic, host, molecular, clade, and reassortment patterns; do not conflate subtype, clade, reassortant, and introduction.", status("NOT STARTED", PALE_GREY)],
    ["8 / Gate I", "Update the manuscript and in-document tables/appendices.", "Source manuscript remains untouched; no final results have been inserted.", "Update methods, PRISMA flow, results, evidence tables, limitations, discussion, and conclusions only after the library and synthesis are locked.", status("NOT STARTED", PALE_GREY)],
    ["9 / Gate J", "Complete PRISMA 2020, PRISMA-S, SWiM, reference, and reproducibility audit.", "No final audit has been completed.", "Check every checklist item, search appendix, flow count, citation, DOI, terminology distinction, and dated amendment before submission.", status("NOT STARTED", PALE_GREY)],
]
story.append(data_table(workflow_rows, [20 * mm, 49 * mm, 77 * mm, 94 * mm, 29 * mm], header=True))

# Search source status
story.append(PageBreak())
story.append(Paragraph("2. Search-source status and formal implications", styles["Section"]))
story.append(Paragraph("Counts below are operational records, not a final deduplicated evidence count. The 16 September 2026 snapshot and the 17 September Google Scholar/API updates must remain separately dated.", styles["Body"]))
search_rows = [
    ["Source", "Date / method", "Current evidence", "Formal status", "Required next action"],
    ["PubMed / MEDLINE", "16 Sep 2026; NLM E-utilities; v3", "140 base records; 53 molecular subset. Working screening notes include 142 screened records when two v1-only items are counted.", status("RECORDED", PALE_GREEN), "Preserve the exact v3 strings and export provenance; carry eligible and excluded decisions into the final canonical library."],
    ["Scopus", "16 Sep 2026; manual export", "204 records in the manual import.", status("RECORDED", PALE_GREEN), "Validate the export metadata and reconcile against the canonical DOI/PMID/title-year identity table."],
    ["ScienceDirect", "16 Sep 2026; manual export", "25 displayed/exported records.", status("RECORDED", PALE_GREEN), "Retain the search wording, date, filters, and export; reconcile with the canonical library."],
    ["OpenAlex / Crossref", "Supplement; raw files 41/42", "1,744 canonical supplement records after local processing; 1,627 were novel versus the PubMed working set under the prior comparison.", status("SUPPLEMENT", PALE_BLUE), "Use only after identifier remapping; do not present this supplement as a replacement for a locked database search without a documented amendment."],
    ["Google Scholar via SerpApi", "17 Sep 2026; dated update supplement", "140 raw rows; 99 cross-query canonical groups; 49 matched the current library and 50 remain unmatched. Direct Scholar was rate-limited (429).", status("SUPPLEMENT", PALE_BLUE), "Complete executed-string/filter reconciliation and adjudicate the 50 unmatched groups before deciding whether to merge or retain as an update search."],
    ["Web of Science", "17 Sep 2026; Clarivate portal / CLI attempt", "No query, hit set, or export. Free Trial API subscription request is pending; portal view reached but Documents were disabled.", status("BLOCKED / WAITING", PALE_RED), "Wait for approval; if granted, run the frozen WoS string and preserve API version, key plan, date, request count, and export. If not granted, document the non-search transparently and use a pre-submission update."],
    ["AJOL", "Manual/automation attempt", "Automation returned 403; no validated hit set or export in the current snapshot.", status("BLOCKED / WAITING", PALE_RED), "Run a compliant manual search/export if access is available; otherwise record the failed access attempt and pre-submission update plan."],
]
story.append(data_table(search_rows, [29 * mm, 34 * mm, 71 * mm, 29 * mm, 106 * mm], header=True))
story.append(Spacer(1, 5 * mm))
story.append(Paragraph("Interpretation rule", styles["Subsection"]))
story.append(Paragraph("The review may proceed only after the project records one of two defensible decisions: (1) complete WoS/AJOL access and merge their results into the current search set, or (2) formally document the access limitation and treat them as a dated pre-submission update rather than silently implying that they were searched.", styles["Body"]))

# Reconciliation
story.append(PageBreak())
story.append(Paragraph("3. Evidence-library reconciliation: current numbers and controls", styles["Section"]))
story.append(Paragraph("These figures describe the current audit state. They should not be copied into the PRISMA flow until the canonical library, screening denominator, and exclusion reasons are frozen.", styles["Body"]))
recon_rows = [
    ["Audit item", "Current result", "Meaning / control"],
    ["Input rows audited", "2,161 rows", "PubMed 188 + supplement 1,744 + manual 229. This is an input total, not a unique-study total."],
    ["Canonical components", "1,869", "Sequential DOI -> PMID -> normalized title-year grouping. Use as a reconciliation estimate only until adjudication is complete."],
    ["Cross-source components", "174", "Components containing records from more than one source under the identity rule."],
    ["Identifier conflicts", "None detected under the current rule", "Still review title-year collisions and incomplete identifiers; absence of a conflict is not proof of perfect matching."],
    ["Supplement-to-PubMed matching", "124 supplement records matched", "113 by DOI and 11 by PMID; 117 stored true flags were present, but stored overlap fields require remapping."],
    ["Manual-to-PubMed matching", "127 manual records matched", "115 by DOI and 12 by title-year; stored true flags were zero, so stored overlap metadata is not trusted."],
    ["SerpApi Scholar update", "140 rows -> 99 canonical groups", "49 matched current library; 50 unmatched pending title/abstract review. No eligibility decisions changed."],
    ["Provisional queue", "160 upper-bound items", "Not final. Do not use for PRISMA counts or begin definitive screening from it until Gate C is passed."],
]
story.append(data_table(recon_rows, [46 * mm, 46 * mm, 177 * mm], header=True))
story.append(Spacer(1, 6 * mm))
story.append(Paragraph("Data-quality safeguards before screening", styles["Subsection"]))
for t in [
    "Recompute source overlap from identifiers rather than trusting legacy overlap fields.",
    "Inspect title-year matches manually where DOI and PMID are absent or ambiguous.",
    "Keep Iran and other non-Nigeria records in the audit trail as exclusions; for example, PMID 27677611 is not Nigeria-specific.",
    "Do not infer eligibility from an AIV keyword alone; apply the Nigeria-specific eligibility anchor.",
    "Keep the dated SerpApi supplement separate until its executed query strings, filters, and merge decisions are documented.",
]:
    story.append(bullet(t))

# Roadmap
story.append(PageBreak())
story.append(Paragraph("4. Completion roadmap from the current position", styles["Section"]))
story.append(Paragraph("The roadmap begins at canonical reconciliation and ends at a submission-ready manuscript. Each stage has an explicit output and a stop condition so that unresolved search access does not become an undocumented methodological assumption.", styles["Body"]))
road_rows = [
    ["Order", "Next controlled action", "Required output", "Exit condition"],
    ["1", "Close Gate B: reconcile exact strings, dates, filters, export provenance, and source exceptions; decide WoS/AJOL disposition.", "Database search log and amendment note with all source statuses.", "Every named source is either searched and exported or transparently recorded as inaccessible/pending."],
    ["2", "Close Gate C: recompute canonical identity mapping and adjudicate ambiguous title-year matches, including the 50 unmatched Scholar groups.", "Locked candidate library, deduplication log, and denominator memo.", "One record-level identity and source-membership decision for every candidate."],
    ["3", "Pilot title/abstract screening with frozen eligibility rules.", "Calibration memo; pilot disagreements; final operational inclusion/exclusion rules.", "R1/R2 agreement is acceptable and all rule changes are recorded before full screening."],
    ["4", "Complete title/abstract screening and retrieve full texts.", "Screening log and full-text inventory.", "All candidates have a decision or an explicit awaiting-status; full-text exclusions have reasons."],
    ["5", "Pilot extraction, then extract all included studies.", "Study-level extraction table inside the manuscript workflow; versioned extraction decisions.", "Pilot corrections are incorporated and every included study has complete or explicitly missing fields."],
    ["6", "Complete RoB and narrative certainty assessment.", "JBI/custom molecular assessments and evidence-gap narrative.", "No score-sums; judgments are domain-based and traceable to study information."],
    ["7", "Conduct SWiM synthesis and decide whether any quantitative pooling is defensible.", "Evidence tables, structured narrative synthesis, and any justified quantitative summaries.", "Synthesis matches data structure; subtype, clade, reassortant, and introduction are not conflated."],
    ["8", "Update the single source manuscript and in-document appendices/tables.", "Revised DOCX with methods, results, flow, tables, limitations, and discussion.", "All claims trace to the locked library and extraction/RoB records."],
    ["9", "Run final PRISMA 2020, PRISMA-S, SWiM, reference, DOI, and terminology audit.", "Submission-ready manuscript and completed checklist evidence.", "All checklist items pass; counts agree across text, tables, flow, and appendices."],
]
story.append(data_table(road_rows, [15 * mm, 75 * mm, 78 * mm, 101 * mm], header=True))
story.append(Spacer(1, 6 * mm))
story.append(Table([[P("Immediate next action", "TableHead"), P("Complete the canonical reconciliation memo and the Gate B source-disposition decision before any definitive screening work. This is the project bottleneck and the next auditable deliverable.", "Body")]], colWidths=[38 * mm, 231 * mm], style=TableStyle([
    ("BACKGROUND", (0, 0), (0, 0), BLUE), ("BACKGROUND", (1, 0), (1, 0), PALE_BLUE),
    ("BOX", (0, 0), (-1, -1), 0.6, BLUE), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
])))

# Gates and governance
story.append(PageBreak())
story.append(Paragraph("5. Decision gates, risks, and governance controls", styles["Section"]))
gate_rows = [
    ["Gate", "Pass criteria", "Current result", "Control if not passed"],
    ["A - protocol / scope", "Question, eligibility, dates, framework, roles, and reporting standard are frozen.", "Operationally recorded; amendment boundary still needs one clean final note.", "Do not change eligibility or start definitive screening without recording the amendment."],
    ["B - search completeness", "Every planned source has an exact string, date, filter, export, and access outcome.", "Not passed: WoS pending; AJOL 403; Scholar direct 429; SerpApi update needs reconciliation.", "Document access limitation and dated update plan; no silent substitution of sources."],
    ["C - canonical library", "All source records mapped, duplicates resolved, and screening denominator locked.", "Not passed: overlap metadata remapping and provisional queue remain open.", "No definitive PRISMA counts or full screening until the denominator memo is approved."],
    ["D - screening calibration", "Pilot decisions stable; R2 verification and all-excludes recheck complete.", "Not started for the final canonical library.", "Freeze the rulebook before full screening; record disagreements and resolutions."],
    ["E-J - downstream", "Full text, extraction, RoB, synthesis, manuscript, and audit are complete and internally consistent.", "Not started.", "Do not populate final results from provisional counts or unverified candidate decisions."],
]
story.append(data_table(gate_rows, [30 * mm, 77 * mm, 78 * mm, 84 * mm], header=True))
story.append(Spacer(1, 6 * mm))
risk_rows = [
    ["Risk", "Why it matters", "Mitigation"],
    ["Pending WoS approval", "The planned source is not yet searched in the current snapshot and its Starter API subscription is pending.", "Retain portal evidence; wait for approval within the project decision window; otherwise record transparent non-access and a pre-submission update."],
    ["AJOL access failure", "A 403 means no validated AJOL result set exists in the current snapshot.", "Use compliant manual access if available; otherwise preserve the failed-attempt record and avoid implying completion."],
    ["Search-date mismatch", "The protocol endpoint and operational snapshot are not identical.", "Keep the actual snapshot date; record the endpoint/amendment distinction in the methods and search appendix."],
    ["Legacy overlap fields", "Stored flags do not consistently reproduce independent identity matching.", "Recompute all overlaps from DOI, PMID, and normalized title-year identity; treat old flags as non-authoritative."],
    ["Premature screening", "Screening a provisional queue can bias the final denominator and PRISMA flow.", "Gate C must pass before definitive screening; preliminary decisions remain provisional."],
]
story.append(data_table(risk_rows, [36 * mm, 88 * mm, 145 * mm], header=True))

# Audit trail / handoff
story.append(PageBreak())
story.append(Paragraph("6. Formal record and handoff checklist", styles["Section"]))
story.append(Paragraph("The following artifacts are the evidence base for this status report. They should remain the controlling project record unless a later dated amendment supersedes them.", styles["Body"]))
artifact_rows = [
    ["Artifact", "Role in project control"],
    ["Workbench/13_WORKFLOW_prospective.md", "Protocol and prospective workflow; records the operational reviewer-role design."],
    ["Workbench/15_RUN_LOG.md", "Dated run log, gate re-audit, search-source statuses, amendments, and current decisions."],
    ["Workbench/11_Phase1_search_rebuild_DRAFT.md", "Draft search architecture and database-specific line structure; not yet the final reconciled search appendix."],
    ["Workbench/45_MANUAL_DB_CHECKLISTS.md", "Frozen historical/manual checklist for Scopus, WoS, ScienceDirect, Scholar, and AJOL."],
    ["Workbench/46_DEDUP_COLLAPSED.json", "Current supplement records used in the mechanical identity audit."],
    ["Workbench/47_MANUAL_IMPORT_candidates.json", "Current Scopus/ScienceDirect manual import records used in the audit."],
    ["Workbench/49_NEXT_SESSION_HANDOFF.md", "Next-session gates and safe continuation instructions."],
    ["Workbench/50_END_TO_END_WORKPLAN.md", "End-to-end phase plan and current project-position summary."],
    ["Avian_review_paper_fellow.docx", "Single manuscript source of truth; not yet updated with final search, screening, or synthesis results."],
]
story.append(data_table(artifact_rows, [78 * mm, 191 * mm], header=True))
story.append(Spacer(1, 6 * mm))
story.append(Paragraph("Next-session acceptance checklist", styles["Subsection"]))
check_items = [
    "Confirm this status report against the latest run log and note any new external response from Clarivate or AJOL.",
    "Produce the canonical reconciliation memo with record-level source membership and unresolved-match decisions.",
    "Finalize the Gate B decision for WoS, AJOL, and the SerpApi Scholar supplement.",
    "Approve or revise the screening denominator; only then begin the controlled screening phase.",
    "Keep the manuscript unchanged until the canonical library and screening rules are formally locked.",
]
for i, t in enumerate(check_items, 1):
    story.append(P(f"{i}. {t}", "BodySmall"))
story.append(Spacer(1, 4 * mm))
story.append(HRFlowable(width="100%", thickness=1, color=GRID, spaceBefore=2, spaceAfter=6))
story.append(Paragraph("Prepared status: 17 September 2026. This report deliberately separates completed evidence from provisional, pending, and blocked work so that the review can progress without overstating search completeness or study eligibility.", styles["SmallMuted"]))

doc.build(story)
print(OUT)
