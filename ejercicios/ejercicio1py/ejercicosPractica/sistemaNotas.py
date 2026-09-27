# notas=[]

# def registrarNota():
#     nota=float(input("Ingrese la nota: "))
#     notas.append(nota)
#     print("Nota registrada.")
# def mostrarPromedio():
#     if len(notas)== 0:
#         print("No hay notas registradas.")
#     else:
#         Suma = 0

#         for nota in notas: 
#             suma = suma + nota

#         promedio = suma / len(notas)
      
# def verificarAprobacion():
#     if len(notas)==0:
#         print("No hay notas registradas.")
#     else: 
#         suma = 0
#         for nota in notas: 
#             suma = suma + nota
#             promedio = suma / len(notas)

#         if promedio >=3:
#             print("El estudiante aprobó.")
#         else:
#             print("El estudiante n o aprobó. ")
        
# while True:
#     print("\n === SISTEMA DE NOTAS ===")
#     print("1. Registrar nota.")
#     print("2. Mostrar promedio.")
#     print("3. Saber si aprueba.")
#     print("4. Salir.")

#     opcion= int(input("Selecciona una opción: "))

#     if opcion == 1:
#         registrarNota()
#     elif opcion == 2:
#         mostrarPromedio()
#     elif opcion == 3:
#         verificarAprobacion()
#     elif opcion==4:
#         print("Programa finalizado.")
#     else: 
#         print("Opción no válida.")


#SISTEMA DE NOTAS CON MATCH

# notas=[]

# def registrarNotas():
#     cantidad= int(input("Cuantas notas deseas registrar?: "))

#     for i in range (cantidad):
#         nota=float(input("Ingresa la nota: "+str(i+1) + ":"))
#         notas.append(nota)
#     print("Notas registradas correctamente.")

# def mostrarPromedio():
#     if len(notas)==0:
#         print("No hay notas registradas.")
#     else: 
#         suma = 0

#         for nota in notas: 
#             suma = suma + nota
#         promedio = suma / len(notas)
#         print("El promedio es: ", promedio)

# def verificarAprobado():
#     if len(notas)==0:
#         print("No hay notas registradas.")
#     else:
#         suma = 0
#         for nota  in notas: 
#             suma = suma + nota
#         promedio = suma / len(notas)

#         if promedio >=3.0:
#             print("El estudiante aprueba.")
#         else:
#             print("El estudiante no aprueba.")
# while True:
#     print("\n === SISTEMA DE NOTAS ===")
#     print("1. Registrar notas.")
#     print("2. Mostrar promedio.")
#     print("3. saber si aprueba. ")
#     print("4. Salir. ")

#     opcion= input("Selecciona una opción: ")
#     match opcion:
#         case "1":
#             registrarNotas()
#         case "2":
#             mostrarPromedio()
#         case "3":
#             verificarAprobado()
#         case "4":
#             print("Programa finalizado.")
#             break
#         case _:
#             print("Opción no válida.")


# def registrarNotas ():
#     notas =[]

#     cantidad= int(input("¿Cuantas notas desea registrar?: "))
#     for i in range (cantidad):
#         nota=float(input("Ingresa la nota: "))
#         notas.append(nota)

#     return notas

# def analizarNotas(notas):
#     suma = 0
#     aprobadas = 0
#     perdidas = 0

#     for nota in notas:
#         suma = suma + nota

#         if nota >=3.0:
#             aprobadas = aprobadas + 1
#         else: 
#             perdidas = perdidas + 1 

#     promedio = suma / len(notas)

# print("\n Notas: ", notas)
# print("Nota mas alta: ", max(notas))
# print("nota mas baja: ", min(notas))
# print("Promedio: ", promedio)
# print("Notas aprobadas: ", aprobadas)
# print("Notas perdidas: ",perdidas)

# while True:
#     notas = registrarNotas()
#     analizarNotas (notas)

#     continuar = input("\n Desea registrar mas notas? S/N: ")
#     if continuar == "N" or continuar == "n":
#         break

# def regitrarProductos():
#     productos =[]
#     totales = []

#     cantidad = int(input("¿Cuantos productos desea registrar?: "))

#     for i in range (cantidad):
#         nombreProducto= input("Nombre del producto: ")
#         precio= float(input("Precio del producto: "))
#         cantidadProducto= int(input("Cantidad: "))

#         total = precio + cantidadProducto
#         productos.append(nombreProducto)
#         totales.append(total)
#         return productos, totales

#     def calcularCompra (totales):
#         totalCompra=0

#         for total in totales:
#             totalCompra = totalCompra + total

#         if totalCompra >=100000:
#             descuento=totalCompra * 0,10
#             totalCompra = totalCompra - descuento
#             return totalCompra

# productos, totales = regitrarProductos()
# total= calcularCompra(totales)
# print("\n Productos.")

# for i in range(len(productos)):
#     print(Productos [i] ,"=", totales [i] )

# print("\n Total compra: ", total)
# posicion = totales.index(max(totales))

# print("Producto con mayor precio: ",productos[posicion])

def sumar(numeros):
    resultado = 0
    for numero in numeros: 
        resultado = resultado + numero
    return resultado

def restar(numeros):
    resultado = numeros[0]
    for i in range (1, len (numeros)):
        resultado = resultado - numeros[i]
    return resultado

def multiplicar(numeros):
    resultado = 1
    for numero in numeros:
        resultado = resultado * numero
    return resultado

def dividir(numeros):
    resultado = numeros[0]
    for i in range(1, len(numeros)):
        if numeros[1] == 0:
            return "no se puede dividir entre cero."
        resultado = resultado / numeros[i]
        return resultado
numeros = []

while True:
    
    print("\n === MENÚ ===")
    print("1. Registrar números.")
    print("2. sumar.")
    print("3. Restar.")
    print("4. Multiplicar.")
    print("5. Dividir.")
    print("6. Mostrar números.")
    print("7. Salir.")

    opcion = int(input("Selecciona una opción: "))

    match opcion:
        case 1:
            cantidad = int(input("¿cuantos números desea registrar?: "))
            numeros =[]
            for i in range (cantidad):
                numero=float(input("Ingrese los números: "))
                numeros.append(numero)
            print("Números registrados correctamente!" )

        case 2:
            if len(numeros)>0:
                print("El resultado final es: ", sumar(numeros))
            else:
                print("Primero debes registrar números." )

        case 3:
            if len (numeros)>0:
                print("El resultado es: ", restar(numeros))
            else:
                print("Primero debes registrar números." )

        case 4:
            if len(numeros)>0:
                print("El resultado es: ", multiplicar(numeros))
            else:
                print("Primero debes registrar números. ")

        case 5:
            if len (numeros)>0:
                print("El reusltado es: ", dividir(numeros))
            else:
                print("Primero debe registrar números.")

        case 6:
            print("Números registrados: ", numeros)

        case 7:
            print("Programa finalizado.")
            break
        case _:
            print("Opción no válida.")