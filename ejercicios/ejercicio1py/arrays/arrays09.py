print("====EL SEGUNDO NÚMERO MAYOR===")

numeros=[]

cantidad= int(input("Cantidad de números: "))

for i in range(cantidad):
    numero=int(input("Ingresa el números: "))
    numeros.append(numero)

mayor = numeros[0]
segundoMayor = numeros[0]

for numero in numeros: 
    if numero > mayor:
        segundoMayor = mayor
        mayor = numero
    elif numero > segundoMayor and numero != mayor:
        segundoMayor = numero


print("El segundo numero mayor es: ", segundoMayor)

# numeros = []

# cantidad = int(input("Cantidad de números: "))

# for i in range(cantidad):
#     numero = int(input("Ingresa el número: "))
#     numeros.append(numero)

# mayor = numeros[0]
# segundo_mayor = numeros[0]

# for numero in numeros:
#     if numero > mayor:
#         segundo_mayor = mayor
#         mayor = numero
#     elif numero > segundo_mayor and numero != mayor:
#         segundo_mayor = numero

# print("El segundo número mayor es:", segundo_mayor)