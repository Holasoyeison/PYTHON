#Escribir un programa que pregunte al usuario cuántos productos quiere ingresar.Para cada producto, debe pedir:El nombre del producto.El precio del producto. Los nombres deben almacenarse en una lista y los precios en otra.

print ("===== PRODUCTOS Y PRECIOS=====")

productos =[]
precios=[]

cantidad= int(input(" ¿Cuantos productos vas a ingresar?. "))

for  i in range (cantidad):
    producto = input("ingresa el nombre del producto: " )
    productos.append(producto)

print(f"="*31)
for producto in productos:
    precio=float(input("¿Cual es el precio de " +producto+ "?"))
    precios.append(precio)

print(f"="*31)
for i in range(len (productos)):
    print("El producto", productos[i], "cuesta $: " ,precios[i])

promedio = sum(precios)/len(precios)

print(f"="*31)
print("el promedio d ela compra es: " , promedio)
