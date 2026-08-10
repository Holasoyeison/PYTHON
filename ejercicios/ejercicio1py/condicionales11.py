#Escribir un programa que pida al usuario una nota entre 0 y 5 y diga:
print("======CLASIFICACION DE NOTAS======")

nota =float(input("Ingresa la nota del estudiante: "))

if nota <=2.9:
    print ("Reprobado.")
elif nota <=3.9:
    print ("Aprobado.")
elif nota<=4.5:
    print ("Notable.")
else:
    print("Excelente!")