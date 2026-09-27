print("=== DESCUENTO POR MONTO D ECOMPRA ===")

compra=int(input("Ingres ael valor de compra: "))

if compra>500000:
    descuento= compra*0.10
else:
    descuento=0
total = compra-descuento

print("El descuento eS: ",descuento)
print("El total a pagar: ",total)