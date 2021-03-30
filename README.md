# JARVIS For LINUX

An AI assistant like the one in marvel's iron man movies
## 1. Requirements :
1. Python modules :
    1. webbrowser `$ sudo pip3 install webbrowser`
    2. wikipedia  `$ sudo pip3 install wikipedia`
    3. playsound  `$ sudo pip3 install playsound`
    4. speech_recognition `$ sudo pip3 install SpeechRecognition`
2. Linux tools :
    1. espeak `$ sudo apt-get install espeak`
    2. flite  `$ sudo apt-get install flite`
    
## Text To Speech

In the `Text_To_Speech.py` file, the `flite` command is being executed in the Linux shell using the `subprocess` python module .
`flite` command takes as option `-voice` to choose the voice,  in our case it is 'rms`. To see all available voices in `flite`, 
execute the following line in the Linux shell `flite -lv`.

## How it works :

The JARVIS object takes a command from the user using google speech recognizer and executes what it was told and talks to the user using the `flite` command .

## List of commands available for now :

1. At startup, no command is taken the JARVIS module plays the `JARVIS.mp3` file which is taken from the iron man marvel movie clip .
2. `"hello"` or `"hi"` so that JARVIS could greet the user based on what time it is, morning, noon or evening .
3. `"open site example.com"` so that JARVIS will open `example.com` in the user's browser .
4. `"search wikipedia for example"` so that JARVIS would search for results and tell the user a summary of what it found (if exists) .
5. `"goodbye"` , "bye"` , "turn off"` , `"shut down"` or `"system off"` so that JARVIS would stop the program from running .
6. If JARVIS was given a command not listed in his dataset, it respond with `"Sorry, I can't do that"` .

These commands are being handled by a function in the JARVIS class called `decision` .
