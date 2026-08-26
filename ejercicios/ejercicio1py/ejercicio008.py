print("=== PRECIO CON DESCUENTO ===")

precioProducto=int(input("Ingrese el valor del producto: "))

descuento=0.15
descuentoAplicado= precioProducto*descuento
precioFinal=precioProducto-descuentoAplicado

print(f"="*33)

print("Precio dle producto: " "$",precioProducto)
print("Descuento aplicado: " "$",descuentoAplicado)
print("Valor total a pagar es: " "$",precioFinal)