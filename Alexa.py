#19DCS147  OM TANK
#PYTHON_MINI_PROJECT
#MINI_ALEXA WORKS SAME AS ALEXA VIRTUAL ASSISTANT
#WORK WITH VOICE COMMANDS 

import speech_recognition as sr
import wikipedia
import pywhatkit
import datetime
import pyjokes
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 

def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def run_alexa_mini():
    command = take_command()
    print(command)
    if 'play' in command:
        song= command.replace('play', '')
        talk('you asked me to play the song '+ song)
        talk('playing' + song)
        pywhatkit.playonyt('song')


    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%S %p')
        talk('you asked me the time and current time is ' + time)
        print(time)


    elif 'who is' in command:
        person = command.replace('who is' ,'')
        info=wikipedia.summary(person,2)
        print(info)
        talk(info)


    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())

        
    else:
        talk('please say the command again')


while True:
    run_alexa_mini()    