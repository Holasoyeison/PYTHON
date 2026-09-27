print ("=======Calculo total de una copra con iva=======")

precio = float (input("Ingrese el precio del producto:"))
iva = float (input("Ingresa el vlaor del iva %:"))

valorIva = precio * (iva/100)
total = precio + valorIva

print ("---RESULTADO---")
print(" El pprecio del producto es: $", precio)
print("El iva es:", iva, "%")
print("el valor del iva es:", valorIva)
print("Precio total a pagar es: $", total)
