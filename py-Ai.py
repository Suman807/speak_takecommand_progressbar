import pyttsx3 
import speech_recognition as sr
import datetime
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User Said : {query}\n")
    except Exception as e:
        print("say that again please .....")
        return "None"
    return query

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")

def progress_bar():
    spam = True
    while spam:
        fill = '■'
        prefix='Progress'
        suffix='complete'
        for i in range(0,105,5):
            num=(i/10)+5
            print(f"\r{prefix} : ",end="")
            print(f"{fill*int(num)} ",end="")
            print(f"{i}% {suffix}",end="\r")
            time.sleep(0.01)
        print("\n")
        spam = False 
