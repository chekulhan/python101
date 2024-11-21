# ojo - NO es un set vacio, sino un diccionario
mi_set = {} # es un dicionarrio
mi_set = {"Hola", 3, 5} # si, es un set


impar = set({1, 3, 5, 7})
par = {2, 4, 6, 8, 1, 3}

print(type(impar))
print(2 in impar)
impar.add(9)
print(impar)

for i in impar:
    print(i)

impar.remove(9)
impar.discard(9)
#impar.remove(9)

# union
union_set = par | impar   # union_set = set_a.union(set_b)
print(union_set)

intersection_set = par & impar  # intersection_set = set_a.intersection(set_b)
print(intersection_set)

difference_set = par - impar  # difference_set = set_a.difference(set_b)

print(difference_set) 

symmetric_difference_set = par ^ impar # uno pero no en los dos
print(symmetric_difference_set)  # symmetric_difference_set = set_a.symmetric_difference(set_b)





# Actividad
# Existentes de direcciones de correo electrónico (nuevas inscripciones)
suscriptores_existentes = {'alice@example.com', 'bob@example.com', 'carol@example.com'}

# Nueva lista de direcciones de correo electrónico (nuevas inscripciones)
nuevas_inscripciones = {'dave@example.com', 'bob@example.com', 'ellen@example.com'}

# 1. Mostrar un set con todos los correos, pero sin duplicar los correos (serán correos únicos)
# 2. Queremos saber quienes son los nuevos suscriptores - o sea, dave y ellen

empleados = ['alice@example.com', 'bob@example.com', 'bob@example.com', 'carol@example.com', 'alice@example.com']
# 3. Teniendo una lista [] de empleados, queremos sacar los empleados únicos, pero en formato final de lista [], no un set


# Respuestas:
total = suscriptores_existentes | nuevas_inscripciones
print(total)

# Queremos saber quien son los nuevos suscriptores - o sea, dave y ellen
nuevos_inscripciones_unicos = nuevas_inscripciones - suscriptores_existentes
print(nuevos_inscripciones_unicos)

# teniendo una lista [] de empleados, queremos sacar los empleados únicos, pero en formato final de lista []
empleados = ['alice@example.com', 'bob@example.com', 'bob@example.com', 'carol@example.com', 'alice@example.com']

empleados_unicos = list(set(empleados))
print(empleados_unicos)
