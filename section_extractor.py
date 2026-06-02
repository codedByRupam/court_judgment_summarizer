import re


def find_section(text, keywords, window=4000):

    text_lower = text.lower()

    for keyword in keywords:

        pos = text_lower.find(keyword)

        if pos != -1:
            return text[pos:pos + window]

    return ""


def extract_sections(text):

    sections = {}

    sections["facts"] = find_section(
        text,
        [
            "this petition has been filed",
            "brief facts",
            "facts giving rise",
            "the case of the petitioner",
            "the petitioner claims"
        ]
    )

    sections["petitioner"] = find_section(
        text,
        [
            "learned counsel for the petitioner",
            "petitioner submitted",
            "petitioner contended",
            "the petitioner submits",
            "according to the petitioner"
            "learned counsel for the petitioner",
            "counsel for the petitioner submitted",
            "it is submitted by the petitioner",
        ]
    )

    sections["respondent"] = find_section(
    text,
    [
        "learned counsel for the respondent",
        "respondent submitted",
        "respondent contended",
        "the state submitted",
        "according to the respondent",

        "learned government advocate",
        "standing counsel submitted",
        "counsel appearing for the state"
    ]
)

    sections["reasoning"] = find_section(
    text,
    [
        "i have heard",
        "we have heard",
        "after hearing",
        "having heard",
        "this court finds",
        "this court is of the view",
        "it appears",
        "upon consideration",

        "this court observes",
        "this court holds",
        "considering the submissions",
        "on perusal of the records"
    ]
)

    sections["verdict"] = find_section(
        text,
        [
            "petition is dismissed",
            "petition is allowed",
            "writ petition is dismissed",
            "writ petition is allowed",
            "appeal is dismissed",
            "appeal is allowed",
            "stands disposed of"
        ],
        window=1200
    )

    return sections