#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
print("======MATERIAS REPROBADAS ======")

materias=[]
notas=[]

cantidad=int(input("¿Cuantas asignaturas vas a ingresar: ?"))

for i in range (cantidad):
    materia= input("Ingrese la materia: ")
    materias.append(materia)
for materia in materias.copy():
    nota=float(input("¿Qué nota sacaste en : " + materia+ "?" ))
    notas.append(nota)

    if nota >=3.0:
        materias.remove(materia)

print(f"="*32)
print("La materias reprobadas son: ")
for materia in materias:
   
    print(materia)

promedio = sum(notas)/ len (notas)

print(f"="*32)

print("El promedio de las notas son : ", promedio)

