print("======VALIDACI+ON DE CONTRASEÑA======")

contrasenia = input("Ingrese la contraseña: ")

while contrasenia != "admin123":
    print("Contraseña incorrecta")
    contrasenia=input("Ingrese nuevamente la contraseña: ")

print ("Contraseña correcta.")
print ("Acceso permitido.")