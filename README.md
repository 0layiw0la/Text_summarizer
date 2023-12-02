# Text Summarizer App
This is a simple Text Summarizer App built with Python using the Streamlit library.
- **Live application** - https://0lastextsummarizer.streamlit.app/

## Overview
The Text Summarizer App allows users to input text and receive a summarized version of the text, you can either upload or copy and paste text. Additionally, the app provides sentiment analysis for the entered text.
**Note**: Only pdf,docx,txt files can be uploaded for now.

## Features
- Text Summarization: The app uses natural language processing techniques to generate a concise summary of the input text.

- Sentiment Analysis: Users can perform sentiment analysis on the entered text to determine if it is positive, negative, or neutral.

## Getting Started
### Prerequisites
Python (version 3.10.13)

Install the required packages by running:
pip install -r requirements.txt

### How to Run
1. Clone the repository:
- git clone https://github.com/0layiw0la/Text_summarizer.git

2. Navigate to the project directory:
- cd Text_summarizer

3. Run the app:
- streamlit run TextAnalyzer.py

4. Access the app in your web browser at http://localhost:8501.

## Usage
- Enter text in the provided text area.
- Click the "Generate Summary" button to get a summarized version of the text.
- Optionally, click the "Perform Sentiment Analysis" button to analyze the sentiment of the entered text.

## Dependencies
- NLTK: Natural Language Toolkit for natural language processing.
- Streamlit: Open-source Python library for creating web applications.
- BART: Bidirectional and Auto-Regressive Transformers, a transformer-based model developed by Facebook AI. It is designed for various natural language processing tasks, including text generation and summarization.

## Limitations
- Sentiment analysis function performs poorly when dealing with sarcastic text (best used for academic or more formal text).
- Only docx,txt and pdf files can be uploaded for now

## Contributing
If you have suggestions or found a bug, feel free to open an issue or create a pull request.

## License
This project is licensed under the [MIT License](https://www.mit.edu/~amini/LICENSE.md).
