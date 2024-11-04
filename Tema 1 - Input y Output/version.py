import sys

print(sys.version)
print(sys.version_info)

help(sys)

dir(sys)
print(sys.__doc__)


help(sys.version_info)
help(sys.exit)


# Actividad: Usando el módulo platform, crear un programa para mostrar información del plataform
import platform


# Respuesta:
import platform
print(platform.release(), platform.version(), platform.architecture())
