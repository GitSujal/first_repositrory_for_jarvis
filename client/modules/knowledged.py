# -*- coding: utf-8-*-
import random
import re
import wolframalpha
import time
import sys
from sys import maxint
import os
import datetime

from client import jasperpath
WORDS = ["WHO", "WHAT", "HOW MUCH", "HOW MANY", "HOW OLD"]
PRIORITY = 1
fileDir = os.path.dirname(os.path.realpath('__file__'))

def logdata(filename,text):
    date_string = datetime.datetime.now()
    issue_time = str(date_string.year) +'-' + str(date_string.month) +'-' + str(date_string.day) +','+ str(date_string.hour) +':'+ str(date_string.minute) +':'+ str(date_string.second)
    filename = os.path.join(fileDir, '../Logs/'+filename)
    filename = os.path.abspath(os.path.realpath(filename))
    with open(filename, "a") as myfile:
        print("Name of the file: ", myfile.name)
        print("Opening mode : ", myfile.mode)
        myfile.write('"' +text + '"' + ',' + issue_time )
        myfile.close()
        print("File Closed : ", myfile.closed)
    return 



def handle(text, mic, profile):

    messages = ["Searching Online databases","Let me google that for you"]
    message = random.choice(messages)
    mic.say(message)

    app_id = profile['keys']['WOLFRAMALPHA']
    client = wolframalpha.Client(app_id)

    query = client.query(text)
    if len(query.pods) > 0:
        filename = "Knowledge.CSV"
        texts = ""
        pod = query.pods[1]
        if pod.text:
            text = text
            texts = pod.text
        else:
            texts = "I can not find anything"
            text = ""

        mic.say(texts.replace("|",""))
        logdata(filename,text)

    else:
        mic.say("Sorry, Could you be more specific?.")




def isValid(text):
    if re.search(r'\bwho\b', text, re.IGNORECASE):
        return True
    elif re.search(r'\bwhat\b', text, re.IGNORECASE):
        return True
    elif re.search(r'\bhow much\b', text, re.IGNORECASE):
        return True
    elif re.search(r'\bhow MANY\b', text, re.IGNORECASE):
        return True
    elif re.search(r'\bhow old\b', text, re.IGNORECASE):
        return True
    else:
        return False
