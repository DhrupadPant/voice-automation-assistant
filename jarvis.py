import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit 
import os

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  

engine.setProperty("rate", 180)
engine.setProperty("volume", 1.0)  

def talk(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        talk("Ooooh child, Good mornin’ ")
    elif 12 <= hour < 18:
        talk("Ooooh it’s the afternoon already? And here I was thinkin’ you'd sleep through the whole day!")
    else:
        talk("Good evenin’ sugar. You lookin’ for trouble or just passin’ through?")
    talk("I’m JARVIS. Don’t waste my time—what we doin’ today?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        command = r.recognize_google(audio)
        print("You:", command)
    except:
        talk("Say what now? Run that back for me, nice and clear.")
        return ""
    return command.lower()

def run_jarvis():
    wish_me()
    while True:
        command = take_command()

        if "time" in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            talk(f"Let’s see… it’s {time} darlin’. Which means you got just enough time to get your life together.")
        
        elif "Wassup" in command or "Sup" in command:
            talk("Hey! Ready to get things done, or just here to chat?")

        elif "hi" in command or "hello" in command:
            talk("Hey! Ready to get things done, or just here to chat?")

        elif "wikipedia" in command:
            topic = command.replace("wikipedia", "")
            summary = wikipedia.summary(topic, sentences=2)
            talk("Mmmkay, Wikipedia’s got the tea. Here’s what they spillin")
            talk(summary)

        elif "open notepad" in command:
            os.system("notepad")

        elif "open chrome" in command:
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome_path)

        elif "search" in command:
            topic = command.replace("search", "")
            talk(f"Hold up, lemme see what the internet gossip says ‘bout {topic}")
            pywhatkit.search(topic)

        elif "play" in command:
            song = command.replace("play", "")
            talk(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)

        elif "goodbye" in command or "stop" in command:
            talk("Aight, I’m outta here. Don’t miss me too much, alright?")
            break

        elif command != "":
            talk("Ain’t got that on my playlist just yet. Check back later, alright?")

run_jarvis()