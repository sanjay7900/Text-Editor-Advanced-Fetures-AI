import speech_recognition as sr

start=sr.Recognizer()
with sr.Microphone() as source:
    catch_data=start.listen(source)
    try:
        text=start.reconize_google(catch_data)
        print(text)
    
    except:
        print("hjk")
