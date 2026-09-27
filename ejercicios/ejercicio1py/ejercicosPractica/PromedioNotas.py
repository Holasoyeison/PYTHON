print("======PROMEDIO DE NOTAS======")

suma=0
contador=1

while contador <=5:
    nota= float(input("Ingrese la nota del estudiante: "))
    suma = suma + nota
    contador= contador+1

promedio = suma/5

print ("La suma total de las cinco notas son: ", suma)
print("El promedio de las cinco notas es: ", promedio)
