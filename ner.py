import spacy

nlp = spacy.load("en_core_web_sm")


def extract_entities(text):

    doc = nlp(text[:50000])

    entities = {
        "persons": [],
        "organizations": [],
        "dates": [],
        "locations": []
    }

    for ent in doc.ents:

        if ent.label_ == "PERSON":
            entities["persons"].append(ent.text)

        elif ent.label_ == "ORG":
            entities["organizations"].append(ent.text)

        elif ent.label_ == "DATE":
            entities["dates"].append(ent.text)

        elif ent.label_ in ["GPE", "LOC"]:
            entities["locations"].append(ent.text)

    # Remove duplicates and junk values
    for key in entities:

        entities[key] = list(set(entities[key]))

        entities[key] = [
            entity
            for entity in entities[key]
            if len(entity.strip()) > 2
        ]

    return entities