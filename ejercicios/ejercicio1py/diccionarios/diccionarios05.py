# print("====FRECUENCIA DE PALABRAS===")

# palabra=input("Ingresa la palabra: ")

# letras={}

# for letra in palabra:
#     if letra in letras: 
#         letras[letra]+=1
#     else:
#         letras[letra]=1

# for letra, cantidad in letras.items():
#     print(letra, ":", cantidad)

# print("===FRECUENCIA DE PALABRAS===")

# frase=input("Ingresa una frase: ")

# palabras={}

# for palabra in frase.split():
#     if palabra in palabras: 
#         palabras[palabra]+=1
#     else:
#         palabras[palabra]=1

# for palabra, cantidad in palabras.items():
#     print(palabra, ":", cantidad)


print("===REGISTRO DE ESTUDIANTES===")

estudiantes={}

cantidad=int(input("Cantidad de estudiantes: "))
for i in range(cantidad):
    nombre=input("Ingresa nombre dle estudiante: ")
    nota=float(input("Ingrese la nota dle estudiante: "))
    estudiantes[nombre] = nota

for nombre, nota in estudiantes.items():
    print(nombre, ":", nota)