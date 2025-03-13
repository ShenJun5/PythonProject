# 📄 PDF Chatbot with Streamlit & OpenAI

This project is a **PDF-based chatbot** built using **Streamlit**, **PyPDF2**, **FAISS**, and **OpenAI's GPT-3.5-turbo**. Users can upload a PDF file, ask questions about its content, and receive AI-generated responses based on document embeddings.

## 🚀 Features
- **Upload PDF files** 📂
- **Answer user queries** 

## 🛠️ Installation

1. **Clone the repository**  
   ```sh
   git clone https://github.com/ShenJun5/PythonProject.git
   cd PythonProject
   ```

2. **Install the required dependencies**
   ```sh
   pip install streamlit pypdf2 langchain faiss-cpu openai tiktoken langchain-community
   ```

3. **Set your OpenAI API Key**
    In the code, replace the placeholder API key with your actual OpenAI API key:
    
    ```python
    OPENAI_API_KEY = "your_openai_api_key_here"
    ```
4. **Run the app**

    streamlit run chatbot.py

