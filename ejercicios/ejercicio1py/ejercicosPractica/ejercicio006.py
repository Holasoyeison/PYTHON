print("=== CONVERSOR DE SEGUNDOS ===")

segundos=int(input("Ingrese los segundos: "))
hora=segundos // 3600
resto=segundos % 3600
minutos=resto // 60 
segRestantes= resto % 60

print(segundos, "segundos, equivalen a: ")

print(hora,"hora(s)")
print(minutos, "minutos")
print(segRestantes, "segundos")