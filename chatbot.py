import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_community.chat_models import ChatOpenAI

#openAI key
OPENAI_API_KEY = "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";

#Upload PDF files
st.header("My first Chatbot")

with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader("Upload a PDF file and start asking questions",
type="pdf")

#Extract the text
if file is not None:
    pdf_reader = PdfReader(file)
    text=""
    for page in pdf_reader.pages:
        text+=page.extract_text()
        # st.write(text)

#Break it into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators="\n",
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    # st.write(chunks)

    #generating embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    #creating vector store - FAISS facebook ai semantic search
    vector_store = FAISS.from_texts(chunks, embeddings)
    # - embeddings(OpenAI)
    # - initilazing FAISS
    # - store chunks & embeddings

    #get user question
    user_question = st.text_input("Type your question here")

    #do similarity search
    if user_question:
        match = vector_store.similarity_search(user_question)
        # A = question -> user_question
        # B = vector_DB -> vector_store
        # st.write(match)

        #defind the LLM
        llm = ChatOpenAI(
            openai_api_key = OPENAI_API_KEY,
            temperature = 0,
            #lower the value, ask the LLM to not be random but more specific
            max_tokens = 1000,
            model_name = "gpt-3.5-turbo"
        )

        #output results
        # chain -> take the question, get relevant document, pass it to the LLM, generate the output
        chain = load_qa_chain(llm, chain_type="stuff")
        response = chain.run(input_documents = match, question = user_question)
        st.write(response)