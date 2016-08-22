import re
import bluetooth
from time import sleep
i = int(0)
bd_addr = '30:14:10:27:11:99' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 1
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

WORDS = ["CAR","RIGHT","LEFT","FORWARD","AHEAD","BACK","BACKWARD","SELFIE","TAKE PICTURE","TAKE PHOTO","HARDWARE","CONTROL"]
PRIORITY = 1

ValidDirection = ["LEFT","RIGHT","FORWARD","BACKWARD","AHEAD","BACK","FRONT","CAM FRONT","cCAMERA FRONT","ROTATE FRONT", "OFF","STOP","HALT","REVERSE","CAM RIGHT","CAMERA RIGHT","ROTATE LEFT","CAM LEFT","CAMERA LEFT","ROTATE LEFT","TAKE SELFIE","NOW","PHOTO","TAKE PICTURE","TAKE SELFIE"]
ValidStop = ["stop","STOP","HALT","halt","there","off"]
Serial_message = ['z','a','b','c','d','e','f','g']
ahead = ["ahead","front","forward"]
back = ["back","backward","reverse"]
camright = ["cam right","camera right","rotate right"]
camleft = ["cam left","camera left","rotate left"]
camfront = ["cam front","camera front","rotate front"]
selfie = ["take selfie" ,"now" ,"photo","take picture"]

def carcontrol(mic):
	Direction = mic.activeListen()
	if  True: #Direction in (ValidDirection.upper()):
		handledirection(mic,Direction)
		mic.say("I'm going %s " %Direction)
		carcontrol(mic)

	else:
		mic.say("That's not a valid direction")
		carcontrol(mic)
	return		


def handledirection(mic,Direction):
	if "left" in Direction.lower():
		transimitmessage = Serial_message[1]
		s.send(transimitmessage)
		
	elif "right" in Direction.lower():
		transimitmessage = Serial_message[2]
		s.send(transimitmessage)
	elif "ahead" in Direction.lower():
			transimitmessage = Serial_message[4]
			s.send(transimitmessage)
	elif "back" in Direction.lower():
			transimitmessage = Serial_message[3]
			s.send(transimitmessage)
	elif "cam right" in Direction.lower():
			transimitmessage = Serial_message[5]
			s.send(transimitmessage)
	elif  "cam front"in Direction.lower():
		transimitmessage = Serial_message[6]
		s.send(transimitmessage)
	elif "camleft" in Direction.lower():
		transimitmessage = Serial_message[7]
		s.send(transimitmessage)
	elif Direction in ValidStop:
		s.send('z')	
	elif "selfie" in Direction.lower():
		takeselfie(mic);
	return

def takeselfie(mic):
	mic.say("Taking selfie smile")
	return



def isValid(text):
	#TO know the input is for Selfie-Bot
    return bool(re.search(r'\b(CAR|Selfie|Camera|CONTROL| HARDWARE |picture | take photo)\b', text, re.IGNORECASE))
 

def handle(text,mic,profile):
	try:
		s.connect((bd_addr, port))
		print "conected to "+ bd_addr
		mic.say("I'm controlling selfie-bot now give me directions")
		carcontrol(mic)
	except:
		mic.say("error connecting bluetooth")
	return	

