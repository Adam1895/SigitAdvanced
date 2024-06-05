import pyttsx3

engine = pyttsx3.init()
text = "first time i'm using a package in next.py course"

engine.say(text)
engine.runAndWait()