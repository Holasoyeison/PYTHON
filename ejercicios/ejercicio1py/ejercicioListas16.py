#Edades de estudiantes de mayor a menor. 

print("=====EDADES ESTUDIANTES=====")

edades=[]

for i in range(3):
    edad=int(input("Ingresa la edad del alumno: "))
    edades.append(edad)
edades.sort(reverse=True)

print ("Las edades ordenadas son: ")
print(edades)
