🔊 Chat with Your YouTube Video using LLMs 🤖<br>

 🚀 Built an AI-powered app that lets you chat with YouTube videos using LLMs!<br>
I recently developed ChatAudio, a project that allows users to interact with YouTube video content in a conversational way — powered by LangChain, OpenAI, and Streamlit.<br>
🎯 Goal<br>
Enable users to extract transcripts from YouTube videos and ask any question about the content — just like chatting with the video!

![image alt](https://github.com/Narendra8767/Chat_with_Audio/blob/9455e4ed93f411a692e53e58b5cb5e50beedc0f8/image/index.png)


🔁 Workflow Overview<br>
1️⃣ User inputs a YouTube video URL<br>
 2️⃣ App fetches subtitles using YouTubeTranscriptAPI<br>
 ➕ If subtitles are missing, you can optionally use AssemblyAI for speech-to-text<br>
 3️⃣ Transcript is saved and processed via LangChain:<br>
Loaded with TextLoader<br>
Split using CharacterTextSplitter<br>
Embedded via OpenAIEmbeddings<br>
Stored with FAISS for fast vector search<br>
 4️⃣ The query is passed to the LLM (ChatOpenAI) using a RetrievalQA chain<br>
 5️⃣ 💬 User receives a smart answer based on actual video content!<br>

![image alt](https://github.com/Narendra8767/Chat_with_Audio/blob/40a68154e904e85f98c23f86da13874c13e30e6c/image/chatAudio.png)


🧠 Tech Stack<br>
✅ Streamlit – UI & interaction<br>
 ✅ LangChain – Document processing & RAG<br>
 ✅ OpenAI GPT-3.5 – Question answering<br>
 ✅ FAISS – Vector storage<br>
 ✅ YouTubeTranscriptAPI – Subtitle extraction<br>
 ✅ AssemblyAI (Optional) – Audio transcription fallback<br>
 ✅ PyTube – For downloading audio from YouTube<br>


📌 Key Highlights<br>
✔️ Converts YouTube content into a conversational AI interface<br>
 ✔️ Real-time interaction with a smooth Streamlit frontend<br>
 ✔️ Skip the full video – just ask what you want to know<br>
 ✔️ Modular codebase with robust error handling and retrieval pipeline<br>
 ✔️ Efficient, fast, and scalable for real-world use<br>


🐳 Docker Deployment <br>
To make it easy for anyone to run the app locally, I’ve also Dockerized the project and published it on <br>
Docker Hub: https://lnkd.in/d-trNx98

