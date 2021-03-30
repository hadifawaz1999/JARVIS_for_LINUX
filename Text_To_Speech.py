import subprocess

class TTS:
    def __init__(self,voice):
        self.voice = voice

    def say(self,text):
        command = "flite -voice " + self.voice + " -t " + chr(34) + text + chr(34)
        my_errors = subprocess.call(command, shell=True)