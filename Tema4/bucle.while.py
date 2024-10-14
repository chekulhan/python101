# demo del bucle while

while True:
  pass

while True:
  print("hola")

i = 0
while i<10:
  print(f"i con valor {i} es menos que 10.")
  i += 1  # ¿qué ocurre si no tengo ese instruccion? Se ve la diferencia a range()
print("fin de programa")

i = 10
while i>0:
  print(f"i con valor {i} es mayor que 0.")
  i = i-1

# break
i = 0
while i<10:
  if i == 5:
    break
  else:
    print(i)
  i = i+1


# continue
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  


# j = 1
# while j<=5:
#     print(f"j con valor {j} es menos o igual que 1.")
#     j = j+1
# else:
#     print(f"ahora no lo es {j}")

# accion = input("¿Quieres continuar (s, n)")
# while accion=="s":
#     print("haciendoo bucle")
#     accion = input("¿Quieres continuar (s, n)")
# print("fin de programa")

# Respuesta ###############

# imprimir de 1 a 9
# i = 1
# while i < 10:
#   print(i)
#   i += 1


# contando desde 100 hasta 50
# i = 100
# while i>=50:
#     print(f"i con valor {i} es mayor o igual que 50.")
#     i = i-1

# Como un estudiante de matemáticas, quiero imprimir todos los números de 0 a 99
# excluyendo (10, 20, 30, 40, 50, 60, 70, 80, 90) y usando un bucle WHILE

# for i in range(100):
#     if i not in (10, 20, 30, 40, 50, 60, 70, 80, 90):
#         print(i)

# i = 0
# while i < 100:
#     if i not in (10, 20, 30, 40, 50, 60, 70, 80, 90):
#         print(i)
#     i = i +1


while True:
  pwd1 = input("Introducir tu contraseña: ")
  pwd2 = input("Introducir de nuevo tu contraseña: ")
  if pwd1 == pwd2:
    print("Muy bien. las contraseñas coinciden.")
    break
  print("Las contrseñas no coinciden. Hacerlo de nuevo.")

  
  
  
i = 1
ch = "*"
while i < 10:
  print(ch*i)
  i= i+2
else:
  print("--------")

i = 9
while i > 0:
  print(ch*i)
  i= i-2
