print("===LISTA D EPRODUCTOS===")

productos=[]

cantidad=int(input("Cantidad de productos: "))

for i in range(cantidad):
    
    producto=input("Ingrese el nombre del producto: ")
    productos.append(producto)
    

print(f"="*33)
print("\n===Lista de compras===")
print(f"="*33)

for i in range(len(productos)):
    
    print(str(i + 1) +"." + productos[i])