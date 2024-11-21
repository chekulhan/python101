# Intro hacer kwargs para funciones
# https://github.com/chekulhan/python101/blob/93629184e2341a0f170ba018dd0eeef7e6373f09/Tema%207%20-%20Funciones/avanzado.py#L95

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

# actualizar datos
acciones.update({"SAN": 8.71})
print(acciones)
acciones["MSFT"] = 92.5
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



# ACTIVIDADES de clase
# Sumar todos los precios, incluyendo una nueva accion de OHL, y excluyendo SAN
acciones = {"MSFT": 91.5, "REP": 7.91, "BBVA": 6.9}

acciones.update({"OHLA": 0.59})
suma = 0
for key, value in acciones.items():
  if key != "SAN":
    suma+= value
  
print(f"La total de los precios de las acciones es {suma}")

# Actividad
acciones = {"MSFT": [91.5, 54.1, 76.4], "REP": [7.91, 5.6, 6.7], "BBVA": [6.9]}

for k, v in acciones.items():
    print(k, v)
    print(type(k))
    print(type(v))
    for precios in v:
        print(precios)



# Termninar este programa para la gestión de la configuración de un servidor

config = {
    "server": "localhost",
    "port": 8080,
    "debug": True,
    "log_level": "INFO"
}

def gestion_configuracion():
    print("Elija una opción:")
    print("1. Obtener configuración")
    print("2. Actualizar configuración")
    print("3. Listar todas las configuraciones")
    
    opcion = int(input("Introducur el número de la opción: "))

    match opcion:
        case 1:
            clave = input("Introducur la clave que desea obtener: ")
            # mostrar la clave deseada
            # .....
            
        case 2:
            clave = input("Ingrese la clave que desea actualizar: ")
            valor = input("Ingrese el nuevo valor: ")
            # Actualizar el valor de uno de las opciones de configuración
            # ...
        case 3:
            # imprimir la configuración
            # ....
        case _:
            print("Opción no válida. Intente nuevamente.")

# Llamar a la función de gestión
gestion_configuracion()

