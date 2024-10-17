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
