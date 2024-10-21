# El bytecode o código intermedio
# Python no genera un código de máquina como generaría un programa en C o C++, sino que funciona más o menos como  Java, tiene una maquina virtual que interpreta bytecode.
# Este intérprete (CPython) es el que se encarga de ejecutar el bytecode en tu ordenador.

def sumar(x, y):
  return x+y
  
def imprimir(msg):
  print(msg)

print(sumar.__code__.co_code) # bytecode
print(sumar.__code__.co_varnames) # parámetros

# disassembler module
# utilizar el módulo dis para desarmar el código

import dis
dis.dis(sumar)
dis.show_code(sumar)

bytecode_string=dis.Bytecode(sumar)
for x in bytecode_string:
  print (x)

dis.dis('print("hola mundo")')

# Cada instrucción en Python tiene un OPCODE (Código de operación)
# LOAD_FAST : Carga una variable a la cima del stack.
# BINARY_ADD : Suma los dos valores que hay en la cima del stack y los devuelve a la cima del stack.
# RETURN_VALUE : Devuelve el valor que esté en la cima del stack.
