import speech_recognition as sr
import pyttsx3
from datetime import datetime, timedelta
import webbrowser
import pyjokes
import os
import requests
from googletrans import Translator
import re
import time

recognizer = sr.Recognizer()
tts_engine = pyttsx3.init('sapi5')
voices = tts_engine.getProperty('voices')
tts_engine.setProperty('voice', voices[1].id)

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand")
            return None
        except sr.RequestError:
            print("Could not request results.")
            return None

def parse_time(time_string):
    match = re.match(r'(\d{1,2}:\d{2}\s*[APMapm]*)', time_string)
    if match:
        time_string = match.group().upper().replace(" ", "")
        if "AM" in time_string or "PM" in time_string:
            return datetime.strptime(time_string, '%I:%M%p').strftime('%I:%M %p')
        elif "A" in time_string or "P" in time_string:
            return datetime.strptime(time_string.replace("A", "AM").replace("P", "PM"), '%I:%M%p').strftime('%I:%M %p')
    return None

def handle_command(command, user_name):
    if command is None:
        speak("Sorry, I did not understand that!")
        return True

    if "hello" in command or "hi" in command:
        speak(f"Hello {user_name}, how can I help you today?")

    elif "your name" in command:
        speak("I am your voice assistant Amara.")

    elif "time" in command:
        now = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}")
        
    elif "date" in command:
        today = datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {today}")

    elif "day" in command:
        day = datetime.now().strftime("%A")
        speak(f"Today is {day}")

    elif "exit" in command or "thank you" in command or "thanks" in command:
        speak("Thank you for giving me your time. Goodbye!")
        return False
    
    elif "hungry" in command:
        speak("Go and cook something then")

    elif "help" in command:
        speak("Sure! How may I help you?")

    elif "sad" in command:
        speak("What's troubling you?")

    elif 'joke' in command:
        speak(pyjokes.get_joke())

    elif 'open youtube' in command:
        speak("Here you go to YouTube\n")
        webbrowser.open("https://www.youtube.com")

    elif 'open google' in command:
        speak("Here you go to Google\n")
        webbrowser.open("https://www.google.com")

    elif "exams" in command:
        speak("Go study. Want any help?")

    elif "who created you" in command:
        speak("I was created by Ameen Zehra")

    elif "tell me about her" in command:
        speak("She is a smart B.Tech student")

    elif 'how are you' in command:
        speak("I am fine, thank you")
        speak(f"How are you, {user_name}?")

    elif 'fine' in command or "good" in command:
        speak("It's good to know that you're fine")

    elif "what's your name" in command or "what is your name" in command:
        speak("My friends call me Amara")

    elif 'open camera' in command:
        speak("Opening camera")
        os.system("start microsoft.windows.camera:")

    elif 'open gmail' in command or 'open email' in command:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")

    elif 'open powerpoint' in command:
        speak("Opening Microsoft PowerPoint")
        os.system("start powerpnt")

    elif 'open word' in command:
        speak("Opening Microsoft Word")
        os.system("start winword")

    elif 'open excel' in command:
        speak("Opening Microsoft Excel")
        os.system("start excel")

    elif 'open notes' in command:
        speak("Opening Notepad")
        os.system("notepad")
        
    elif 'calculate' in command:
        expression = command.replace('calculate', '').strip()
        try:
            result = eval(expression)
            speak(f"The result of {expression} is {result}")
        except:
            speak("Sorry, I couldn't calculate that.")

    else:
        speak("Sorry, I don't know how to respond to that.")
        
    return True

def main():
    speak("Voice assistant initialized. What is your name? Please type it.")
    user_name = input()
    if user_name:
        speak(f"Hello {user_name}, how may I help you today?")
    else:
        user_name = "User"
        speak("I couldn't catch your name. I'll call you User. How may I help you today?")
    
    while True:
        command = listen()
        if not handle_command(command, user_name):
            break

if __name__ == "__main__":
    main()
