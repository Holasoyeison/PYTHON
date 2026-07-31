print("=====COSTO TOTAL DEL VIAJE=====")

kilometros= float (input("Ingresa los kilometros recorridos:"))
galonPrecio=float(input("Ingresa le valor del galón de gasolina."))
rendimiento= float(input("Cuantos kilometros rinde el coche por galon?"))

costoTotal= (kilometros/rendimiento)*galonPrecio

print ("El costo total del viaje es:", costoTotal, "pesos.")
