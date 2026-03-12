import os 
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client=Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("AI CHATBOT")

user_input=st.chat_input("ASK ANY QUESTION HERE")

if user_input:
    response=client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages =[{"role":"user", "content":user_input}]
    )
    
    st.chat_message("user").write(user_input)
    st.chat_message("assistant").write(response.choices[0].message.content)
    
    