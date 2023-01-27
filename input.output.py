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
