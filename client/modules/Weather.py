# -*- coding: utf-8-*-
import random
import re
from datetime import datetime
import  pywapi
import os

fileDir = os.path.dirname(os.path.realpath('__file__'))
WORDS = [""]

PRIORITY = 4

def logdata(filename,text):
    date_string = datetime.now()
    issue_time = str(date_string.year) +'-' + str(date_string.month) +'-' + str(date_string.day) +','+ str(date_string.hour) +':'+ str(date_string.minute) +':'+ str(date_string.second)
    filename = os.path.join(fileDir, '../Logs/'+filename)
    filename = os.path.abspath(os.path.realpath(filename))
    with open(filename, "a") as myfile:
        print("Name of the file: ", myfile.name)
        print("Opening mode : ", myfile.mode)
        myfile.write('"' +text + '"' + ',' + issue_time + '\n')
        myfile.close()
        print("File Closed : ", myfile.closed)
    return 

def temperatureSuggestion(temp):
    
    global string 
    string = ""
    if 0 > temp :
        string = "It's freezing cold so I'd suggest warm clothes as well as a winter coat. "
    elif (0<=temp) and (temp<5):
        string = "It's rather cold so I'd suggest warm clothes.One might consider a winter coat. "
    elif (5<=temp) and (temp< 16):
        string = "It's rather cold today so I'd suggest moderatly long trousers and a pullover . As for a coat, a spring jacket should suffice. "
    elif (16<=temp)and (temp<22):
        string = "It's rather fresh today so I'd suggest long trouses and a t-shirt. Maybe a jacket is needed. "
    elif (22<=temp)and (temp<25):
        string = "It's hot today. I'd suggest shorts and a t-shirt. "
    elif (25<=temp)and (temp<30):
        string = "It's very hot today. I'd suggest wearing the least amount of clothes you can. "
    elif 30 <= temp:
        string = "It's blazing today. I'd not to outside if I were you. "

    string +=". "
    return string

def rain(list):
    
    date = datetime.now().day
    integer = 0
    loc = 0
    string = ""

    for day in list:
        if str(date) in day["date"].lower():
            loc = integer

        integer +=1

    likelyhood_string = list[loc]["day"]["chance_precip"]
    likelyhood = int(likelyhood_string)

    if (0 <= likelyhood) and (likelyhood<= 30):
        string += "It should not rain."
    elif (30 < likelyhood) and (likelyhood<= 50):
        string += "There is a slight chance of rain today."
    elif(50< likelyhood) and (likelyhood <65):
        string += "It's probably going to rain today"
    else:
        string += "It's definitly going to rain today."

    return string

def rainchance(list):
    
    date = datetime.now().day
    integer = 0
    loc = 0
    string = ""

    for day in list:
        if str(date) in day["date"].lower():
            loc = integer

        integer +=1

    likelyhood_string = list[loc]["day"]["chance_precip"]
    return likelyhood_string


def handle(text, mic, profile):
    filename = "Weather.CSV"
    weather_com_result = pywapi.get_weather_from_weather_com('NPXX0002')
    weather_status = weather_com_result['current_conditions']['text'] 
    weather_felttemp = weather_com_result['current_conditions']['feels_like']
    weather = "The weather conditions are "+weather_status+" with a felt temperature of "+ weather_felttemp+ " degrees Celsius. "
    rainprop = rainchance(weather_com_result['forecasts'])
    text = '"' + weather_status + '"' + ',' + weather_felttemp + "Celsius" + ',"' + rainprop
    logdata(filename,text)
    if ("clothes" in text.lower()) or ("wear" in text.lower()):
        chance_rain = rain(weather_com_result['forecasts'])
        felttemp_int = int(weather_felttemp)
        weather_suggestion = temperatureSuggestion(felttemp_int)
        weather_suggestion += chance_rain
        
        mic.say(weather_suggestion)

    elif ("hot" in text.lower()) or ("temperature" in text.lower()) or ("cold" in text.lower()):
        mic.say("There's currently a felt temperature of "+weather_felttemp+" degrees Celsius.")	
    elif "rain" in text.lower():
        rainprop = "Chance of" + rain(weather_com_result['forecasts'])
        mic.say(rainprop)

    else :
    	mic.say(weather)


def isValid(text):
    
    return bool(re.search(r'\b((rain|weather|wear|clothes|hot|cold|temperature))\b', text, re.IGNORECASE))



