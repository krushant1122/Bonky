import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 160)



def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:

        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Bonky' in command:
                command = command.replace('Bonky', '')
                print(command)

    except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"  
    return command


def run_Bonky():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1,auto_suggest=False)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke()) 
    elif 'tell me your name' in command:
        talk('I am Bonky. Your deskstop Assistant')
    elif 'who made you' in command or 'who created you' in command:
        talk('I have been first created by Krushant Patel,but multiple people helped me get better.')
    elif 'what is your name' in command or 'who are you' in command:
        talk('Did I forget to introduce myself? I am your personal assistant. Bonky!.')
    elif 'when is your birthday' in command:
        talk('I go through lots and lots of updates. So thats about 365-birthdays.')
    elif 'where do you live' in command:
        talk('I’m stuck inside a device!! Help! Just kidding. I like it in here. Sometimes I hang out in the Cloud. It gives me a great view of the World Wide Web.')
    elif 'do you sleep' in command or 'when do you sleep' in command:
        talk('I take power naps when we arent talking.')
    elif 'self-destruct' in command:
        talk('Commencing Self-Destruct protocol in T-minus 2 seconds Boom! Actually I think Ill stick around')
    elif 'what do you think about me' in command or 'what is your opinion about me' in command:
        talk('I think youre extremely cool')
    elif 'bye' in command:
	    talk('Bye. Have a nice day!')
	    exit()        
    else:
        talk('Please say the command again.')
        


while True:
    run_Bonky()
