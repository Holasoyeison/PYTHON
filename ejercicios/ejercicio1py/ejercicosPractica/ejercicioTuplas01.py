print("===== MULTIPLICAICÓN DE MATRICES =====")

a= [
    [1,2,3],
    [4,5,6]
]

b=[
    [-1,0],
    [0,1],
    [1,1]
]

resultado=[]

for i in range(len(a)):
    fila=[]
    for j in range(len(b[0])):
        suma=0
        for k in range(len(b)):
            suma=suma + a[i][k] * b[k][j]
        fila.append(suma)
    resultado.append(fila)
print("La matriz a: ", a)
print("La matriz b: ", b)
print("Producto: ", resultado)