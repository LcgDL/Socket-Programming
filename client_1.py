#!/usr/bin/python
import socket

s = socket.socket()
hostServer = 'ip_server'
port = port_server
s.connect((hostServer, port))
m = input(('Write a message and press enter: \n'))
s.sendall(m.encode())    
s.close()
