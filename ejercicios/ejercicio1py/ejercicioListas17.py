#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

print("===== VOCALES POR PALABRA ======")

palabra=input("Ingresa una palabra: ")
vocales=["a","e","i","o","u"]

for vocal in vocales: 
    contador=0
    for letra in palabra:
        if letra==vocal:
            contador+=1

    print("la vocal",vocal, "aparece",str(contador), "veces.")