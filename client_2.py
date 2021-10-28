import socket, sys

socket = socket.socket()
ipServer = 'ip_server'
port = port_server

socket.connect((ipServer,port))
print("'Enter-key' to send, '-q' to finish")
while 1:
    try:
        m = input("Write: ")
        if m == '-q':
            socket.sendall(m.encode())
            break
        else:
            socket.sendall(m.encode())
    except KeyboardInterrupt:
        print(" KeyboardInterrupt->EXIT ")
        socket.close()
        sys.exit(0)
        
socket.close()
