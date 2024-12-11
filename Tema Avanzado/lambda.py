# Las funciones Lambda son funciones anónimas (sin nombre) que solo pueden contener una expresión.
# Una función lambda se usa cuando necesitas una función sencilla y de rápido acceso

def multiplicado_por5(c):
  return c*5
   
print(multiplicado_por5(5))

c = lambda y : y*5 # se lee asi - una funcion que acepta "y" y devuelve y*5  
 
print(c(5))

def sumar(a, b):
  return a + b
   
print(sumar(5,6))

# se lee asi - una funcion que acepta a y b y devuelve a +b
x = lambda a, b: a+b
print(x(5,6))
print((lambda a, b: a+b) (2, 3))

# ACTIVIDAD 
# Crear unas funciones lambda para hacer matemáticas. Por ejemplo, restar y dividir

# ACTIVIDAD AVANZADO de funciones lambda
# Imprimir True si el valor en la lista es positivo y False si no lo es

# RESPUESTA AVANZADO
z = lambda x: x>0

mi_lista= [5,6,-3,7,-1]
positivos = [z(num) for num in mi_lista]
print(positivos)

for num in mi_lista:
  print(z(num))

resultado = [(lambda x:x>0)(i) for i in mi_lista]
print(resultado)

number = -10
(lambda x: "Positive" if x>0 else "Negative")(number)
