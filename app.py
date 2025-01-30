import streamlit as st
from chatbot import get_gemini_response
from db import get_all_chat_sessions, save_chat, create_new_session, get_chat_history, delete_chat_session

# Streamlit Page Configuration
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")

st.title("AI Chat Bot")

# Initialize session ID if not present in session state
if "session_id" not in st.session_state:
    st.session_state.session_id = create_new_session()  # Generate a new session ID for new chats

# Initialize messages if not present in session state
if "messages" not in st.session_state:
    st.session_state.messages = []  # Initialize the messages list if it's not already initialized

# Function to start a new chat
def start_new_chat():
    st.session_state.session_id = create_new_session()  # Generate a new session ID for new chats
    st.session_state.messages = []  # Clear the current chat history

# Sidebar: Display chat titles (without IDs) as clickable buttons
sessions = get_all_chat_sessions()  # Get all sessions
session_titles = [session[1] for session in sessions]  # Extract the user message as the title
session_ids = [session[0] for session in sessions]  # Extract session IDs

# Button to create a new chat session
if st.sidebar.button("➕ New Chat"):
    start_new_chat()  # Start a new chat when clicked

# Variable to hold selected session title
selected_session_title = None

# Display buttons for each session title with a delete button next to each one
for idx, title in enumerate(session_titles):
    col1, col2 = st.sidebar.columns([8, 1])  # Create two columns: one for the title and one for the delete button
    with col1:
        if st.button(title, key=f"title_{idx}"):
            selected_session_title = title  # Set the selected session when button is clicked
    with col2:
        if st.button("🗑️", key=f"delete_{idx}"):  # Change delete button to trash emoji
            # When delete is clicked, delete the session from the database
            delete_chat_session(session_ids[idx])
            st.experimental_rerun()  # Refresh the page to reflect changes in the sidebar

# Only retrieve and display chat history if a session is selected
if selected_session_title:
    # Get the session ID corresponding to the selected session title
    session_id = session_ids[session_titles.index(selected_session_title)]

    # Get the chat history based on the selected session ID
    chat_history = get_chat_history(session_id)

    # Show the chat history in the main chat window
    for message in chat_history:
        if message[0]:  # User message
            with st.chat_message("user"):
                st.write(message[0])
        if message[1]:  # Bot response
            with st.chat_message("assistant"):
                st.write(message[1])

else:
    # Initial clean screen message when no chat is selected
    st.write("Welcome How can i help you today.?")

# User Input Box to chat with the bot
user_input = st.chat_input("Ask Anything!")

if user_input:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Get bot response
    bot_response = get_gemini_response(user_input)

    # Display bot response
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.write(bot_response)

    # Save the chat message in the database under the current session
    save_chat(st.session_state.session_id, user_input, bot_response)
