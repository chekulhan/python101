


# ----------------------------------------
# carta usando match 
pedido = input("Qué quieres tomar?")

match pedido.lower():
  case "café":
      print("Has seleccionado Café. El precio es $2.50.")
  case "té":
      print("Has seleccionado Té. El precio es $1.80.")
  case "jugo":
      print("Has seleccionado Jugo. El precio es $3.00.")
  case "sándwich":
      print("Has seleccionado Sándwich. El precio es $4.50.")
  case "muffin":
      print("Has seleccionado Muffin. El precio es $2.00.")
  case _:
      print(f"Lo siento, no tenemos {pedido} en el menú.")

# carta usando if 
pedido = input("¿Qué quieres tomar?").lower()

if pedido == "café":
    print("Has seleccionado Café. El precio es $2.50.")
elif pedido == "té":
    print("Has seleccionado Té. El precio es $1.80.")
elif pedido == "jugo":
    print("Has seleccionado Jugo. El precio es $3.00.")
elif pedido == "sándwich":
    print("Has seleccionado Sándwich. El precio es $4.50.")
elif pedido == "muffin":
    print("Has seleccionado Muffin. El precio es $2.00.")
else:
    print(f"Lo siento, no tenemos {pedido} en el menú.")
