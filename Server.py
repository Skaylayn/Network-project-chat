#!/usr/bin/python

from socket import *

host = 'localhost'
port = input('input port: ')

addr = (host,port)

tcp_socket = socket(AF_INET, SOCK_STREAM)

tcp_socket.bind(addr)

tcp_socket.listen(1)

while True:    
    	print('waiting for client...')
	conn, addr = tcp_socket.accept()
    	print('client addr: ', addr)
	
	while True:    
    		data = conn.recv(1024)
    
		if (data == 'exit'):
			print('client was disconnected')
			conn.close()
			break
		else:
        		print('Client: ', data)
			data = raw_input('to client: ')
			conn.send(data)
			if (data == 'exit'):
				print('you were disconnected')
				conn.close()
				break    
	if (raw_input('Would you like to exit?  y//n: ') == 'y'):
		print('SYSTEM: server is shut down')
		tcp_socket.close()
		break

