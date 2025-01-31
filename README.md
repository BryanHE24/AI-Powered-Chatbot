# AI-Powered ChatBot Web Application

## Overview

This is a web-based chatbot application powered by Google's Gemini AI. It allows users to interact with the chatbot, save chat sessions, and view chat history. Users can also delete past chats from the sidebar and create new chat sessions.

## Technologies Used

- **Streamlit**: Used for building the interactive web interface.
- **SQLite**: Database to store chat sessions and history.
- **Python**: Main programming language for backend logic.
- **Google Gemini**: AI language model for generating responses.
- **UUID**: To generate unique session IDs.

## Features

- **Chat Interface**: Interact with the chatbot through a clean and user-friendly interface.
- **Chat History**: Save past chat sessions and view them from the sidebar.
- **Session Management**: Create new sessions and delete previous ones.
- **Responsive**: Works well across devices with an intuitive UI.

## How It Was Created

This project was built to allow users to have conversations with a chatbot powered by Google’s Gemini model. The app stores chat histories in a local SQLite database and provides a simple interface built with Streamlit. Each session is uniquely identified by a session ID and the first user message serves as the session title. Users can view past conversations, start new chats, and delete old sessions from the sidebar.

### Project Structure

- `app.py`: Main file where the Streamlit app runs, handles session management, and displays chat history.
- `chatbot.py`: Contains functions for interacting with Google Gemini and generating chatbot responses.
- `db.py`: Handles the SQLite database operations, such as saving and retrieving chat history and managing chat sessions.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/BryanHE24/AI-Powered-Chatbot
    ```

2. Navigate to the project folder:
    ```bash
    cd AI-Powered ChatBot
    ```

3. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Create a .env file and store your gemini API Key Like this:
   ```bash
    GEMINI_API_KEY=yourkey
    ```

7. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Usage

Once the app is running, you can:

1. **Start a new chat**: Click the "Start New Chat" button in the sidebar.
2. **View previous chats**: Click on any chat title in the sidebar to see the chat history.
3. **Delete chats**: Click the 🗑️ (trash) emoji next to any chat in the sidebar to delete it.
4. **Chat with the AI**: Type your message in the input box at the bottom and hit Enter.

## Images
![image](https://github.com/user-attachments/assets/660fae8c-a8c5-4278-8e53-af27f4c5da70)
![image](https://github.com/user-attachments/assets/1b7bfea8-f64d-48dd-81b3-15a66920eb7e)

## Contributing

If you’d like to contribute to this project, feel free to fork the repository and submit a pull request.

## License
This project is open-source and available under the [MIT License](LICENSE).
