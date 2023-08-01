import time 
from elevenlabs import generate
def speech(responce,api):
    audio = generate(
    text=responce,
    voice="Arnold",
    model='eleven_monolingual_v1',
    api_key=api
    )
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    f_name = "rec"
    file_name = f"{f_name}_{timestamp}.wav"
    
    with open(file_name, "wb") as out:
    
        out.write(audio)
        print('Audio content written to file "output.mp3"')
    return file_name
   

    
