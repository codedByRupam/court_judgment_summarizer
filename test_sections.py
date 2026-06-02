from utils import extract_text_from_pdf
from section_extractor import extract_sections
from legal_summarizer import summarize_section

text = extract_text_from_pdf("sample.pdf")

sections = extract_sections(text)

print("\nFACTS\n")
print(summarize_section(sections["facts"]))

print("\nPETITIONER ARGUMENTS\n")
print(summarize_section(sections["petitioner"]))

print("\nRESPONDENT ARGUMENTS\n")
print(summarize_section(sections["respondent"]))

print("\nCOURT REASONING\n")
print(summarize_section(sections["reasoning"]))

print("\nVERDICT\n")
print(sections["verdict"])