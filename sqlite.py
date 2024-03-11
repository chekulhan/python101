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

