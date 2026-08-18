#Escribir un programa que pida al usuario una palabra y muestre por pantalla cuántas letras tiene.

print("===== LETRAS EN UNA PALABRA =====")

palabra=input("Ingresa una palabra: ")
contador=0

for letra in palabra:
    contador+=1
print("La palabra tiene " ,contador, "letras.")