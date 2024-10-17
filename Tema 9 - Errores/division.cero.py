def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero."
    except TypeError:
        return "Error: Ambos argumentos deben ser números."

print(dividir(10, 2))  # Salida: 5.0
print(dividir(10, 0))  # Salida: Error: No se puede dividir por cero.
print(dividir(10, "2"))  # Salida: Error: Ambos argumentos deben ser números.

