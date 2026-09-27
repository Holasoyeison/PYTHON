#Escribir un programa que pregunte al usuario el valor de una compra y calcule el descuento:
print("=====DESCUENTO TIENDA=====")

valorCompra=float(input("Ingrese el valor de la compra: "))

if valorCompra<50:
    descuento=0 #"No tiene descuento."
    valorTotal=valorCompra
elif valorCompra<=100:
    descuento = valorCompra*0.10
    valorTotal= valorCompra-descuento
else:
    descuento=valorCompra*0.20
    valorTotal=valorCompra-descuento
print ("="*32)
print ("El valor de tu compra es: ", valorCompra, "Euros")
print ("El descuento de tu compra es: ", descuento, "Euros")
print ("El valor a pagar es: ",valorTotal, "Euros")
