import streamlit as st
from transformers import pipeline


@st.cache_resource
def load_model():

    return pipeline(
        "summarization",
        model="sshleifer/distilbart-cnn-12-6"
    )


summarizer_model = load_model()