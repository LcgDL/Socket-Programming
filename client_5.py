import socket, threading, sys,os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('ip_server',port))
print("'Enter-key' to send, '-q' to finish")
a = input("Enter your alias: ").encode()

def send_mess():
    while 1:
        i = input('> ') 
        if i == '-q': os._exit(1)
        else:
            m = '{} : {}'.format(a,i)
            s.send(m.encode())
   
def recv_mess():
    while 1:
        try:
            m = s.recv(1024).decode()
            if m == 'Your alias: ':
                s.send(a)
            else:
                print(m)
        except:
            print('Error!'), s.close()
            break
        
threading.Thread(target=recv_mess).start()
threading.Thread(target=send_mess).start()