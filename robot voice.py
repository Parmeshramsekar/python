import speech_recognition as sr
from gtts import gTTS
import os
voice = ""
while true :

    r = sr.recognizer()
    with sr.microphone() as source:
        try:
            audio = r.listen(source)
            text = r.recognize.google(audio)
            print(text)
            if text =="stop":
                break
                text = r.recognize.google(audio)
                voice = voice + str(text)
        except :
            print("say something.....")
            hr = gTTS(text=voice,lang='en',slow=false)
            hr.save("1.wav")