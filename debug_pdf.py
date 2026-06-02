import fitz
import os

pdf_path = "sample.pdf"

print("Exists:", os.path.exists(pdf_path))
print("Size:", os.path.getsize(pdf_path))

doc = fitz.open(pdf_path)

print("Number of pages:", len(doc))

text = doc[0].get_text()

print("\nFirst 500 characters:\n")
print(text[:500])