nombres=[]
tiempos=[]

while True:
    print("\n=== MENÚ OPCIONES ===")
    print("1. Registrar deportista. ")
    print("2. Mostrar deportistas. ")
    print("3. Buscar deportista. ")
    print("4. Mostra rmejor tiempo. ")
    print("5. Mostrar tiempo promedio. ")
    print("6. Salir. ")

    opcion=int(input("Selecciona una opción: "))

    match opcion:
        case 1: 
            print("\n=== Registrar deportista ===")
            nombre= input("Ingresa el nombre del deportista: ")
            nombres.append(nombre)
            tiempo=float(input("Ingresa el tiempo obtenido: "))
            tiempos.append(tiempo)
            print("Registro exitoso!")

        case 2:
            print("\n=== Mostrar deportistas ===")
            if len(nombres) ==0:
                print("No hay registro de ateltas.")
            else:
                for i in range(len(nombres)):
                    print("Nombre:", nombres[i], "tiempo:", tiempos[i], "seg")

        case 3:
            print("\n=== Buscar deportista ===")
            if len(nombres)==0:
                print("No hay ateltas registrados.")
            else:
                buscado=input("Ingresa el nombre dle deportista: ")
                encontrado = False

                for i in range(len(nombres)):
                    if nombres[i] == buscado:
                        print("Deportista encontrado: " +nombres[i]+ "Tiepo: "+str(tiempos[i]+ "seg. "))

                        encontrado= True
                if encontrado == False:
                    print("deportista no encontrado. ")

        case 4:
            print("\n=== Mejor posición ===")
            if len (nombres) == 0:
                print("No hay deportistas registrados. ")
            else:
                tiempoMenor = tiempos[0]
                mejorPosicion = 0

                for i in range(len(tiempos)):
                    if tiempos[i] < tiempoMenor:
                        tiempoMenor = tiempos[i]
                        mejorPosicion = i

                print("El mejor tiempo es de: " +nombres[mejorPosicion]+ "con" +str(tiempoMenor)+ "seg.")

        case 5:
            print("\n=== Tiempo promedio ===")
            if len(nombres) == 0:
                print("No hay deportistas registrados. ")
            else: 
                sumaTiempos=0
                for i in tiempos:
                    sumaTiempos = sumaTiempos + i 

                promedio = sumaTiempos/len(tiempos)
                print("El tiempo promedio es: " +str(promedio)+"seg. ")

        case 6:
            print("Gracias pos usas nuestros servicios!")
            break
        case _:
            print("\nOpción no válida. ")

