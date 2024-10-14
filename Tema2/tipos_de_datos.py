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
