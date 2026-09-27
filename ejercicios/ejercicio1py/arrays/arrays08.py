print("===LISTAS COMBINADAS===")

lista1=[]
lista2=[]
combinada=[]

cantidad = int(input("Cantidad d enúmeros: "))

print(f"="*33)
print("===LISTA #1===")

for i in range(cantidad):
    numero= int(input("Ingresa el número: "))
    lista1.append(numero)

print(f"="*33)
print("===LISTA #2===")

for i in range(cantidad):
    numero=int(input("iingresa el número: "))
    lista2.append(numero)


for numero in lista1:
    combinada.append(numero)

for numero in lista2:
    combinada.append(numero)

print(f"="*33)
print("===LISTA COMBINADA===")

for numero in combinada:
    print(numero)