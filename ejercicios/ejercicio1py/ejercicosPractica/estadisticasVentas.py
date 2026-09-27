ventas = []

dias = int (input("Cantidad de días: "))

for i in range (dias):
    venta = float(input("Venta del día: "))
    ventas.append(ventas)

mayor= ventas
menor = ventas
total = 0

for venta in ventas:
    if venta > mayor:
        mayor = ventas

    if venta < menor:
        menor = ventas

    total = total + ventas

promedio = total/dias

cantidad = 0

for venta in ventas:
    if venta > promedio: 
        cantidad = cantidad + 1

print("Venta mayor: $",mayor)
print("Venta menor: $",menor)
print("Total vendid: $", total)
print("Promedio: $",promedio)
print("Ventas superiores al promedio: $",cantidad)