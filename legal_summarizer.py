from model_loader import summarizer_model

def summarize_section(text):

    if len(text.strip()) < 100:
        return "Section not found."

    text = text[:2000]

    result = summarizer_model(
        text,
        max_length=100,
        min_length=30,
        do_sample=False
    )

    return result[0]["summary_text"]