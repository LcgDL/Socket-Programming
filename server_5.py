import socket, threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',port))
s.listen()
print("Server is listen...")
client= []
alias = []

def send_mess_all(m):
    for c in client: 
       c.send(m)

def handle_clients(c):
    while 1:
        try:
            m = c.recv(1024)
            send_mess_all(m)
        except:
            i=client.index(c)
            client.remove(c)
            c.close()
            a=alias[i]
            send_mess_all(f'{a} has left the chatroom'.encode() )
            alias.remove(a)
            break                            

def receive_mess():
    while 1:
        c, add = s.accept()
        print(f'Connection from {str(add)}')
        c.send('Your alias: '.encode())
        ali = c.recv(1024)
        alias.append(ali)
        client.append(c)
        send_mess_all(f'{ali} had joined the Chatroom!'.encode())
        
        threading.Thread(target=handle_clients, args=(c,)).start()
    
receive_mess()
