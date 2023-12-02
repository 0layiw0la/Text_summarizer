import streamlit as st
from textly import sentiment,summarize

#positive_style = "color: green; font-weight: bold;"
#negative_style = "color: red; font-weight: bold;"
def main():  
    st.title('Text Summarizer App')
    col1,col2,col3,col4 = st.columns([1,1,1,0.5])
    with col1:
        short = st.button("Brief overview")
    with col2:
        long = st.button("Comprehensive summary")
    user_input = st.text_area('Enter text here')
    
    # Button to trigger summarization
    if short:
        # Check if user input is not empty
        if user_input:
            summary = summarize(user_input, max_value= 120, min_value = 20)
            # Display the generated summary
            st.subheader("Generated Summary:")
            st.write(summary)
    if long:
        # Check if user input is not empty
        if user_input:
            summary = summarize(user_input, max_value= 350, min_value = 80)
            # Display the generated summary
            st.subheader("Generated Summary:")
            st.write(summary)
        # Button to trigger sentiment analysis
  #  if st.button("Perform Sentiment Analysis"):
   #     # Perform sentiment analysis using the sentiment function
    #    sentiment_result = sentiment(user_input)
     #   if sentiment_result =='Positive':
      #      style = positive_style
       # elif sentiment_result == "Negative" :
        #    style = negative_style
        #else: 
         #   style = ""

        # Display the sentiment analysis result
        #st.subheader("Sentiment Analysis Result:")
        #st.markdown(f"**Sentiment:** <span style='{style}'>{sentiment_result}</span>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
