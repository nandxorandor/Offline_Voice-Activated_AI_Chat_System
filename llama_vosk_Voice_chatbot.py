import sounddevice as sd
import numpy as np
from vosk import Model, KaldiRecognizer
import json
from langchain.llms import LlamaCpp
import sys
import pyttsx3
import torch
import os

# Device setup for PyTorch
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Number of GPU layers for LlamaCpp
model_n_gpu_layers = int(os.environ.get('MODEL_N_GPU_LAYERS', 56))

# Settings
model_path = "C:/Users/userName/llama_models_notes_generators/vosk-model-en-us-0.22-lgraph"
llama_model_path = "openhermes-2.5-mistral-7b.Q4_K_M.gguf"
sample_rate = 16000
device = None  # None uses the default audio device
chunk_size = 1024  # Size of each audio chunk

# Initialize Vosk model
vosk_model = Model(model_path)

# Initialize Llama model
llm_chatbot = LlamaCpp(streaming=True, model_path=llama_model_path, temperature=0.75, max_new_tokens=25, top_p=0.1, repetition_penalty=5, verbose=True, n_ctx=4096, n_gpu_layers=56)

# Initialize Text-to-Speech engine
tts_engine = pyttsx3.init()

# Conversation history
conversation_history = []  # Initialize the conversation history

# Constants for response processing
MAX_RESPONSE_LENGTH = 50  # Maximum words in the response
PROMPT_INSTRUCTION = "Keep your response short and concise unless asked for details."

# Post-process response to ensure it's short and concise
def post_process_response(response_text):
    words = response_text.split()
    if len(words) > MAX_RESPONSE_LENGTH:
        response_text = ' '.join(words[:MAX_RESPONSE_LENGTH]) + "..."
    return response_text

def process_audio_data(data, recognizer):
    data_bytes = bytes(data)
    if recognizer.AcceptWaveform(data_bytes):
        result = json.loads(recognizer.Result())
        transcription = result.get('text', '').strip()

        # Check if the transcription is substantial
        if transcription and len(transcription.split()) > 1:  # Adjust the condition as needed
            print("Recognized:", transcription)
            conversation_history.append("User: " + transcription)

            conversation_context = PROMPT_INSTRUCTION + " " + " ".join(conversation_history[-5:])
            response = llm_chatbot.generate([conversation_context])
            response_text = response.generations[0][0].text.strip()
            response_text = post_process_response(response_text)
            print("Response:", response_text)

            conversation_history.append("Bot: " + response_text)
            tts_engine.say(response_text)
            tts_engine.runAndWait()
        else:
            print("No substantial transcription detected")
    else:
        print("Recognizer did not accept waveform")


# Main loop
with sd.RawInputStream(samplerate=sample_rate, blocksize=chunk_size, device=device, dtype='int16', channels=1) as stream:
    recognizer = KaldiRecognizer(vosk_model, sample_rate)
    print("Listening...")
    while True:
        data, overflowed = stream.read(chunk_size)
        if overflowed:
            print("Audio buffer has overflowed", file=sys.stderr)
        process_audio_data(data, recognizer)
