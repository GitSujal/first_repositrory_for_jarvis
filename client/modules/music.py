import os
import re
import random

WORDS = ["PLAY","play","MUSIC","music","SONG","song"]
PRIORITY = 2 

def handle(text, mic, profile):
    """
        Reports that the user has unclear or unusable input.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """

    messages = ["Sure sir Here is a music","Sure sir tell me which song","Ok"]

    message = random.choice(messages)

    mic.say(message)
    os.system(' omxplayer /home/pi/song.mp3')

def isValid(text):
	#TO know the input is for Selfie-Bot
    return bool(re.search(r'\b(play|music|song|)\b', text, re.IGNORECASE))