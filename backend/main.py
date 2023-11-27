#source venv/Scripts/activate
#uvicorn main:app --reload

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

# Custom Function Imports
from functions.database import store_messages, resetMessages
from functions.openai_requests import convert_audio_to_text, get_chat_response
from functions.text_to_speech import convert_text_to_speech

# Initiate app
app = FastAPI()


# CORS
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4174",
    "http://localhost:3000",
    "http://localhost:8000",
]


# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Check Health
@app.get("/health")
async def check_health():
    return {'message':'healthy'}

@app.get("/reset")
async def reset_conversation():
    resetMessages()
    return {'message':'conversation reset'}



# @app.get("/post-audio-get/")
# async def get_audio():
@app.post("/post-audio/")
async def post_audio(file: UploadFile = File(...)):

# Get saved audio
    # audio_input = open("DanielVoice.mp3", "rb")


# Save audio from frontend
    with open(file.filename, 'wb') as buffer:
      buffer.write(file.file.read())
    audio_input = open(file.filename, 'rb')


    message_decoded= convert_audio_to_text(audio_input)


    # Guard
    if not message_decoded: 
        raise HTTPException(status_code=400, detail="Failed to decode audio")
    
    # Get ChatGPT response
    chat_response = get_chat_response(message_decoded)


    # Store messages
    store_messages(message_decoded, chat_response)
    print(chat_response)
       # Guard
    if not chat_response: 
        raise HTTPException(status_code=400, detail="Failed chat response")


    # Convert chat response to audio
    audio_output = convert_text_to_speech(chat_response)
    # Guard
    if not audio_output: 
        raise HTTPException(status_code=400, detail="Failed audio output")
    

    # Creat a generator that yields chunks of data
    def iterfile():
        yield audio_output

    # Return output audio
    return StreamingResponse(iterfile(), media_type="application/octet-stream")


    
    print(chat_response)

    return "Done"
# POST bot response
# Note: Not playing in browser when using post request

# @app.post("/post-audio/")
# async def post_audio(file: UploadFile = File(...)):
#     print("HELLO")

@app.get("/")
def read_root():
    return {"Hello": "World"}