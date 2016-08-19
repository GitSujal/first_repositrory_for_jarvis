import re
import bluetooth
from time import sleep
i = int(0)
bd_addr = '30:14:10:27:11:99' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 1
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

WORDS = ["CAR","RIGHT","LEFT","FORWARD","AHEAD","BACK","BACKWARD","Selfie","Selfie bot","Camera","YES"]
PRIORITY = 1

ValidDirection = ["LEFT","RIGHT","FORWARD","BACKWARD","AHEAD","BACK","left","right","forward","backward","ahead","back","off","OFF"]
ValidStop = ["stop","STOP","HALT","halt","there"]
Serial_message = ['z','a','b','c','d','e','f','g']

def carcontrol(mic):
	Direction = mic.activeListen()
	if Direction in ValidDirection:
		handledirection(mic,Direction)
		mic.say("I'm going %s " %Direction)
		carcontrol(mic)
		'''	stop = mic.activeListen()
		if stop in ValidStop:
			mic.say("I'm in position now would you like  a selfie")
			permission = mic.activeListen()
			if permission == "yes" | "YES" | "ok" | "OK":
				takeselfie(mic)
			else:
				return 
		else: 
			carcontrol(mic) '''
	else:
		mic.say("That's not a valid direction")
		carcontrol(mic)
	return		


def handledirection(mic,Direction):
	if Direction ==  "left":
		transimitmessage = Serial_message[1]
		s.send(transimitmessage)
		

	elif Direction == "right":
		print "conected to "+ bd_addr
		transimitmessage = Serial_message[2]
		s.send(transimitmessage)
	
	elif Direction == "AHEAD":# | "ahead" |"FORWARD" | "forward":
		transimitmessage = Serial_message[3]
		s.send(transimitmessage)
	
	elif Direction == "back":# | "BACK" | "BACKWARD" |"backward":
		transimitmessage = Serial_message[4]
		s.send(transimitmessage)
	elif Direction == "off":# | "BACK" | "BACKWARD" |"backward":
		s.send('z')	
	return

def takeselfie():
	mic.say("Taking selfie smile")
	return



def isValid(text):
	#TO know the input is for Selfie-Bot
    return bool(re.search(r'\b(CAR|Selfie|Camera)\b', text, re.IGNORECASE))
 

def handle(text,mic,profile):
	try:
		s.connect((bd_addr, port))
		print "conected to "+ bd_addr
		mic.say("I'm controlling selfie-bot now give me directions")
		carcontrol(mic)
	except:
		mic.say("Problem connecting Bluetooth")
	return	

