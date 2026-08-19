print("===== COMPARACION DE LISTAS =====")

lista1=[]
lista2=[]

cantidad=int(input("Cantidad de números en lista ?: "))

print(f"="*33)

print("Ingresa los números de la lista 1: ")

print(f"="*33)

for i in range(cantidad):
    numero=int(input("Ingresa el número: "))
    lista1.append(numero)

print(f"="*33)

print("Ingresa los números de la lista 2: ")

print(f"="*33)

for i in range(cantidad):
    numero=int(input("Ingrese el número: "))
    lista2.append(numero)

print(f"="*33)

for i in range(cantidad):
    if lista1==lista2:
        print("La posición",i,": Son iguales.")
    else:
        print("La posición",i, ": No son iguales.")