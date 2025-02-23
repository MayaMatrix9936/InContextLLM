import streamlit as st
from PyPDF2 import PdfReader
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
import os
 
api_key=st.secrets["api_key"]
 
# Sidebar contents
with st.sidebar:
    st.title(' LLM Chat App')
    st.markdown('''
    This app is an LLM-powered chatbot built using:
    - [Streamlit](https://streamlit.io/)
    - [LangChain](https://python.langchain.com/)
    - [OpenAI](https://platform.openai.com/docs/models) LLM model
 
    ''')
    add_vertical_space(5)

 
 
def main():
    st.header("Chat with PDF 💬")
 
    if 'history' not in st.session_state:
        st.session_state.history = []
    # upload a PDF file
    pdf = st.file_uploader("Upload your PDF", type='pdf')
 

    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
 
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
            )
        chunks = text_splitter.split_text(text=text)
 

        store_name = pdf.name[:-4]
        st.write(f'{store_name}')
  
 
        if os.path.exists(f"{store_name}.index"):
            x=FAISS.load_local(store_name)

        else:
            embeddings = OpenAIEmbeddings(api_key=api_key)
            VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
            VectorStore.save_local(store_name)
 
      
        query = st.text_input("Ask questions about your PDF file:")

 
        if query:
            docs = VectorStore.similarity_search(query=query, k=3)
            llm = OpenAI(api_key=api_key)
            chain = load_qa_chain(llm=llm, chain_type="stuff")
            with get_openai_callback() as cb:
                response = chain.run(input_documents=docs, question=query)
                print(cb)
            st.write(response)
            st.session_state.history.append({'role': 'user', 'message': query})
            st.session_state.history.append({'role': 'assistant', 'message': response})
    with st.sidebar:
        st.write("### Chat History")
        for entry in st.session_state.history:
            if entry['role'] == 'user':
                st.markdown(f"**You:** {entry['message']}")
            else:
                st.markdown(f"**Assistant:** {entry['message']}")
if __name__ == '__main__':
    main()