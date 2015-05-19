import socket

host = "localhost"
port = 5000

ss = socket.socket()

ss.bind((host, port))

ss.listen(3)

cs, addr = ss.accept()

mat = raw_input('Matricula: ')

cs.send(mat)

while True:

    data = cs.recv(1024)
    print ' ' + data + ' '
    if not data: break

ss.close() 
