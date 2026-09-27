print ("DESCUENTOS DE SU COMPRA")

descuento=0.20
descuento2=0.10
valorCompra=float(input("Ingrese el valor dela compra:"))


if valorCompra>=100000:
    dcto=valorCompra*descuento
    compra=valorCompra-dcto
    print ("El valor del descuento es:",dcto)
    print("El valor de la compra es:",compra)
elif valorCompra>=50000:
    dcto=valorCompra*descuento2
    compra=valorCompra-dcto
    print ("El valor del descuento es:",dcto)
    print("El valor de la compra es:",compra)
else:
    print("No tiene ningún descuento")

