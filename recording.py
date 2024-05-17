#RINKU BABU LODHI
import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(filename, duration, sample_rate=44100):
    print("Recording...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='int16')
    sd.wait()  
    write(filename, sample_rate, audio)  
    print(f"Recording saved to {filename}")

def main():
    filename = "output.wav"
    duration = 5  
    record_audio(filename, duration)

if __name__ == "__main__":
    main()
