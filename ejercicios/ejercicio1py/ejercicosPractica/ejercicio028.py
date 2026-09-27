print("=== SUMA D ENÚMEROS IMPARES ===")

num=int(input("Ingresa el número: "))

suma= 0 

for i in range (1, num + 1, 2):
    suma = suma + i

print("La suma de los números es: ",suma)
 