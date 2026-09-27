print("===LISTA DE ASIGNATURAS===")

asignaturas =[]

print (f"="*26)

for i in range (4):
    asignatura = input("Ingrese una materia: ")
    asignaturas .append(asignatura)
print ("Las asignaturas so: ")

print (f"="*26)

for asignatura in asignaturas:
    print ("Yo estudio", asignatura)

