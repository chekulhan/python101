instrumentos = ["guitarra", "piano", "ukelele", "bateria"]
print(instrumentos)
for i in instrumentos:
  print("Instrumento es " + i)

print(len(instrumentos))
# cuidado - no es el numero de objetos, sino la cuenta de un valor
print(instrumentos.count("piano"))

#acceso
print(instrumentos[0])
print(instrumentos[1])
print(instrumentos[2])
print(instrumentos[-1])  # comenzar desde la final -2, -3 ...
print(instrumentos[2:3])  # rango - devuelve una lista
print(instrumentos[:3])  # coger todos desde prinipio hasta ...
print(instrumentos[2:])  # coger todos desde fin hasta ...
#print(instrumentos[3]) # error

if "piano" in instrumentos:
  print("Piano existe")

# modificar
instrumentos[1] = "PIANO"
print(instrumentos[1])

# añadir
instrumentos.append("bajo")
instrumentos.insert(2, "voz")

print(instrumentos)

# quitar
instrumentos.pop()
print(instrumentos)
instrumentos.remove("PIANO")
print(instrumentos)

# ordenar
instrumentos.sort()
print(instrumentos)
instrumentos.sort(reverse=True)
print(instrumentos)

# tuple - no cambia
dias = ("Lunes", "Martes", "Miercoles")
for d in dias:
  print(d)
print(dias[1])
# dias[1] = "MARTES" # error
#dias.append("Jueves") # error
