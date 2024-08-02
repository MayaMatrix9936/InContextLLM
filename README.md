# LLM Chat App 🤖📄

## Overview

The LLM Chat App is a Streamlit-based application that allows users to interact with PDF documents using a large language model (LLM) from OpenAI. The app utilizes LangChain for text processing and FAISS for efficient similarity search.

## Features

- **Upload PDF** 📤: Upload a PDF file to process.
- **Text Extraction** ✍️: Extract text from the uploaded PDF.
- **Text Chunking** 🧩: Split the extracted text into chunks for better processing.
- **Embedding and Vector Storage** 💾: Convert text chunks into embeddings and store them using FAISS.
- **Question Answering** ❓: Ask questions about the content of the PDF and receive answers powered by OpenAI's LLM.
- **Chat History** 📝: Maintain and display a history of user interactions and responses.

## Dependencies

The following Python packages are required:

- `langchain`
- `PyPDF2`
- `python-dotenv`
- `streamlit`
- `faiss-cpu`
- `streamlit-extras`
- `openai`
- `langchain-community`
- `tiktoken`

**## Live Demo** 🎥:
Explore a live demo of the LLM Chat App at the following URL:

[screen-capture.webm](https://github.com/user-attachments/assets/725c6ba2-ec3f-4bd8-87de-f78145d77680)

This demo showcases the core functionalities of the app, allowing you to upload PDFs, ask questions, and view responses in real-time.

## Setup


1. **Install Dependencies** 📦:

   Create a virtual environment and install the required packages using the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt

2. **Set Up API Key** 🔑:

   Store your OpenAI API key in the .streamlit/secrets.toml file or set it as an environment variable. For example, in .streamlit/secrets.toml:

   ```bash
   api_key="API KEY HERE"

 3. **Run the App** 🚀:

    Launch the Streamlit using the command:

    ```bash
    streamlit run llm.py

**## Contributing**
Feel free to open issues or submit pull requests for improvements. Contributions are welcome! 🤝

**Contact**
For questions or support, please contact jwalinb9963@gmail.com 📧.
