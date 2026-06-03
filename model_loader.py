import streamlit as st
import transformers
from transformers import pipeline

print("Transformers version:", transformers.__version__)

@st.cache_resource
def load_model():
    return pipeline(
        task="summarization",
        model="sshleifer/distilbart-cnn-12-6"
    )

summarizer_model = load_model()