# saldo = 1000000

# def consultarSaldo():
#     print(f"="*33)
#     print("Su saldo es: ", saldo)
# def retirarDinero(cantidad):
#     global saldo

#     if cantidad <= saldo:
#         saldo =saldo - cantidad
#         print(f"="*33)
#         print("Retiro realizado.")
#         print(f"="*33)
#         print("Su nuevo saldo es: ", saldo)

#     else:
#         print("Fondo insuficientes.")

# def depositarDinero(cantidad):
#     global saldo
#     saldo = saldo + cantidad
#     print(f"="*33)
#     print("Deposito exitoso.")
#     print(f"="*33)
#     print("Su nuevo saldo es: ", saldo)

# while True:
#     print("\n=== CAJERO AUTOMATICO ===")
#     print("1. Consultar saldo.")
#     print("2. Retirar dinero.")
#     print("3. Depositar dinero.")
#     print("4. Salir.")

#     opcion= int(input("Selecciona una opción: "))

#     if opcion == 1: 
#         consultarSaldo()
#     elif opcion == 2:
#         cantidad= float(input("¿Cuanto dinero desea retirar?: "))
#         retirarDinero(cantidad)
#     elif opcion == 3:
#         cantidad = float(input("¿Cuanto dinero desea depositar?: "))
#         depositarDinero(cantidad)
#     elif opcion ==4:
#         print(f"="*33)
#         print("Gracia spor usas nuestros servicios.")
#         break
#     else:
#         print(f"="*33)
#         print("Opción no válida.")


#CAJERO USANDO MATCH

saldo = 1000000

def consultaSaldo():
    print("Su saldo es: ",saldo)
def retiroDinero(cantidad):
    global saldo
    if cantidad <= saldo:
        saldo = saldo - cantidad
        print("Retiro exitoso.")
        print("Su nuevo saldo es: ", saldo)
    else:
        print("Fondos insuficientes.")
def depositarDinero(cantidad):
    global saldo
    saldo = saldo + cantidad
    print("Depósito realizado.")
    print("Su nuevo saldo es: ",saldo)

while True:

    print("=== CAJERO AUTOMATICO ===")
    print("1. Consultar saldo.")
    print("2. Retirar dinero.")
    print("3. Depositar dinero.")
    print("4. salir.")

    opcion= int(input("Seleccina una opción: "))

    match opcion:
        case 1:
            consultaSaldo()
        case 2:
            cantidad=float(input("¿Cuanto dinero desea retirar?: "))
            retiroDinero(cantidad)
        case 3:
            cantidad=float(input("¿Cuanto dinero desea depositar?: "))
        case 4:
            print("Gracias por usas nuestros servicios.")
            break
        case _:
            print("Opción no válida.")
