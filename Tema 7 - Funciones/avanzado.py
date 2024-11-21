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



# empezando con las tareas, completar las funciones
to_do_list = [["Comprar leche", False], ["Hacer las deberes", False], ["Regar las plantas", False] ]
mostrar_not_done(to_do_list)
mark_as_done(to_do_list, "Comprar leche")
add_new_task(to_do_list, "Comprar huevos")

# respuesta:
def mark_as_done(to_do_list, task):
    for i in to_do_list:
        if i[0] == task:
            i[1] = True
        
def mostrar_not_done(to_do_list):
    for i in to_do_list:
        if i[1] == False:
            print(i)


# Actividad de kwargs con diccionario
# Usar para introduccion a dictionary
# quieres mandar un correo - usar **kwargs para solucionarlo

enviar_correo(recipiente="ckulhan@nazaret.eus", asunto="Hola", cuerpo="Hola, qué tal?")
enviar_correo(recipiente="ckulhan@nazaret.eus", cuerpo="Hola, qué tal?")

# respuesta:
def enviar_correo(recipiente, **kwargs):
    asunto, cuerpo = "", ""

    if "asunto" in kwargs:
        asunto = kwargs["asunto"]
    if "cuerpo" in kwargs:
        cuerpo = kwargs["cuerpo"]
    
    print(f"""Enviando correo a {recipiente}
    asunto: {asunto}
    cuerpo: {cuerpo}
    """)
