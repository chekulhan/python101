# PREGUNTA 1
# Terminar las clases para Mago y Arquero

class Personaje:
    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud

    def atacar(self):
        return f"{self.nombre} ataca!"


# Guerrero (hijo de Personaje)
class Guerrero(Personaje):
    def __init__(self, nombre, salud, fuerza):
        super().__init__(nombre, salud)
        self.fuerza = fuerza

    def atacar(self):
        return f"{self.nombre} ataca con fuerza de {self.fuerza}!"


# Mago (hijo de Personaje)
# al atacar, lanza un hechizo de magia (Fuego)


# Arquero (hijo de Personaje)
class Arquero(Personaje):
  ...

  # al atacar, lanza flechas...¿qué ocurre con self.flechas cada vez que ataca?
  def atacar(self):
        if self.flechas > 0:
          ....

# ---------------------------------
guerrero = Guerrero("Carlos", 100, 30)
mago = Mago("Luna", 70, "Fuego")
arquero = Arquero("Leo", 80, 5)

# Demostración
print(guerrero.atacar())  # Salida: Carlos ataca con fuerza de 30!
print(mago.atacar())      # Salida: Luna lanza un hechizo de magia Fuego!
print(arquero.atacar())   # Salida: Leo dispara una flecha! Flechas restantes: 4
print(arquero.atacar())   # Salida: Leo dispara una flecha! Flechas restantes: 3


# PREGUNTA 2 - map
numeros = [1, 2, 3, 4, 5]
# usando map, conseguir el siguiente output (resultado)
Resultado: [2, 4, 6, 8, 10]

# PREGUNTA 3
# usar el comando filter para filtrar y presentar solo los clientes menos de edad (adulto)
clientes = [
    {"nombre": "Alice", "edad": 15},
    {"nombre": "Bob", "edad": 35},
    {"nombre": "Charlie", "edad": 13},
    {"nombre": "David", "edad": 40}
]

# PREGUNTA 4 desempaquetar

persona = ("Alice", 25, "Engineer")

# resultado:
print(nombre)        
print(edad)         
print(rol)  

# PREGUNTA 5 desempaquetar
numeros = [1, 2, 3, 4, 5]

# resultado:
print(primero)   # Output: 1
print(mitad)  # Output: [2, 3, 4]
print(ultimo)    # Output: 5


# PREGUNTA 6 list comprehension
# Usando list comprehension...
nombres = ["Ana", "Luis", "Carlos", "Maria", "Pedro"]

print(primeras_letras)  # Salida: ['A', 'L', 'C', 'M', 'P']
# avanzado: seleccionar solo los nombres de Luis, Carlos y Maria.

