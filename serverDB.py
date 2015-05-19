import socket

host = '192.168.0.18'
port = 5000

ss = socket.socket()

ss.bind((host, port))

ss.listen(3)

cs, addr = ss.accept()

mat = raw_input('Matricula: ')

cs.send(mat)

while 1:

    data = cs.recv(1024)
    print ' ' + data + ' '
    if not data: break

ss.close() 
