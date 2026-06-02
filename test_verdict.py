from utils import extract_text_from_pdf
from verdict import extract_verdict

text = extract_text_from_pdf("sample.pdf")

print(extract_verdict(text))