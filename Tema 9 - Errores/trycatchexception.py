# Solicitar un número al usuario
entrada = input("Por favor, ingresa un número: ")

try:
    # Intentar convertir la entrada a un entero
    numero = int(entrada)
    print(f"Has ingresado el número: {numero}")
except ValueError:
    # Capturar el error si la conversión falla
    print("¡Error! Debes ingresar un número válido.")




import traceback

try:
  with open("abc.txt", "r") as f:
    print("open")

except Exception as error:
  s = traceback.format_exc()
  # traceback.print_exc() # directamente a stdoutput


print("END")
print(s)


# respuesta a actividad

while True:
  x = input("Introducir un número o 'exit' para salir.")
  
  if x.lower() == "exit":  # Comprobar si quiere continuar o no
        print("Adios!")
        break

  try:
    numero = int(x)
    print(f"Has introducido {numero}")

  except ValueError as error:
    print("Error. Introducir un número")
