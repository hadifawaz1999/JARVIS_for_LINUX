from playsound import playsound
from Text_To_Speech import TTS
import datetime
import webbrowser
import wikipedia
import time
from bs4 import BeautifulSoup
import speech_recognition as sr

class JARVIS:

    def __init__(self,show_command=True,show_response=True):

        playsound('JARVIS.mp3')
        self.show_response = show_response
        self.show_command = show_command
        self.text_to_speech_engine = TTS('rms')
        self.speek("How can I help you Sir ?")

    def takeCommand(self):
        r = sr.Recognizer()

        self.command = ""
        with sr.Microphone() as source:
            print("Listening ...")
            audio = r.listen(source)

            try:
                self.command = r.recognize_google(audio, language='en-in')
                print(f"user said : {self.command}\n")
                self.command = self.command.lower()
                self.decision()

            except Exception as e:
                self.speek("Sorry, I didn't quite understand. Can you say that again?")


    def speek(self,text):
        
        self.text = text
        if self.show_response:
            print(self.text)

        self.text_to_speech_engine.say(self.text)
        

    def decision(self):

        if "hello" in self.command or "hi" in self.command:
            self.greatMe()
        
        elif "open site" in self.command:
            self.command = self.command.replace("open site ","")
            self.openSite()
        
        elif "search wikipedia for" in self.command:
            self.command = self.command.replace("search wikipedia for ","")
            print(self.command)
            self.searchWikipediaFor()
        
        elif "goodbye" in self.command or "bye" in self.command or "turn off" in self.command or "shut down" in self.command or "system off" in self.command:
            self.destroy()

        else:
            self.speek("Sorry, I can't do that .")

    def greatMe(self):
        hour = datetime.datetime.now().hour

        if hour >= 0 and hour < 12:
            self.speek("Hello, good morning sir.")
        elif hour >= 12 and hour < 18:
            self.speek("Hello, good afternoon sir.")
        else:
            self.speek("Hello, good evening sir.")
    
    def openSite(self):
        self.speek('Opening web site now Sir .')
        webbrowser.open_new_tab(self.command)

    def searchWikipediaFor(self):
        self.speek("Searching Wikipedia now Sir ...")
        try:
            results = wikipedia.summary(self.command,senteces = 2)
            self.speek("Sir according to Wikipedia :")
            time.sleep(0.5)
            self.speek(results)
        except Exception:
            self.speek("Couldn't find anything on the wikipedia for "+self.command)



    def destroy(self):

        self.speek("Good bye Sir .")
        exit()