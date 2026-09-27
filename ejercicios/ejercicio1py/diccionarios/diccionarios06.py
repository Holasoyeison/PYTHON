# print("===REGISTRO DE ESTUDIANTES===")

# estudiantes={}

# cantidad=int(input("Cantidad de estudiantes: "))
# for i in range(cantidad):
#     nombre=input("Ingresa nombre dle estudiante: ")
#     nota=float(input("Ingresa la nota del estudiante: "))
#     estudiantes[nombre]=nota

# if estudiantes:
#     mejorEstudiante=""
#     mejorNota=-1.0

# for nombre, nota in estudiantes.items():
#     if nota >mejorNota:
#         mejorNota=nota
#         mejorEstudiante=nombre

# print("\nEl mejor estudiante con mejor nota es: \n")
# print(f"{mejorEstudiante} > {mejorNota}")

# print("===REGISTRO DE PRODUCTOS===")

# productos={}

# cantidad=int(input("Cantidad de productos: "))

# for i in range(cantidad):
#     nombre=input("Nombre del producto: ")
#     precio=float(input("Precio del producto: "))
#     productos[nombre] = precio

# if productos:
#     productoMasCaro=""
#     precioMasAlto=-1.0
# for nombre, precio in productos.items():
#     if precio > precioMasAlto:
#         precioMasAlto=precio
#         productoMasCaro=nombre


# print("\nEl producto mas costoso es: ")
# print(f"{productoMasCaro} -> {precioMasAlto}")
8
print("===MEJOR EMPLEADO===")

ventaEmpleados={}
cantidad=int(input("Cantidad de trabajadores: "))
for i in range(cantidad):
    nombre=input("Nombre del empleado: ")
    totalVentas=float(input("Valor total ventas:"))
    ventaEmpleados[nombre] = totalVentas

if ventaEmpleados:
    mejorEmpleado=""
    mejorVenta=-1.0

for nombre, ventas in ventaEmpleados.items():
    if ventas > mejorVenta:
        mejorVenta= ventas
        mejorEmpleado=nombre.upper()

print("\nEl mejor empleado del es: ")
print(f"{mejorEmpleado} con un total de: {mejorVenta}")