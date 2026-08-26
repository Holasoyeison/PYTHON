print("=== CALCULO DE UN SALARIO DE UN EMPLEADO ===")

nombreEmpleado=input("Ingrese el nombre del empleado: ")
horasTrabajadas=float(input("Ingrese las horas trbajadas: "))
valorhora=25000

salarioTotal= valorhora*horasTrabajadas

print("Nombre del empleado: ",nombreEmpleado)
print("Horas trabajadas: ",horasTrabajadas)
print("El valor de la hora de trabajo es: ", valorhora)
print("El pago total al empleado es: ",salarioTotal)