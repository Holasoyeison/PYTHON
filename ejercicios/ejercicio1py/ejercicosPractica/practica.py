# Ejercicio 1. Análisis de temperaturas semanales

## Enunciado

# Una estación meteorológica registra la temperatura máxima de cada día durante una semana.

# Desarrolle un programa que solicite las temperaturas de los siete días y las almacene en una lista. Al finalizar, el programa debe mostrar:

# - La temperatura más alta registrada.
# - La temperatura más baja registrada.
# - El promedio de las temperaturas.
# - La cantidad de días cuya temperatura estuvo por encima del promedio.

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado", "Domingo"]
temperaturas=[]

print("=== CONTROL DE TEMPERATURAS ===")

for dia in dias:
    temperatura=float(input("Ingrese el valor de la temperatura del día " + dia + " : "))
    temperaturas.append(temperatura)

mayor = temperaturas[0]
menor = temperaturas[0]
suma = 0

for temperatura in temperaturas: 
    suma = suma + temperatura

    if temperatura > mayor:
        mayor = temperatura
    if temperatura < menor: 
        menor = temperatura

promedio = suma / len(temperaturas)
cantidad=0

for temperatura in temperaturas:
    if temperatura > promedio:
        cantidad= cantidad + 1 

print("La temperatura mas alta es: ", mayor)
print("La temperatura mas baja es: ", menor)
print("El promedio de las temperaturas es: ", promedio)
print("Dias que la temperatura estvu por encima del promedio: ",cantidad)


