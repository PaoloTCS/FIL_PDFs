import os, csv, pathlib, PyPDF2, pandas as pd

PDF_DIR = pathlib.Path(".")
rows = []

for pdf in sorted(PDF_DIR.glob("*.pdf")):
    try:
        reader = PyPDF2.PdfReader(open(pdf, "rb"))
        pages = len(reader.pages)
        text0 = reader.pages[0].extract_text() or ""
        first = text0.strip().split("\n")[0][:120]
    except Exception as e:
        pages, first = 0, f"Error: {e}"
    # rudimentary tagging rules
    tags = []
    name = pdf.name.lower()
    if "lightcone" in name or "curvature" in name: tags += ["geometry"]
    if "bound" in name or "accelleration" in name: tags += ["bounds"]
    if "mask" in name or "shadow" in name or "gaussian" in name: tags += ["dynamics"]
    if "particle" in name or "big bang" in name: tags += ["physical"]
    if "comput" in name: tags += ["computational"]
    if not tags: tags = ["foundations"]
    rows.append([pdf.name, pages, first, ",".join(tags)])

# CSV
with open("catalog/catalog.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["File", "Pages", "FirstSnippet", "Tags"])
    writer.writerows(rows)

# Markdown prettified
md_lines = ["# FIL_PDFs Catalog  (" + str(len(rows)) + " files)\n",
            "| # | PDF | Pages | First-line snippet | Tags |",
            "|---|-----|-------|--------------------|------|"]
for i, r in enumerate(rows, 1):
    md_lines.append(f"| {i} | {r[0]} | {r[1]} | {r[2]} | {r[3]} |")
with open("catalog/catalog.md", "w") as f:
    f.write("\n".join(md_lines))
print("Catalog built → catalog/catalog.csv & catalog/catalog.md")
