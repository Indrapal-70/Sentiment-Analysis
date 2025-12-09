import streamlit as st
import sys
import os
print(f"Executable: {sys.executable}")
print(f"Path: {sys.path}")
import pickle
import tensorflow as tf
try:
    import tensorflow.keras
except ImportError as e:
    print(f"Explicit import failed: {e}")


with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

st.title("Sentiment Analysis")

# Get user input
user_review = st.text_area("Enter your movie review:")

if st.button("Analyze"):
    if user_review:
        sequence = tokenizer.texts_to_sequences([user_review])
        padded_sequence = pad_sequences(sequence, maxlen=200)

        prediction = model.predict(padded_sequence)[0][0]

        if prediction > 0.5:
            st.success("Positive Sentiment")
        else:
            st.error("Negative Sentiment")
    else:
        st.warning("Please enter a review.")
