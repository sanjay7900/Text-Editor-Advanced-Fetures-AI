import speech_recognition as sr
import webbrowser
import pyttsx3
from gtts import gTTS
import pygame
#import win32api
eng = pyttsx3.init('dummy')
pygame.mixer.init()

#eng.getProperty('rate')
#print(v[0].id)
#eng.setProperty('volume', 0.9)
#eng.say("sanjay gfytdyiutrt")
#eng.runAndWait()

text=""
r= sr.Recognizer()
def aud():
   
   
   with sr. Microphone() as source:
      print("say something")
      r.pause_threshold=1
      audio=r.listen(source)
   try:
      
      text= r.recognize_google(audio)
      print(text)
      i=gTTS(text)
      i.save("muc.mp3")
      pygame.mixer.music.load('muc.mp3')
      pygame.mixer.music.play()
      
 
   except Exception as es:
      print("try again",es)
      #return "none"
#finally:
 #     print(text)
if __name__ == "__main__":
   
   aud()
