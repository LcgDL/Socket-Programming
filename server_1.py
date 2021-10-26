#!/usr/bin/python
import socket
#import subprocess
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostServer = 'ip_server'
port = 'port_server'
s.bind((hostServer, port))
print('Socket-port: '+ str(port))
s.listen(3)
print('Socket is listening...')

while 1:
    c, addr = s.accept()
    print('Connection from: ', addr)
    data = c.recv(1024)
    print('>>',data.decode())
    c.close()

