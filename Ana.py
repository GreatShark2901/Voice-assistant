from sqlite3 import connect
from time import strftime, struct_time
import webbrowser
import pyttsx3
import speech_recognition as sr
from datetime import datetime
import wikipedia
import webbrowser
import os
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")    
    
    else:
        speak("Good Evening!")

    speak("I am Ana . Please tell me how may i help you")    

def takeCommand():
      

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising....")
        query = r.recognize_google(audio,language='En-In')
        print(f"User said: {query}\n")


    except Exception as e:
        
        print("Say that again please....")
        return"None"  

    return query


if __name__== "__main__":
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()

        if'wikipedia' in query:
            speak('Searching wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com") 

        elif 'open google' in query:
            webbrowser.open("google.com")   

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'show weather' in query:
            webbrowser.open("weather.com")  


        elif 'open pycharm' in query:
            webbrowser.open("pycharm64")    


        elif 'open eclipse' in query:
            webbrowser.open("eclipse") 

        elif 'the time' in query:
            strTime = datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to Aditya' in query:
            try:
                speak("What should i say ?")
                content = takeCommand()
                sendEmail(adityakeshri0729@gmail.com,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, Email has not been send")    





