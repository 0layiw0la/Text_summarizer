import streamlit as st
from textly import set_global_max,set_global_min,sentiment,summarize

positive_style = "color: green; font-weight: bold;"
negative_style = "color: red; font-weight: bold;"
def main():
    
    st.title('Text Summarizer App')
    #Buttons that determine summary length
    max_value = 250
    min_value = 50

    # Buttons that determine summary length
    if st.button('Short'):
        max_value = 150
        set_global_min(20)
    elif st.button('Long'):
        set_global_max(350)
        set_global_min(90)
    user_input = st.text_area('Enter text here')
    # Button to trigger summarization
    if st.button("Generate Summary"):
        # Check if user input is not empty
        if user_input:
            # Generate summary using the function
            summary = summarize(user_input,max_value,min_value)

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
