import pyaudio
import wave

def record_voice():
    # Set the duration and sampling frequency for recording
    duration = 6  # Recording duration in seconds
    sample_rate = 44100  # Sampling frequency in Hz
    chunk_size = 1024  # Number of frames per buffer

    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Open audio stream
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=sample_rate, input=True, frames_per_buffer=chunk_size)

    # Start recording
    print("Recording started. Press Ctrl+C to stop recording.")
    frames = []

    try:
        for _ in range(int(duration * sample_rate / chunk_size)):
            data = stream.read(chunk_size)
            frames.append(data)
    except KeyboardInterrupt:
        pass

    # Stop recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio to a WAV file
    file_name = "recorded_audio.wav"
    wf = wave.open(file_name, "wb")
    wf.setnchannels(1)
    wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    wf.setframerate(sample_rate)
    wf.writeframes(b"".join(frames))
    wf.close()

    print(f"Recording saved as {file_name}")
