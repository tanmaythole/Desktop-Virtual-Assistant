import pyttsx3
import speech_recognition as sr
import webbrowser
import os
from datetime import datetime

engine = pyttsx3.init()

def wishme():
    engine.say("Hello Sir, This is Jarvis. How can I help you?")
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(src)
    
    try:
        q = r.recognize_google(audio, language='en-in')
        print(q)
        return q
    except Exception as e:
        print(e)

def speak(sp):
    engine.say(sp)
    engine.runAndWait()
    
def showtimedate():
    dt = datetime.now()
    print(dt.strftime("%d %B, %Y"))
    print(dt.strftime("%I:%M %p"))
    speak(f"Todays date is {dt.strftime('%d %B, %Y')} and current time is {dt.strftime('%I:%M %p')}")

if __name__=='__main__':
    wishme()
    while True:
        cmd = takecommand().lower()
        if 'open browser' in cmd:
            webbrowser.open('https://google.com')

        elif 'search' in cmd:
            srch = cmd.split('search')
            query = srch[len(srch) - 1]
            webbrowser.open(f'https://google.com/search?q={query}')

        elif 'open youtube' in cmd.lower():
            webbrowser.open('https://youtube.com')
        
        elif 'open vs code' in cmd:
            os.startfile("C:\\Users\\Tanmay Thole\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        
        elif 'time' in cmd or 'date' in cmd:
            showtimedate()
        break