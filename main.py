# prompt: give me streamlit code to deploy the model on web such that it takes user input as review and gives out result as positive or negative

import streamlit as st
import pickle
import tensorflow as tf


# Load the model and tokenizer
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

# Define the Streamlit app
st.title("Sentiment Analysis")

# Get user input
user_review = st.text_area("Enter your movie review:")

if st.button("Analyze"):
    if user_review:
        # Preprocess the review
        sequence = tokenizer.texts_to_sequences([user_review])
        padded_sequence = tf.keras.preprocessing.sequence(sequence, maxlen=200)

        # Make prediction
        prediction = model.predict(padded_sequence)[0][0]

        # Display the result
        if prediction > 0.5:
            st.success("Positive Sentiment")
        else:
            st.error("Negative Sentiment")
    else:
        st.warning("Please enter a review.")
