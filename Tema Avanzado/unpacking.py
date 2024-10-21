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

# Example 5: Unpacking dictionary items
for key, value in person.items():
    print(f"{key}: {value}")


# Example 6: Unpacking a set
my_set = {7, 8, 9}
a, b, c = my_set

print(a, b, c)  # Output can be any order of 7, 8, 9
