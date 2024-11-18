from datetime import datetime

# Para usar una fecha escrita en castellano. 
# import locale
# locale.setlocale(locale.LC_TIME, "Spanish_Spain.1252")  


x = input("¿Cuál es tu fecha de cumpleños en inglés (19 May 1976)?")

print(type(x))

birthday = datetime.strptime(x, "%d %B %Y")

print(type(birthday))
print(birthday.day)
print(birthday.month)
print(birthday.year)

#  International Standard (ISO 8601)
print(f"Guardando tu cumpleaños en formato {birthday.strftime('%Y-%m-%d')}")

hoy = datetime.today().date()

if birthday.date() >= hoy:
    print("La fecha no es valida")
