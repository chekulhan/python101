# Los diseñadores de Python crearon pdb, una librería nativa cuyo único propósito es permitir a los desarrolladores inspeccionar la ejecución de sus programas de una forma fácil y rápida
# Depurando usando pdb
import pdb

print("Asignar valores a variables")
a = 1
b = 2
pdb.set_trace()
# ¿qué valores tienen ahora? teclear "p a" o "p b" o "p c"
# cuando hayas inspeccionar, continuar. teclear "continue"

# ahora, cambiamos los valores
a = a * 2
b = b * 3
c = a * b
pdb.set_trace()
# ¿qué valores tienen ahora? teclear "p a" o "p b" o "p c"

print("fin de programa")

# Al ejecutar el programa, verás un prompt interactive de >>(Pdb) donde puedes intoducir comandos para inspeccionar las variables 
# Preguntas:
# En el prompt interactivo de Pbd, qué resultado consigues con:
# >> (Pbd) w
# >> (Pbd) n
# >> (Pbd) w
# >> (Pbd) c
# >> (Pbd) print(a)
