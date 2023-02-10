
nombres= ['Arturo','Julio','Dani']

counter = 0
for i in nombres:
  presente = input(f"¿Ha venido {i} a clase? (y, n)")
  if presente == "y":
    counter +=1

print(f"{str(counter)} alumno(s) estan presente hoy.")
