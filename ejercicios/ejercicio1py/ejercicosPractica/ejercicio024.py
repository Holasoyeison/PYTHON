print("=== TABLAS DE MULTIPLICAR ===")

num= int(input("Ingresa el número: "))

for i in range( 1, 11):
    resultado = num * i
    print(num ,"x", i, "=",resultado)