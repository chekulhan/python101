
# DEMO
# Trabajando con Diccionarios {key:value}
acciones = {"MSFT": 91.5, "REP": 7.91, "BBVA": 6.9}

print(type(acciones))
print(acciones)
print(acciones["MSFT"])

for key, value in acciones.items():
    print(key, value)

for key in acciones.keys():
    print(key)

for price in acciones.values():
  print(price)

print("REP" in acciones.keys())

acciones.update({"SAN": 8.71})
print(acciones)

# DEMO Diccionario a JSON 

acciones = {"MSFT": 91.5, "REP": 7.91, "BBVA": 6.9, "OHL": 45.6}

import json

a = json.dumps(acciones)
print(type(a))
print(a)

b = json.loads(a)
print(type(b))
print(b)


# ACTIVIDAD
acciones = {"MSFT": 91.5, "REP": 7.91, "BBVA": 6.9}

acciones.update({"OHLA": 0.59})
suma = 0
for key, value in acciones.items():
  if key != "SAN":
    suma+= value
  
print(f"La total de los precios de las acciones es {suma}")
