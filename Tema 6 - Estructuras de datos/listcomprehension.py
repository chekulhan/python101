rutas = ["MANZANA", "pera", "NARANJA", "uva", "MELON"]

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
