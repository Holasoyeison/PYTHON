# ordenar la siguiente lista, sin usar .sort. solamente con arreglos. sin necesidad de generar otra lista. ni introducir datos
numeros=[7,3,1,2,4,6,9,5,8]

# for num in range(len(numeros)):
#     for num2 in range(num + 1, len(numeros)):
#         if numeros[num] > numeros[num2] :
#             numeros[num], numeros[num2] = numeros[num2], numeros[num]
# print(numeros)

for num in range (len(numeros)):
    for num2 in range(len(numeros)-1):
        if numeros[num2] > numeros [num2 + 1 ]:
            temporal = numeros[num2]
            numeros[num2] = numeros [num2 + 1]
            numeros[num2 + 1] = temporal
print(numeros) 