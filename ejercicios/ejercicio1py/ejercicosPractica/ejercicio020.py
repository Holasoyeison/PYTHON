print("=== Clasificación de triangulos ===")

lado1=int(input("Ingresa el lado 1: "))
lado2=int(input("Ingresa el lado 2: "))
lado3=int(input("Ingresa el lado 3: " ))

if lado1 == lado2 and lado2 == lado3:
    print("El triangulo es equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triangulo es isóceles. ")
else: 
    print("El triangulo es escaleno. ")