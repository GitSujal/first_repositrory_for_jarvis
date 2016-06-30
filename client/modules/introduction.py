import re
import random

WORDS = ["WHO","YOU","INTRODUCE","INTRODUCTION"]
PRIORITY = 1
Messages = ["Hi I am JARVIS speed 2 gegahertz memory thirty two gegabyte . A voice controlled artificial intelligence","I am JARVIS voice controlled computer you can ask me to do anything","I' am tired giving introductions just google JARVIS and you will know"]

def handle(text, mic):
	message = random.choice(Messages)
	mic.say(message)
	return

def isValid(text):
	return bool(re.search(r'\b(who are you | what is this | INTRODUCTION | INTRODUCE| about YOU) \b', text, re.IGNORECASE))


