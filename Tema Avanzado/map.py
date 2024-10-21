productos = ["raqueta", "balon", "guantes", "pelota", "gorra", "zapatilla"]

def convert_upper(s):
  return s.upper()

# function, lista
print(list(map(convert_upper, productos)))

print(list(map(lambda x: x.upper(), productos)))
print(list(map(lambda x: x.capitalize(), productos)))


def sum(a, b):
  return a + b

# demo con 2 parametros
numero1 = [4, 6, 8, 2, 1, 5 ]
numero2 = [4, 6, 8, 2, 1, 5 ]

print(list(map(sum, numero1, numero2)))

# ejercicio 1: sumar 2 a cada elemento de la lista
# ejercicio 2:import math para aprovechar de la función math.sqrt
# ejercicio 3:teniendo 3 listas de números, multiplicar cada numero en la lista

# respuesta 1
numeros = [4, 6, 8, 2, 1, 5 ]

lambda x: x + 2

print(list(map(lambda x: x+2, numeros)))

# respuesta 2
import math
math.sqrt
numeros = [4, 6, 8, 2, 1, 5 ]

print(list(map(math.sqrt, numeros)))


# respuesta 3
numeros1 = [4, 6, 8, 2, 1, 5 ]
numeros2 = [3, 6, 8, 9, 1, 5 ]
numeros3 = [1, 5, 6, 7, 2, 6 ]

print(list(map(lambda x, y, z: x*y*z, numeros1, numeros2, numeros3)))
