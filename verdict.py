import re

def extract_verdict(text):

    patterns = [
        r"petition is dismissed",
        r"petition stands dismissed",
        r"writ petition is dismissed",
        r"appeal is dismissed",

        r"petition is allowed",
        r"petition stands allowed",
        r"writ petition is allowed",
        r"appeal is allowed",

        r"disposed of"
    ]

    text = text.lower()

    for pattern in patterns:

        match = re.search(pattern, text)

        if match:
            return match.group()

    return "Verdict not detected"