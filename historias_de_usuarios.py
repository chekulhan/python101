# COMO un alumno de primaria, QUIERO calcular el área de un rectangulo PARA QUE no tenga que estudiar

# importamos sys para coger los argumentos
import sys
# Recogemos las variables del usuario
arg = sys.argv

if(len(arg)>2):
# Calculamos el area
    areaResult = int(arg[1]) * int(arg[2])
else:
# Calculamos el area
    largo = input("largo:")
    ancho = input("ancho:")
    areaResult = int(largo) * int(ancho)

# Mostramos el resultado
print(f"El resultado de el area es: {areaResult}")
