print("=======CALCULO DE NOTAS======")

suma=0

for i in range(1,6):
    nota = float (input(f"Ingrese las notas [i]: "))
    suma =suma+nota

promedio = suma/5

print ("="*33)
print ("====Notas Finales====")
print ("La suma de las notas son: ", suma)
print ("El promedio de las notas es:", promedio)