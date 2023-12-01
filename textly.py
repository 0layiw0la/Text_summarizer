import nltk
from transformers import pipeline
import streamlit as st

# Function to summarize text
def summarize(text):
    text = str(text)
    if len(text.split(" ")) > 700:
        return "Input too long"
    else:
        # Download the summarization model
        @st.cache_resource
        summarizer = pipeline('summarization')
        # Generate summary
        sum_result = summarizer(text, max_length=500, min_length=20, do_sample=True)
        return sum_result[0]['summary_text']

# Function to perform sentiment analysis
@st.cache_resource
def sentiment(text):
    nltk.download('vader_lexicon')
    from nltk.sentiment import SentimentIntensityAnalyzer
    text = str(text)
    sia = SentimentIntensityAnalyzer()
    sent = sia.polarity_scores(text)
    if sent['pos'] > 0.1 and (sent['pos'] > sent['neg']):
        sentiment_label = 'Positive'
    elif (sent['neg'] > 0.1) and (sent['neg'] > sent['pos']):
        sentiment_label = 'Negative'
    elif sent['neu'] > 0.8:
        sentiment_label = 'Neutral'
    else:
        sentiment_label = 'Neutral'
    return sentiment_label
