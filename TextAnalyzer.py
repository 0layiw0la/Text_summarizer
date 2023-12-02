import streamlit as st
from textly import summarize
from textly import sentiment

positive_style = "color: green; font-weight: bold;"
negative_style = "color: red; font-weight: bold;"
def main():
    
    st.title('Text Summarizer App')
    #Buttons that determine summary length
    if st.button('Short'):
        max = 200
        min = 30
    if st.button('Long'):
        max = 350
        min = 90
    user_input = st.text_area('Enter text here')
    # Button to trigger summarization
    if st.button("Generate Summary"):
        # Check if user input is not empty
        if user_input:
            # Generate summary using the function
            summary = summarize(user_input,max,min)

            # Display the generated summary
            st.subheader("Generated Summary:")
            st.write(summary)
        # Button to trigger sentiment analysis
    if st.button("Perform Sentiment Analysis"):
        # Perform sentiment analysis using the sentiment function
        sentiment_result = sentiment(user_input)
        if sentiment_result =='Positive':
            style = positive_style
        elif sentiment_result == "Negative" :
            style = negative_style
        else: 
            style = ""

        # Display the sentiment analysis result
        st.subheader("Sentiment Analysis Result:")
        st.markdown(f"**Sentiment:** <span style='{style}'>{sentiment_result}</span>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
