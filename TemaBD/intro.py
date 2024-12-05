# aprender CREATE TABLE, SELECT
https://www.khanacademy.org/computer-programming/new/sql

# Descargar una base de datos
https://sqliteonline.com/


# Aprender:
# 1. Connectar / desconectar
# 2. Sacar resultados en formato lista (estándar)
# 3. Sacar resultados en formato objeto (OOP)
# 4. Sacar resultados en formato diccionario



# Viene instalado por defecto en la biblioteca stadard

import sqlite3



class Demo:
    def __init__(self, ID, Name, Hint):
        self.ID = ID
        self.Name = Name
        self.Hint = Hint
        

connection = sqlite3.connect("sqlite.db")

connection.row_factory = sqlite3.Row. # for dictionary access only

cursor = connection.cursor()


sSQL = "SELECT * FROM demo"

cursor.execute(sSQL)

rows = cursor.fetchall()

# LISTA 
for row in rows:
    print(row)



# OBJECTS
demos = [Demo(*row) for row in rows] # unpacking
for d in demos:
    print(d.ID, d.Name)

print(type(rows))
for row in rows:
    print(row[0], row[2])

# DICTIONARY
demos = [dict(row) for row in rows]
for d in demos:
    print(type(d))
    print(d)
    print(f"ID: {d['ID']}, Name: {d['Name']}")


connection.close()
