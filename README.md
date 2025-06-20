# DashMate - Speech Driven RAG Chatbot with LangChain and GPT

DashMate is your intelligent, audio-powered assistant for understanding your car's warning messages and technical documentation. Simply speak your question about a dashboard light or a car manual detail, and DashMate will provide an instant, clear audio explanation.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![OS](https://img.shields.io/badge/OS-Cross--platform-lightgrey?logo=windows)
![LangChain](https://img.shields.io/badge/LangChain-🔗-orange)
![pathlib](https://img.shields.io/badge/Pathlib-built--in%20module-informational)
![OpenAI](https://img.shields.io/badge/OpenAI-API-green?logo=openai)

## Overview 
This project demonstrates how to build a voice-interactive Retrieval-Augmented Generation (RAG) chatbot. Navigating complex car manuals and deciphering cryptic dashboard warnings can be a headache. DashMate solves this by leveraging advanced AI to transform dense technical documentation into easily digestible audio responses. It's like having an expert mechanic or a detailed car manual available instantly, just by asking. It integrates Whisper for audio transcription, LangChain for chaining logic and document indexing, and OpenAI APIs for text generation and speech synthesis. 

### Use Case
Imagine you’re driving and a warning light appears—what does it mean? This chatbot allows users to ask such questions aloud. It transcribes the audio, pulls context from a car manual PDF using vector search, and returns an AI-generated, human-like spoken answer.

## Features
- Voice-Activated: Interact with DashMate using natural spoken language.
- Context-Aware: Understands your specific questions about car warning messages and technical details.
- Audio Responses: Receive clear, spoken explanations, making it easy to understand complex information hands-free.
- Comprehensive Knowledge: Built upon your car's technical documentation to provide accurate and relevant answers.

## How It Works
DashMate uses a cutting-edge technology called Retrieval Augmented Generation (RAG), powered by LangChain and OpenAI. Here's a quick look at what happens behind the scenes:

1. **Documentation Loading**: Your car's technical manual is loaded and intelligently broken down into smaller, manageable pieces.
2. **Smart Storage**: These pieces are then converted into numerical representations (embeddings) and stored in a specialized database called a vector store (Chroma DB), making them quickly searchable.
3. **Your Question**: When you speak a question, an OpenAI model transcribes it into text.
4. **Intelligent Retrieval**: DashMate searches its vector store for the most relevant sections of your car manual based on your question.
5. **Answer Generation**: These retrieved sections, along with your question, are fed to a powerful Large Language Model (LLM) from OpenAI. The LLM then generates a precise and coherent answer.
6. **Audio Reply**: Finally, the text answer is converted back into speech using an OpenAI audio model, and played back to you.

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

To set up DashMate locally, follow these steps:
1. **Clone the Repository**:

Bash
git clone [https://github.com/your-username/your-rag-chatbot.git](https://github.com/dvouna/speech_driven_rag_chatbot_using_langchain_and_gpt)
cd your-rag-chatbot 

2. **Set Up Environment Variables**:
Create a .env file in the root directory of the project and add your OpenAI API key:
OPENAI_API_KEY=your_openai_api_key_here
Replace your_openai_api_key_here with your actual OpenAI API key.

3. **Install Dependencies**:

Bash

pip install -r requirements.txt

4. **Place Your Documentation**:
Put your car manual (e.g., car_manual.pdf) inside the data/ directory.

Run the Application:
