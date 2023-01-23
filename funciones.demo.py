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

