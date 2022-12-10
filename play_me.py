import os
import speech_recognition as sr

file = open("output.txt","w")

r = sr.Recognizer()
print("Please ask a question...")
with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data)
    print(text)
    file.writelines(text)

file.close()
os.system("python extension.py")

