import sqlite3
import uuid

# Create or connect to SQLite database
def init_db():
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT NOT NULL,
            user_message TEXT NOT NULL,
            bot_response TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

# Insert a new chat record
def save_chat(session_id, user_message, bot_response):
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO chat_history (session_id, user_message, bot_response) VALUES (?, ?, ?)",
                   (session_id, user_message, bot_response))
    conn.commit()
    conn.close()

# Retrieve past chat history by session_id
def get_chat_history(session_id):
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute("SELECT user_message, bot_response, timestamp FROM chat_history WHERE session_id = ? ORDER BY timestamp ASC", 
                   (session_id,))
    chats = cursor.fetchall()
    conn.close()
    return chats

# Retrieve all chat sessions (session titles without IDs)
def get_all_chat_sessions():
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()

    # Retrieve the first user message (title) for each session_id
    cursor.execute("""
        SELECT session_id, user_message 
        FROM chat_history
        WHERE id IN (
            SELECT MIN(id) 
            FROM chat_history 
            GROUP BY session_id
        )
    """)
    sessions = cursor.fetchall()
    conn.close()

    return sessions

# Create a new session (generate a unique ID and use the first prompt as title)
def create_new_session():
    return str(uuid.uuid4())  # Generate a unique session ID for new chats

# Delete a session (by session ID)
def delete_chat_session(session_id):
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    
    # Delete all chat history related to the session ID
    cursor.execute("DELETE FROM chat_history WHERE session_id = ?", (session_id,))
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Initialize database when script runs
init_db()
