

WORDS = ["CAR","RIGHT","LEFT","FORWARD","AHEAD","BACK","BACKWARD","Selfie","Selfie bot","Camera","YES"]
PRIORITY = 1

ValidDirection = ["LEFT","RIGHT","FORWARD","BACKWARD","AHEAD","BACK","left","right","forward","backward","ahead","back"]
ValidStop = ["stop","STOP","HALT","halt","there"]
Serial_message = [000,001,010,011,100,101,110,111]

def carcontrol(mic):
	Direction = mic.activeListen()
	if Direction in ValidDirection:
		handledirection(mic,Direction)
		mic.say("I'm going %s tell me when to stop",Direction)
		stop = mic.activeListen()
		if stop in ValidStop:
			mic.say("I'm in position now would you like  a selfie")
			permission = mic.activeListen()
			if permission == "yes" | "YES" | "ok" | "OK"
				takeselfie(mic)
				else:
					return
			else: 
				carcontrol()
	else:
		mic.say("That's not a valid direction")
		carcontrol(mic)
	return		


def handledirection(mic,Direction):
	if Direction == "LEFT" | "left":
		transimitmessage = Serial_message[1]
	if Direction == "RIGHT" | "right":
		transimitmessage = Serial_message[2]
	
	if Direction == "AHEAD" | "ahead" |"FORWARD" | "forward":
		transimitmessage = Serial_message[3]
	
	if Direction == "back" | "BACK" | "BACKWARD" |"backward":
		transimitmessage = Serial_message[4]
	return

def takeselfie():
	mic.say("Taking selfie 		smile")
	return



def isValid(text):
	#TO know the input is for Selfie-Bot
    return bool(re.search(r'\b(CAR|Selfie|Camera)\b', text, re.IGNORECASE))
 

def handle(text, mic):
	mic.say("I'm controlling selfie-bot now give me directions")
	carcontrol(mic)
	return	

