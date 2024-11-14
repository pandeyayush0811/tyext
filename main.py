from fastapi import FastAPI
from fastapi.responses import FileResponse
from TTS.api import TTS
import os

app = FastAPI()

# Load the TTS model
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DCA")

@app.get("/generate_audio/")
async def generate_audio(text: str):
    # Create a path for the audio file
    audio_path = "generated_audio.wav"
    
    # Generate audio file
    tts.tts_to_file(text=text, file_path=audio_path)
    
    # Return the audio file as response
    return FileResponse(audio_path, media_type='audio/wav', filename="generated_audio.wav")
