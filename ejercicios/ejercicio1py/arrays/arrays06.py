print("===ELEMENTO REPETIDO===")

numeros=[]
sinRepetir=[]

cantidad=int(input("Cantidad de números: "))

for  i in range(cantidad):
    numero=int(input("Ingresa el número: "))
    numeros.append(numero)

for numero in numeros:
    if numero not in sinRepetir:
        sinRepetir.append(numero)

print("Numeros repetidos: " )

for numero in sinRepetir:
    print(numero)