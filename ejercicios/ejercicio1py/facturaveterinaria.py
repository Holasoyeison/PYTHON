print("====FACTURA DE VENTA VETERINARIA====")

nombrePropietario =input("Nombre propietario de la mascotA: ")
nombreMascota= input("Nombre de la mascota: ")
tipoMascota= input("Tipo de nascota: ")

valorConsulta= float(input("Precio de la consulta: $"))
medicamentosValor= float(input("Precio de los medicamentos: $"))
OtroServicio= float(input("Otros servicios ofrecidos: $"))

totalPago= valorConsulta+medicamentosValor+OtroServicio

print("==============================")
print("El nombre del propietario de la mascota: ",nombrePropietario)
print("Nombre d ela mascota:", nombreMascota)
print("Mascota tipo:", tipoMascota)

print ("=====TOTAL A PAGAR ES:====", totalPago, "Pesos.")