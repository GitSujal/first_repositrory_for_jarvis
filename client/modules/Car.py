import re
import bluetooth
from time import sleep
i = int(0)
bd_addr = '30:14:10:27:11:99' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 1
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

WORDS = ["CAR","RIGHT","LEFT","FORWARD","AHEAD","BACK","BACKWARD","TAKE PICTURE","TAKE PHOTO","Selfie","Selfie bot","HARDWARE","CONTROL"]
PRIORITY = 1

ValidDirection = ["LEFT" |"RIGHT" |"FORWARD" |"BACKWARD" | "AHEAD" | "BACK" | "front" | "cam front" | "camera front" | "rotate front" | "left" | "right" | "forward" | "backward" | "ahead" | "back" | "OFF" |"STOP" | "HALT" | "halt" | "there" | "off" | "reverse" | "cam right" | "camera right" | "rotate right" | "cam left" | "camera left" | "rotate left" | "take selfie"  | "now"  | "photo" | "take picture" | "TAKE SELFIE"]
ValidStop = ["stop","STOP","HALT","halt","there","off"]
Serial_message = ['z','a','b','c','d','e','f','g']
ahead = ["ahead","front","forward"]
back = ["back","backward","reverse"]
camright = ["cam right","camera right","rotate right"]
camleft = ["cam left","camera left","rotate left"]
camfront = ["cam front","camera front","rotate front"]
selfie = ["take selfie" ,"now" ,"photo","take picture", "TAKE SELFIE"]

def carcontrol(mic):
	Direction = mic.activeListen()
	#if Direction in ValidDirection:
	if bool(re.search(r'\b(ValidDirection)\b', direction, re.IGNORECASE)):
		handledirection(mic,Direction)
		mic.say("I'm going %s " %Direction)
		carcontrol(mic)

	else:
		mic.say("That's not a valid direction")
		carcontrol(mic)
	return		


def handledirection(mic,Direction):
	if "LEFT" in Direction:
		transimitmessage = Serial_message[1]
		s.send(transimitmessage)
		
	elif "RIGHT" in Direction:
		transimitmessage = Serial_message[2]
		s.send(transimitmessage)
	
	elif Direction in ahead:
		transimitmessage = Serial_message[4]
		s.send(transimitmessage)
	
	elif Direction in back:
		transimitmessage = Serial_message[3]
		s.send(transimitmessage)
	elif Direction in camright:
		transimitmessage = Serial_message[5]
		s.send(transimitmessage)
	elif Direction in camfront:
		transimitmessage = Serial_message[6]
		s.send(transimitmessage)
	elif Direction in camleft:
		transimitmessage = Serial_message[7]
		s.send(transimitmessage)
	elif Direction in ValidStop:
		s.send('z')	
	elif Direction in selfie:
		takeselfie(mic);
	return

def takeselfie(mic):
	mic.say("Taking selfie smile")
	return



def isValid(text):
	#TO know the input is for Selfie-Bot
    return bool(re.search(r'\b(CAR|Selfie|Camera | control| hardware |picture | take photo)\b', text, re.IGNORECASE))
 

def handle(text,mic,profile):
	s.connect((bd_addr, port))
	print "conected to "+ bd_addr
	mic.say("I'm controlling selfie-bot now give me directions")
	carcontrol(mic)
	
	return	

