import re

WORDS = ["LIGHT","BULB","DIM","BRIGHT","OFF","ON","FAN","HOT","COLD"]
PRIORITY = 1

COMMAND_BULB = ["LIGHT","BULB","light","bulb"]
COMMAND_FAN = ["FAN","HOT","COLD","fan","hot","cold"]
VALID_DIM = ["DIM","dim","DIMMER","dimmer","low","LOW"]
VALID_BRIGHT  = ["BRIGHT","bright","BRIGHTER","brighter","high","HIGHER"]
VALID_ON = ["ON", "HOT","FAN ON","on","hot","fan on","YES","yes"]
VALID_OFF = ["OFF","COLD","off","cold","no","NO","NOT","not"]
def handlebulb(text,mic):
	if text in VALID_DIM:
		mic.say("I dimmed the bulb do you like this brightness")
		response = mic.activeListen()
		if response == "yes":
			mic.say("Previous brightness restored")
			return
		else:
			return
	elif text in VALID_BRIGHT:
		mic.say("I increased birhgtness do you like this brightness")
		response = mic.activeListen()
		if response == "yes":
			mic.say("Previous brightness restored")
			return
		else:
			return
	return

def handlefan(text,mic):
	if text in VALID_ON:
		mic.say("I turned on the fan")
		return
	elif text in VALID_OFF:
		mic.say("Fan turned off remember me when you feel hot again")
		return
	
	else:
		return
		
	return
	


def handle(text, mic,profile):
	if bulbbool:
		mic.say("I'm controlling bulb.")
		handlebulb(text,mic)

	elif fanbool:
		mic.say("Feeling hot?")
		handlefan(text,mic)
	else:
		return

	return	



def isValid(text):
    """
        Returns True if the input is related to BULB or Fan.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    bulbbool =  bool(re.search(r'\b(LIGHT | DIM | BRIGHT)\b', text, re.IGNORECASE))
    fanbool =  bool(re.search(r'\b(COLD | HOT | Fan)\b', text, re.IGNORECASE))
    if bulbbool: 
    	return bulbbool
    elif fanbool:
    	return fanbool
    else :
    	return False
