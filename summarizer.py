from model_loader import summarizer_model

def summarize_text(text):

    text = text[:3000]

    result = summarizer_model(
        text,
        max_length=150,
        min_length=50,
        do_sample=False
    )

    return result[0]["summary_text"]