import socket, threading, os

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

def send():
    while 1:
        n = 'c1'
        i = input('> ') 
        if i == '-q': os._exit(1)
        else:
            m = '{} : {}'.format(n,i)
            s.sendto(m.encode(),('IP_Server',port))
        
def receiv():
    while 1:
        mS=s.recvfrom(1024)
        print("\t\t\t\t "+mS[0].decode())

threading.Thread(target=send).start()
threading.Thread(target=receiv).start()