# INT, FLOAT, STRING, BOOL, NONE
# nombrando variables 
# camelCase = nombreAlumno, PascalCase = NombreAlumno, snake_case = nombre_alumno

# todos los tipos de datos (variables) son objetos
print(type(x)) 

# FLOATS
# Formatear con % - formato antiguo
a = 433.32
b = 0.2121
print("Completed in %d %.2f" %(a,b))  # d = int, f = float, s = str

# Formatear con f - a partir de Python 3.6 preferible
a = 32.5432
b = 0.2121
print(f'Completed in {a:.2f}')
print(f"Completed in {a:.0f} and {b:.2f}")

# precision
x = 0.12345678912345678912345  # hasta 15 o 17 decimales
print(x)

#representación con e
y = 5.5e2  # equivalente a 5.5 * 10^2, or 550.0
small_number = 4.23e-5  # This is equivalent to 4.23 * 10^-5, or 0.0000423
print(f"The small number in decimal form is: {small_number:.12f}")

# MAX float
import sys
print(sys.float_info.max)   # Maximum float value (~1.7976931348623157e+308)
x = 1.8e308  # Slightly larger than the max float value
print(x)     # Output: inf

# STRINGS

descripcion = "Bienvenidos a 'ABC Banco'" # mezclando
# mezclando y multi-linea
descripcion = """
Bienvenidos a 'ABC Banco'
y puedes incluir " aqui
"""

a = "hello"
b = "hello"
print(a is b)
print(a == b)

# bool
x = True
if x:
  print("verdadero")

x = "Hola"
if x == "Hola": # evaluado como True
  print("Hola")

print(True + 1)  # matemáticas, esta representado como 0, 1
print(bool(10))
print(bool("Hola"))
print(bool(""))


# NONE type
x = None
print(type(x))
if x:
    print("Tiene un valor")
else:
    print("No tiene nada")


# variables en una linea
x, y, z = 5, 10, "Hello"
print(x)
print(y)
print(z)
print(x, y, z)

x = 10; y = 20
print(x, y)

# numeros complejos
z = 3 + 4j # en matemáticas, se suele usar i. Pensar en coordinadas en un plano de x (real), y (imaginary)
print(z.real)
print(z.imag)


# asignación múltiple
x, y, z = 1, 2, 3
x = y = z = 0

i = "Hola"
print(isinstance(i, int))
print(isinstance(i, str))
print(isinstance(i, float))
print(isinstance(i, bool))


# pistas - type hints
nombre: str = "Juan"
edad: int = 20
precio: float = 20.32
funciona: bool = True

# Mutable / inmutable
| **Mutable** Data Types      | **Immutable** Data Types    |
|-----------------------------|-----------------------------|
| `list`                      | `int`                       |
| `dict`                      | `float`                     |
| `set`                       | `str`                       |
| `bytearray`                 | `tuple`                     |
| `deque` (from collections)  | `frozenset`                 |
| `Array` (from array module) | `bytes`                     |

# inmutable
x = 1000
print(id(x))
x = 2000
print(id(x))

inflacion = 3.765
x = id(inflacion)
inflacion = 3.876
y = id(inflacion)
print(x==y)

# mutable
lista = [56, 27]
print(id(lista))
lista.append(25)
print(lista)
print(id(lista))

# interning - > -5 a 256 para int
a = 10
print(id(a))
b = 10
print(id(b))

# interning con strings
a = "hello"
b = "hello"
print(id(a) == id(b))

# borrar variables
x = 10
print(x)
del x
print(x) # error

# collector de basura
import gc
x = 1000
print("id de x:", id(x))
del x # es un candidato para la colección de basura
gc.collect() # Desencadenar manualmente la recolección de basura
print("Garbage collection triggered.")

# contando las referencias a variables - internamente, usarán más referencias, por eso no suele empezar con 1
import sys
i = "Hola Mundo"
print(sys.getrefcount(i))
j = i
print(sys.getrefcount(i))
del j
print(sys.getrefcount(i))




# Respuestas a ejercicios -----------------------

# nocion e
y = 5.67e4  # #equivalente a 5.67 * 10^4, or 56700.0
print(y)

# usuario y contraseña
USUARIO = "admin"
PASSWORD = "password123"

# Prompt the user for their username and password
user_name = input("Introducir tu nombre de usuario: ")
user_password = input("Contraseña: ")


