import nltk
from transformers import pipeline, AutoModelForQuestionAnswering, AutoTokenizer
import streamlit as st
import docx
from PyPDF2 import PdfReader

@st.cache_resource
def load_model():
    return pipeline('summarization')
# Function to summarize text

def extract_text_from_txt(file):
    text = str(file.read())
    return text

def extract_text_from_docx(file):
    doc = docx.Document(file)
    full_text = ""
    for para in doc.paragraphs:
        full_text += para.text + "\n"
    return full_text

def extract_text_from_pdf(file):
    pdf_reader = PdfReader(file)
    full_text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        full_text += page.extract_text() + "\n"
    return full_text
    
def summarize(text,max_value=350,min_value=50):
    text = text.replace('.','.<eos>')
    text = text.replace('?','?<eos>')
    text = text.replace('!','!<eos>')
    max_chunk = 600
    sentences = text.split('<eos>')
    current_chunk = 0 
    chunks = []
    for sentence in sentences:
        if len(chunks) == current_chunk + 1: 
            if len(chunks[current_chunk]) + len(sentence.split(' ')) < max_chunk:
                chunks[current_chunk].extend(sentence.split(' '))
            else:
                current_chunk += 1
                chunks.append(sentence.split(' '))
        else:
            chunks.append(sentence.split(' '))
    for chunk_id in range(len(chunks)):
        chunks[chunk_id] = ' '.join(chunks[chunk_id])
    summarizer = load_model()
    summary = []
    for i in chunks:
        sumr = summarizer(i,max_length=max_value,min_length=min_value,do_sample=False)[0]['summary_text']
        summary.append(sumr)
    return ' '.join(summary)

# Function to perform sentiment analysis

def sentiment(text):
    nltk.download('vader_lexicon')
    from nltk.sentiment import SentimentIntensityAnalyzer
    text = str(text)
    sia = SentimentIntensityAnalyzer()
    sent = sia.polarity_scores(text)
    if sent['pos'] > 0.15 and (sent['pos'] > sent['neg']):
        sentiment_label = 'Positive'
    elif (sent['neg'] > 0.15) and (sent['neg'] > sent['pos']):
        sentiment_label = 'Negative'
    elif sent['neu'] > 0.8:
        sentiment_label = 'Neutral'
    else:
        sentiment_label = 'Neutral'
    return sentiment_label

