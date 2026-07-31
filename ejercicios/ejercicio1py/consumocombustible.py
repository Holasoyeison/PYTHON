print ("===== CONSUMO DE COMBUSTIBLE=====")

kilometroRecorridos = float (input( "Ingrese la distancia recorrida: "))
litrosConsumo = float (input ("Ingresa los litros consumidos: "))

consumo = litrosConsumo / kilometroRecorridos
#consumoTotal = kilometroRecorridos * consumo

print ("El consumo del combustibles litro por kilómetro es: ", consumo,  "l/Km")