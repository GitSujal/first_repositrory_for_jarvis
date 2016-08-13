import datetime
import os
from time import sleep
fileDir = os.path.dirname(os.path.realpath('__file__'))
stringvariable = "This is a first string"
stringVariable2 = "This is a second string" 

date_string = datetime.datetime.now()
filename = str(date_string.year) +'-' + str(date_string.month) +'-' + str(date_string.day) +','+ str(date_string.hour)
issue_time = str(date_string.year) +'-' + str(date_string.month) +'-' + str(date_string.day) +','+ str(date_string.hour) +':'+ str(date_string.minute) +':'+ str(date_string.second)

print(date_string)
'''src = '/Users/SuZal/Desktop/first_repositrory_for_jarvis/test.txt'
dst = '/Users/SuZal/Desktop/first_repositrory_for_jarvis/%s.txt' % filename
'''
filename = os.path.join(fileDir, '../Logs/'+filename+'.txt')
filename = os.path.abspath(os.path.realpath(filename))
with open(filename, "w") as myfile:
	print("Name of the file: ", myfile.name)
	print("Opening mode : ", myfile.mode)
	myfile.write(stringvariable + '\t' +  issue_time )
	myfile.close()
	print("File Closed : ", myfile.closed)
'''os.rename(src, dst) '''
sleep(5)
date_string2 = datetime.datetime.now()
filename2 = str(date_string2.year) +'-' + str(date_string2.month) +'-' + str(date_string2.day) +','+ str(date_string2.hour)
issue_time2 = str(date_string2.year) +'-' + str(date_string2.month) +'-' + str(date_string2.day) +','+ str(date_string2.hour) +':'+ str(date_string2.minute) +':'+ str(date_string2.second)
filename2 = os.path.join(fileDir, '../Logs/'+filename2+'.txt')
filename2 = os.path.abspath(os.path.realpath(filename2))
with open( filename2, "a") as myfile:
	print("Name of the file: ", myfile.name)
	print("Opening mode : ", myfile.mode)
	myfile.write('\n' + stringVariable2 + '\t' +  issue_time2)
	myfile.close()
	print("File Closed : ", myfile.closed)
