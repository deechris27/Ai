# 🤖 Generative AI & Machine Learning Portfolio

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev)
[![LangChain](https://img.shields.io/badge/LangChain-121212?style=for-the-badge&logo=chainlink&logoColor=white)](https://langchain.com)
[![Gradio](https://img.shields.io/badge/Gradio-FF6B6B?style=for-the-badge&logo=gradio&logoColor=white)](https://gradio.app)

> A comprehensive collection of **30+ AI projects** demonstrating expertise in **LLMs**, **RAG systems**, **Multi-Agent architectures**, **Vector databases**, and **production-ready AI applications**.

---

## 🛠️ Tech Stack & Skills Demonstrated

### **Core AI/ML Technologies**
- **Large Language Models**: GPT-4o, Google Gemini 2.0, Claude, DeepSeek, LLaMA, Ollama 3.2
- **AI Frameworks**: LangChain, LangGraph, Transformers, Sentence Transformers
- **Vector Databases**: FAISS (Facebook AI Similarity Search)
- **Fine-tuning**: LoRA (Low-Rank Adaptation) on GPT-2

### **Development & Deployment**
- **UI/UX**: Gradio for interactive web interfaces
- **APIs**: FastAPI, RESTful endpoints, Uvicorn server
- **Data Processing**: BeautifulSoup, PDF processing, Web scraping
- **ML Libraries**: NumPy, Scikit-learn, Cosine Similarity
- **Development**: Anaconda, Jupyter Lab, Git

### **AI Architectures Implemented**
- **RAG (Retrieval-Augmented Generation)** systems
- **Multi-Agent** conversational systems
- **Semantic Search** with embeddings
- **Memory-enabled** chatbots
- **Function Calling** with external APIs

---

## 🚀 Featured Projects

### 🎯 **Production-Ready Applications**

#### **Multi-Agent Resume Critique System** (LangGraph)
- **Tech**: LangGraph, Gemini, PDF processing, Multi-agent architecture
- **Features**: Grammar review, skills analysis, format optimization, ATS compatibility
- **Production**: FastAPI endpoints with file upload and chat interfaces

#### **Airline AI Assistant** 
- **Tech**: GPT-4o, Gradio, OpenAI Function Calling
- **Features**: Real-time ticket price fetching, natural language interface
- **Integration**: External API calls for live data

#### **RAG-Powered Knowledge Systems**
- **Tech**: LangChain, FAISS, Vector embeddings, PDF processing
- **Features**: Document ingestion, semantic search, context-aware responses
- **Use Cases**: Teaching assistant, company knowledge base

### 🔬 **Advanced AI Techniques**

#### **Multi-Agent Debate System**
- **Innovation**: Two AI models (Gemini vs GPT) with distinct personalities
- **Tech**: Concurrent LLM orchestration, streaming responses
- **Demonstrates**: Advanced prompt engineering, AI behavior modeling

#### **Fine-Tuning & Model Optimization**
- **Project**: LoRA fine-tuning on GPT-2 for causal language modeling
- **Achievement**: Runs efficiently on 16GB RAM consumer hardware
- **Skills**: Model optimization, resource-efficient training

#### **Document Analysis Pipeline**
- **Tech**: LangGraph, PDF Plumber, Intent parsing, CRUD operations
- **Features**: Multi-step processing, structured data extraction
- **Architecture**: Microservices with FastAPI backend

### 📊 **Data Science & Analytics**

#### **Semantic Search & Embeddings**
- **Implementation**: Custom similarity search using sentence transformers
- **Visualization**: Vector database embedding visualization
- **Models**: HuggingFace paraphrase-MiniLM-L6-v2 (production-ready, no API keys)

#### **Web Intelligence**
- **Projects**: Automated web scraping with AI summarization
- **Tech Stack**: BeautifulSoup + GPT-4o/Ollama integration
- **Output**: Streaming summaries and company intelligence reports

---

## 📋 Quick Start Guide

### Prerequisites
```bash
# Clone repository
git clone [your-repo-url]
cd Ai

# Setup environment
conda env create -f environment.yml
conda activate llms

# Start Jupyter Lab
jupyter lab
```

### API Configuration
Create a `.env` file with your API keys:
```env
OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_gemini_key
ANTHROPIC_API_KEY=your_claude_key
DEEPSEEK_API_KEY=your_deepseek_key
```

### Run Multi-Agent Systems
```bash
# Start FastAPI server for advanced projects
uvicorn app.main:app --reload

# Upload resume for analysis
POST /upload (multipart/form-data: file)

# Chat with document
POST /chat {"query": "your question"}
```

---

## 🔗 API Documentation & References

| Provider | Documentation | Specialty |
|----------|--------------|-----------|
| **OpenAI** | [API Reference](https://platform.openai.com/docs/api-reference/introduction) | GPT models, Function calling |
| **Google Gemini** | [Getting Started](https://ai.google.dev/gemini-api/docs) | Multimodal AI, Fast inference |
| **Anthropic Claude** | [API Docs](https://docs.anthropic.com/en/api/getting-started) | Constitutional AI, Long context |
| **DeepSeek** | [API Documentation](https://api-docs.deepseek.com/) | Code generation, Reasoning |
| **Meta LLaMA** | [Developer Guide](https://www.llama.com/docs/get-started/) | Open source LLMs |

---

## 📈 Project Categories

### **🤖 Conversational AI** (8 projects)
Chatbots, memory systems, personality-driven agents, streaming responses

### **📚 Knowledge Management** (6 projects)  
RAG systems, PDF processing, vector databases, semantic search

### **🌐 Web Intelligence** (4 projects)
Scraping, summarization, real-time data integration

### **⚙️ Production Systems** (4 projects)
FastAPI backends, multi-agent orchestration, CRUD operations

### **🧠 Model Training** (2 projects)
Fine-tuning, LoRA adaptation, efficient training

### **📊 Analytics & Visualization** (2 projects)
Embedding visualization, similarity analysis

---

## 💼 Skills Demonstrated for Recruiters

✅ **Production-Ready Development**: FastAPI, REST APIs, scalable architectures  
✅ **Multi-Modal AI**: Text, PDF, web data processing  
✅ **Advanced Prompting**: Function calling, agent orchestration, persona design  
✅ **Vector Operations**: Embeddings, similarity search, FAISS optimization  
✅ **Model Integration**: Multiple LLM providers, streaming, async processing  
✅ **User Experience**: Gradio interfaces, responsive design  
✅ **DevOps**: Environment management, API key security, deployment ready  

---

## 🎯 Business Impact

- **Productivity Tools**: Resume optimization, email drafting, content creation
- **Customer Service**: AI assistants with real-time data integration  
- **Knowledge Management**: Automated document processing and Q&A systems
- **Content Intelligence**: Web scraping with AI-powered analysis
- **Educational Technology**: Teaching assistants with context awareness

---

*This portfolio demonstrates comprehensive expertise in modern AI/ML technologies with a focus on practical, production-ready applications that solve real business problems.*
