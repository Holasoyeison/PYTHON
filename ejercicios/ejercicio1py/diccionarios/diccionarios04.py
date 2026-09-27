print("===CANTIDAD DE PALABRAS===")

frase=input("Ingrese una palabra: ")
palabras = frase.split()
contador ={}

for palabra in palabras:
    if palabra in contador:
        contador[palabra] = contador[palabra] + 1
    else:
        contador [palabra] = 1

for palabra, cantidad in contador.items():
    print(palabra, ":" , cantidad)