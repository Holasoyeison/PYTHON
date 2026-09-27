print("=== CLASIFICACIÓN POR EDAD ===")

edad= int(input("Ingresa la edad: "))

if edad <=12:
    print("Clasificación: Niño.")
elif edad<=17:
    print("Clasificaicón: Adolecencia. ")
elif edad<=59:
    print("Clasificación: Adulto.")
else: 
    print("Clasificación: Adulto mayor. ")