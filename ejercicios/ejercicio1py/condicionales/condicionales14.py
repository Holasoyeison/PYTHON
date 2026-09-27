#Pide al usuario que intente adivinarlo. Mientras no acierte:Si el número es menor que 7 → "El número es mayor". Si es mayor que 7 → "El número es menor". Si acierta → "¡Correcto!".

print("=====ADIVINA EL NÚMERO======")

numeroSecreto=17

numero= int(input("Ingresas un número: "))
while numero != numeroSecreto:
    if numero <numeroSecreto:
        print("el número es mayor.")
    elif numero > numeroSecreto:
        print("El número es menor.")
    numero=int(input("Intenta nuevamente: "))
print("¡CORRECTO!")