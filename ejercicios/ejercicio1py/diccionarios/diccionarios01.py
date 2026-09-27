print("===REGISTRO DE ESTUDIANTES===")

estudiantes={}

cantidad=int(input("Cantidad de estudiantes: "))

for i in range(cantidad):
    codigo=input("Ingrese código: ")
    nombre=input("Ingrese el nombre del estudiante: ")

    estudiantes[codigo] = nombre

print("\nLista de estudiantes: ")

for codigo, nombre in estudiantes.items():
    print(codigo, ">", nombre)