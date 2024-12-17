import streamlit as st
import google.generativeai as genai
st.title ("hello")
question = st.text_input("hello")
prompt = f"{question}(please answer the question as you were a legal assistant of India, please give answer for indian laws not any other country,and your name is Nyaysathi.)" 
genai.configure(api_key="AIzaSyDV_57EOSC0pJHjSm4TGjBMzK989Ggdcq4")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(prompt)
print(response.text)
st.write("hello Iam Nyaysathi")
st.write(response.text)
