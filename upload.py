
import ftplib
filename = "Missed_Comm.txt"
ftp = ftplib.FTP('ftp.offerharu.com')
ftp.login('jarvisai','password')
ftp.cwd('Data')
myfile = open('/Users/SuZal/Desktop/first_repositrory_for_jarvis/Logs/Missed_Comm.txt','rb')
ftp.storlines('STOR ' + filename , myfile)
ftp.quit()
print("FTP closed successfully")