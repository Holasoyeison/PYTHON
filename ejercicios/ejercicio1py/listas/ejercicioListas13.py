print("====== NOTAS DE ESTUDIANTES =====")

nombres =[]
notas=[]

print(f"="*33)

cantidad= int(input("¿Cuantos alumnos ingresarás?: " ))


print(f"="*33)

for i in range (cantidad):
    nombre=input("Ingresa el nombre del alumno: " )
    nombres.append(nombre)

print(f"="*33)

for nombre in nombres:
    nota=float(input("Ingresa la notas de " +nombre+ " : " ))
    notas.append(nota)
    
print(f"="*33)

for i in range(len(nombres)):
    print(nombres[i], "tiene una nota de: ", notas[i])