print("===== MEDIA Y DESVIACIÓN TÍPICA =====")

numeros=input("Introduce los números aseparados por comas: ")
numeros=numeros.split(",")
numeros=[float(numero) for numero in numeros]
media=sum(numeros) / len(numeros)
suma=0

for numero in numeros:
    suma=suma+(numero-media)**2
desviacion=(suma/len(numeros))** 0.5

print("Los números son: ", numeros)
print("La media es: ", media)
print("La desviación típica es: ", desviacion)