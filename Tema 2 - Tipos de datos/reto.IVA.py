# Calcular IVA de un producto
# Comprobar tus resultados con https://www.impulsa-empresa.es/calculadora-iva/
# COMO un contable de un negocio, 
# QUIERO saber el precio total que tengo que pagar para un producto a haciendo con IVA, 
# PARA QUE pueda sacar informes correctamente para haciendo

# Mejoras:
# - añadir validación: producto tiene que tener un precio  > 0; No se puede introducir datos que no sean números;
# - cada producto tiene un IVA según su tipo (diferentes categorias)

IVA = 0.21
producto = float(input("Introducir el precio del producto en euros, por ejemplo: 39.12: "))  # 39.12 # euros


precio_iva = producto * IVA
print(precio_iva)

precio_total = producto * (1 + IVA)

currency = "€{:,.2f}".format(precio_total)
print(f"El total de este produco es {currency}.")

# Informe histórico - datos sacado del servidor web
historicos = [2.4, 6.7, 9.3]

print("\n Informe ----------------")
for producto in historicos:
    precio_iva = producto * IVA
    precio_total = producto * (1 + IVA) 
    print(f"El precio con IVA de €{producto:.2f} es €{precio_total:.2f}")
print(" Fin de Informe ----------------")


# pruebas
# input 2.40, expected €2.90, actual ____
# input 6, expected €7.26, actual ____

precios_input = [2.40, 6]
precios_esperados = ["€2.90","€7.26"] # cambiar para ver el resultado

for i, producto in enumerate(precios_input):
    precio_iva = producto * IVA
    precio_total = producto * (1 + IVA) 
    format_precio = f"€{precio_total:.2f}"

    assert format_precio == precios_esperados[i], "El calculo no es correcto"

print("***Todas las pruebas se ha ejectuado correctamente***")
