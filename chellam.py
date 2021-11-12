import speech_recognition as sr
import pyttsx3
import datetime
import pdf_summary as ps
import webbrowser
import os
import time
import subprocess
import json
from elmo import ELmo
import subprocess

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def note(text,file_name):
    with open(file_name, "a+") as f:
        f.write(text+"\n")

def speak(text):
    engine.say(text)
    engine.runAndWait()

def commence():
    r = sr.Recognizer()
    with sr.Microphone() as source:


        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")
            if "activate" in statement:
                return False
        except Exception as e:
            return True
        return True
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            print(e)
            return "None"
        return statement

def pause():
    y = True
    print("Say \"activate\" to activate Chellam Sir ")
    while y:
        y = commence()
    return

class Chellam():
    def __init__(self):
        x = True
        file_sel = ""
        cwd = "D:/Desktop/college"
        pause()
        print('Loading your AI personal assistant : Chellam Sir')
        speak("Loading your AI personal assistant Chellam Sir")
        while x:

            speak("Tell me how can I help you now?")
            statement = takeCommand().lower()
            print(statement)
            speak(statement)
            if "deactivate" in statement:
                print("Pausing")
                speak("Pausing")
                pause()

            elif "complete" in statement:
                print("OK bye bye")
                speak("OK bye bye")
                x = False
                continue
            elif 'find on google' in statement:
                statement = statement.replace('find on google ', "")
                webbrowser.open_new_tab("https://www.google.com/search?q={}".format(statement))
                speak("Google chrome is open now")
                time.sleep(5)
            elif 'select file' in statement:
                statement = statement.replace('select file ', "")
                speak(statement)
                file_sel = statement
                time.sleep(5)
            elif 'search' in statement:
                statement = statement.replace("search ", "")
                ps.PDFsum(statement,file_sel,cwd)
                z = file_sel + '_' + statement + '.pdf'
                print("created summary PDF on "+ statement+" . Want to search further? yes or no")
                speak("created summary PDF on "+ statement+" . Want to search further? yes or no")
                statement = takeCommand().lower()
                if "yes" in statement:
                    print("say search statement")
                    speak("say search statement")
                    statement = takeCommand().lower()
                    ELmo(z,statement)
                elif "no" in statement:
                    pass
                else:
                    print("none")
                    speak("none")
                time.sleep(5)
            elif 'go back' in statement:
                cwd = "/".join(cwd.split("/")[:-1])
                print(cwd)
                speak(cwd)
            elif 'position' in statement:
                now = "you are currently in " + cwd
                print(now)
                speak(now)
            elif ('open' in statement or 'enter' in statement):
                print(statement)
                cmd = " ".join(statement.split(" ")[1:])
                ctd = cwd + "/{}".format(cmd)
                try:
                    power = "{}".format(ctd)
                    os.startfile(power)
                    cwd = ctd
                except Exception as e:
                    print(e)
                    try:
                        power = "{}.pdf".format(ctd)
                        os.startfile(power)
                    except Exception as e:
                        print(e)
                        speak("No such file or directory found!")
                        continue
            elif 'make a note' in statement:
                cont = True
                date = datetime.datetime.now()
                file_name = str(date).replace(":", "-") + "-note.txt"
                while cont:
                    speak("speak the notes")
                    temp = takeCommand().lower()
                    note(temp,file_name)
                    speak("continue?")
                    resp = takeCommand().lower()
                    if resp == 'no':
                        cont = False
                    elif resp == 'yes':
                        continue
                subprocess.Popen(["notepad.exe", file_name])
            else:
                speak("command not understood")

