from transformers import pipeline

print("Loading summarization pipeline...")

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

print("Pipeline loaded successfully!")