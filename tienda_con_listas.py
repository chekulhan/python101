# Actividad para gestionar productos en una tienda, usando listas

listaDeRopa = ["camiseta","pantalones", "bañador"]
accion = int(input("Teclea '1' para ver los productos, '2' para el listado de inventario, y '3' para borrar un producto..."))

if accion == 1:
    for ropa in listaDeRopa:
        print(f"Artículo {ropa}")

elif accion==2:
    compra = input("Qué quieres comprar?")
    if compra in listaDeRopa:
        # pedir al usuario dinero
        dinero=float(input("Cuesta 20 euros. Cuanto tienes?"))
        print(f"Gracias. Devolvemos ${dinero-20:.2f}")

    else:
        print("No tenemos este producto.")

elif accion == 3:
    # pedir al usuario el product para quitar
    borrar=input("¿Qué producto quieres borrar")
    if borrar in listaDeRopa:
        listaDeRopa.remove(borrar)
        print(f"{borrar} ha sido elimiado.")
        print(listaDeRopa) # para confirmar que ha sido eliminado
    else:
        print("No tenemos este producto.")
else:
    print ("No existe este opcion.")
