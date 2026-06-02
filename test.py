from utils import extract_text_from_pdf, clean_text

pdf_path = "sample.pdf"

text = extract_text_from_pdf(pdf_path)

cleaned = clean_text(text)

print(cleaned[:2000])