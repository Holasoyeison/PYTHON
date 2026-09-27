print ("======SUMA ACUMULADA======")

numero =int(input("Ingresa un número entero: "))
suma=0
while numero !=0:
    suma=suma+numero
    numero =int(input("Ingrese otro número: "))

print ("El resultado total de la suma es: ", suma)