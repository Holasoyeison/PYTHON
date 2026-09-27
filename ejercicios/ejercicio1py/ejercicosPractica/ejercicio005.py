print("=== INTERCAMBIO DE VALORES ===")

variable1=int(input("Ingrese el primer número: "))
variable2=int(input("Ingrese el segundo número: "))

aux=variable1
variable1=variable2
variable2=aux

print(f"="*33)

print("=== RESULTADO DE INTERCAMBIO DE VALORES ===")
print(f"="*33)

print("el número uno es: ",variable1)
print("El número dos es: ",variable2)