login_ok = (user_name == USUARIO) and (user_password == PASSWORD)

if login_ok:
    print("Login bien! Ongi Etorri.")
else:
    print("Login fallido!")


# Calcular IVA de un producto
# Comprobar tus resultados con https://www.impulsa-empresa.es/calculadora-iva/

pantalones = 39.12 # euros
IVA = 0.21

precio_iva = pantalones * IVA
print(precio_iva)

precio_total = pantalones * (1 + IVA)

currency = "€{:,.2f}".format(precio_total)
print(f"El total de su compra de pantalones es {currency}.")

# Tu Product Owner te ha asignado prioridad a los siguientes historias:
# Mostrar el precio de IVA en la pantalla
# Cómo un consumidor, quiero calcular el importe total de la compra incluyendo una cantidad (5 pantalones, por ejemplo) - prioridad 1
# Cómo un usuario de la aplicación, quiero tener la posibilidad de introducir mi propio precio y cantidad, para calcular el importe total de compra)  - prioridad 2


#NOTAS:
# desired_representation = "symbol{:,}".format(my_currency)
# Historias de Usuario: «Como <rol> quiero <funcionalidad> para <cuál es el beneficio que obtengo con ello>»



# Actividades de clase
accion = 3.0172
print(accion)
print(int(accion))

# comparar tipos de datos
a = 5
b = 4.32
c = 10

resultado = 0
if isinstance(a, int):
  resultado =+ a
if isinstance(b, int):
  resultado =+ b
if isinstance(c, int):
  resultado =+ c
print(resultado)


a = 4
b = 6.55
c = 3

suma =0
if isinstance(a, int):
    suma +=a # suma = suma + a
if isinstance(b, int):
    suma +=b
if isinstance(c, int):
    suma +=c
print(suma)


a = 4
b = 6.55
c = 3
lista = [a, b, c, 5.66, 8]
suma =0
for i in lista:
    if isinstance(i, int):
        suma +=i # suma = suma + a

print(suma)


# Ejercicio de propina ---------------
total_cuenta = float(input("Ingresa el total de la cuenta en $: "))

# Solicitar el porcentaje de propina que se desea dejar
porcentaje_propina = int(input("Ingresa el porcentaje de propina que deseas dejar (por ejemplo, 15 para 15%): "))

# Calcular el valor de la propina
propina = total_cuenta * (porcentaje_propina / 100)

# Calcular el total a pagar
total_pagar = total_cuenta + propina

# Mostrar los resultados
print(f"La propina es de: ${propina:.2f}")
print(f"El total a pagar es: ${total_pagar:.2f}")


# ejercicio de range
precio = 10.51

for i in range(5):
    print(f"Si hay una venta de {i}, las ganacias serian {precio*i} euros.") # formatearlo 



# Ejercicio complejo ---------------------
# Calculadora de Autobuses
# Este programa calculará cuántos autobuses necesitas para llevar a un grupo de estudiantes a una excursión. Cada autobús tiene una capacidad de 50 personas (CAPACIDAD = 50). El programa debe preguntar cuántos estudiantes y cuántos profesores van a la excursión y calcular cuántos autobuses completos necesitas.

  
capacidad_autobus = 50

# Solicitar al usuario cuántos estudiantes y profesores van a la excursión
estudiantes = int(input("¿Cuántos estudiantes van a la excursión? "))
profesores = int(input("¿Cuántos profesores van a la excursión? "))

# Calcular el total de personas
total_personas = estudiantes + profesores

# Calcular cuántos autobuses completos se necesitan
autobuses_necesarios = -(-total_personas // capacidad_autobus)  # División entera redondeada hacia arriba

# Mostrar el resultado
print(f"Necesitarás {autobuses_necesarios} autobuses para llevar a todos a la excursión.")

"""
En Python, el operador // realiza una división entera, lo que significa que devuelve el cociente sin los decimales. Siempre redondea hacia abajo, es decir, hacia el entero más pequeño.

La expresión -(-total_personas // capacidad_autobus) se utiliza para hacer una división entera redondeada hacia arriba, lo cual es útil cuando necesitas asegurarte de que obtienes suficientes autobuses (o cualquier otro recurso) para cubrir el número total de personas, sin dejar a nadie fuera.

Se podria haber utilizado math.ceil:
autobuses_necesarios = math.ceil(total_personas / capacidad_autobus)
"""



