nombreCliente = input("Ingrese el nombre dle cliente: ")
procesador = input (" Ingresa el procesador del computador: ")
ram = input("Ingrese la cantidad de memoria RAM: ")
disco= input("Ingrese la capacidad del disco duro: ")
procesadorPrecio = float (input ("Ingrese el precio del procesador: "))
ramPrecio = float(input("Ingrese el precio d ela memoria RAM: "))
discoPrecio = float(input("Ingrese el precio del almacenamiento: "))

valorTotal= procesadorPrecio + ramPrecio + discoPrecio
iva = valorTotal * 0.19
valorTotalConIva = valorTotal + iva

print("====================") 
print ("Resumen de la compra")
print("====================")

print("El cliente", nombreCliente, "ha comprado un computador con procesador", procesador, "memoria ram", ram, "y disco ducro", disco)
print("El valor total de la compra es: ", valorTotalConIva)
print("El iva es: ", iva)
print("El valor total con iva es: ", valorTotalConIva)
print("====================")
print("Gracias por su compra. Vuelva pronto!")
print("====================")

