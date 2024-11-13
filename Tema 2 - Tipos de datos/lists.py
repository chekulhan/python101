nombres= ['Arturo','Julio','Dani']

counter = 0
for i in nombres:
  presente = input(f"¿Ha venido {i} a clase? (y, n)")
  if presente == "y":
    counter +=1

print(f"{str(counter)} alumno(s) estan presente hoy.")



notas = [6, 4, 1, 10, 10, 7, 4]
total = 0
for n in notas:
  total += n

print(total)
print(len(notas))
print("media" + str(total/len(notas)))


# vocales
letras = ["a", "b", "e", "f", "o", "x", "c"]

for l in letras:
    if l in ["a", "e", "i", "o", "u"]:
        print(True)
    else: 
        print(False)

# camping
maria = ["tienda", "linterna", "saco de dormir"]
ana = ["linterna", "brújula", "cuchillo"]   
carlos =  ["saco de dormir", "mochila", "cantimplora"] 

equipamiento = maria + ana + carlos
# Mostrar el equipamiento de cada persona
print("Equipamiento de cada persona:")
print(f"Maria lleva {maria}")
print(f"Ana lleva {', '.join(ana)}")  # ojo!
print(f"Carlos lleva {carlos}")

# Mostrar la lista única de todos los objetos
print("Lista de todos los objetos:")
print(", ".join(equipamiento))

contarTiendas = 0
for i in equipamiento:
    if i in "tienda":
        contarTiendas += 1
print(f"Al final, tenemos {contarTiendas} tienda(s)")



"""
Listas de 2 dimensiones
 1  2  3  4   - filas y columnas
 5  6        
 7  8  9 
"""

datos = ([1, 2, 3, 4], [5, 6], [7, 8, 9])
for fila in datos:
    for columna in fila:
        print(f"{columna} ," , end="")
    print("\n Nueva fila")



"""
Estas gestionando los asientos en un avión
"O" representa un asiento libre .
"X" representa un asiento ocupado.

FILA x: Asiento A, B, C, D

fila 1: "0", "O", "X", "O"  
fila 2: "O", "X", "O", "O"
fila 3: "O", "O", "O", "X"

"""

avion_asientos = [
    ["O", "O", "X", "O"],  
    ["O", "X", "O", "O"],  
    ["O", "O", "O", "X"] 
]

# avion con una lista de dos dimensions - con enumerate
# ¿está fila 1, asiento B disponible?
print(avion_asientos[0][1])
# ¿está la última fila y el último asiento disponsible?
print(avion_asientos[-1][-1])
# ejecutar una venta en el asiento 2A
avion_asientos[1][0]= "X"

# imprimir en un formato de filas y asientos y su disponibilidad

contar_filas = 0
for fila in avion_asientos:
    print(f"Fila {contar_filas+1}")
    for columna in fila:
        print(columna)
    contar_filas += 1

asientos = ("A", "B", "C", "D")
print("    " + "    ".join(asientos))
for index, fila in enumerate(avion_asientos): # enumerate() nos da el indice y el valor
    print(index+1, fila)
