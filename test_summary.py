from utils import extract_text_from_pdf, clean_text
from summarizer import summarize_text

pdf_path = "sample.pdf"

text = extract_text_from_pdf(pdf_path)

text = clean_text(text)

summary = summarize_text(text)

print("\nSUMMARY:\n")
print(summary)