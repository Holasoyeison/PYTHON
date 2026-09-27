print("=== NÚMEROS PRIMOS ===")

num= int(input("Ingresa el numero: "))

esPrimo= True

for i in range(2, num):
    if num % i ==  0:
        esPrimo= False
if esPrimo: 
    print("El número ",num, "es primo.")
else:
    print("El número ",num, "no es primo. ")
