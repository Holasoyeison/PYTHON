print ("====== CALCULO DE PRECIO DE ENTRADAS=====")

edad = int (input("Ingrese su edad, por favor: "))

if edad <= 5:
    print ("¡Entrada gratis!")
elif edad >=5 and edad <= 12:
    print ("El vlaor a pagar es: $15.000 pesos.")
elif edad >=13 and edad <=59:
    print("El vlaor a pagar es: $30.000 pesos. ")
else :
    print ("Su valor a pagar es: $20.000 pesos.")