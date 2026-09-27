# # while True: 
#     print("\n=== CALCULADORA ===")
#     print("1. Sumar.")
#     print("2. Restar.")
#     print("3. Multiplicar.")
#     print("4. Dividir.")
#     print("5. Salir.")

#     opcion= int(input("Selecciona una opción: "))

#     if opcion ==5:
#         print("Programa finalizado.")
#         break

#     num1=int(input("Ingresa el primer número: "))
#     num2=int(input("Ingresa el segundo númmero: "))

#     if opcion==1: 
#         resultado= num1+num2
#         print(f"="*33)
#         print("El resultado es: ",resultado)

#     if opcion==2:
#         resultado= num1-num2
#         print(f"="*33)
#         print("El resultado es: ",resultado)

#     elif opcion==3:
#         resultado= num1*num2
#         print(f"="*33)
#         print("El resultado es: ",resultado)

#     elif opcion==4:
#         if num2 !=0:
#             resultado = num1/num2
#             print(f"="*33)
#             print("El resultado es: ",resultado)
#         else:
#             print(f"="*33)
#             print("No se puede dividir entre cero.")
#     else:   
#         print(f"="*33)
#         print("Opción no válida.")

def sumar(a,b):
    return a + b

def restar(a , b):
    return a - b 

def multiplicar (a , b):
    return a * b

def dividir (a , b):
    if b != 0:
        return a / b
    else: 
        return "No se puede dividir entre cero."

while True:
    print("\n === CALCULADORA ===")
    print("1. Sumar.")
    print("2. Restar.")
    print("3. Multiplicar.")
    print("4. Dividir.")
    print("5. Salir.")

    opcion= int(input("Selecciona una opción: "))

    if opcion == 1:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("El resultado es: ", sumar(a,b))
    elif opcion == 2:
        a = float (input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("El resultado es: ", restar(a,b))
    elif opcion == 3:
            a = float (input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print("El resultado es: ", multiplicar(a,b))
    elif opcion == 4:
            a = float (input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print("El resultado es: ", dividir(a,b))
    elif opcion == 5:
         print("Programa terminado.")
         break
    else:
         print("Opción no válida.")