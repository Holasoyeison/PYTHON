print ("=====PAGO DE HORAS EXTRAS=====")

horas= float(input("Ingrese la horas trabajdas: "))
valorhora=float(input("Ingrese le valor de la hora de trabajo: "))

if horas>40:
    horasExtras= horas-40
    pagoNormal= 40*valorhora
    pagoExtra= horasExtras*(valorhora*2)
    pagoTotal= pagoNormal+pagoExtra
else:
    pagoTotal= horas*valorhora

print("El pago total es:", pagoTotal,"pesos.")
