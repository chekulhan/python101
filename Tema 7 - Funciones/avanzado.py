# Example 1: Assigning a function to a variable
def greet(name):
    return f"Hello, {name}!"

greet_func = greet  # Assign function to a variable
print(greet_func("Alice"))  # Output: Hello, Alice!


# Example 2: Passing a function as an argument
def say_hello():
    return "Hello!"

def execute_function(func):
    print("Executing function...")
    print(func())  # Calling the function passed as an argument

execute_function(say_hello)  # Output: Executing function... Hello!


# Example 3: Storing functions in a list
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

operations = [add, subtract]  # List of functions
print(operations[0](5, 3))  # Output: 8 (calls add)
print(operations[1](5, 3))  # Output: 2 (calls subtract)

# Example 5: Storing functions in a dictionary
func_dict = {
    'add': add,
    'subtract': subtract
}

print(func_dict['add'](10, 2))  # Output: 12
print(func_dict['subtract'](10, 2))  # Output: 8

# el tema "Tema Avanzado", aprenderemos a usar decorators

# ejercicios avanzados
# un string, al revés, sin usar metodos

def reverse_string(text):
    new_string = ""
    max_len = len(text)
    for i in range(max_len, 0, -1):
        new_string = new_string + (text[i-1])
    return new_string

print(reverse_string("Hello"))

# factorial

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1) 


print(factorial(5)) # 4 * 3 * 2 * 1
print(5 * 4 * 3 * 2 * 1)
