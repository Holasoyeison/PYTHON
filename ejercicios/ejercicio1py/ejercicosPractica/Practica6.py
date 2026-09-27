print("=====COSTOT TOTAL DE COMPRA=====")

valorCompra= float(input("Ingresa el valor de la compra: "))
desuentoPorcentaje=0.20

if valorCompra>100000:
    descuento= valorCompra*desuentoPorcentaje
    total= valorCompra-descuento
    print("El descuento es:", descuento)
else:
    total=valorCompra
    print("No aplica descuento.")

print ("=====TOTAL A PAGAR:", total, "PESOS")

