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
