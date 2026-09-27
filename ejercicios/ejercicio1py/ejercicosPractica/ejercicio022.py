print("=== LA SUMA DE LOS DOS PRIMEROS NÚMEROS ===")

n= int(input("N: "))

suma=0


for numero in range(1,n+1):
    suma = suma + numero
print("La suma de los dos primeros números", n, "números es: ", suma)