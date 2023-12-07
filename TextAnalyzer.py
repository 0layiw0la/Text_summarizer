import streamlit as st
from textly import sentiment,summarize,extract_text_from_txt,extract_text_from_docx,extract_text_from_pdf

positive_style = "color: green; font-weight: bold;"
negative_style = "color: red; font-weight: bold;"
def main():  
    st.title('Text Summarizer App')
    col1,col2,col3,col4,col5 = st.columns([1,1,1,1,1])
    with col1:
        short = st.button("Brief overview")
    with col2:
        long = st.button("Full summary")
        
    user_input = st.text_area('Enter text here')
    uploaded_file = st.file_uploader("Choose a file", type=["txt", "docx", "pdf"])
    if uploaded_file is not None:
        file_extension = uploaded_file.name.split(".")[-1]

        if file_extension == "txt":
            text = extract_text_from_txt(uploaded_file)

        elif file_extension == "docx":
            text = extract_text_from_docx(uploaded_file)

        elif file_extension == "pdf":
            text = extract_text_from_pdf(uploaded_file)

    # Button to trigger summarization
    if short:
        # Check if user input is not empty
        if user_input:
            summary = summarize(user_input, max_value= 100, min_value = 20)
            # Display the generated summary
            st.subheader("Generated Summary:")
            st.write(summary)
        elif uploaded_file is not None:
            summary = summarize(text,max_value= 100, min_value = 20)
            st.write(summary)
    if long:
        # Check if user input is not empty
        if user_input:
            summary = summarize(user_input, max_value= 350, min_value = 90)
            # Display the generated summary
            st.subheader("Generated Summary:")
            st.write(summary)
        elif uploaded_file is not None:
            summary = summarize(text,max_value= 350, min_value = 80)
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
