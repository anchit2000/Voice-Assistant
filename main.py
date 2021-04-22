import speech_recognition as sr
import pyttsx3
import pyaudio
import pywhatkit
import sys
import datetime
# import wikipedia as wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
#voices = engine.getProperty('voices')      # To change voice of your assistant.
#engine.setProperty('voice',voices[1].id)   # Female voice is not working properly so I have commented it.

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            initiator = listener.recognize_google(voice).lower()
        if 'assistant' in initiator:
            talk("I am listening")
            print("listening")
            print("try saying \"what can you do\"")
            with sr.Microphone() as source:
                voice = listener.listen(source)
                speech = listener.recognize_google(voice).lower()
            return speech
        else:
            take_command()

    except:
        talk("Please check your microphone")
        print("check your microphone")


def run_assistant():
    command = take_command()
    if 'play' in command:
        song = command.replace("play","")
        talk("Playing "+song)
        try:
            pywhatkit.playonyt(song)
        except:
            talk("An unknown error occured")
            print("An unknown error occured")


    elif 'google search' in command:
        searcher = command.replace("google search","")
        talk("searching on google "+searcher)
        try:
            pywhatkit.search(searcher)
        except:
            talk("An unknown error occured")
            print("An unknown error occured")

    elif 'wikipedia search' in command:
        wikipedia = command.replace("wikipedia search","")
        talk("searching on wikipedia "+wikipedia)
        try:
            pywhatkit.info(wikipedia)
        except:
            talk("An unknown error occured")
            print("An unknown error occured")

    elif 'repeat' in command:
        command = command.replace("repeat", "")
        talk(command)
        print(command)

    elif 'what can you do' in command:
        help = command
        talk("Here's what you can ask me to do.")
        print("if you want me to play something from youtube, say \'play + name of the song\'")
        print("if you want me to search something from google, say \'google search + keyword\'")
        print("if you want me to search something from wikipedia, say \'wikipedia search + keyword\'")
        print("if you want me to repeat what you said, say \'repeat + your statement\'")

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('The current time is '+time)

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    #
    # elif 'who is' or 'what is' in command:
    #     person = command.replace("who is ",'')
    #     info = wikipedia.summary(person,1)
    #     print(info)
    #     talk(info)

    elif 'exit' in command:
        sys.exit()

    else:
        talk("I did not understand")
        print("I did not understand.")
        print("if you want me to play something from youtube, say \'play + name of the song\'")
        print("if you want me to search something from google, say \'google search + keyword\'")
        print("if you want me to search something from wikipedia, say \'wikipedia search + keyword\'")
        print("if you want me to repeat what you said, say \'repeat + your statement\'")
        print("Please say one of the command again.")
        talk("Please say one of the the command again.")
        run_assistant()






if __name__ == '__main__':
    print("Say assistant to activate")
    while True:
        run_assistant()
