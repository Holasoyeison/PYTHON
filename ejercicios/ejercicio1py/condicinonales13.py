#Crea un programa con un saldo inicial de $100.000.
#El usuario puede elegir: 1. Consultar saldo 2. Retirar dinero 3. Salir
print("======CAJERO SENCILLO======")

saldo=1000000
opcion=0

print("=====BIENVENIDO A NUESTROS CAJEROS.=====")

while opcion !=3:
    print("\n-----CAJERO-----")
    print("1. Consultar saldo.")
    print("2. Retirar dinero.")
    print("3. Salir.")

    opcion=int (input("Selecciona una opción: "))

    if opcion==1:
        print ("Su saldo es: ",saldo)
    elif opcion==2:
        retiro=int(input("¿Cuanto desea retirar?: "))
        if retiro <=saldo:
            saldo=saldo-retiro
            print("\n===RETIRO EXITOSO===\nSaldo actual: ",saldo)
        else:
            print("Saldo insuficiente.")
    elif opcion==3:
       
        print("Gracias por usar nuestros servicios")
    else:
        print("Opción no válida.")

