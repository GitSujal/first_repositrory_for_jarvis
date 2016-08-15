import re
import random

WORDS = ["JARVIS","jarvis","JASPER","jasper"]
PRIORITY = 0
def handle(text, mic, profile):
    
    message = "Yeah that's me tell me what to do" 

    mic.say(message)
    return 0


def isValid(text):
    return bool(re.search(r'\bjarvis\b',re.IGNORECASE))
