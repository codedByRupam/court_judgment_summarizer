from model_loader import summarizer_model

def generate_bullets(text):

    text = text[:3000]

    result = summarizer_model(
        text,
        max_length=150,
        min_length=50,
        do_sample=False
    )[0]["summary_text"]

    bullets = []

    for sentence in result.split("."):
        sentence = sentence.strip()

        if len(sentence) > 10:
            bullets.append("• " + sentence)

    return bullets[:5]