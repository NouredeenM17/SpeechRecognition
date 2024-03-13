import os
import wave
import json
import vosk

def recognize_speech():
    model_path = "vosk-model-en-us-0.22-lgraph"
    audio_file = "recorded_audio.wav"

    wf = wave.open(audio_file, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print("Audio file must be WAV format mono PCM.")
        exit(1)

    model = vosk.Model(model_path)
    rec = vosk.KaldiRecognizer(model, wf.getframerate())

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            pass


    def write_string_to_txt(string, file_name):
        with open(file_name, "w") as file:
            file.write(string)
        print(f"String written to {file_name} successfully.")

    result = rec.FinalResult()[14:-3]
    
    words = result.split()
    if words and words[-1] == "the":
        words.pop()
    result = ' '.join(words)
        
    print(result)

    write_string_to_txt(result, "recognizedText.txt")