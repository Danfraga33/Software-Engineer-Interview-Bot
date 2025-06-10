from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import os

print("Starting FastAPI application...")

# Custom Function Imports
try:
    from functions.database import store_messages, resetMessages
    from functions.openai_requests import convert_audio_to_text, get_chat_response
    from functions.text_to_speech import convert_text_to_speech
    print("✓ All imports successful")
except Exception as e:
    print(f"✗ Import error: {e}")
    raise

# Check environment variables
try:
    openai_key = os.environ.get("OPEN_AI_KEY")
    if openai_key:
        print("✓ OpenAI API key found")
    else:
        print("✗ OpenAI API key not found in environment variables")
except Exception as e:
    print(f"✗ Error checking environment variables: {e}")

# Initiate app
app = FastAPI()
print("✓ FastAPI app created")

# CORS
origins = [
    "http://localhost:5173",
    "http://localhost:5174", 
    "http://localhost:4173",
    "http://localhost:4174",
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:5175"   
]

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
print("✓ CORS middleware added")

# Check Health
@app.get("/health")
async def check_health():
    return {'message': 'healthy'}

@app.get("/reset")
async def reset_conversation():
    try:
        resetMessages()
        return {'message': 'conversation reset'}
    except Exception as e:
        print(f"Error resetting conversation: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/post-audio/")
async def post_audio(file: UploadFile = File(...)):
    print(f"Received file: {file.filename}, content_type: {file.content_type}")
    
    try:
        # Save audio from frontend
        filename = f"temp_{file.filename}"
        print(f"Saving file as: {filename}")
        
        with open(filename, 'wb') as buffer:
            content = await file.read()  # Use await for async file reading
            buffer.write(content)
        
        print(f"File saved, size: {os.path.getsize(filename)} bytes")
        
        # Open the saved file for transcription
        with open(filename, 'rb') as audio_input:
            print("Converting audio to text...")
            message_decoded = convert_audio_to_text(audio_input)
        
        print(f"Transcribed message: {message_decoded}")
        
        # Clean up temp file
        try:
            os.remove(filename)
            print("Temp file cleaned up")
        except Exception as cleanup_error:
            print(f"Warning: Could not remove temp file: {cleanup_error}")
        
        # Guard
        if not message_decoded: 
            print("Failed to decode audio")
            raise HTTPException(status_code=400, detail="Failed to decode audio")
        
        # Get ChatGPT response
        print("Getting chat response...")
        chat_response = get_chat_response(message_decoded)
        
        # Guard
        if not chat_response: 
            print("Failed to get chat response")
            raise HTTPException(status_code=400, detail="Failed chat response")
        
        # Store messages
        store_messages(message_decoded, chat_response)
        print(f"Chat response: {chat_response}")
        
        # Convert chat response to audio
        print("Converting text to speech...")
        audio_output = convert_text_to_speech(chat_response)
        
        # Guard
        if not audio_output: 
            print("Failed to convert text to speech")
            raise HTTPException(status_code=400, detail="Failed audio output")
        
        print("Returning audio response")
        
        # Create a generator that yields chunks of data
        def iterfile():
            yield audio_output
        
        # Return output audio
        return StreamingResponse(iterfile(), media_type="application/octet-stream")
        
    except Exception as e:
        print(f"Error in post_audio: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    print("Starting server on http://localhost:5175")
    uvicorn.run(app, host="0.0.0.0", port=5175)