🔊 Chat with Your YouTube Video using LLMs 🤖

 🚀 Built an AI-powered app that lets you chat with YouTube videos using LLMs!
I recently developed ChatAudio, a project that allows users to interact with YouTube video content in a conversational way — powered by LangChain, OpenAI, and Streamlit.

🎯 Goal
Enable users to extract transcripts from YouTube videos and ask any question about the content — just like chatting with the video!

🔁 Workflow Overview
1️⃣ User inputs a YouTube video URL
 2️⃣ App fetches subtitles using YouTubeTranscriptAPI
 ➕ If subtitles are missing, you can optionally use AssemblyAI for speech-to-text
 3️⃣ Transcript is saved and processed via LangChain:
Loaded with TextLoader
Split using CharacterTextSplitter
Embedded via OpenAIEmbeddings
Stored with FAISS for fast vector search
 4️⃣ The query is passed to the LLM (ChatOpenAI) using a RetrievalQA chain
 5️⃣ 💬 User receives a smart answer based on actual video content!

🧠 Tech Stack
✅ Streamlit – UI & interaction
 ✅ LangChain – Document processing & RAG
 ✅ OpenAI GPT-3.5 – Question answering
 ✅ FAISS – Vector storage
 ✅ YouTubeTranscriptAPI – Subtitle extraction
 ✅ AssemblyAI (Optional) – Audio transcription fallback
 ✅ PyTube – For downloading audio from YouTube

📌 Key Highlights
✔️ Converts YouTube content into a conversational AI interface
 ✔️ Real-time interaction with a smooth Streamlit frontend
 ✔️ Skip the full video – just ask what you want to know
 ✔️ Modular codebase with robust error handling and retrieval pipeline
 ✔️ Efficient, fast, and scalable for real-world use

🐳 Docker Deployment 
To make it easy for anyone to run the app locally, I’ve also Dockerized the project and published it on 
Docker Hub: https://lnkd.in/d-trNx98
Github Repo : https://lnkd.in/dtPT_HkG
