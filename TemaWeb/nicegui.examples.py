# introducciónes
from nicegui import ui

def show_message(input_box):
    ui.label(f'Hola, {input_box}!')  # Display message with input value

# Create an input box and a button
name_input = ui.input(label='Introducir tu nombre')
ui.button('Hola', on_click=lambda: show_message(name_input.value))  # Pass the input box to the function

ui.run()

# random number generator
import random
from nicegui import ui

@ui.refreshable
def number_ui():
    ui.label(f'Random number is: {random.randint(0, 100)}')

def add_number():
    number_ui.refresh()  # Refreshes to show a new random number

number_ui()  # Initial display
ui.button('Add random number', on_click=add_number)

ui.run()


# ejercicio - calcular el indice de masa corporal (IMC o BMI en ingles)
# Fijate en los ... para completar la actividad

from nicegui import ui

def calculate_bmi(altura, peso):
    ...
    altura_m = altura / 100  # convertir a metros
    bmi = peso / (altura_m ** 2)
    ui.label(f'Tu IMC es: ...')

altura= ui.input(label='Introducir tu altura (cm)')
...
ui.button('Calcular BMI', on_click=lambda: calculate_bmi(altura.value, ...)) 

ui.run()





# respuesta a ejercicio de BMI -------------
from nicegui import ui

def calculate_bmi(altura, peso):
    altura = float(altura)
    peso = float(peso)
    altura_m = altura / 100  # convertir a metros
    bmi = peso / (altura_m ** 2)

    ui.label(f'Your BMI is: {bmi:.2f}')

altura= ui.input(label='Introducir tu altura (cm)')
peso = ui.input(label='Introducir tu peso (kg)')

ui.button('Calcular BMI', on_click=lambda: calculate_bmi(altura.value, peso.value))  # Pass the input box to the function

ui.run()
