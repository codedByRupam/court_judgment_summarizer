from model_loader import summarizer_model


def generate_bullets(text):

    text = text[:4000]

    result = summarizer_model(
        text,
        max_length=180,
        min_length=80,
        do_sample=False
    )[0]["summary_text"]

    sentences = result.split(".")

    bullets = []

    for sentence in sentences[:5]:

        sentence = sentence.strip()

        if len(sentence) > 10:
            bullets.append("• " + sentence)

    return bullets