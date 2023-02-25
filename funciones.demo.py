# Usar este códgio para mostrar a la clase, poco a poco, los conceptos de funciones

def hola1():
  pass

print(hola1)


def hola2(i):
  print(f"Hola {i}")

for i in range(5):
  print(hola2(i))

def sumar1(x, y):
  print("sumando")
  return x + y

print(sumar1(1,4))

def sumar2(x, y):
  print("sumando")
  return x + y
  print("fin de funcion") # no se ejecuta esta linea

print(sumar2(6,7))

def sumar3(x=3, y=5):
  return x + y

print(sumar3())
print(sumar3(9))
print(sumar3(x=9))
print(sumar3(x=9, y=10))

def sumar4(x, y):
  CONST = 10
  a = x + CONST
  b = y + CONST
  return a, b

a, b = sumar4(6, 7)
print(type(a))
print(a)
a = sumar4(6, 7)
print(type(a))
print(a)


# ámbito, alcance o scope de las variables
x = "Hola GLOBAL" # variable global

def mensaje():
  y = "mundo"
  x = "Hola LOCAL"
  print(y)
  print(x)

print(x)
#print(y) # error
mensaje()

# programa
if __name__ == '__main__':
  llamar_funcion()

  
# RESPUESTAS
# Actividad: Repetir x veces

# devolver el numero del usuario
def get_numero():
  numero = int(input("Introducir tu numero"))
  return numero

# imprimir un número x veces, imprimiendo a la pantalla
def repetir_numero(contar):
  for i in range(contar):
    print(i + 1)

if __name__ == "__main__":
  print("Un programa para repetir un numero.")
  numero = get_numero()
  repetir_numero(numero)
  
  
# Actividad: AREA m2
# Pedir los lados del usuario
def get_lados():
  lado = float(input("Ingresa el lado del cuadrado: "))
  ancho = float(input("Ingresa el ancho del cuadrado: "))
  return lado, ancho

# calcular el área 
def calcular_area(lado, ancho):
  return lado * ancho

if __name__ == "__main__":
  print("Un programa para calcular el área de una superficie.")
  lado, ancho = get_lados()
  area = calcular_area(lado, ancho)
  print(f"El area del cuadrado es: {area} cm")
