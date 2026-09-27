print("=== INICIO DE SESIÓN ===")

usuario= input("Ingresa tu usuario: ")
contrasenia=input("Ingresa tu contraseña: ")

if usuario == "admin" and contrasenia == "Python123":
    print("Acceso concedido. ")
else: 
    print("Acceso denegado. ")