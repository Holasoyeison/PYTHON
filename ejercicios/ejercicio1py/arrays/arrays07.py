print("===LISTA ORDENADA===")

numeros = []

cantidad = int(input("Cantidad de números: "))

for i in range(cantidad):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        if numeros[i] > numeros[j]:
            temporal = numeros[i]
            numeros[i] = numeros[j]
            numeros[j] = temporal

print("Lista ordenada:")

for numero in numeros:
    print(numero)