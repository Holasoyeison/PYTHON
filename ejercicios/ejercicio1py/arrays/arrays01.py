numeros=[]

cantidad=int(input("Cantidad de números?: "))

for i in range(cantidad):
    numero=int(input("Ingresa el número: "))
    numeros.append(numero)

mayor = numeros[0]
menor = numeros[0]

for numero in numeros: 
    if numero > mayor:
        mayor = numero

    if numero < menor:
        menor = numero

print("\nMayor: ",mayor)
print("Menor: ",menor)