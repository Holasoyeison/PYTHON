# print("===REGISTRO DE BIBLIOTES===")

# biblioteca={}

# cantidad=int(input("Cantidad de libros: "))

# i=0
# while i < cantidad:
#     codigo=input(f"\nIngrese código del libro {i+1}: ")

#     if codigo in biblioteca:
#         print("¡Atención! Códico ya existe, ingresa otro: ")
#     else:
#         nombreLibro= input("Nombre libro: ")
#         biblioteca[codigo] = nombreLibro
#         i += 1 

# print("\n===Consulta de libro: ")
# codigoBuscar =input("Consulta dódigo: ")
# if codigoBuscar in biblioteca:
#     tituloEncontrado= biblioteca[codigoBuscar]
#     print("\nLibro encontrado: ")
#     print(f"{codigoBuscar} -> {tituloEncontrado}")
# else:
#     print("código no válido.")

print("===REGISTRO DE BIBLIOTCA===")

biblioteca={}

cantidad=int(input("Cantidad de libros: "))
i = 0
while i < cantidad:
    codigo=input(f"\nIngreseel código del libro {i+1}: ")
    if codigo in biblioteca:
        print("Atención! El código ya existe. Ingrese otro. ")
    else: 
        nombreLibro=input("Nombre del libro: ")
        biblioteca[codigo] = nombreLibro
        i+=1
while True:
    print("\n===Menú de biblioteca===")
    print("1. Código a consultar.")
    print("2. salir.")

    opcion= input("Elige una opción: ")

    if opcion =="1":
        print(f"="*33)
        codigoBuscar= input("\nIngrese el código a consultar: ")
        print(f"="*33)

        if codigoBuscar in biblioteca:
            tituloEncontrado= biblioteca[codigoBuscar]
            print(f"="*33)
            print("\nLibro encontrado!")
            print(f"{codigoBuscar} = {tituloEncontrado}")
        else:
            print(f"="*33)
            print(f"\nEl código ingresado no es válido.")
            
    elif opcion == "2":
        print(f"="*33)
        print("\nSaliendo dle programa. Hasta pronto!")
        print(f"="*33)
        break
    else:
        print(f"="*33)
        print("\nOpción no válida.")
