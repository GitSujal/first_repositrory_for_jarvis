import os

def readFile(filename):
    filehandle = open(filename)
    print (filehandle.read())
    filehandle.close()


fileDir = os.path.dirname(os.path.realpath('__file__'))
print (fileDir)

#For accessing the file in the same folder
filename = "test.txt"
'''readFile(filename)'''

#For accessing the file in a folder contained in the current folder
'''filename = os.path.join(fileDir, 'Logs/'+filename)
readFile(filename)


#For accessing the file in the parent folder of the current folder
filename = os.path.join(fileDir, '../same.txt')
readFile(filename)
'''
#For accessing the file inside a sibling folder.
filename = os.path.join(fileDir, '../Logs/'+filename)
filename = os.path.abspath(os.path.realpath(filename))
print (filename)
readFile(filename)
