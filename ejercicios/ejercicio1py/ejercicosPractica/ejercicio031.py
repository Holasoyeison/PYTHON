print("=== SERIE FIBONACCI ===")

cantidad= int(input("Cantidad de terminos: "))
a = 0
b = 1

for i in range (cantidad):
    print(a, end=(","))

    siguiente = a+ b 

    a = b
    b = siguiente