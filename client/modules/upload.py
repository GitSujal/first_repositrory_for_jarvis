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
		fileext = "/home/pi/Logs/"+ filename
		myfile = open(fileext,'rb')
		ftp.storlines('STOR ' + filename , myfile)
	else :
		print("FTP password missing in profiel addd it under ftp_pwd:")
	ftp.quit()
	return


def isValid(text):
	#to know the input is to upload database
    return bool(re.search(r'\b(UPDATE|upload|Database|update all)\b', text, re.IGNORECASE))
 
def handle(text,mic,profile):
	filenames = ["Missed_Commands.CSV", "Knowledge.CSV", "Movie.CSV","Weather.CSV"]
	try:
		for file in filenames
			updatedatabase(file,profile)
			mic.say("Database %s updated and closed successfully" %file)		
	except:
		mic.say("Sorry there is error with FTP")
	return	
