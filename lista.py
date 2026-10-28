# Lista de compras
# Permite agregar, ver y borrar productos de una lista.

productos = []
opcion = ""

while opcion != "4":
    print("")
    print("=== Lista de compras ===")
    print("1. Agregar producto")
    print("2. Ver lista")
    print("3. Borrar producto")
    print("4. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        producto = input("Producto: ")
        productos.append(producto)
        print(producto, "agregado")
    elif opcion == "2":
        if len(productos) == 0:
            print("La lista esta vacia")
        else:
            for i in range(len(productos)):
                print(i + 1, "-", productos[i])
    elif opcion == "3":
        producto = input("Producto a borrar: ")
        if producto in productos:
            productos.remove(producto)
            print(producto, "borrado")
        else:
            print("Ese producto no esta en la lista")
    elif opcion == "4":
        print("Hasta luego!")
    else:
        print("Opcion no valida")
