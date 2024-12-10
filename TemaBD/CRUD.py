import sqlite3

class Demo:
    def __init__(self, ID, Name, Hint):
        self.ID = ID
        self.Name = Name
        self.Hint = Hint
        

connection = sqlite3.connect("sqlite.db")

cursor = connection.cursor()

# comando INSERT con tuple

cursor.execute("INSERT INTO demo (ID, Name, Hint) VALUES (?, ?, ?)", (201, 'My name', 'My hint'))
connection.commit()

# con un objeto
demo = Demo(202, "nuevo nombre", "nueva pista")
cursor.execute("INSERT INTO demo (ID, Name, Hint) VALUES (?, ?, ?)", (demo.ID, demo.Name, demo.Hint))

# Para ver los resultados
sSQL = "SELECT * FROM demo WHERE ID IN (200, 201, 202)"
cursor.execute(sSQL)

rows = cursor.fetchall()

for row in rows:
    print(row[0], row[1], row[2])


connection.close()


# UPDATE
cursor.execute('UPDATE users SET age = ? WHERE name = ?', (35, 'Alice'))
# DELETE
# A single-value tuple requires a trailing comma (value,). Por ejemplo: cursor.execute('DELETE FROM users WHERE name = ?', ('Alice',))
cursor.execute('DELETE FROM users WHERE name = ?', ('Alice',))



# una lista de objetos - executemany
demos = [
    Demo(301, "Alice", "Alice"),
    Demo(302, "Alice", "Alice"),
    Demo(303, "Alice", "Alice"),
]

# convertimos la lista de objetos en una tupla
datos = [(demo.ID, demo.Name, demo.Hint) for demo in demos] 
cursor = connection.cursor()

cursor.executemany("INSERT INTO demo (ID, Name, Hint) VALUES (?, ?, ?)", datos)
connection.commit()
