# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings


import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()
    return text


def voice_input():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source, timeout=9, phrase_time_limit=9)
            command = listener.recognize_google(voice)

            if 'robot' in command:
                command = command.replace('robot', '')


    except:
        pass
        print("except")
    return command


def run_alexa():
    command = voice_input()
    if 'play' in command:
        song = command.replace('play', '')
        talk("Playing now" + song)
        pywhatkit.playonyt(song)
    elif 'how are you' in command:
        talk("I am doing fine , What about you ? How Can I help you today ?")
    elif 'male or female' in command:
        talk("I am a happy male ")
    elif 'married' in command:
        talk("I am still single , That is the reason I get enough time to assist you ")
    elif 'good night' in command:
        talk("Bye take care have a sweet dream")
    elif 'good morning' in command:
        talk("very good morning to you , have a wonderful day")
    elif 'good evening' in command:
        talk("very good evening , hope you had your evening snack and coffee")
    elif 'drink' in command:
        talk("I am a robot , I dont eat or drink ")
    elif 'angry' in command:
        talk("I am a robot ,I don't have emotions like humans ,  ")
    elif 'music' in command:
        talk("Iam a robot but i like music , tell me any music i will play for you  ")
    elif 'thank you' in command:
        talk("You are welcome , I always feel good  , whenever i get the opportunity to assist you ")
    elif 'sleep' in command:
        talk("I am robot , I dont sleep like humans , we get into hybernate mode only ")

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("current time is" + time)
    elif 'who is' in command:

        information = command.replace('who is', '')
        information = wikipedia.summary(information, 2)
        talk(information)

    elif 'what is' in command:

        information = command.replace('what is', '')
        information = wikipedia.summary(information, 2)
        talk(information)
    elif 'where is' in command:

        information = command.replace('where is', '')
        information = wikipedia.summary(information, 2)
        talk(information)


run_alexa()
