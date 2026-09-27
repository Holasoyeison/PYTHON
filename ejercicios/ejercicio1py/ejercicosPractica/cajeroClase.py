saldo=1000000

def verSaldo():
    print("Su saldo es:",saldo)
    print(f"="*33)

def retirar():
    global saldo

    dinero=float(input("¿Cuanto dinero desea retirar?: "))

    if dinero <=saldo:
        saldo = saldo - dinero
        print(f"="*33)
        print("Retiro exitoso.")
        print("Su saldo es:" ,saldo)
    else:
        print(f"="*33)
        print("Saldo insuficiente.")

def ingresar():
    global saldo
    dinero=float(input("Cuanto dinero desea ingresar?: "))

    saldo= saldo + dinero
    print("ingreso exitoso.")
    print("Su nuevo saldo es:" "$",saldo)

while True:
    print("\n=== CAJERO AUTOMATICO ===")
    print("1. Ver saldo.")
    print("2. Retirar dinero.")
    print("3. Ingresar dinero.")
    print("4. Salir")

    opcion= int(input("Selecciona una opción: "))
    if opcion ==1:
        print(f"="*33)
        verSaldo()
    elif opcion ==2:
        print(f"="*33)
        retirar()
    elif opcion == 3:
        print(f"="*33)
        ingresar()
    elif opcion == 4:
        print(f"="*33)
        print("\nGracias por usas nuestros servicios.")
        print("¡Vuelve pronto!")
        print(f"="*33)
        break
    else:
        print(f"="*33)
        print("Opción no válida.")