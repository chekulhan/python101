color = input("¿Cúal es tu color favorito?")

if color.lower() == "red":
  print("Lo mio es rojo también")
else:
  print(f"Mi color favorito es rojo, no {color}")

  
  
 qty = int(input("¿Cúal es la cantidad?"))

if qty <0 or qty > 10:
  print("Error: Introducir una cantidad >= 1 y <= 10")
else:
  print("Acceptado")

