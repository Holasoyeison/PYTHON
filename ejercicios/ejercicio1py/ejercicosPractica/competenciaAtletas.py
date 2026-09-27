tiempos = []
cantidad = int(input("Cantidad de atletas: "))

for i in range (cantidad):
    tiempo=float(input("Tiempo de atleta: "))
    tiempos.append(tiempo)

menor = tiempos [0]
mayor = tiempos [0]

for tiempo in tiempos: 
    if tiempo < menor:
        menor = tiempo

    if tiempo > mayor:
        mayor = tiempo

suma = 0

for tiempo in tiempos: 
    suma = suma + tiempo

promedio = suma/ cantidad
cantidadMenor = 0

for tiempo in tiempos:
    if tiempo < promedio:
        cantidadMenor = cantidadMenor + 1

print("Mejor tiempo: ", menor, "Seg.")
print("Peor tiempo: ", mayor, "Seg.")
print("Tiempo promedio: ", round(promedio , 2), "Seg.")
print("Atletas por debajo del promedio: ", cantidadMenor)