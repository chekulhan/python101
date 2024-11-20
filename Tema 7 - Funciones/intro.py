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

  
 # ACTIVIDAD - pasando elementos sin fin a una funcion
def imprimirDiasSemana(*args):
  count = 1
  for i in args:
    print(f"{i} es la {count} dia de la semana")
    count += 1
      
if __name__ == "__main__":
    imprimirDiasSemana("Lunes", "Martes", "Miercoles", "Jueves", "Viernes")
    print("-"*10) 
    imprimirDiasSemana("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")
  
  
  
  
  
 # DEMO - pass by reference, value, object
# metodo - Pass-by-Object
# pasando INMUTABLE objetos - call by value
def ref_demo(x):
  #print("x=",x," id=",id(x))
  x=42
  print(x)
  #print("x=",x," id=",id(x))

x = 100
ref_demo(x)
print("x=",x," id=",id(x))

# pasando MUTABLE objetos - call by reference
def incrementar_ciudad(cities):
    print(cities)
    cities.append("Madrid")
    print(cities)
  
ciudades = ["San Sebastian", "Bilboa"]
incrementar_ciudad(ciudades)
print(ciudades)

# Calcular el precio de los productos en una cafetería
def conseguir_precio(producto):
    match producto:
        case "café":
            return 2.51
        case "té":
            return 1.80
        case _:
            print("Error")
            # return None

if __name__=="__main__":
    producto = input("Qué quieres tomar?")
    precio = conseguir_precio(producto)
    print(f"The product {producto} es {precio*1.1}")



# respuesta propina - argumentos por defecto
def calcular_cuenta(cuenta, propina=10):
  total = cuenta*(1 + 0.01*propina)
  total = round(total,2)
  return total

if __name__ == "__main__":
  # calcular la cuenta sin definir la propina - 10% por defecto
  total = calcular_cuenta(100)
  print(f"Hay que pagar ${total}")

  # calcular la cuenta con una propina de 12%
  total = calcular_cuenta(100, 12)
  print(f"Hay que pagar ${total}")




RESPUESTAS de ejercicios de funciones:

"""
Crear una función para saber si un número es par o impar. 
Usar el % módulo operando, que devuelve lo que sobra de una división.
print(11%3)   - devuelve 2
print(10%3)    - devuelve 1
print(9%3)    - devuelve 0  !!!
 """


def IsPar(x):
    if x % 2 == 0:
        return True # par
    else:
        return False # impar
    
print(IsPar(10)==1)



Con una lista, encuentra el número máximo y mínimo.
lista = [1,4,6,3,9,7]

def minmax(lista):
    return min(lista), max(lista)

def minmax2(*args):
    return min(args), max(args)

x, y = minmax(1,6,4,3,8,9,4,4)

x, y = minmax(lista)
print(x, y)



#En una línea de texto, encuentra la palabra más larga. 
#Por ejemplo, “Me gustan los garbanzos” devuelve “garbanzos”.

texto = "Me gustan, los garbanzos."

def encontrarPalabra(texto):
    palabras = texto.split()
    max_len = 0
    max_palabra = ""

    for palabra in palabras:
        if len(palabra) > max_len:
            max_len = len(palabra)
            max_palabra = palabra

    return max_len, max_palabra

print(encontrarPalabra(texto))


