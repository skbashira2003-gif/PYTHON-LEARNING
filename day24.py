import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime
import urllib.parse

# Initialize
recognizer = sr.Recognizer()
engine = pyttsx3.init()


# Speak Function
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


# Listen Function
def listen():
    with sr.Microphone() as source:
        print("Listening... Speak now!")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=7
            )

            print("Recognizing your voice...")

            text = recognizer.recognize_google(audio, language="en-IN")

            print("You said:", text)
            return text.lower()

        except sr.WaitTimeoutError:
            print("No voice detected. Try again.")
            return ""

        except sr.UnknownValueError:
            print("Voice not understood. Speak clearly.")
            return ""

        except sr.RequestError:
            print("Internet connection issue.")
            return ""
# Main Assistant
speak("Hello. I am your virtual assistant. How can I help you?")

while True:

    command = listen()

    if command == "":
        continue

    # Exit Assistant
    if any(word in command for word in ["exit", "stop assistant", "quit", "goodbye"]):
        speak("Goodbye! Have a nice day.")
        break

    # Hello
    elif "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")

    # Time
    elif "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        speak("The current time is " + current_time)

    # Open Google
    elif "google" in command:
        speak("Opening Google")
        webbrowser.open_new_tab("https://www.google.com")

    # Open YouTube
    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open_new_tab("https://www.youtube.com")

    # Open GitHub
    elif "github" in command:
        speak("Opening GitHub")
        webbrowser.open_new_tab("https://github.com")

    # Open CodeGnan
    elif "codegnan" in command:
        speak("Opening CodeGnan")
        webbrowser.open_new_tab("https://codegnan.com")

    # Google Search
    elif command.startswith("search"):
        query = command.replace("search", "", 1).strip()

        if query:
            speak("Searching for " + query)

            encoded_query = urllib.parse.quote_plus(query)

            url = "https://www.google.com/search?q=" + encoded_query

            webbrowser.open_new_tab(url)

        else:
            speak("What would you like me to search for?")

    # Unknown Command
    else:
        speak("Sorry, this command is not available.")