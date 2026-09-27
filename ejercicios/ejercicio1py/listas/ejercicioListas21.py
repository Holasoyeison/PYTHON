#Contar cuántas veces aparece una letra

print("===== CUANTAS VECES APARECE UNA LETRA =====")

palabra=input("Ingresa una palabra: " )
letraBuscada= input("Ingresa una letra: " )

contador=0

for letra in palabra:
    if letra ==letraBuscada:
        contador +=1

print("La letra" ,letraBuscada, "aparece" ,contador, "veces.")