import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime

#Initialize
recognizer = sr.Recognizer()
engine = pyttsx3.init()

#Speak function, when called assistant speaks the text
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()
    
#listen function, when called assistant listens
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        # Adjust microphone for background noise
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text.lower()
    except sr.UnknownValueError:
        speak("Sorry, I could not understand you.")
        return ""
    except sr.RequestError:
        speak("Sorry, I am having trouble connecting to the speech recognition service.")
        return ""

#Main assistant
speak("Hello. I am your virtual assistant. How can I help you?")
while True:
    command = listen()
    #Empty command
    if command == "":
        continue
    #Hello
    if "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")
    #Time
    elif "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        speak("The current time is " + current_time)
    #Open Google
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    #Open Youtube
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    #Search
    elif command.startswith("search"):
        query = command.replace("search", "", 1).strip()
        if query != '':
            speak("Searching for " + query)
            url = "https://www.google.com/search?q=" + query
            webbrowser.open(url)
        else:
            speak("What would you like me to search for?")
     #github       
    elif "open github" in command:
         speak("Opening GitHub")
         url = "https://github.com"
         webbrowser.open(url)
         