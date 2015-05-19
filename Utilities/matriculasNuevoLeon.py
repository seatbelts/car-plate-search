import MySQLdb as mysql
from random import randint

db = mysql.connect('localhost', 'root', 'root', 'matriculas')

cursor = db.cursor()

#sql = """CREATE TABLE MATRICULAS (
#	 NUMERO CHAR(20) NOT NULL,
#	 NOMBRE CHAR(20) NOT NULL,
#	 APELLIDO CHAR(20),
#	 CIUDAD CHAR(20),
#	 ESTADO CHAR(20) )"""

inicios = ['SAA', 'SAB', 'SAC', 'SAD', 'SAE', 'SAF']
ciudades = ['Monterrey', 'Guadalupe', 'San Nicolas', 'San Pedro']
nombres = ['Ismael', 'Ana', 'Ruth', 'Jorge', 'Carlos', 'Rafael', 'Jesus', 'Daniela', 'Lorena']
apellidos = ['Valdez', 'Torres', 'Sanchez', 'Lopez', 'Ruiz', 'Briones']

for x in inicios:
	for y in range(1000000):
		r = randint(0, 3)
		n = randint(0, 8)
		a = randint(0, 5)
		st = x + '-' + str(y) 
		cmmd = """INSERT INTO NuevoLeon (NUMERO,  
			NOMBRE, APELLIDO, CIUDAD, ESTADO) 
			VALUES ( '%s', '%s', '%s', '%s', '%s')""" % \
			(str(st), nombres[n], apellidos[a], ciudades[r], 'Nuevo Leon')
		
		try:
			cursor.execute(cmmd)
			db.commit()
		except:
			db.rollback()

db.close()
