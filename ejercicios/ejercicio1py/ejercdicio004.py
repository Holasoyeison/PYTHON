print("=== PROMEDIO DE NOTAS ===")

suma=0
contador=0

while contador <=4:
    nota=float(input("Ingrese la nota del estudiante: "))
    suma=suma+nota
    contador=contador+1

promedio= suma/5

print("El promedio de las notas es: ",promedio)