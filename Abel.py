import google.generativeai as genai
import streamlit as st
import shelve

st.title("Nyaysathi")

USER_AVATAR = "👤"
BOT_AVATAR = "🤖"
configure

# Ensure openai_model is initialized in session state
if "genai" not in st.session_state:
    st.session_state["genai"] = ""

# Load Indian Constitution (replace with actual file path)
try:
    with open("indian_constitution.txt", "r", encoding="utf-8") as f:
        constitution_text = f.read()
except FileNotFoundError:
    st.error("Indian Constitution file not found. Please provide the correct file path.")
    constitution_text = ""

# Load chat history from shelve file
def load_chat_history():
    with shelve.open("chat_history") as db:
        return db.get("messages", [])

# Save chat history to shelve file
def save_chat_history(messages):
    with shelve.open("chat_history") as db:
        db["messages"] = messages

# Initialize or load chat history
if "messages" not in st.session_state:
    st.session_state.messages = load_chat_history()

# Sidebar with a button to delete chat history
with st.sidebar:
    if st.button("Delete Chat History"):
        st.session_state.messages = []
        save_chat_history([])

# Display chat messages
for message in st.session_state.messages:
    avatar = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Main chat interface
if prompt := st.chat_input("How can I help?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar=USER_AVATAR):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar=BOT_AVATAR):
        message_placeholder = st.empty()
        full_response = ""
        with st.spinner("Generating response..."):
            for response in client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": "system", "content": f"You are an expert on the Indian Constitution. Please refer to the provided text and use it to enhance your responses, especially when answering questions related to Indian law, rights, and governance."},
                    {"role": "user", "content": prompt},
                ],
                stream=True,
            ):
                full_response += response.choices[0].delta.content or ""
                message_placeholder.markdown(full_response + "|")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Save chat history after each interaction
save_chat_history(st.session_state.messages)
