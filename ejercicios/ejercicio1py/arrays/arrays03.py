print("===NÚMEROS PARES E IMPARES===")

numeros=[]

cantidad=int(input("Cantidad de números: "))

for i in range(cantidad):
    numero=int(input("Ingresa el número: "))
    numeros.append(numero)

pares = 0
impares=0

for numero in numeros:
    if numero %2==0:
        pares = pares + 1
    else:
        impares= impares + 1

print("Pares: ",pares)
print("Impares: ",impares)