# Solicitar un número al usuario
entrada = input("Por favor, ingresa un número: ")

try:
    # Intentar convertir la entrada a un entero
    numero = int(entrada)
    print(f"Has ingresado el número: {numero}")
except ValueError:
    # Capturar el error si la conversión falla
    print("¡Error! Debes ingresar un número válido.")
