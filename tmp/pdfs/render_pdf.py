from pathlib import Path
import pdfplumber
import pypdfium2 as pdfium

root = Path(r"D:\AvianInfluenzaSysRev")
pdf_path = root / "output" / "pdf" / "AvianInfluenzaSysRev_Project_Status_Roadmap_2026-09-17.pdf"
out_dir = root / "tmp" / "pdfs" / "rendered"
out_dir.mkdir(parents=True, exist_ok=True)

with pdfplumber.open(str(pdf_path)) as pdf:
    print(f"pages={len(pdf.pages)}")
    full_text = "\n".join((page.extract_text() or "") for page in pdf.pages)
    for term in ["Current position", "Gate B", "canonical library", "Completion roadmap", "Clarivate", "PRISMA"]:
        print(f"contains[{term}]={term in full_text}")

pdf = pdfium.PdfDocument(str(pdf_path))
for idx in range(len(pdf)):
    page = pdf[idx]
    bitmap = page.render(scale=1.6)
    bitmap.to_pil().save(out_dir / f"page-{idx+1:02d}.png")
    page.close()
pdf.close()
print(out_dir)
