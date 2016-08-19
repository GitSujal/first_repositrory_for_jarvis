import os
import re
import random

WORDS = ["PLAY","play","MUSIC","music","SONG","song"]
PRIORITY = 1

def handle(text, mic, profile):

    messages = ["यहाँ कुछ संगीत है","बस सुनो"]

    message = random.choice(messages)

    mic.say(message)
    os.system(' omxplayer /home/pi/song.mp3')

def isValid(text):
	#TO know the input is for Selfie-Bot
    return bool(re.search(r'\b(play|music|song|tone)\b', text, re.IGNORECASE))