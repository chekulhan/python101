
##########################################
# RETO respuesta - encriptar y descifrar
texto = "Texto para encriptar"
lista = []

# usar lista.append() para agregar los números a la lista
for i in texto:
    lista.append(ord(i) + 10)

# mostrar la lista de la cadena cifrado

# ahora descifra la lista - los números unicode de cada carácter esta en la lista
for j in range(0, len(lista)):
   print(chr(lista[j]-10), end=" ")

    
# RETO respuesta - Amazon sistema de registro
# Palabras para excluir de la contraseña. Hay mejoras formas de hacer eso, con una lista, por ejemplo....
EXCLUDE1 = "password"
EXCLUDE2 = "contraseña"
EXCLUDE3 = "123456"

nombre = input("Cúal es tu nombre?")
apellido = input("Cúal es tu apellido?")
usuario = input("Introducir un nombre de usuario (mínimo 5 carácteres):")
password = input("Introducir la contraseña (mínimo 6 carácteres, sin palabras típicas):")

if len(usuario) < 5:
    print("Por favor, vuelve a introducir un usuario.")
elif len(password) < 6:
    print("Por favor, vuelve a introducir una contraseña.")
elif EXCLUDE1 in password.lower() or EXCLUDE2 in password.lower() or EXCLUDE3 in password:
    print(f"Por favor, vuelve a introducir una contraseña sin palabras claves como {password}.")
else:
    print(f"Bienvenidos a Amazon {nombre.capitalize()}, {apellido.capitalize()}.")
    
    
    
    
    
    
# convertir 122,Python,es,64,un,777,lenguaje,222,de,55,66,programacion a Python es un lenguaje de programacion
text = "   122,Python,es,64,un,777,lenguaje,222,de,55,66,programacion    "
text = text.strip()

print("X" + text + "X")
lista = text.split(",")

print(type(lista))
print(lista)
print(type(lista[0]))
texto_lista = [i for i in lista if not i.isnumeric()]  # list comprehension
print(texto_lista)

# opcion 1
texto_final1 = ""
for i in texto_lista:
  texto_final1 = texto_final1 + " " + i
print(texto_final1.strip())

# opcion 2
texto_final2 = " ".join(str(i) for i in texto_lista)
print(texto_final2)




# actividad encriptado
message = "Hola Mundo"
encriptado = []
for c in message:
    encriptado.append((ord(c) + 1))

print(encriptado)

for i in encriptado:
    print(chr(i-1))


emails = ["jon.smith@microsoft.com", "maria.fernandez@microsoft.com", "david@microsoft.com", "isabel@microsoft.es","alfonso@gmail.com"]

# Generar un informe con:
# - los nombres de los usuarios
# - los dominios únicos (sin repetir el dominio)

nombres = ("maria", "jon", "david")
# con los nombres, generar un texto en format CSV con nuevos correos e.g maria@nazaret.eus,jon@nazaret.eus,david@nazaret.eus

dominios = []
for email in emails:
  nombre, dominio = email.split("@")
  print(nombre)
  if dominio not in dominios:
    dominios.append(dominio)

print(dominios)

nombres = ("maria", "jon", "david")
DOMINIO = "@nazaret.eus"
correos = []
for nombre in nombres:
  correo = nombre + DOMINIO
  correos.append(correo)

texto = ",".join(correos)
print(texto)

# version 2 de lista de correos
correos = ["jon.smith@microsoft.com", "juan@email.com","maria@microsoft.com"]
listadeNombres = []
listadeDominios=[]
for c in correos:
  x, y = c.split("@")
  listadeNombres.append(x)
  listadeDominios.append(y)

# Informe
sTexto= "Informe de usuarios \n"
for i in listadeNombres:
  sTexto = sTexto + i + ","
 
sTexto = sTexto[:-1] # quitamos el ultimo ,

sTexto = sTexto + "\n Aqui son los dominios: \n"
setdeDominios = set(listadeDominios)

for i in setdeDominios:
  sTexto = sTexto + "," + i 

# Guardamos informe en un archivo
print(sTexto)

with open("informe.txt", "w") as f:
  f.write(sTexto)




texto = "    Lo más importante que nos ha mantenido en Python... bueno, hay 2 cosas importantes. Uno son las bibliotecas. La otra cosa que nos mantiene en Python, y esto es lo más importante, es facil de leer y entender. Cuando contratamos nuevos empleados. Solo digo, 'todo lo que escribas debe estar en python'. Sólo para que pueda leerlo. Y es increíble porque puedo ver desde el otro lado de la habitación, mirando su pantalla, si su código es bueno o malo. Porque un buen código de Python tiene una estructura muy obvia. Y eso hace que mi vida sea mucho más fácil        "


# Contar las veces que la palabra Python aparece en el texto
# ...y si a veces aparece en el texto con mayusculas y minusculas - Python, python
print(texto.count("Python"))
print(texto.upper().count("PYTHON"))

# Encuentras la ubicacion (numero de caracter) donde esta la primera ocurrrencia de la palabra Python. ¿Y la segunda?

print(texto.find("Python"))
print(texto.find("Python", 50, len(texto)))

# La palabra 'código' esta en el texto? Usar if ... in ...:

if "código" in texto:
  print("Palabra 'codigo' en texto")
else:
  print("No esta en el texto")

# reemplazar Python por PYTHON
print(texto.replace("Python", "PYTHON"))

# quitar los espacios
print("X" + texto.strip() + "X")

# cambiar la letra de todo el text a "lO MÁS IMPORTANTE QUE NOS HA MANTENIDO EN pYTHON... "
print(texto.swapcase())




# RESPUESTA AMAZON username y contraseñas
# funcion para validar el nombre, según la norma >= 6 caracteres
def validarNombre(nombre):
  LENGTH_NOMBRE = 6
  if len(nombre) < LENGTH_NOMBRE:
    return False
  else:
    return True

# funcion para validar la contraseña, según la norma >= 7 caracteres, not in lista de contrasseñas faciles
def validarPassword(password):
  LENGTH_PASSWORD = 7

  if password in ("password", "contraseña", "1234567", "qwerty"):
    print("La contraseña es demasiado fácil")
    return False
  elif len(password) < LENGTH_PASSWORD:
    print("La contraseña es muy corta ")
    return False
  else:
    return True


if __name__ == "__main__":

  valido = False
  while valido == False:
    nombre = input(
      "Introduce tu nombre, el nombre debe tener 6 o más caracteres ")
    valido = validarNombre(nombre)

  valido = False
  while valido == False:
    contrasena = input("Introduce tu contrasena ")
    valido = validarPassword(contrasena)

  print("Nombre y contraseña validos. Puedes entrar al programa ahora")
  print(f"Bienvenido {nombre} y contraseña {contrasena}")



