# programa que pida al usuario dos números y devuelva su división. Si el usuario no introduce números debe devolver un aviso de error y si el divisor es cero también.
print("======DIVISION=======")

dividendo=float(input("Ingrese el dividendo: "))
divisor=float(input("Ingresa el número divisor: "))

if divisor==0:
    print("Error! No se puede dividir entre cero.")
else: 
    resultado =dividendo/divisor
    print("El resultado de la division es: ",resultado)