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
