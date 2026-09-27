#Escribir un programa que cree una lista vacía y permita al usuario ingresar 5 frutas. Después, el programa debe recorrer la lista y mostrar: Me gusta comer <fruta>

print("===== COMER FRUTA =====")

frutas=[]

#cantidad=int (input("¿Cuantas frutas vas a ingresar?: " ))

for i in range(3):
    fruta=input("Ingresa la fruta: " )
    frutas.append(fruta)
print(f"="*33)

for fruta in frutas:
    print("Me gusta comer ", fruta)
