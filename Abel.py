import streamlit as st
import google.generativeai as genai
st.title ("hello")
apikey="AIzaSyDNcp_JDchji_PfU6mKwjCz2SxGBj0a4Ow"
question = st.text_input()
genai.configure(api_key="apikey")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(question)
print(response.text)
