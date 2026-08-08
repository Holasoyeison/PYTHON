print ("====SUMA DE LOS NÚMEROS====")

numero=int(input("Ingrese un número:"))
suma=0

while numero !=0:
    suma=suma+numero
    numero= int(input("Ingrese otro número: "))

print ("La suma es:",suma)