import re


def extract_metadata(text):

    metadata = {}

    lines = text.split("\n")

    metadata["case_name"] = lines[0] if lines else "Unknown"

    date_match = re.search(
        r'\d{1,2}\s+[A-Za-z]+\s*,?\s*\d{4}',
        text
    )

    if date_match:
        metadata["date"] = date_match.group()
    else:
        metadata["date"] = "Not Found"

    return metadata