# -*- coding: utf-8-*-
import datetime
from sys import maxint
import random
import os

fileDir = os.path.dirname(os.path.realpath('__file__'))
filename = "Missed_Commands.txt"

WORDS = []
PRIORITY = -(maxint + 1)


def handle(text, mic, profile):
    date_string = datetime.datetime.now()
    issue_time = str(date_string.year) +'-' + str(date_string.month) +'-' + str(date_string.day) +','+ str(date_string.hour) +':'+ str(date_string.minute) +':'+ str(date_string.second)
    messages = ["I'm sorry, could you repeat that?",
                "My apologies, could you try saying that again?",
                "Say that again?", "I beg your pardon?","Sorry I miss this command I would upload this request and hope next time you'll get execution for this command","Sorry Try any other command"]

    message = random.choice(messages)
    filename = os.path.join(fileDir, '../../Logs/'+filename)
    filename = os.path.abspath(os.path.realpath(filename))
    with open(filename, "a") as myfile:
    print("Name of the file: ", myfile.name)
    print("Opening mode : ", myfile.mode)
    myfile.write(text + '\t' +  issue_time )
    myfile.close()
    print("File Closed : ", myfile.closed)

    mic.say(message)


def isValid(text):
    return True
