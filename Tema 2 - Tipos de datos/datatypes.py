# Mutable / inmutable
inflacion = 3.765
x = id(inflacion)
inflacion = 3.876
y = id(inflacion)
print(x==y)



# Formatear con %
a = 433.32
b = 0.2121
print("Completed in %d %.2f" %(a,b))

# Formatear con f
a = 32.5432
print(f'Completed in {a:.2f}')

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
