#!/usr/bin/python

from socket import *
import sys

host = raw_input('input server ID: ')
port = input('input port: ')
addr = (host,port)

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.connect(addr)

while True:
	data = raw_input('to server: ')
	if not data :
		print('No message. Please enter a message or "exit" for disconnecting..') 
		continue
	
	tcp_socket.send(data)
	if (data == 'exit'):
		print('SYSTEM: client is shut down')
		tcp_socket.close()
		break
	data = tcp_socket.recv(1024)
	if (data == 'exit'):
		print('server is disconnected')
		tcp_socket.close()
		break
	print('Server: ', data)
	
