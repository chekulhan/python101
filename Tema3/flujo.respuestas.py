# Programa de color

color = input("¿Cúal es tu color favorito?")

if color.lower() == "red":
  print("Lo mio es rojo también")
else:
  print(f"Mi color favorito es rojo, no {color}")

  
# Zara productos
qty = int(input("¿Cúal es la cantidad?"))

if qty <0 or qty > 10:
  print("Error: Introducir una cantidad >= 1 y <= 10")
else:
  print("Acceptado")


  
  
  
# Gastos de electricidad
cantidad = 100000

if cantidad > 1000:
  print("Has gastado mucho este mes")
elif cantidad > 500:
  print("Has gastado bastante este mes")
elif cantidad > 100:
  print("Has gastado poco este mes")
else:
  print("No has gastado nada este mes")
