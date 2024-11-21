import random

def adivinar(num_user, objetivo):
    """ determinar si el numero de usuario es igual que el objetivo """
    if num_user == objetivo:
        print("Lo has conseguido!")
        return True
    elif num_user < objetivo:
        print("El número que estoy pensando es mayor...")
        return False
    else: # num_user > objetivo:
        print("El número que estoy pensando es menor...")
        return False


# Puedes añadir un if __name__ == "__main__": a partir de aqui

objetivo = random.randint(1, 10)
MAX_INTENTOS = 3
accion = "si" # por defecto para la primera vez

print(f"Bienvenido al juego - adivinar un numero entre 1 y 10. Solo tienes {MAX_INTENTOS} intentos")
while accion.lower() in ("si", "s"): 
    intento = 0 # resetear cada nuevo juego
    exito = False
    while intento < MAX_INTENTOS and exito == False:
        num_user = int(input("Adivinar un numero:"))
        if adivinar(num_user, objetivo):
            # numero es correcto - otra opcion es usar un break aqui
            exito = True
        else:    
            intento += 1

    if intento == MAX_INTENTOS:
        print("Lo siento, NO lo has conseguido.")
        print(f"El número fue {objetivo}")

    accion = input("Quieres continue jugando? (si, no)") # si introduce si o s
