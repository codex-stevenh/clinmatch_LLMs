# from ollama import Client

# client = Client(host='http://192.168.0.107:11434')

# response = client.chat(model='llama3:8b', messages=[{
#     "role":"user",
#     "content":"Do you think Dallas could win G1 today against Celtics?"
# }])

# print(response['message']['content'])

# conda create --name clinmatch_streamlit --clone clinmatch


import ollama
import streamlit as st
from typing import Dict, Generator

def ollama_generator(model_name: str, messages: Dict) -> Generator:
    stream = client.chat(
        model=model_name, messages=messages, stream=True)
    for chunk in stream:
        yield chunk['message']['content']

st.title("Codex-Assistant")

client = ollama.Client(host='http://192.168.0.107:11434')

if "_model" not in st.session_state:
    st.session_state["_model"] = "llama3:8b"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        response = st.write_stream(ollama_generator(
            st.session_state._model, st.session_state.messages))
        
    st.session_state.messages.append({"role": "assistant", "content": response})
