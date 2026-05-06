from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant. Give short and clear answers to user questions."),
        ("user", "Question: {question}")
    ]
)

# Streamlit UI
st.set_page_config(page_title="LangChain Chatbot")

st.title("🤖 LangChain Chatbot with Ollama")

input_text = st.text_input("Search the topic you want")

# Ollama Model
llm = Ollama(model="tinyllama")

# Output Parser
output_parser = StrOutputParser()

# Chain
chain = prompt | llm | output_parser

# Generate Response
if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)