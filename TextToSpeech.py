
from pydub.playback import play
import pyttsx3

def text_to_speech(data):
    engine = pyttsx3.init()

    #voices = engine.getProperty('voices')
    # # Get the available voices and print them
    # for voice in voices:
    #     print(voice, voice.id)
    # Set the voice by ID
    #engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
    
    engine.say(data)
    engine.runAndWait()
