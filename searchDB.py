import MySQLdb as mdb
import socket

host = 'localhost'#Your server address
port = 5000

cs = socket.socket()
cs.connect((host, port))
#Receive the request from the server
mat = cs.recv(1024)
				 #DB address, user,  password, DB
db = mdb.connect('localhost', 'root', 'root', 'matriculas')

with db:
	cur = db.cursor()

	cur.execute('SELECT * FROM NuevoLeon')

	#Search for all the elements in the DB
	for x in range(cur.rowcount):
		row = cur.fetchone()
		if mat in row[0]:
			cs.send(row[1])
			cs.send(row[2])
			cs.send(row[3])
			cs.send(row[4])
			break
db.close()
cs.close()
