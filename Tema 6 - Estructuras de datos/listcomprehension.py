frutas = ["MANZANA", "pera", "NARANJA", "uva", "MELON"]

new_frutas = []
for fruta in frutas:
    if fruta.upper() == fruta:
      new_frutas.append(fruta)

print(new_frutas)

x = [fruta for fruta in frutas if fruta.upper() == fruta]
print(x)


numbers = [2, 6, 7, 3, 4, 8]

new_numbers = ["Par" if i % 2 == 0 else "Impar" for i in numbers]

print(new_numbers)

# mas ejercicios sobre página 36 de las notas de clase


# Actividades avanzadas
# conseguir esta lista de numeros squared i.e. 1 cuadrado, 2 cuadrado, 3 cuadrado, ....
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# list comprehension con dicionarios
grades = {'Alice': 85, 'Bob': 70, 'Charlie': 95, 'Diana': 60}

# Generar un diccionario de personas y sus notas, solo si la nota es > 70



# Respuestas
x = [i**2 for i in range(11)]
print({name:grade for name,grade in grades.items() if grade>70})
