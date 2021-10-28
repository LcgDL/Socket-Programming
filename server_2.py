#!/usr/bin/python
import socket, sys

def closeProg():
    s.close()
    sys.exit(0)

def printData():
    if data[:2].decode("utf-8") == '-q': closeProg()
    else: print('>> '+ data.decode())

def recvgData():
    global data
    try:
        s.listen(3)
        print('Socket is listening...')
        c, addr = s.accept()
        print('Connection from: ', addr)    
        while 1:
            data = c.recv(1024)
            if not data: closeProg()
            else: printData()
    except KeyboardInterrupt:
        print(" KeyboardInterrupt->EXIT ")
        closeProg()

s = socket.socket()
s.bind(('',port_number))
recvgData()
