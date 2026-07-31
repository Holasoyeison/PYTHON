print("======SALARIO NETO======")

horasTrabajadas = input("Ingrese el número de horas trabajadas: ")
valorHora = input("Ingrese el valor de la hora trabajada")

salarioBruto = float(horasTrabajadas) * float(valorHora)
descuento = salarioBruto * 0.12
salarioNeto = salarioBruto - descuento

print ("El salario bruto es: ", salarioBruto)
print ("El descuento es: ", descuento)
print ("El salario neto es: ", salarioNeto)

