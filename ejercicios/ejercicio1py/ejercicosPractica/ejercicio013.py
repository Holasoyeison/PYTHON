print("=== EL MAYOR NÚMERO ENTRE TRES ===")

num1=int(input("Ingresa el primer número: "))
num2=int(input("Ingresa el segundo número: "))
num3=int(input("Inigresa el tercer número: "))

if num1>=num2 and num1>= num3:
    print("El número mayor es: ",num1)
elif num2>=num1 and num2>=num3:
    print("El número mayor es: ",num2)
else: 
    print("El número mayor es: ",num3)