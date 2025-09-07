import sys

print(sys.version)
print(sys.version_info)

help(sys)

dir(sys)
print(sys.__doc__)


help(sys.version_info)
help(sys.exit)


# Actividades
# Actividad platform: Usando el módulo platform, crear un programa para mostrar información del plataform

import platform


# Actividad datetime: ¿Cuantos segundos hay en un dia (demostrarlo)? ¿Qué es el epoch?
# Si importamos el datetime asi, from datetime import datetime, ¿Qué cambios tenemos que realizar para que funcione?

import datetime  

epoch = datetime.datetime(1970, 1, 1)
print(epoch)
print(epoch.timestamp())

# Mostrar el timestamp para el aterrizaje de la luna en 1969.


# Actividad time
import time

print(time.time())
print(time.ctime())

# Convertir el formato de la hora en 2025-05-21, y luego añadir la hora, minutos y segundos
print(time.strftime("%d-%m-%Y"))

# El datetime module es más potente para trabajar con fechas
from datetime import datetime

# Datetime object for now
now = datetime.now()
print("datetime.now():", now)

# Custom formatting
print("strftime:", now.strftime("%Y-%m-%d %H:%M:%S"))

--------

# Respuestas:
import platform
print(platform.release(), platform.version(), platform.architecture())

moon_landing = datetime(1969, 7, 20, 20, 17, 0)  # Apollo 11 moon landing

