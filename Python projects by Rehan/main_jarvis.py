import os 
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import random
import smtplib
from wikipedia import exceptions
import tkinter as tk

engine = pyttsx3.init("sapi5") # sap5 is speech api
voices= engine.getProperty("voices")

engine.setProperty("voices", voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("A very Good Morning REHAN ")
    elif hour>12 and hour<18:
        speak("Good Afternoon REHAN")
    else:
        speak("Good Evening REHAN")
    

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as sources:
        print("Listening.....")
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
def sendEmail(to, mail):
    server= smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("rehanmahat999@gmail.com", "chessgambit")
    server.sendmail("rehanmahat999@gmail.com", to, mail)
    server.close()


if __name__ == "__main__":
    greet()
    speak("Please TEll me  how can I help you")
    if 1:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak("searching Wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif "open youtube" in query:
            youtube_path = "C:\\Users\\user\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Chrome Apps\\YouTube"
            os.startfile(youtube_path)

        elif "open chess" in query:
            webbrowser.open("lichess.org")

        elif "open google" in query:
            webbrowser.open("google.com")
        
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            musicfile = "D:\\my_fav_song"
            fav_song = os.listdir(musicfile)
            random_song = random.randint(0,22)
            os.startfile(os.path.join(fav_song[random_song])) 

        elif "time" in query:
            strtime = datetime.datetime.now().strftime("%H : %M: %S")
            speak(strtime)
        
        elif "send email" in query:
            try:
                speak("What should I say")
                mail = takeCommand()
                to = "rsmahat3@gmail.com"
                sendEmail(to, mail)
                speak("Email has been sent!")
                
            except Exception as e:
                print(e)
                speak("Sorry! mail has not been delivered")

        # elif "play movie":
        #     try:
        #         moviepath = "E:\\MOVIES"
        #         fav_movie = os.listdir(moviepath)
        #         os.startfile(os.path.join(fav_movie[1]))

        #     except Exception as e:
        #         print(e)
        #         speak("Sorry movie not found")

        elif "billa song" in query:
            try: 
                song_url = "https://youtu.be/0aUav1lx3rA"
                webbrowser.open(song_url)
            except Exception as e:
                print(e)
                speak("song not found ")

        elif  "osman" in query:
            webbrowser.open('https://youtu.be/1QP3Mq2aYi4')
        
        
            