import streamlit as st 
import google.generativeai as genai


st.title("Welcome to mystream api")

Chatbot = st.text_input("Ask me anything")

genai.configure(api_key = "AIzaSyA-QODIRTROM6_8zs4gRp9ppFKA2FfBZFA")

model = genai.GenerativeModel("models/gemini-2.5-flash")

if Chatbot :
    response = model.generate_content(Chatbot)
    st.write("Response", response.text)