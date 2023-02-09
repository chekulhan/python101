# Respuestas
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
print(f"La temperatura en fahrenheit es {fahrenheit}")

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
print(f"La temperatura en grados celsius es {celsius}")
