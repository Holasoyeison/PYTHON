print("===EJERCICIOS ARRAYS===")

# print(f"="*33)
# print("===NÚMERO MAYOR AL PROMEDIO===")

# numeros=[]

# cantidad=int(input("Cantidad de números: "))

# for i in range(cantidad):
#     numero=int(input("Ingresa el número: "))
#     numeros.append(numero)
# suma = 0

# for numero in numeros: 
#     suma = suma + numero

# promedio = suma / cantidad
# mayores= 0 

# for numero in numeros: 
#     if numero > promedio:
#         mayores = mayores + 1 

# print(f"="*33)
# print("El promedio: ", round(promedio))
# print("Cantidad de números mayores al promedio es: ", mayores)
print(f"="*33)
print("===BUSCA LA PALABRA===")

palabras =[]

cantidad=int(input("Cantidad de palabras: "))

for i in range(cantidad):
    palabra=input("Ingresa la palabra: ")
    palabras.append(palabra)

print(f"="*33)
buscar=input("Palabra a buscar: ")

for i in range(len(palabras)):
    if palabras[i].lower() == buscar.lower():
        print("La palabra", buscar, "se encuentra en la posicion: ", i +1 ,".")
        break
else:
    print("Palabra no se encuentra en la lista.")