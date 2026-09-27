print ("====CLASIFICACIÓN DE TEMPERATURA====")

temperatura=0
print("="*35)

temperatura= float (input("Ingrese la temeperatura del ambiente:"))
if temperatura>25:
    print("Hace demasiado calor")
elif temperatura>=11:
    print("Temperatura agradable")
else:
    print("Hace resto de frio")



