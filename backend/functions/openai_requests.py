from decouple import config
import openai
from functions.database import get_recent_messages 
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai_api_key = os.environ["OPEN_AI_KEY"]
client = OpenAI(api_key=openai_api_key)

# Open AI - Whisper
# Convert audio to text
def convert_audio_to_text(audio_file):
    try:
        # Updated syntax for openai>=1.0.0
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
        message_text = transcript.text
        return message_text
    except Exception as e:
        print(f"Error transcribing audio: {e}")
        return None

# OPEN AI - CHATGPT
# GET Response to our messages
def get_chat_response(message_input):
    messages = get_recent_messages()
    user_message = {"role": "user", 
                    "content": message_input}
    messages.append(user_message)

    try: 
        # Fixed: Use chat.completions.create instead of completions.create
        response = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=messages
        )
        
        # Fixed: Correct way to access response content
        message_text = response.choices[0].message.content
        return message_text
    except Exception as e: 
        print(f"Error getting chat response: {e}")
        return None