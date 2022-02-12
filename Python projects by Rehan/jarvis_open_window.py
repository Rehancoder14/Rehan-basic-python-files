import pyttsx3 as rs
import speech_recognition as sr
import tkinter as tk
from tkinter import*

engine = rs.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty("voices", voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    speak("Good Morning Rehan")

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone as sources:
        print("LISTENING.......")
        r.pause_threshold = 0.8
        r.energy_threshold =280
        audio = r.listen(sources)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language = "en-in")
        print(f"User said : {query}\n" )
    except Exception as e: 
        print(e)

        print("Sorry! didn't get that")
        return "None"
    return query

# def __init__(self, root):
#     self.root = root
#     self.root.title("Way to success")
#     self.root.geometry("1000x600+0+0")

if __name__ == "__main__":
    greet()
    
    if 1:
        query = listen_command().lower()
        query = 

