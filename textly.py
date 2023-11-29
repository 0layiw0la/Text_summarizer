import nltk

def generate_summary(text):
    import string
    from heapq import nlargest
    nltk.download('stopwords')
    nltk.download('punkt')
    
    text = str(text)
    sent_list = nltk.sent_tokenize(text)
    if len(sent_list) > 12:
        length = int(round(len(sent_list) / 7, 0))
    else:
        length = 1

    nopuch = [char for char in text if char not in string.punctuation]
    nopuch = "".join(nopuch)

    processed_text = [word for word in nopuch.split() if word.lower() not in nltk.corpus.stopwords.words('english')]

    word_freq = {}
    for word in processed_text:  
        if word not in word_freq:  
            word_freq[word] = 1
        else: 
            word_freq[word] += 1

    max_freq = max(word_freq.values())
    for word in word_freq:
        word_freq[word] = word_freq[word] / max_freq

    sent_score = {}
    for sent in sent_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_freq:
                if sent not in sent_score:
                    sent_score[sent] = word_freq[word]
                else:
                    sent_score[sent] += word_freq[word]

   # Use nlargest on sentences instead of length
    summary_sents = nlargest(length, sent_score, key=sent_score.get)
    summary = " ".join(summary_sents)

    return summary
def sentiment(text):
    nltk.download('vader_lexicon')
    from nltk.sentiment import SentimentIntensityAnalyzer
    text = str(text)
    sia = SentimentIntensityAnalyzer()
    sent = sia.polarity_scores(text)
    if sent['neu'] > 0.8:
        sentiment_label = 'Neutral'
    elif sent['pos'] > 0.1 and (sent['pos'] > sent['neg']):
        sentiment_label = 'Positive'
    elif (sent['neg'] > 0.1) and (sent['neg'] > sent['pos']):
        sentiment_label = 'Negative'
    else:
        sentiment_label = 'Neutral'
    return sentiment_label

        
    
