print("=== CALCULADORA BÁSICA ===")

num1=int(input("Ingresa el número 1: "))
num2=int(input("Ingresa el número 2: "))

print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

operacion= int(input("Opreación: "))

if operacion==1:
    resultado= num1+num2
elif operacion==2:
    resultado= num1-num2
elif operacion==3:
    resultado = num1*num2
elif operacion==4:
    resultado=num1/num2
else: 
    print(" Opreación no válida. ")

print("El resultado es: ",resultado)