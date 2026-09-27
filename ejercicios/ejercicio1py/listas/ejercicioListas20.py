#Mostrar una palabra al revés

print("====== MOSTRAR PALABRA AL REVÉS =====")

palabra=input("Ingresa una palabra: ")
invertida=""

for letra in palabra:
    invertida= letra+invertida

print("La palabra invertida es: ", invertida)