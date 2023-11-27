import requests
from decouple import config

ELEVEN_LABS_API_KEY = config("ELEVEN_LABS_API_KEY")

# Eleven labs
# convert text to speech

def convert_text_to_speech(message):

   body = {
      'text': message,
      'voice_settings': {
         'stability':0,
         'similarity_boost': 0 
      }
   }

# Define Voice
   voice_rachel='EXAVITQu4vr4xnSDxMaL'


# Constructing EndPoint
   headers = {
      'xi-api-key': ELEVEN_LABS_API_KEY, "Content-Type": "application/json", "accept": 'audio/mpeg'
   }

   url = "https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL"

   # Send req
   try:
      response = requests.post(url, json=body, headers = headers)
   except Exception as e:
      return
   
   # Handle Response
   if response.status_code == 200:
      return response.content
   else: 
      return 