import sqlite3

# Cerrar conexion despues de cada actividad - conn.close()
# PASO 1: Crear una BD y una tabla -------------
conn = sqlite3.connect('test.db')

conn.execute("create table empleados (id integer, name text)")

# PASO 2: Insertar muchos datos a la tabla -------------

sData = [(1, "Jon"),
        (2, "Maria")]

cur = conn.cursor()

cur.executemany("INSERT INTO empleados (id, name) VALUES (?, ?);", sData)
conn.commit() # default not auto commit!!!!


# PASO 3: Ver los datos en la tabla -------------
cur.execute("SELECT * FROM empleados;")

rows = cur.fetchall()
for row in rows:
  print(row[0], row[1])  # row is a tuple



# PASO 4: SELECT basados en una consulta  -------------
cur = conn.cursor()

for row in cur.execute("SELECT * FROM empleados WHERE id = :myid", {'myid': 1}):
  print(row)



# CERRAR despues de cada ejecucion --------
conn.close()





# Usando clases -----------------

from dataclasses import dataclass, astuple

@dataclass
class Empleado:
  id: int
  name: str
  
conn = sqlite3.connect('test.db')


cur = conn.cursor()

cur.execute("SELECT * FROM empleados;")

empleados: list[Empleado]  = cur.fetchall()

for row in empleados:
  empleado: Empleado = Empleado(*row)  # convert row into an Empleado class, unpack
  print(empleado.id, empleado.name)  # row is now an object Empleado

# Insertar con un objeto ----
e = Empleado(5, 'Juan')
print(astuple(e))

cur.execute("INSERT INTO empleados (id, name) VALUES (?, ?);", (e.id, e.name))  # use () tuple here
cur.execute("INSERT INTO empleados (id, name) VALUES (?, ?);", astuple(e))  # use () tuple here

conn.close()





# Para crear una tabla con campo de autoincremento, usar: INTEGER PRIMARY KEY AUTOINCREMENT
conn.execute("CREATE TABLE Users (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre text, salario real)")


# Actividad de clase CRUD para peliculas.
import sqlite3

print("Programa de BD CRUD")

conn = sqlite3.connect('pelis.db')

while True:

    accion = int(input("Qué quieres hacer? 1. SELECT, 2. INSERT, 3. UPDATE 4. DELETE, 5. SELECT query 6. CLOSE"))

    if accion == 1:
        # mostrar todas las pelis
        sSQL = "SELECT * FROM Peliculas"
        cursor = conn.cursor()
        cursor.execute(sSQL)
        filas = cursor.fetchall()
        for fila in filas:
            print(fila)
    elif accion == 2:
        nombre = input("Cual es el nombre")
        duracion = input("Cual es la duracion")
        cur = conn.cursor()
        sSQL = "INSERT INTO Peliculas (nombre, duracion) VALUES (?,?)"
        cur.execute(sSQL, (nombre, duracion) )
        conn.commit()
        print("Tu transaccion ha funcionado correctamente")

    elif accion == 3: # UPDATE
        id = input("Qué numero quieres actualizar?")
        duracion = input("Qué duracion tiene?")

        cur = conn.cursor()
        sSQL = "UPDATE Peliculas SET duracion = ? WHERE id = ?"
        cur.execute(sSQL, (duracion, id) )
        conn.commit()
    
    elif accion == 4: # DELETE
        id = input("Qué numero quieres borrar?")

        cur = conn.cursor()
        sSQL = "DELETE FROM Peliculas WHERE id = " + id
        cur.execute(sSQL )
        conn.commit()
            
    elif accion == 5:
        # mostrar todas las pelis
        nombre = input("Qué peli buscas?")
        nombre = nombre + "%"
        sSQL = f"SELECT * FROM Peliculas WHERE nombre LIKE ?"
        cursor = conn.cursor()
        cursor.execute(sSQL, (nombre,))     # OJO, a veces hay que poner comma ","  - parece para indicar tuple
        filas = cursor.fetchall()
        for fila in filas:
            print(fila)

    elif accion==6:
        print("cerrando")
        conn.close()
        break
    else:
        pass
