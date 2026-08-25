print("===== NÚMERO MAYOR A LA MEDIA ====")

numeros=input("Introduce los numeros separados ppr comas: ")
numeros= numeros.split(",")
numeros=[int(numero) for numero in numeros]
media=sum(numeros)/len(numeros)
cantidad=0

for numero in numeros: 
    if numero> media:
        cantidad=cantidad+1

print("Los números son: ", numeros)
print("La media es: ",media)
print("Hay", cantidad, "números mayores que la media.")