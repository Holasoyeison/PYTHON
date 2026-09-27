print("===ENCONTRAR ELEMENTO===")

numeros=[]
print(f"="*33)
cantidad=int(input("Cantidad de números: "))

for i in range(cantidad):
    numero=int(input("Ingresa el número: "))
    numeros.append(numero)

print(f"="*33)

buscar= int(input("Número a buscar: "))

for i in range(len(numeros)):
    if numeros[i]==buscar:
        print(f"="*33)
        print("el número",buscar, "se encuentra en la posición: ",i)
        break
else:
    print(f"="*33)
    print("El número no ha sido encontrado. ")