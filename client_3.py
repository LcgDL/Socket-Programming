#!/usr/bin/python
import socket

s = socket.socket()
s.connect(('Server_IP',port))

def readAnsw():
    data = s.recv(1024)
    print("S>> "+data.decode())

print("'Enter-key' to send, '-q' to finish")
while 1:
    try:
        m = input('write: ')
        if m == '-q': break 
        else:s.send(m.encode()), readAnsw()
    except KeyboardInterrupt:
        print(' Exit')
        break

s.close()
