#Escribir un programa que pregunte al usuario cuántos estudiantes quiere ingresar.Para cada estudiante, debe pedir: l nombre del estudiante.La nota que obtuvo.Los nombres deben guardarse en una lista y las notas en otra.

#print("======APROBADOS Y REPROBADOS======")

#estudiantes =[]
#notas =[]

#cantidad = int(input("¿cuantos alumnos va a ingresas?: " ))

#for i in range (cantidad):
#    estudiante=input("Ingrese el nombre del estudiante: ")
#    estudiantes.append(estudiante)

#print(f"="*31)

#for estudiante in estudiantes:
#   nota= float(input("¿Qué nota sacó " +estudiante+ " ? "))
#    notas.append(nota)

#print(f"="*31)

#aprobado= 0
#reprobados= 0

#for i in range (len(estudiantes)):
#    if notas[i]>=3.0:
 #       print(estudiantes[i], " sacó " , notas[i], " Aprobado. ")
  #      aprobado +=1



   # else: 
    #    print (estudiantes[i], " sacó " , notas[i], " Reprobado. ")
     #   reprobados +=1

#print(f"="*31)

#promedio = sum(notas)/len(notas)

#print(f"="*31)

#print("promedio",round(promedio,2 ))
#print("Aprobados: ", aprobado)
#print("Reprobados: ", reprobados)

print("======APROBADOS Y REPROBADOS======")

estudiantes =[]
notas=[]
aprobados=[]
reprobados=[]

cantidad = int (input(" ¿ Cuantos alumnos va sa ingresar?: "))

for i in range (cantidad):
    estudiante= input("Ingrese el nombre del estudiante: ")
    estudiantes.append(estudiante)

print(f"="*31)

for estudiante in estudiantes:
    nota= float(input("¿Cuanto sacó " + estudiante+ " ? "))
    notas.append(nota)

print(f"="*31)

for i in range (len(estudiantes)):
    if notas [i] >=3.0:
        aprobados.append(estudiantes[i])
    else:
        reprobados.append(estudiantes[i])

promedio= sum(notas)/len(notas)
print(f"="*31)

print("\n Estudiantes que aprobaron : ")
for estudiante in aprobados:
    print(estudiante)

print(f"="*31)
print("\n estudiantes que reprobaron : " )
for estudiante in reprobados:
    print(estudiante)

print(f"="*31)
print("\n Promedio : " , round (promedio, 2))