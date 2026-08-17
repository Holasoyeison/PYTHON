#Escribir un programa que permita al usuario ingresar los nombres de 5 estudiantes y los almacene en una lista. espués, el programa debe preguntar la edad de cada estudiante y almacenarla en otra lista.

print("===== EDADES DE ALUMNOS =====")

estudiantes =[]
edades=[]

cantidad= int(input("¿Cuantos alumnos vas a ingresar:? "))

for i in range(cantidad):
    estudiante= input("¿Nombre del estudiante : ")
    estudiantes.append(estudiante)
print(f"="*31)
for estudiante in estudiantes:
    edad= int(input("¿Qué edad tiene " + estudiante + "?"))
    edades.append(edad)
print(f"="*31)
for i in range (len(estudiantes)):
    print (estudiantes [i], "tiene" , edades[i], "años")