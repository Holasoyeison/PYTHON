# print("===AGENDA TELEFONICA===")
# agenda={}

# cantidad=int(input("Cantidad de contactos: "))
# while True:
#     for i in range(cantidad):
#         print(f"="*32)
#         nombre=input("Nombre de contacto: ")
#         numTelefono=input("Número de contacto: ")

#         agenda [nombre] = numTelefono

#     buscar=input("Buscar contacto: ")
#     if buscar in agenda:
#         print("Telefono de", buscar, + ":", agenda[buscar])
#     else:
#         print("Contacto no encontrado.")

print("===AGENDA TELEFONICA===")

agenda ={}
cantidad = int(input("Cantidad de contactos: "))

for i in range(cantidad):
    print(f"="*32)
    nombre=input("Ingresa nombre del contacto: ")
    numTelefono=input("Ingresa el número telefónico del contacto: ")

    agenda [nombre] = numTelefono
while True:
    buscar= input("\nBuscar nombre o número de telefono o (Salir): ")
    if buscar.lower()=="salir":
        break
    encontrado= False

    for nombre,numTelefono in agenda.items():
        if buscar.lower() == nombre.lower() or buscar == numTelefono:
            print("Nombre contacto: ", nombre)
            print("Número de contacto: ",numTelefono)
            encontrado = True
    if encontrado ==False:
        print("El contacto no está en la agenda. ")