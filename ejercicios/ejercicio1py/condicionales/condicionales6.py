#Los tramos impositivos para la declaración de la renta en un determinado país.

print("======IMPUESTOS TRIBUTARIOS======")

renta = float(input("¿Cual es tu renta anual?"))

if renta <10000:
    impuesto = renta*0.05
elif renta<=20000:
    impuesto=renta* 0.15
elif renta <=35000:
    impuesto=renta*0.20
elif renta <= 60000:
    impuesto= renta*0.30
else: 
    impuesto = renta*0.45

print("El impuesto que debes de pagar es de : ", impuesto, "euros.")