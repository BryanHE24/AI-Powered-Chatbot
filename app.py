import streamlit as st
import os
import google.generativeai as genai
from db import get_chat_history, save_chat

# Ensure API key is set
if not os.getenv("GEMINI_API_KEY"):
    st.error("🚨 Missing Gemini API key! Set GEMINI_API_KEY in your environment variables.")
    st.stop()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Streamlit Page Configuration
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")

st.title("🤖 Gemini AI Chatbot")
st.write("Chat with an AI-powered bot using Google Gemini.")

# Initialize chat history in Streamlit session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Function to get Gemini response
def get_gemini_response(user_message):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_message)
        bot_response = response.text if response.text else "Sorry, I couldn't generate a response."
        
        # Save chat to database
        save_chat(user_message, bot_response)

        return bot_response
    except Exception as e:
        return f"Error: {str(e)}"

# User Input
user_input = st.chat_input("Type your message here...")

if user_input:
    try:
        # Display user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)

        # Get bot response
        bot_response = get_gemini_response(user_input) or "I couldn't understand that. Try again!"

        # Display bot response
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        with st.chat_message("assistant"):
            st.write(bot_response)
    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")

# Show Chat History from Database
st.subheader("📜 Chat History")
chat_history = get_chat_history()
if chat_history:
    for chat in chat_history:
        st.write(f"**You:** {chat[0]}")
        st.write(f"**Bot:** {chat[1]}")
        st.write(f"_Timestamp: {chat[2]}_")
        st.write("---")
else:
    st.info("No chat history yet. Start a conversation!")
