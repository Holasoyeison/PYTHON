#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante. 
print("===== ABECEDARIO=====")

import string

abecedario =list(string.ascii_lowercase)

for i in range (len(abecedario),0, -1):
    if i %3 == 0:
        abecedario.pop(i-1)

print(abecedario)

