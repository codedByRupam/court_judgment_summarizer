import fitz
import re


def extract_text_from_pdf(pdf_path):

    # Open PDF document
    doc = fitz.open(pdf_path)

    text = ""

    # Read every page
    for page in doc:

        # Extract text from page
        text += page.get_text()

    return text



def clean_text(text):

    # Remove multiple newlines
    text = re.sub(r'\n+', '\n', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    # Remove leading/trailing spaces
    text = text.strip()

    return text