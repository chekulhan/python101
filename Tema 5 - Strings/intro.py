texto = "programazioa gustatzen zait"

# numero de caracteres
print(len(texto))
# la primera caracter en mayúsculo
print(texto.capitalize())
# mayúsculos - lo opuesto en lower()
print(texto.upper())

# strip espacios
s = "    Hola.       "
s = s.strip()   # tambien hay lstrip, rstrip
print("X" + s + "X")

t = "###hola###"
t = t.strip("#")
print("X" + t + "X")

u = "Hola a todos todos todos"
u = u.replace("todos", "TODOS")
print(u)


#split
nombre_completo = "jon#smith"

nombres = nombre_completo.split("#")
print(type(nombres))
nombre, apellido = nombre_completo.split("#")
print(type(nombre), type(apellido))


# multi-linea con \n
print("programazioan\ngustatzen\nzait")
# substring
print(texto[13:22])
# los primeros 10 caracteres
print(texto[:12])
# al reves
print(texto[::-1])

# imprimir todo 5 veces
print(texto*5)




# imprimir cada cáracter en una linea
#for s in texto:
#   print(s)

# quitar espacios
texto = "     programazioa gustatzen zait.   "
print("X" + texto + "X")
print("X" + texto.strip() + "X")


BUSCAR = "gustatZEN"
if BUSCAR in texto:
    print("Encontrado")
else:
    print("No encontrado")

    
tuple = ("Jon", "Maria", "Antonio")
a = "$".join(tuple)
print(a)

z  = "abc"
y = " ".join(z)
print(y)



# recibe un carácter y devuelve su representación en código unicode
print(ord("ñ"))
# recibe un número y devuelve su representación como carácter
print(chr(241))


# ACTIVIDAD juntos de clase:
s="    122,Python,es,64,un,777,lenguaje,222,de,55,66,programación  "
a = s.strip()
b = a.split(",")
print(b)

for w in b:
    if not w.isnumeric():
        print(w)

