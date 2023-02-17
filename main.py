import sqlite3

db_connection = sqlite3.connect('primera conexion con una base de datos python')
db_cursor = db_connection.cursor()

#db_cursor.execute("CREATE TABLE Alumnos(Id INT, Nombre TEXT, Apellido TEXT)")

db_cursor.execute("INSERT INTO Alumnos VALUES(1,'Maria', 'Lopez')")
db_cursor.execute("INSERT INTO Alumnos VALUES(2,'Francisco', 'Rodriguez')")
db_cursor.execute("INSERT INTO Alumnos VALUES(3,'Maria', 'Martinez')")
db_cursor.execute("INSERT INTO Alumnos VALUES(4,'Francisco', 'Perez')")
db_cursor.execute("INSERT INTO Alumnos VALUES(5,'Jorge', 'Herrero')")
db_cursor.execute("INSERT INTO Alumnos VALUES(6,'Clara', 'García')")
db_cursor.execute("INSERT INTO Alumnos VALUES(7,'Monica', 'Santamaria')")
db_cursor.execute("INSERT INTO Alumnos VALUES(8,'Pablo', 'Villanueva')")
db_cursor.execute("INSERT INTO Alumnos VALUES(10,'Marcos', 'Lopez')")
db_cursor.execute("INSERT INTO Alumnos VALUES(9,'Francisco', 'Lopez')")
db_connection.commit()

db_cursor.execute("SELECT * FROM Alumnos WHERE Nombre = 'Francisco'")

filas = db_cursor.fetchall()

print(filas)

db_connection.close()