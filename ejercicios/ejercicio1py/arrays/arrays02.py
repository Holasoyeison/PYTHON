print("===NOTA PROMEDIO===")

notas=[]

cantidad =int(input("Cantidad de notas: "))
for i in range(cantidad):
    nota=float(input("Ingrese la calificaicón: "))
    notas.append(nota)
suma =0

for nota in notas: 
    suma = suma + nota
promedio = suma / cantidad

print("El promedio es: ", promedio)