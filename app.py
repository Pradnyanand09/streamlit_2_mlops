import streamlit as st
from textblob import TextBlob

# Streamlit app setup
st.title("Basic Sentiment Analysis App")
st.write("Enter some text below, and I'll analyze the sentiment!")

# Input from user
user_input = st.text_area("Enter Text:", height=150)

if user_input:
    # Perform Sentiment Analysis
    blob = TextBlob(user_input)
    sentiment = blob.sentiment.polarity

    # Determine sentiment
    if sentiment > 0:
        st.success("The sentiment is Positive! 😊")
    elif sentiment < 0:
        st.error("The sentiment is Negative. 😢")
    else:
        st.warning("The sentiment is Neutral. 😐")
