# Example 1: Simple list unpacking
numbers = [1, 2, 3]
a, b, c = numbers

print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3


# Example 2: Unpacking a tuple
coordinates = (4, 5, 6)
x, y, z = coordinates

print(x)  # Output: 4
print(y)  # Output: 5
print(z)  # Output: 6


# Example 3: List unpacking with arbitrary length
numbers = [1, 2, 3, 4, 5]
a, *b, c = numbers

print(a)  # Output: 1
print(b)  # Output: [2, 3, 4]
print(c)  # Output: 5

# Example 4: Unpacking a dictionary (keys)
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
name, age, city = person  # Only keys will be unpacked

print(name)  # Output: 'name'
print(age)   # Output: 'age'
print(city)  # Output: 'city'

n, a, c = person.keys() # desempaquetar keys y values
n, a, c = person.values()
print(n)

# Example 5: Unpacking dictionary items
for key, value in person.items():
    print(f"{key}: {value}")


# Example 6: Unpacking a set
my_set = {7, 8, 9}
a, b, c = my_set

print(a, b, c)  # Output can be any order of 7, 8, 9

# Unpack objeto - usar __dict__.values()
class Person:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

person = Person(name="Charlie", age=28, city="San Francisco", country="USA")

a,*b, c = person.__dict__.values()


# Actividades
# Imaginate que recibes datos en CSV como este
personas = [
    ['Jon', 30, 'Nueva York'],
    ['Maria', 25, 'Madrid'],
    ['Charlie', 28, 'San Francisco']
]

for persona in personas:
    # aqui desempaquetar los valores de nombre, edad y ciudad
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")


# NOTAS del examen - quieres el primero y el ultimo. En ordén.
notas_del_examen = [6, 5, 2, 8, 5]

# Mostramos los resultados
print(f"La primera puntuación es: {primero}")
print(f"La última puntuación es: {ultimo}")


# Respuesta
nombre, edad, ciudad = persona

notas_del_examen.sort()

# Extraemos el primer y último valor usando * para el resto de la lista
primero, *_, ultimo = notas_del_examen
