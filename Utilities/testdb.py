import MySQLdb as mysql

db = mysql.connect('localhost', 'root', 'root', 'matriculas')

cursor = db.cursor()

sql = '''CREATE TABLE Jalisco (
	 NUMERO CHAR(20) NOT NULL,
	 NOMBRE CHAR(20) NOT NULL,
	 APELLIDO CHAR(20),
	 CIUDAD CHAR(20),
	 ESTADO CHAR(20) )'''

try: 
	cursor.execute(sql)
	db.commit()
except:
	db.rollback()

db.close()
