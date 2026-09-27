#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

print("===== NÚMERO GANADOR DE MAYOR A MENOR =====")

numeros=[]

cantidad =int(input("ingrese la cantidad de numeros ganadores: "))
print(f"="*31)
for i in range (cantidad):
    numero=int(input("Ingresa el número ganador: "))
    numeros.append(numero)
numeros.sort()
print(f"="*31)
print("NÚMEROS GANADORES DE MENOR A MAYOR")
print(f"="*31)

for numero in numeros:
    print (numero)

