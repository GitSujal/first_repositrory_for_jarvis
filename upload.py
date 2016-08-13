import ftplib
filename = "data.txt"
ftp = ftplib.FTP('ftp.offerharu.com')
ftp.login('jarvisai','minor#468&Net')
ftp.cwd('Data')
myfile = open(filename,'rb')
ftp.storlines('STOR ' + filename , myfile)
ftp.quit()
print("FTP closed successfully")