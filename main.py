# Importing

import os
import pyttsx3
import pyautogui
import speech_recognition as sr
import time
import webbrowser
import random
import datetime
from datetime import date

# Variables

assistant = pyttsx3.init()
acknowledgement = ["you're welcome!", "no problem!", "don't mention it!",
                   "It's no bother!", "my pleasure!", "It's alright!", "sure thing, anything else?"]
greetings = ["Hello! How may I help you today?", "Hey there, how can I assist you today?",
             "Good time of the day! what can I do for you?"]
musicPath = "C:/Users/nandi/AppData/Local/Programs/Python/Python310/Fun stuff lol/Audio"

# Heart

voices = assistant.getProperty('voices')
assistant.setProperty('voice', voices[2].id)

# Defining


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(query)
            return query
        except Exception as e:
            return "Some Error Occurred! Try again."

# Main loop

while True:
    print("Listening...")
    text = command()
    # Open youtube
    if "Open Youtube".lower() in text.lower():
        assistant.say("Opening YouTube")
        webbrowser.open_new_tab("https://www.youtube.com")

    # Open Google
    elif "Open Google".lower() in text.lower():
        assistant.say("Opening Google")
        webbrowser.open_new_tab("https://www.google.com")

    # Open Spotify
    elif "Open Spotify".lower() in text.lower():
        os.system("spotify")
        time.sleep(5)
        pyautogui.hotkey("ctrl", "l")
        time.sleep(0.5)
        for i in range(20):
            pyautogui.hotkey("backspace")
        song = command()
        pyautogui.write(song)
        pyautogui.hotkey("enter")
        for key in ['enter', 'pagedown', 'tab', 'enter', 'enter']:
            time.sleep(1)
            pyautogui.press(key)
        assistant.say("playing "+song+" on spot if hi")

    elif "Pause spotify".lower() in text.lower() or "play spotify".lower() in text.lower():
        os.system("spotify")
        time.sleep(2)
        pyautogui.hotkey("space")

    # Back to vscode
    elif "Your Code".lower() in text.lower():
        assistant.say("Opening my code.")
        os.system("test.py")

    # Audio check
    elif "Are you listening".lower() in text.lower() or "Are you still listening".lower() in text.lower():
        assistant.say("Yes, i am waiting for your command.")

    elif "Thank you".lower() in text.lower():
        assistant.say(random.choice(acknowledgement))

    elif "Hello".lower() in text.lower() or "Hi".lower() in text.lower() or "hey".lower() in text.lower():
        assistant.say(random.choice(greetings))

    # Open WhatsApp
    elif "Open WhatsApp".lower() in text.lower():
        webbrowser.open("https://web.whatsapp.com")
        time.sleep(10)
        for key in ['tab', 'tab', 'tab', 'tab', 'tab']:
            time.sleep(0.1)
            pyautogui.press(key)
        name = command()
        time.sleep(1)
        pyautogui.write(name, interval=0.1)
        time.sleep(1)
        pyautogui.hotkey("enter")
        message = command()
        pyautogui.write(message, interval=0.05)
        pyautogui.hotkey("enter")
        assistant.say("Sending message to"+name)

    elif "send message on whatsapp".lower() in text.lower():
        new_message = command()
        pyautogui.write(new_message, interval=0.1)
        pyautogui.hotkey("enter")

    # Discord

    elif "Open Discord".lower() in text.lower():
        webbrowser.open_new_tab("https://discord.com/channels/@me")
        time.sleep(10)
        pyautogui.press("tab")
        name = command()
        time.sleep(1)
        pyautogui.write(name, interval=0.1)
        time.sleep(1)
        for key in ['tab', 'tab', 'tab', 'enter']:
            time.sleep(0.1)
            pyautogui.press(key)
        time.sleep(1)
        message = command()
        pyautogui.write(message, interval=0.05)
        pyautogui.hotkey("enter")
        assistant.say("Sent message to"+name)   

    elif "Send message on discord".lower() in text.lower():
        time.sleep(2)
        message = command()
        pyautogui.write(message, interval=0.05)
        pyautogui.hotkey("enter")
        assistant.say("Sending message")

    elif "Edit message".lower() in text.lower():
        time.sleep(2)
        pyautogui.hotkey("up")
        time.sleep(0.5)
        pyautogui.hotkey("ctrl","a")
        time.sleep(0.5)
        pyautogui.hotkey("backspace")
        time.sleep(0.5)
        message = command()
        pyautogui.write(message, interval=0.1)
        pyautogui.hotkey("enter")
        assistant.say("Edited the last message you sent.")

    elif "the time".lower() in text.lower():
        Time = datetime.now().strftime("%H:%M")
        assistant.say("The time is " + Time + ".")

    elif "the date".lower() in text.lower():
        today = str(date.today())
        assistant.say("Today's date is " + today + ".")

  # W.I.P

    elif "play game".lower() in text.lower():
        text = command()

    assistant.runAndWait()
