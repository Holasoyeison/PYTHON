print("====FACTURA DE VENTA VETERINARIA====")

nombrePropietario =input("Nombre propietario de la mascotA: ")
nombreMascota= input("Nombre de la mascota: ")
tipoMascota= input("Tipo de nascota: ")

valorConsulta= float(input("Precio de la consulta: $"))
medicamentosValor= float(input("Precio de los medicamentos: $"))
OtroServicio= float(input("Otros servicios ofrecidos: $"))
iva=0.19
totalPago= (valorConsulta+medicamentosValor+OtroServicio)*iva
totalPago= totalPago+iva

print ("=======FACTURA=======")

print("==============================")
print("El nombre del propietario de la mascota: ",nombrePropietario)
print("Nombre d ela mascota:", nombreMascota)
print("Mascota tipo:", tipoMascota)
print("Iva: ", iva,)
print ("=====TOTAL A PAGAR ES:====", totalPago, "Pesos.")