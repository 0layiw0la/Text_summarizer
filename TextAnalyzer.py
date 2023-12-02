import streamlit as st
from textly import sentiment,summarize

positive_style = "color: green; font-weight: bold;"
negative_style = "color: red; font-weight: bold;"
def main():
    if 'max_value' not in st.session_state:
        st.session_state['max_value'] = 250
        st.session_state['min_vale'] = 50
    st.title('Text Summarizer App')
    s = st.button('short')
    if s:
        st.session_state.max_value = 120
        st.session_state.min_value = 20
    l = st.button('Long')
    if l:
        st.session_state.max_value = 350
        st.session_state.min_value = 80  
    user_input = st.text_area('Enter text here')
    # Button to trigger summarization
    if st.button("Generate Summary"):
        # Check if user input is not empty
        if user_input:
            summary = summarize(user_input,st.session_state.max_value,st.session_state.min_value)

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
