# Respuestas

# formulario en colab para convertir Celsius a Fahrenheit y viceversa
# @title Calculador de Productos {"run":"auto","form-width":"200px","display-mode":"form"}
camiseta = 4.5 # @param {"type":"number","placeholder":"Intruducir el coste del producto"}
pantalon = 1 # @param {"type":"number","placeholder":"Intruducir el coste del producto"}
corbata = 2.2 # @param {"type":"number","placeholder":"Intruducir el coste del producto"}

print(f"El cost total es {camiseta + pantalon + corbata} euros")
total = camiseta + pantalon + corbata
print(f"El cost total es {total:.2f} euros") # floating point - punto flotante . = los decimales, 2 = 2 decimales, f = floating point numero

# version para VS Code
"""
Este programa convierte Celsius a Fahrenheit y viceversa.

Ejemplo: (50°F - 32) x 0.5556 = 10°C
"""

accion = input("Para convertir de Fahrenheit a Celsius, teclear 'c'. Para Celsius a Fahrenheit, teclear 'f': ")

if accion == "f":
    celsius = float(input("Introduce la temperatura en Celsius: "))
    fahrenheit = (celsius * 1.8) + 32
    print("La temperatura en Fahrenheit es: %.2f" % fahrenheit)  # Formato de float tradicional
    # print(f"La temperatura en Fahrenheit es: {fahrenheit:.2f}")  # formato más actual para usar Python 3.6

elif accion == "c":
    fahrenheit = float(input("Introduce la temperatura en Fahrenheit: "))
    celsius = (fahrenheit - 32) * 0.5556
    print("La temperatura en Celsius es: %.2f" % celsius)  # Formato de float 

else:
    print("Lo siento. Tienes que introducir 'c' o 'f'")



# Kilos a libras y viceversa

peso = int(input('Cuánto pesas? '))
unidad = input('En (kg) o (lb)? ')
if unidad.lower() == "kg":
    conversion = peso * 2.205
    print(f'Your weight in pounds is {conversion}lb')
else:
    conversion = peso / 2.205
    print(f'your weight in kilograms is {conversion}kg')

    
    
    
    
####    Google COLAB 
#@title Programa para convertir Celsius (grados) a Fahrenheit
celsius = 30 #@param {type:"integer"}
#(celsius * 1.8) + 32

"""
To convert temperatures in degrees Fahrenheit to Celsius, subtract 32 and multiply by .5556 (or 5/9).

Example: (50°F - 32) x .5556 = 10°C
To convert temperatures in degrees Celsius to Fahrenheit, multiply by 1.8 (or 9/5) and add 32.
Example: (30°C x 1.8) + 32 = 86°F
"""
fahrenheit = (celsius * 1.8) + 32
print("La temperatura en fahrenheit es %.2f" % fahrenheit) # fijaos en el formato del float 

#@title Programa para convertir Fahrenheit a Celsius (grados)
fahrenheit = 99 #@param {type:"integer"}
#(celsius * 1.8) + 32

"""
To convert temperatures in degrees Fahrenheit to Celsius, subtract 32 and multiply by .5556 (or 5/9).

Example: (50°F - 32) x .5556 = 10°C
To convert temperatures in degrees Celsius to Fahrenheit, multiply by 1.8 (or 9/5) and add 32.
Example: (30°C x 1.8) + 32 = 86°F
"""
celsius = (fahrenheit - 32)  * 0.5556
print(f"La temperatura en grados celsius es {celsius:.3f}") # fijaos en el formato del float 





# COMO un alumno de primaria, QUIERO calcular el área de un rectangulo PARA QUE no tenga que estudiar

# importamos sys para coger los argumentos
import sys
# Recogemos las variables del usuario
arg = sys.argv

if(len(arg)>2):
# Calculamos el area
    areaResult = int(arg[1]) * int(arg[2])
else:
# Calculamos el area
    largo = input("largo:")
    ancho = input("ancho:")
    areaResult = int(largo) * int(ancho)

# Mostramos el resultado
print(f"El resultado de el area es: {areaResult}")
