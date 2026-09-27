# def kilometroMetros(km):
#     return km*1000
# def metrosCentimetros(m):
#     return m*100
# def kilogramosGramos(kg):
#     return kg*1000
# def celsiusFarenheit(c):
#     return (c*9/5)+32

# while True:
#     print("\n === CONVERSOR ===")
#     print("1. Kilometros a metros.")
#     print("2. Metros a centiumetros.")
#     print("3. Kilogramos a gramos.")
#     print("4. Celsius a Farenheit.")
#     print("5. Salir.")

#     print(f"="*33)

#     opcion= int(input("Selecciona una opción: "))

#     if opcion == 1:
#         km=float(input("INgresa los kilometros: "))
#         resultado = kilometroMetros(km)
#         print(f"="*33)
#         print("Resultado: ",resultado, "mts.")
#     elif opcion == 2:
#         metros=float(input("Ingrese los metros: "))
#         resultado=metrosCentimetros(metros)
#         print(f"="*33)
#         print("Resultado: ",resultado, "cm.")
#     elif opcion==3:
#         kilos=float(input("Ingrese los kilogramos: "))
#         resultado=kilogramosGramos(kilos)
#         print(f"="*33)
#         print("Resultado: ", resultado, "gr.")
#     elif opcion == 4:
#         celsius=float(input("Ingrese los grados celsius: "))
#         resultado=celsiusFarenheit(celsius)
#         print(f"="*33)
#         print("Resultado: ", resultado,"F")
#     elif opcion == 5:
#         print(f"="*32)
#         print("Programa finalizado.")
#         break
#     else:
#         print("Opción no válida.")

#CONVERSO CON MATCH

def kilometroMetro(km):
    return km * 1000
def metrosCentimetros (metros):
    return metros * 100
def kilogramosGramos (kilos):
    return kilos * 1000
def celsiusFarenheit (celsius):
    return (celsius *9/5 )+32

while True:
    print("\n === CONVERSO ===")
    print("1. Kilometros a metros.")
    print("2. Metros a centimetros. ")
    print("3. Kilogramos a gramos. ")
    print("4. Celsiua a farenheit. ")
    print("5. Salir. ")

    opcion= int(input("seleccione una opción: "))

    match opcion:
        case 1:
            km= float(input("Ingrese los kilometros: "))
            resultado= kilometroMetro(km)
            print("Resultado: ", resultado, "mts.")
        case 2:
            metros=float(input("Ingrese los metros: "))
            resultado =metrosCentimetros(metros)
            print("Resultado: ", resultado, "cm.")
        case 3:
            kilos= float(input("Ingrese los kilogramos: "))
            resultado= kilogramosGramos(kilos)
            print("Resultado: ", resultado, "gr.")
        case 4:
            celsius= float(input("Infrese la temperatura en celsius: "))
            resultado = celsiusFarenheit (celsius)
            print("Resultado: ", resultado, "C.")
        case 5: 
            print("Programa finalizado. ")
            break
        case _:
            print("Opción no válida.")