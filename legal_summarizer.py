from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6n"
)


def summarize_section(text):

    if len(text.strip()) < 100:
        return "Section not found."

    text = text[:2500]

    result = summarizer(
        text,
        max_length=100,
        min_length=30,
        do_sample=False
    )

    return result[0]["summary_text"]