
# Ejemplos de clase de tipo de dato range() con un bucle for

for i in range(5):
    print(i)
  
# empezar y terminar
for i in range(2, 10):
    print(i)

# empezar, terminar y un step (pasos)
for i in range(1, 10, 2):
    print(i)

# atrás
for i in range(10, 0, -1):
    print(i)

# atrás o al reves
for i in reversed(range(5)):
  print(i)

# range con lists
frutas = ['manzana', 'banana', 'kiwi']

for i in range(len(frutas)):
    print(f"Index {i}: {frutas[i]}")

# ------------------------------------------
# respuestas
# ------------------------------------------
# matemáticas
for i in range(11):
  print(f"5*{i}={5*i}")

# numeros pares
for i in range(10, 22, 2):
  print(i)

# Lista de tareas diarias
tareas = [
    "Revisar correos",
    "Actualizar informe semanal",
    "Reunión de equipo",
    "Análisis de datos",
    "Planificación de la próxima semana"
]

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

for i in range(5):
  print(f"{dias_semana[i]} - tu tarea es {tareas[i]}")


# Count down
import time

segundos = 10

print("Count down")
for i in range(segundos, 0, -1):
    print(i)
    time.sleep(1)

print("Blast off! Despegue!")

# Calcular el tiempo para hacer una tarea
# timeit module puede ser utilizado tambien

import time

start = time.perf_counter() # comenzar

for i in range(100000):
    pass

end = time.perf_counter() # terminar
print(f"Elapsed time: {end - start}")

%%timeit  # en Colab, usar el magic command

