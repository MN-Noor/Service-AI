from google.cloud import speech_v1p1beta1 as speech

def transcription(file_name):
    client = speech.SpeechClient.from_service_account_file('key.json')

    with open(file_name, 'rb') as f:
        mp3_data = f.read()

    audio_file = speech.RecognitionAudio(content=mp3_data)

    config = speech.RecognitionConfig(
        sample_rate_hertz=48000,
        enable_automatic_punctuation=True,
        language_code='en-US'
    )

    response = client.recognize(
        config=config,
        audio=audio_file
    )

    transcript = ""
    for result in response.results:
        for alternative in result.alternatives:
            transcript += alternative.transcript
    transcript = transcript.replace(".", "")

    return transcript





