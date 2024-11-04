# Respuestas



# variables en una linea
x, y, z = 5, 10, "Hello"
print(x)
print(y)
print(z)
print(x, y, z)

x = 10; y = 20
print(x, y)

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
