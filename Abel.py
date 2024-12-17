import streamlit as st
import google.generativeai as genai
st.title ("hello")
question = st.text_input("hello")
genai.configure(api_key="AIzaSyDV_57EOSC0pJHjSm4TGjBMzK989Ggdcq4")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(question)
print(response.text)
st.write(response.text)
