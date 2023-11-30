import nltk
from transformers import pipeline
summarizer = pipeline('summarization')
def summarize(text):
    text = str(text)
    if len(text.split(" ")) > 1000:
        return "Input too long"
    else:
        short_text = summarizer(text,max_length = 500, min_length=20,do_sample=True)
        return str(short_text)
    
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

        
    
