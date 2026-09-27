print("==== NÚMEROS PARES ====")

cantidad =int(input("¿Cuantos números quieres ingresar?: "))
pares=[]

for numero in range(1,cantidad + 1 ):
    if numero %2 ==0:
        pares.append(numero)
print ("Los números pares son: ", pares)