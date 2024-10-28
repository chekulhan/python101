# demostración del profesor
texto = "Eso es un texto con <p>html</p> entre las <b>palabras</b>"

print("es" in texto)
print("xyz" in texto)

import re


print(bool(re.search("es", texto)))

x = re.search("es", texto) # ¿qué tipo ed objeto es devuelto?
print(x)
print(type(x)) # <class 're.Match'>

# assumir que None es False - puede usar en condicionales
if re.search("xyz", texto):
    print("xyz existe")
else:
    print("xyz no existe")

# empleando listas
palabras = ["texto", "html", "perro"]

for p in palabras:
    print(re.search(p, texto))


# mejorar el rendimiento - usar compile, cuando hay que usar en muchos casos
mascota = re.compile("perro")

print(type(mascota))
print(bool(mascota.search("Ayer compré un perro")))
print(bool(mascota.search("Ayer compré un gato")))
print(bool(mascota.search("Empezar desde aqui. Ayer compré un perro y no un gato", 20, 40))) # empezar, terminar

# Hacer ahora la actividad 1

texto = "Ayer compré un perro pero no compré un gato"
patron = "perro|gato|pájaro"

print(bool(re.findall(patron, texto)))

for l in re.findall(patron, texto):
    print(l)

# Actividad 2 ¿Cuál es la diferencia entre .search y .findall?
# Modificar el ejemplo de findall y usar search  


# Patrones
texto = "El 1 de mayo compré un perro pero no compré un gato."

print(bool(re.search("\d", texto))) # dígito
print(bool(re.search("\D", texto))) # non-dígito
print(re.search("\s", texto))  # espacio o TAB  - \S para non-espacios

texto = "bsgdshdaaaaaaaaahdgfhfgk"

print(re.search("a+", texto)) # multiples ocurrencias de la letra 'a'. 


texto = "hola holahola holaholaholaholaholahola holaholahola holaholaholaholaholaholaholaholahola!"
resultado = re.finditer("(hola){4,10}", texto)  # Matches 'hola' entre 4 y 10 veces

for _ in resultado:
    print(f"Conseguido: {_.group()} , {_.span()}")


# ACTIVIDADES --------------------------

# Actividad 1
# Esperas recibir un mensaje con el dia de la reunión. Cambiar este código para usar el módulo RE
texto = "Hola chicos, La reunión será el lunes, nada más empezar la jornada. Nos vemos"

dias = ("lunes", "martes", "miércoles", "jueves", "viernes")

for d in dias:
    if d in texto:
        print(f"La reunion es {d}")


# Actividad 2 ¿Cuál es la diferencia entre .search y .findall? Modificar el ejemplo de findall y usar search

#Actividad 3 - patrones
texto = "ha dicho ja, y luego continuaba diciendo jajajaja. Finalmente, terminó con jaja!"
# - Cúantas veces dijo "ja"?
# - Encontrar las posiciones de jaja y jajajaja. O sea, excluir ja solamente




# RESPUESTAS -----------------------
# Actividad 1:
for d in dias:
    if re.search(d, texto):
        print(f"La reunion es {d}")

# Actividad 2 ¿Cuál es la diferencia entre .search y .findall? Modificar el ejemplo de findall y usar search
print(re.search(patron, texto))

#Actividad 3 - patrones
texto = "ha dicho ja, y luego continuaba diciendo jajajaja. Finalmente, terminó con jaja!"

resultado = re.findall("ja+", texto)
- Cúantas veces dijo "ja"?
print(len(resultado))

resultado = re.finditer("(ja){2,4}", texto)  # Matches 'ja' repetido 2 a 4 veces
for _ in resultado:
    print(f"Conseguido: {_.group()} , {_.span()}")
  

# REFERENCIA ------------
Here's a quick cheat sheet for regular expressions in Python with `re.search`, showing some basic and common patterns to get started!

### Basic Patterns and Their Meanings

| Pattern       | Description                                       | Example                   | Matches in Text                |
|---------------|---------------------------------------------------|---------------------------|---------------------------------|
| `\d`          | Any digit (0-9)                                   | `re.search(r'\d', "abc1")`| `'1'`                           |
| `\D`          | Any non-digit character                           | `re.search(r'\D', "1a")`  | `'a'`                           |
| `\w`          | Any alphanumeric character (letters, digits, _)   | `re.search(r'\w', "$#a")` | `'a'`                           |
| `\W`          | Any non-alphanumeric character                    | `re.search(r'\W', "a$")`  | `'$'`                           |
| `\s`          | Any whitespace character (space, tab, newline)    | `re.search(r'\s', "a b")` | `' '`                           |
| `\S`          | Any non-whitespace character                      | `re.search(r'\S', " a")`  | `'a'`                           |

### Quantifiers (Repeaters)

| Pattern       | Description                                   | Example                          | Matches in Text                  |
|---------------|-----------------------------------------------|----------------------------------|-----------------------------------|
| `a*`          | 0 or more occurrences of `a`                 | `re.search(r'a*', "bcaa")`       | `''` (matches empty string first)|
| `a+`          | 1 or more occurrences of `a`                 | `re.search(r'a+', "bcaa")`       | `'aa'`                           |
| `a?`          | 0 or 1 occurrence of `a`                     | `re.search(r'a?', "bcaa")`       | `''` (matches empty string first)|
| `a{2,3}`      | 2 to 3 occurrences of `a`                    | `re.search(r'a{2,3}', "baaa")`   | `'aa'`                           |

### Position Anchors

| Pattern       | Description                                   | Example                          | Matches in Text                  |
|---------------|-----------------------------------------------|----------------------------------|-----------------------------------|
| `^a`          | `a` at the start of a string                  | `re.search(r'^a', "abc")`        | `'a'`                            |
| `a$`          | `a` at the end of a string                    | `re.search(r'a$', "cba")`        | `'a'`                            |
| `\bword\b`    | Matches whole word                            | `re.search(r'\bdog\b', "dogged")`| No match                         |

### Character Sets and Ranges

| Pattern       | Description                                   | Example                          | Matches in Text                  |
|---------------|-----------------------------------------------|----------------------------------|-----------------------------------|
| `[abc]`       | Any character in brackets                    | `re.search(r'[abc]', "apple")`   | `'a'`                            |
| `[^abc]`      | Any character not in brackets                | `re.search(r'[^abc]', "def")`    | `'d'`                            |
| `[a-z]`       | Any lowercase letter                         | `re.search(r'[a-z]', "Apple")`   | `'p'`                            |
| `[A-Z]`       | Any uppercase letter                         | `re.search(r'[A-Z]', "apple")`   | `'A'`                            |
| `[0-9]`       | Any digit                                    | `re.search(r'[0-9]', "abc3")`    | `'3'`                            |

### Escaping Special Characters

- To search for special characters (like `.`, `*`, `+`), escape them with a backslash (`\`).
  
  ```python
  re.search(r'\.', "3.14")  # Matches the '.' character, not "any character"
  ```
