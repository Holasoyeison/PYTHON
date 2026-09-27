# Caso Práctico – Sistema de Registro de Vehículos # Una empresa de transporte desea desarrollar un sistema para registrar los vehículos
# que hacen parte de su flota. # El programa deberá mostrar un menú de opciones que se repetirá continuamente # hasta que el usuario decida salir del sistema.

placas=[]
marcas=[]
anios=[]

while True:
    print("=== MENÚ ===")
    print("1. Registrar vehículo. ")
    print("2. Mostrar vehiculo.")
    print("3. Buscar vehiculo.")
    print("4. Mostrar vehículo mas antiguo.")
    print("5. Mostrar año promedio.")
    print("6. Salir.")

    opcion=int(input("Selecciona una opción: "))

    match opcion:
    
        case 1:
            placa=input("Ingres ala placa del vehículo: ")
            marca=input("Ingresa la marca del vehiculo: ")
            anio=int(input("Ingrese el año de fabricación: "))
            placas.append(placa)
            marcas.append(marca)
            anios.append(anio)

            print("Vehículos registrados correctamente!")

        case 2:
            if len(placas)==0:
                print("No existe vehiculo registrados.")
            else:
                print("\n === VEHÍCULOS REGISTRADOS === ")

                for i in range(len(placas)):
                    print("Placas: ",placas[i])
                    print("Marca: ", marcas[i])
                    print("años: ",anios[i])
                    print(f"="*32)
        case 3:
            buscar= input("Ingrese la placa a buscar: ")
            encontrado= False
            for i in range(len(placas)):
                if placas[i] == buscar:
                    print("\nVehículo encontrado:")
                    print("Placa: ", placas[i])
                    print("Marca: ",marcas[i])
                    print("Año: ",anios[i])
                    encontrado = True
            if encontrado == False:
                print("Vehículo no encontrado.")

        case 4: 
            if len(placas)==0:
                print("No existen vehiculos registrados.")
            else:
                posicion = 0
                for i in range(1, len(anios)):
                    if anios[i] < anios[posicion]:
                        posicion = 1
                print("\n=== VEHÍCULO MAS ANTIGUO ===")
                print("placa: ",placas[posicion])
                print("Marca: ",marcas[posicion])
                print("Año: ",anios[posicion])
        case 5:
            if len(placas)==0:
                print("No existen vehiculos registrados.")
            else:
                suma =0

                for i in range(len(anios)):
                    suma = suma + anios [i]
                    promedio= suma / len(anios)

                print("El promedio de fabricación es: ",promedio)

        case 6:
            print("Gracias por utilizar nuestros servicios.")
            break

        case _:
            print("Opción no válida.")


placas =[]
marcas=[]
anios=[]

while True:
    print("\n=== MENÚ ===")
    print("1. Registrar vehículo.")
    print("2. Mostrar vehiculos.")
    print("3. Buscar vehiculos.")
    print("4. Mostrar vehiculo mas antiguo.")
    print("5. Mostrar año promedio.")
    print("6. salir.")

    opcion=int(input("Selecciona una opción: "))

    match opcion:
        case 1:
            placa=input("Ingresa la placa: ")
            marca=input("Registra la marca del vehículo: ")
            anio=int(input("Ingresa año de fabricación: "))

            placas.append(placa)
            marcas.append(marca)
            anios.append(anio)

            print("Vehículo registrado correctamente.")

        case 2:
            if len(placas)==0:
                print("No hay ningún vehículo registrado.")
            else:
                for i in range(len(placas)):
                    print("Vehículo: ", i+1)
                    print("Placas: ", placas[i])
                    print("Marca: ", marcas[i])
                    print("Año: ", anios[i])

        case 3:
            buscar=input("Ingrese la placa a buscar: ")
            encontrado = False
            for i in range(len (placas)):
                if placas[i] == buscar:
                    print("\n=== Vehículo Encontrado ===")
                    print("Placa: ", placas[i])
                    print("Marca: ", marcas[i])
                    print("Año: ", anios[i])

                    encontrado= True
            if encontrado == False:
                print("vehículo no encontrado.")

        case 4:
            if len(placas)==0:
                print("No hay vehículo registrado.")
            else: 
                posicion = 0
                for i in range(1, len(anios)):
                    if anios[i] < anios[posicion]:
                        posicion = i

                print("\n=== Vehículo Antiguo ===")
                print("Placa: ", placas[posicion])
                print("Marca: ", marcas[posicion])
                print("AÑo: ", anios[posicion])

        case 5:
            if len(placas)==0:
                print("No hay vehículo registrado. ")
            else:
                suma = 0
                for i in range(len(anios)):
                    suma = suma + anios[i]
                promedio = suma / len(anios)
                print("El promedio es: ", promedio)

        case 6:
            print("Gracias por usar nuestros servicios. ")
            break

        case _:
            print("Opción no válida. ")

