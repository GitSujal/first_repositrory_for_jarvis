import re
import ftplib
import os


fileDir = os.path.dirname(os.path.realpath('__file__'))

WORDS = ["update","DATABASE","database","UPLOAD","upload",]
PRIORITY = 1

def updatedatabase(filename,profile):
	if 'ftp_pwd' in profile:
		ftp_pwd = profile['ftp_pwd']
		ftp = ftplib.FTP('ftp.offerharu.com')
		ftp.login('jarvisai',ftp_pwd)
		ftp.cwd('Data')
		myfile = open('/home/pi/Logs/Missed_Commands.txt','rb')
		ftp.storlines('STOR ' + filename , myfile)
	else :
		print("FTP password missing in profiel addd it under ftp_pwd:")
	ftp.quit()
	return


def isValid(text):
	#to know the input is to upload database
    return bool(re.search(r'\b(UPDATE|upload|Database|update all)\b', text, re.IGNORECASE))
 
def handle(text,mic,profile):
	filename = "Missed_Commands.CSV"
	try:
		updatedatabase(filename)
		mic.say("Database updated and closed successfully")	
	except:
		mic.say("Sorry there is error with FTP")
	return	
