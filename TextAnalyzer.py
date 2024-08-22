import streamlit as st
from textly import sentiment, summarize, extract_text_from_txt, extract_text_from_docx, extract_text_from_pdf

positive_style = "color: green; font-weight: bold;"
negative_style = "color: red; font-weight: bold;"

def main():  
    st.title('Text Summarizer App')

    # Load the model when the page is loaded
    summarizer = load_model()

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
    if st.button("Generate Summary"):
        if user_input:
            summary = summarize(user_input, summarizer, max_value=350, min_value=90)
            st.subheader("Generated Summary:")
            st.write(summary)
        elif uploaded_file is not None:
            summary = summarize(text, summarizer, max_value=350, min_value=80)
            st.write(summary)

    # Button to trigger sentiment analysis
    if st.button("Perform Sentiment Analysis"):
        sentiment_result = sentiment(user_input)
        if sentiment_result == 'Positive':
            style = positive_style
        elif sentiment_result == "Negative":
            style = negative_style
        else: 
            style = ""

        st.subheader("Sentiment Analysis Result:")
        st.markdown(f"**Sentiment:** <span style='{style}'>{sentiment_result}</span>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
