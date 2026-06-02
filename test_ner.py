from utils import extract_text_from_pdf
from ner import extract_entities

text = extract_text_from_pdf("sample.pdf")

entities = extract_entities(text)

print("\nPERSONS:")
print(entities["persons"][:10])

print("\nDATES:")
print(entities["dates"][:10])

print("\nLOCATIONS:")
print(entities["locations"][:10])

print("\nORGANIZATIONS:")
print(entities["organizations"][:10])