print (" ======VERIFICADOR DE TRIANGULOS======")


lado1 = float (input("ingresa El vlaor del primer lado: "))
lado2 = float (input("Ingrese el vlaor del segundo lado: "))
lado3 = float (input("INgres el valor del tercer lado : "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):

    if  lado1 == lado2 and lado2 == lado3:
        print("Es un triangulo equilateto.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print ("Es un triangulo isoseles.")
    else:
        print("Es un triangulo escaleno.")
else:
    print ("Los datos ingresados, no forman ningún triangulo")
