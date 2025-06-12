import requests
from decouple import AutoConfig
config = AutoConfig()

# Get API key with error handling
try:
    ELEVEN_LABS_API_KEY = config("ELEVEN_LABS_API_KEY")
    if not ELEVEN_LABS_API_KEY:
        raise ValueError("ELEVEN_LABS_API_KEY not found")
    print("ElevenLabs API key loaded successfully")
except Exception as e:
    print(f"Error loading ElevenLabs API key: {e}")
    ELEVEN_LABS_API_KEY = None

def convert_text_to_speech(message):
    if not ELEVEN_LABS_API_KEY:
        print("Error: ElevenLabs API key not available")
        return None
    
    if not message or not message.strip():
        print("Error: Empty message provided")
        return None

    body = {
        'text': message,
        'voice_settings': {
            'stability': 0.5,  # Increased for better quality
            'similarity_boost': 0.5  # Increased for better quality
        }
    }

 
    voice_sarah = 'EXAVITQu4vr4xnSDxMaL'

    # Constructing Headers
    headers = {
        'xi-api-key': ELEVEN_LABS_API_KEY,
        'Content-Type': 'application/json',
        'accept': 'audio/mpeg'
    }

    # Constructing URL
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_sarah}"

    try:
        print(f"Sending TTS request for message: {message[:50]}...")
        response = requests.post(url, json=body, headers=headers)
        
        print(f"TTS Response status: {response.status_code}")
        
        if response.status_code == 200:
            print("TTS conversion successful")
            return response.content
        else:
            print(f"TTS API Error: {response.status_code}")
            print(f"Response: {response.text}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Request error in TTS: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error in TTS: {e}")
        return None