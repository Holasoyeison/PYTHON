print("===== Valor medio de tres números =====")

#numeros = int [num1, num2, num3]


num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
num3 = int(input("Ingrese el tercer número entero: "))

if (num1 >= num2 and num1 <= num3) or (num1 <= num2 and num1 >= num3):
    medio =num1

elif (num2 >= num1 and num2 <= num3 ) or (num2 <= num1 and num2 >= num3):
    medio = num2

else : 
    medio = num3

print ("El valor medio entre los números es:", medio)


