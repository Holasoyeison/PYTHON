#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

#print("===== PALABRA PALINDROMO =====")

#palabra = input("Inresa una palabra: ")
#invertida=""

#for letra in palabra: 
 #   invertida= letra+invertida

#if palabra == invertida:
 #   print("La palabra es palindromo.")
#else:
 #   print("la palabra no es un palindromo.")

print("===== PALABRA PALINDROMO =====")

palabra=input("Ingresa una palabra: ")
palabraInversa=palabra
palabra=list(palabra)
palabraInversa=list(palabraInversa)
palabraInversa.reverse()

if palabra==palabraInversa:
    print("La palabra es palindromo.")
else:
    print("La palabra no es palindromo. ")