import streamlit as st
import google.generativeai as genai
st.title ("hello")
question = st.text_input("hello")
prompt = f"{question}(please answer the question as you were a legal assistant of India, please give answer for indian laws not any other country,and please introduce yourself as a legal assistant of India) "
genai.configure(api_key="AIzaSyDV_57EOSC0pJHjSm4TGjBMzK989Ggdcq4")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content()
print(response.text)
st.write(response.text)
