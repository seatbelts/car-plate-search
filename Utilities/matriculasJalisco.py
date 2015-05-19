import MySQLdb as mysql
from random import randint

db = mysql.connect('localhost', 'root', 'root', 'matriculas')

cursor = db.cursor()

#sql = """CREATE TABLE MATRICULAS (
#	 NUMERO CHAR(20) NOT NULL,
#	 NOMBRE CHAR(20) NOT NULL,
#	 APELLIDO CHAR(20),
#	 CIUDAD CHAR(20),
##	 ESTADO CHAR(20) )"""

inicios = ['JBA', 'JBB', 'JBC', 'JBD', 'JBE', 'JBF']
ciudades = ['Guadalajara', 'Zapopan', 'Tonala', 'Tlaquepaque', 'El Salto']
nombres = ['Ismael', 'Ana', 'Ruth', 'Jorge', 'Carlos', 'Rafael', 'Jesus', 'Daniela', 'Lorena']
apellidos = ['Valdez', 'Torres', 'Sanchez', 'Lopez', 'Ruiz', 'Briones', 'Martinez', 'Ramos']

for x in inicios:
	for y in range(1000000):
		r = randint(0, 3)
		n = randint(0, 8)
		a = randint(0, 7)
		st = x + '-' + str(y) 
		cmmd = """INSERT INTO Jalisco (NUMERO,  
			NOMBRE, APELLIDO, CIUDAD, ESTADO) 
			VALUES ( '%s', '%s', '%s', '%s', '%s')""" % \
			(str(st), nombres[n], apellidos[a], ciudades[r], 'Nuevo Leon')
		
		try:
			cursor.execute(cmmd)
			db.commit()
		except:
			db.rollback()

db.close()
