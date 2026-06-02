from model_loader import summarizer_model


def chunk_text(text, chunk_size=2000):

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks


def summarize_text(text):

    chunks = chunk_text(text)

    final_summary = []

    for chunk in chunks[:5]:

        try:

            result = summarizer_model(
                chunk,
                max_length=120,
                min_length=40,
                do_sample=False
            )

            final_summary.append(
                result[0]["summary_text"]
            )

        except Exception:
            pass

    return "\n".join(final_summary)