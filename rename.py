import bluetooth

bd_addr = "30:14:10:27:11:99"

port = 1
	sock= bluetooth.BluetoothSocket(bluetooth.RFCOMM) 
	sock.connect((bd_addr, port)) # Parentheses! 
	print("Initial connection")
	conn = 1
    sock.send('S')	
