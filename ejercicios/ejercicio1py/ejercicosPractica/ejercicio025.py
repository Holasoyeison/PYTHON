print("=== FACTORIAL DE UN NÚMERO ===")

num= int(input("Ingresa el número: "))

factorial= 1

for i in range (1, num + 1):
    factorial= factorial*i

print("El factorial de ",num, "es: ", factorial)