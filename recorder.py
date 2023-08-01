import pyaudio
import numpy as np
import streamlit as st
from google.cloud import speech_v1p1beta1 as speech

def record():
    freq = 48000
    duration = 5

   
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=freq, input=True, frames_per_buffer=int(duration * freq))
    st.write("Recording...")
    recording = np.frombuffer(stream.read(int(duration * freq)), dtype=np.int16)
    stream.stop_stream()
    stream.close()
    audio.terminate()
    st.write("recording stopped")
    
    audio_content = recording.tobytes()

   
    client = speech.SpeechClient.from_service_account_json('key.json')

    audio = speech.RecognitionAudio(content=audio_content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=freq,
        language_code="en-US",
    )

    
    response = client.recognize(config=config, audio=audio)

    
    transcript = " "
    for result in response.results:
        for alternative in result.alternatives:
            transcript += alternative.transcript
    transcript = transcript.replace(".", "")

    return transcript

   
   