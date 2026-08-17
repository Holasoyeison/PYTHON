#scribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
print("======ASIGNATURAS Y NOTAS======")

asignaturas=[]
notas=[]


cantidad=int(input("Cuantas asignaturas vas a ingresar:? "))
print(f"="*31)

for i in range(cantidad):
    asignatura=input("Ingresa la asignatura: ")
    asignaturas.append(asignatura)
print(f"="*31)
for asignatura in asignaturas:
   
    nota=input("qué nota has sacado en: "+asignatura+ "?")
    notas.append(nota)
print(f"="*30)   
for i in range(len(asignaturas)):
   
    print ("En", asignaturas[i],"has sacado", notas[i])