import socket, sys

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',port))
print('UDP Server is actived...')

addC = []
try:
    while 1:
        d, a = s.recvfrom(1024)
        print('Conection from: ' + str(a)[19:24] + ' Message: '+ d.decode())
        if a not in addC: addC.append(a)
        for c in addC:
            if c != a: s.sendto(d,c)
except KeyboardInterrupt:
    print(' Exit'), s.close(),sys.exit(0)