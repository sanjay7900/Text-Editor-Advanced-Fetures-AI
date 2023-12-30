import speech_recognition as sr
import pyaudio
start=sr.Recognizer()
with sr.Microphone() as source:
    print("say")
    
    try:
        catch_data=start.listen(source)
        text=start.recognize_google(catch_data)
        print(text)
    except Exception as e:
        print(e)

