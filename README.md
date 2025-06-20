# Speech Driven RAG Chatbot with LangChain and GPT


![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![OS](https://img.shields.io/badge/OS-Cross--platform-lightgrey?logo=windows)
![LangChain](https://img.shields.io/badge/LangChain-🔗-orange)
![pathlib](https://img.shields.io/badge/Pathlib-built--in%20module-informational)
![OpenAI](https://img.shields.io/badge/OpenAI-API-green?logo=openai)

## Overview 
This project demonstrates how to build a voice-interactive Retrieval-Augmented Generation (RAG) chatbot. It integrates Whisper for audio transcription, LangChain for chaining logic and document indexing, and OpenAI APIs for text generation and speech synthesis.

### 🚀 Use Case
Imagine you’re driving and a warning light appears—what does it mean? This chatbot allows users to ask such questions aloud. It transcribes the audio, pulls context from a car manual PDF using vector search, and returns an AI-generated, human-like spoken answer.


## 🧠 Architecture Overview

The system flows through four core stages: 

1. **Audio to Text**  
   - The users query is captured via voice (`user_input_audio.mp3`).
   - Transcription is handled by OpenAI Whisper (`whisper-1` model).

2. **Contextual Search**  
   - The provided car manual (`car_manual.pdf`) is parsed using LangChain loaders and split into chunks.
   - Text chunks are embedded with `text-embedding-3-small` and stored in a ChromaDB vector store.
   - A query retrieves the most relevant content for grounding the response.

3. **Response Generation**  
   - A prompt template injects the user's query and retrieved context into a GPT-4o-mini model.
   - The output is short, clear, and context-aware.

4. **Text to Speech**  
   - The answer is converted into spoken form using OpenAI's TTS (`gpt-4o-mini-tts`) and saved as `user_output_1.mp3`.

---

## 🧰 Tech Stack

- **Python 3.10+**
- **LangChain**: Orchestrates document loading, splitting, and chaining
- **ChromaDB**: In-memory vector store for document embeddings
- **OpenAI APIs**: 
  - `Whisper` for STT (Speech to Text)
  - `GPT-4o-mini` for language modeling
  - `TTS` for synthesized voice output
- **PDF Handling**: `PyPDFLoader`
- **Environment Management**: `python-dotenv`
- **Filepaths & Audio**: `pathlib`, `os`, standard Python I/O

---

## 📝 Getting Started

### Install dependencies

```bash
pip install -r requirements.txt

OPENAI_API_KEY=your_openai_api_key_here



