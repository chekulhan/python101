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
class Mago(Personaje):
    def __init__(self, nombre, salud, magia):
        super().__init__(nombre, salud)
        self.magia = magia

    def atacar(self):
        return f"{self.nombre} lanza un hechizo de magia {self.magia}!"

# Arquero (hijo de Personaje)
class Arquero(Personaje):
    def __init__(self, nombre, salud, flechas):
        super().__init__(nombre, salud)
        self.flechas = flechas

    def atacar(self):
        if self.flechas > 0:
            self.flechas -= 1
            return f"{self.nombre} dispara una flecha! Flechas restantes: {self.flechas}"
        else:
            return f"{self.nombre} no tiene flechas!"

# Uso
guerrero = Guerrero("Carlos", 100, 30)
mago = Mago("Luna", 70, "Fuego")
arquero = Arquero("Leo", 80, 5)

# Demostración
print(guerrero.atacar())  # Salida: Carlos ataca con fuerza de 30!
print(mago.atacar())      # Salida: Luna lanza un hechizo de magia Fuego!
print(arquero.atacar())   # Salida: Leo dispara una flecha! Flechas restantes: 4
print(arquero.atacar())   # Salida: Leo dispara una flecha! Flechas restantes: 3


PREGUNTA 2: 
numbers = [1, 2, 3, 4, 5]

# Using map with a lambda to double each number
doubled_numbers = list(map(lambda x: x * 2, numbers))

print(doubled_numbers)  # Output: [2, 4, 6, 8, 10]

PREGUNTA 3:

clientes = [
    {"nombre": "Alice", "edad": 15},
    {"nombre": "Bob", "edad": 35},
    {"nombre": "Charlie", "edad": 13},
    {"nombre": "David", "edad": 40}
]

# Using filter and lambda to find customers older than 30
no_adultos = list(filter(lambda x: x["edad"] < 18, clientes))

print(no_adultos)

# PREGUNTA 4 desempaquetar

persona = ("Alice", 25, "Engineer")
nombre, edad, rol = persona
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

# PREGUNTA 6 desempaquetar
numeros = [1, 2, 3, 4, 5]

# resultado:
print(primero)   # Output: 1
print(mitad)  # Output: [2, 3, 4]
print(ultimo)    # Output: 5
