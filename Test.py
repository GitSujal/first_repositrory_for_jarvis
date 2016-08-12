import bluetooth


i = int(0)
bd_addr = '30:14:10:27:11:99' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 1
backlog = 1
size = 1024
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((bd_addr, port))
print "conected to "+ bd_addr
while True:
  i+=1
  if i==1:
      s.send('a')
  elif (i ==2):
  		s.send('b')
  elif (i ==3):
  		s.send('c')
  elif (i ==4):
  		s.send('d')				
  else:
      s.send('e')

  if(i==10):
          i=0
print("Closing socket")
s.close()
