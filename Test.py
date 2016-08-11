import bluetooth
from time import sleep

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
      sleep(45000)
  else:
      s.send('b')
      sleep(53000)
  if(i==6):
          i=0
print("Closing socket")
s.close()
