print("===INVERTIR LISTA===")

palabras=[]

cantidad=int(input("Cantidad de palabras: "))

for i in range(cantidad):
    palabra=input("Ingres la palabra: ")
    palabras.append(palabra)

print("===LISTA INVERTIDA===")

for i in range(len(palabras)-1,-1,-1):
    print(palabras[i])