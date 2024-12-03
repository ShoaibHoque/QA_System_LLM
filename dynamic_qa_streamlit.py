import os
import streamlit as st
from langchain_groq import ChatGroq

# Initialize the ChatGroq LLM
llm = ChatGroq(
    temperature=1,
    groq_api_key=os.environ.get('GROQ_API'),
    model='llama-3.1-70b-versatile'
)

# Streamlit App
st.title("Dynamic Multilingual Question Answering System")
st.write("Ask questions in Bangla or English, and get answers from the LLaMA model!")

# Input field for user query
question = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if question:
        response = llm.invoke(question)
        st.write("### Answer:")
        st.write(response.content)
    else:
        st.error("Please enter a question!")
