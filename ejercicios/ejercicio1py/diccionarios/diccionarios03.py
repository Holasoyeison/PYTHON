print("===INVENTARIO DE PRODUCTOS===")

# inventario={}

# cantidad= int(input("Cantidad de productos: "))
# for i in range(cantidad):
#     producto=input("Nombre de producto: ")
#     cantidad=int(input("Cantidad del producto: "))

#     inventario[producto] = cantidad

# while True:
#     buscar = input("\nconsultar producto o salir: ")
#     if buscar.lower() == "Salir":
#         break
#     encontrado = False

#     for producto, cantidad in inventario.items():
#         if buscar.lower() == producto.lower():
#             print("Cantidad disponible es: ", producto + ":", cantidad)
#             encontrado = True
#             break
#         if encontrado == False:
#             print("Producto no encontrado.")

# inventario={}
# cantidadProductos=int(input("Cantidad de productos: "))

# for i in range(cantidadProductos):
#     print(f"="*33)
#     producto=input("Nombre del producto: ")
#     cantidad=int(input("Cantidad del producto: "))
#     inventario[producto] = cantidad

#     while True:
#         buscar=input("\nConsultar producto o salir: ")
#         if buscar.lower() == "Salir":
#             break
#         encontrado = False

#         for producto,cantidad in inventario.items():
#             if buscar.lower() == producto.lower():
#                 print("Cantidad disponible de ",producto + ":",cantidad)
#             if encontrado == True:
#                 print("Producto no encontrado.")

inventario = {}

cantidad_productos = int(input("Cantidad de productos: "))

for i in range(cantidad_productos):
    producto = input("Producto: ")
    cantidad = int(input("Cantidad: "))

    inventario[producto] = cantidad

while True:
    buscar = input("\nConsultar producto (o escriba salir): ")

    if buscar.lower() == "salir":
        break

    encontrado = False

    for producto, cantidad in inventario.items():
        if buscar.lower() == producto.lower():
            print("Cantidad disponible de", producto + ":", cantidad)
            encontrado = True

    if encontrado == False:
        print("Producto no encontrado.")