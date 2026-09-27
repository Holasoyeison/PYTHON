print("====LISTAS DE MATERIAS====")

materias =[]

print (f"="*26)

for i in range(5):
    materia = input("Ingrese una materia: ")
    materias.append(materia)
print("Las materias son :")

print (f"="*26)
for materia in materias:
   print(materia)
