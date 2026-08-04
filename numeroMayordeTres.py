print ("====NÚMERO MAYOR DE TRES====")

num1 = float(input ("Ingrese el número 1: "))
num2 = float (input("Ingrese el número 2: "))
num3 = float(input ("Ingrese el número 3: "))

if num1 > num2 and num1 > num3:
    mayor= num1
elif num2 > num1 and num2> num3:
    mayor = num2
else:
    mayor= num3

print ("El número mayor es: ", mayor )
