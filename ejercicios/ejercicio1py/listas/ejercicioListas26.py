print("===== MULTIPLICACIÓN DE LISTAS =====")

lista1=[]
lista2=[]
resultado=[]

cantidad=int(input("¿cuantos números vas a ingresar?: "))

print(f"="*33)

print("Ingresa los números de la primer lista: " )

print(f"="*33)

for i in range(cantidad):
    numero=int(input("Ingresa el número: "))
    lista1.append(numero)

print(f"="*33)

print("Ingresa los números de la segunda lista: " )

print(f"="*33)


for i in range(cantidad):
    numero=int(input("Ingresa el número: " ))
    lista2.append(numero)

print(f"="*33)

for i in range (cantidad):
    multiplicacion=lista1[i]*lista2[i]
    resultado.append(multiplicacion)

print("Los números de las primera lista son: " ,lista1)
print("Los números de las primera lista son: " ,lista2)
print("El resultaod de la multiplicación es: ",multiplicacion)