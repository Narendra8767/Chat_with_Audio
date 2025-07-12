import streamlit as st 
import json 
import os 
import certifi
import time
import sys
from dotenv import load_dotenv
import requests
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ["SSL_CERT_FILE"] = certifi.where()



def save_audio(url):
    try:
        yt = YouTube(url)
        video_id = yt.video_id  # Extract video ID from full URL
    except Exception as e:
        print(f"[ERROR] Invalid YouTube URL: {e}")
        return None

    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
        transcript = " ".join(chunk["text"] for chunk in transcript_list)
        print("[INFO] Transcript fetched successfully.")
        return transcript
    except TranscriptsDisabled:
        print("[ERROR] No subtitles available for this video.")
        return None
    except Exception as e:
        print(f"[ERROR] Transcript fetching failed: {e}")
        return None



def langchain_qa(query):
    
    loader = TextLoader('docs/transcription.txt')
    documents = loader.load()
   
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(documents)
 
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())

    result = qa_chain.run(query)
    return result


st.set_page_config(layout="wide", page_title="ChatAudio", page_icon="🔊")

st.title("Chat with Your Audio using LLM")

input_source = st.text_input("Enter the YouTube video URL")

if input_source is not None:
    col1, col2 = st.columns(2)

    with col1:
      st.info("Your uploaded video")
      st.video(input_source)
      transcript = save_audio(input_source)
      if transcript:
        st.info("Transcript fetched from YouTube:")
        st.write(transcript)

        os.makedirs("docs", exist_ok=True)
        with open("docs/transcription.txt", "w", encoding="utf-8") as f:
            f.write(transcript)
      else:
         st.error("Transcript not available for this video.")
  

    with col2:
        st.info("Chat Below")
        query = st.text_area("Ask your Query here...")
        if query is not None:
            if st.button("Ask"):
                st.info("Your Query is: " + query)
                result = langchain_qa(query)
                st.success(result)

               

