
import os
from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import recorder
import tts

def main():
    load_dotenv()
    st.set_page_config(page_title="Chat PDF")
    st.header("📞 Telephone Customer Service")
    
    # upload file
    pdf = st.file_uploader("Upload your PDF file", type="pdf")
    
    # extract the text
    if pdf is not None:
      pdf_reader = PdfReader(pdf)
      text = ""
      for page in pdf_reader.pages:
        text += page.extract_text()
        
      # split into chunks
      char_text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000,
                                                 chunk_overlap=200,length_function=len)
      text_chunks = char_text_splitter.split_text(text)
      
      # create embeddings
      embeddings = OpenAIEmbeddings()
      docsearch = FAISS.from_texts(text_chunks, embeddings) 
      llm = OpenAI() 
      chain = load_qa_chain(llm, chain_type="stuff")
      
      # show user input
      if st.button('📞'):
        
        query=recorder.record()
        st.write("Query:"+query)
        
        if query:
          docs = docsearch.similarity_search(query)
          response = chain.run(input_documents=docs, question=query)
            
          st.write(response)
          api = st.text_input("Elven Labs Api:")
          file=tts.speech(response,api)

          audio_file = open(file,'rb') 
          audio_bytes = audio_file.read() 
          st.audio(audio_bytes, format='audio/ogg') 

     
     
       
    

if __name__ == '__main__':
    main()