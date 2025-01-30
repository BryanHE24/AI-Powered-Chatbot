import sqlite3

# Create or connect to an SQLite database
def init_db():
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    
    # Create a table to store chat history
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT NOT NULL,
            bot_response TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

# Insert a new chat record
def save_chat(user_message, bot_response):
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO chat_history (user_message, bot_response) VALUES (?, ?)",
                   (user_message, bot_response))
    conn.commit()
    conn.close()

# Retrieve past chats
def get_chat_history():
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute("SELECT user_message, bot_response, timestamp FROM chat_history ORDER BY timestamp DESC")
    chats = cursor.fetchall()
    conn.close()
    return chats

# Initialize database when script runs
init_db()
