from transformers import pipeline

print("Loading summarization pipeline...")

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

print("Pipeline loaded successfully!")