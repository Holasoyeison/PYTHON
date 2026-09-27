print("======CLASIFICAICON DE NOTAS======")

nota=0
nota= float(input("Ingrese la nota del estudiante: "))
if nota >4.5:
    print("Exelente")
elif nota>=3.5:
    print("Bueno")
elif nota>=3.0:
    print("Aceptable")
else:
    nota <3.0
    print("Reprobado")