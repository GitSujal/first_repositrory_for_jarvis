import re
import ftplib
import os


fileDir = os.path.dirname(os.path.realpath('__file__'))

WORDS = ["update","DATABASE","database","UPLOAD","upload",]
PRIORITY = 1

def isValid(text):
	#TO know the input is for Selfie-Bot
    return bool(re.search(r'\b(UPDATE|upload|Database)\b', text, re.IGNORECASE))
 
def handle(text,mic,profile):
	filename = "Missed_Commands.txt"
	filename = os.path.join(fileDir, '../Logs/'+filename)
	filename = os.path.abspath(os.path.realpath(filename))
	ftp = ftplib.FTP('ftp.offerharu.com')
	ftp.login('jarvisai','minor#468&Net')
	ftp.cwd('Data')
	myfile = open(filename,'rb')
	ftp.storlines('STOR ' + filename , myfile)
	ftp.quit()
	mic.say("Database updated and closed successfully")	
	return	
