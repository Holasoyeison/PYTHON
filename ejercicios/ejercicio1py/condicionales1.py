#Usuario ingresa la edad y validar si es mayor o menor de edad. Y pedir nuevamente la edad.
print("=====MAYOR O MENOR DE EDAD======") 

edad= int(input("Ingresa la edad: "))

while edad <18:
    print("Eres menor de edad.")
    edad=int(input("Ingrese nuevamente la edad: "))

print ("Eres mayor de edad.")
print("Bienvenido.")