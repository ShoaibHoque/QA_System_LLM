import os
import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# Step 1: Load personal data (e.g., resume)
loader = TextLoader("resume.txt")
documents = loader.load()

# Step 2: Create embeddings and FAISS retriever
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
vectorstore = FAISS.from_documents(documents, embeddings)

# Step 3: Initialize ChatGroq and retriever
retriever = vectorstore.as_retriever()
llm = ChatGroq(
    temperature=1,
    groq_api_key=os.environ.get('GROQ_API'),
    model='llama-3.1-70b-versatile'
)

# Custom QA chain to handle RAG and LLM fallback
def custom_qa_chain_run(question):
    """
    Custom QA logic to use retriever first and fallback to LLM if no documents are retrieved.
    """
    # Retrieve relevant documents
    retrieved_docs = retriever.invoke(question)

    if retrieved_docs:
        # Combine retrieved context for the prompt
        context = "\n".join([doc.page_content for doc in retrieved_docs])
        prompt = f"Context: {context}\n\nQ: {question}\nA:"
        response = llm.invoke(prompt)
        return {
            "result": response.content,
            "source_documents": retrieved_docs
        }
    else:
        # Fallback to LLM without context
        response = llm.invoke(question)
        return {
            "result": response.content,
            "source_documents": []
        }

# Step 4: Streamlit App
st.title("Question Answering System for both Bangla and English")
st.write("Ask questions, and get answers. you can ask anything regarding CV of Shoaib Hoque or add your personal data to get answer according to that.")

# Input field for user query
question = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if question:
        result = custom_qa_chain_run(question)
        st.write("### Answer:")
        st.write(result["result"])
    else:
        st.error("Please enter a question!")
