import streamlit as st
from transformers import pipeline


@st.cache_resource
def load_model():

    return pipeline(
        "summarization",
        model="facebook/bart-large-cnn"
    )


summarizer_model = load_model()