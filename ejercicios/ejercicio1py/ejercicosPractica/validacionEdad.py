#MIENTRAS QUE EDAD SEA MENOR, DEBERÍA PEDIR NUEVAMENTE LA EDAD.

print(" VALIDACIÓN DE EDAD")

edad=0
edad=int(input("Ingresa la edad de la persona: "))

while edad<18:
    print("Edad no válida.")
    print("Debe ingresar una edad válida. mayor de edad.")
    edad=int(input("Ingresa nuevamente la edad: "))

print("="*33)
print("Edad válida")
print("Puede continuar")
print("=====¡BIENVENIDO!=====")