#Escribir un programa que pida al usuario una nota entre 0 y 5 y diga:
print("======CLASIFICACION DE NOTAS======")

nota =float(input("Ingresa la nota del estudiante: "))
while nota <0 or nota >5: 
    print ("Nota no válida. Debe estar entre 0 y 5.")
    nota= float(input("Ingrese la nota del estudiante:"))

if nota <=2.9:
    print ("Reprobado.")
elif nota <=3.9:
    print ("Aprobado.")
elif nota<=4.5:
    print ("Notable.")
else:
    print("Excelente!")