#pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
print("CONTRASEÑA MAYUSCULAS O MINUSCULAS")

contrasenia="admin"
usuario = input ("Ingrese la contraseña: ")

if usuario .lower()==contrasenia.lower():
    print ("La contrasenia es correcta.")
else:
    print("La contraseña es incorrecta.")