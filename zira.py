import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
#engine.setProperty('rate', 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Zira. Please tell me how may I help you")


def takeCommand():
    # it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendemail(to, content):
    server = smtplib.SMTP('smpt.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("aryakulkarni333@gmail.com","password")
    server.sendmail("aryakulkarni333@gmail.com",to,content)
    server.close()

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

if __name__ == "__main__":
    #wishMe()
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            wishMe()

            while True:  # if 1
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok, you can call me anytime")
                    break
                # logic for executing tasks based on query
                elif 'wikipedia' in query:
                    speak("Searching Wikipedia...")
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

                elif 'open youtube' in query:
                    webbrowser.open("youtube.com")
                elif 'open google' in query:
                    webbrowser.open("google.com")
                elif 'open stack overflow' in query:
                    webbrowser.open("stackoverflow.com")

                elif 'play music' in query:
                    music_dir = 'C:\\Non Crictical\\songs\\Favorite Songs'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir, songs[0]))

                elif 'time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"The time is {strTime}")

                elif 'date' in query:
                    currentDate = datetime.datetime.now().strftime("%d-%m-%Y")
                    speak(f"The date is {currentDate}")

                elif 'day' in query:
                    currentDay = datetime.datetime.now().strftime("%A")
                    speak(f"Today is {currentDay}")


                elif 'email to arya' in query:
                    try:
                        speak("What should I say?")
                        content = takeCommand()
                        to = "aryakulkarni333@gmail.com"
                        sendEmail(to, content)
                        speak("Email has been sent!")

                    except Exception as e:
                        print(e)
                        speak("Sorry I am not able to send this email")

                elif "open" in query:
                    from Dictapp import openappweb

                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb

                    closeappweb(query)

                elif "google" in query:
                    from search import searchGoogle

                    searchGoogle(query)
                elif "youtube" in query:
                    from search import searchYoutube

                    searchYoutube(query)
                # elif "wikipedia" in query:
                # from search import searchWikipedia
                # searchWikipedia(query)

                elif "news" in query:
                    from NewsRead import latestnews

                    latestnews()

                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc

                    query = query.replace("calculate", "")
                    query = query.replace("jarvis", "")
                    Calc(query)

                elif "temperature" in query:
                    search = "temperature in kolhapur"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")  # using this we will fetch temp from google
                    temp = data.find("div", class_="BNeawe").text  # _ is for class error
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "weather in kolhapur"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current{search} is {temp}")

                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")

                elif "finally sleep" in query:
                    speak("going to sleep")
                    exit()


