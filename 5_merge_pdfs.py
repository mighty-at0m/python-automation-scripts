from pathlib import Path
from pypdf import PdfWriter

FOLDER = Path("invoices")
OUTPUT = "merged.pdf"

writer = PdfWriter()
for pdf in sorted(FOLDER.glob("*.pdf")):
    writer.append(pdf)
    print("added", pdf.name)

writer.write(OUTPUT)
print("Saved", OUTPUT, "with", len(writer.pages), "pages")
writer.close()
