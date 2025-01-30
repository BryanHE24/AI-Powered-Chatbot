# In this file we configurate the chatbot 

import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Get gemini responses
def get_gemini_response(user_input):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_input)

        # Check if response contains valid text
        if response.candidates:
            candidate = response.candidates[0]
            if candidate.finish_reason == 4:
                return "⚠️ Sorry, I can't provide that information due to copyright restrictions."
            if candidate.content and candidate.content.parts:
                return candidate.content.parts[0].text
        
        return "⚠️ Sorry, I couldn't generate a response."
    except Exception as e:
        return f"Error: {str(e)}"
