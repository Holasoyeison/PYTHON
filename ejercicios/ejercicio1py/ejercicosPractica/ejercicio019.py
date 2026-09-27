print("=== VERIFIACIÓN DE TRIANGULOS ===")

lado1=int(input("Ingresa el lado 1: "))
lado2=int(input("Ingresa el lado 2: "))
lado3=int(input("Ingresa el lado 3: " ))

if lado1+lado2 and lado1+lado3 >lado2 and lado2+lado3>lado1:
    print("Si es posible crear un triangulo. ")
else: 
    print("No es posible crear un triangulo. ")