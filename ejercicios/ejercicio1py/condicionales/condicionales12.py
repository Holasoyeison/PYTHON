#Ejercicio: Calculadora de salario Escribir un programa que pregunte al usuario cuántas horas trabajó en la semana y cuánto gana por hora. El programa debe calcular su salario

print("======CALCULADORA DE SALARIO======")

horas=float(input("¿Cuantas horas trabajaste?: "))
valorHora=float(input("¿Cuanto ganas por hora?: "))

if horas <=40:
    salarioNormal= horas*valorHora
    salarioTotal= salarioNormal
else:
    salarioNormal=40*valorHora
    horasExtras=horas-40
    salarioExtra=horasExtras*valorHora*2
    salarioTotal=salarioNormal+salarioExtra

print("="*32)

print("Horas trabajadas: ",horas)
print("Salario normal: ", salarioNormal, "Euros.")
print("Su salario total es: ", salarioTotal, "Euros.")