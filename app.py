from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🤖",
    layout="wide"
)

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.title("⚙ Settings")

    model_name = st.selectbox(
        "Choose Model",
        ["tinyllama"]
    )

    st.markdown("---")

    st.info(
        "This chatbot is built using LangChain + Ollama + Streamlit"
    )

    if st.button("Clear Chat"):
        st.session_state.messages = []

# ---------------- TITLE ----------------

st.title("🤖 AI Study Assistant")

st.markdown(
    '''
    <div style="padding:15px;border-radius:10px;background-color:#262730;">
    🚀 Ask questions about AI, coding, internships, studies, and technology.
    </div>
    ''',
    unsafe_allow_html=True
)

# ---------------- PROMPT ----------------

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful AI assistant. Give short and clear answers."
        ),
        (
            "user",
            "Question: {question}"
        )
    ]
)

# ---------------- LLM ----------------

llm = Ollama(model=model_name)

# ---------------- OUTPUT PARSER ----------------

output_parser = StrOutputParser()

# ---------------- CHAIN ----------------

chain = prompt | llm | output_parser

# ---------------- CHAT HISTORY ----------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Previous Messages

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

# ---------------- USER INPUT ----------------

user_input = st.chat_input("Ask your question...")

# ---------------- RESPONSE ----------------

if user_input:

    # Store User Message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Show User Message

    with st.chat_message("user"):
        st.write(user_input)

    # Generate AI Response

    response = chain.invoke(
        {
            "question": user_input
        }
    )

    # Store Assistant Response

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    # Show Assistant Response

    with st.chat_message("assistant"):
        st.write(response)