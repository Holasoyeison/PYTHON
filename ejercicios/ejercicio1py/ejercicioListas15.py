#Escribir un programa que pregunte al usuario 5 números favoritos, los almacene en una lista y los muestre ordenados de menor a mayor.

print("===== MI NÚMERO FAVORITO =====")

numeros =[]

for i in range (5):
    numero=int(input("Ingresa tu número fsvorito: " ))
    numeros.append(numero)

numeros.sort()

print(f"="*32)
print("Los números ordenados son: ")
print(numeros)