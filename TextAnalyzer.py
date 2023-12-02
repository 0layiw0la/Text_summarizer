import streamlit as st
from textly import sentiment,summarize

positive_style = "color: green; font-weight: bold;"
negative_style = "color: red; font-weight: bold;"
def main():
    
    st.title('Text Summarizer App')
    s = st.button('short')
    l = st.button('Long')
    user_input = st.text_area('Enter text here')
    # Button to trigger summarization
    if st.button("Generate Summary"):
        # Check if user input is not empty
        if user_input:
            if s:           
                # Generate summary using the function
                summary = summarize(user_input,120,20)
            elif l:
                summary = summarize(user_input,350,80)
            else:
                summary = summarize(user_input)

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
