#!/usr/bin/python
import socket, sys

s = socket.socket()
s.bind(('',port))
s.listen(3)
print('Listen Connections...')

def answer():
    mS = input('Server >> ')
    c.send(mS.encode())

try:
    c,a = s.accept()
    print('Connection from: ', a)
    while 1:
        data = c.recv(1024)
        if not data: s.close, sys.exit(0)
        else: print('C>> '+data.decode()), answer()
except KeyboardInterrupt:    
    print(' Exit'), s.close, sys.exit(0)
