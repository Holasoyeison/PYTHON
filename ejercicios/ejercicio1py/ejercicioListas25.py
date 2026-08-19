print("===== PRODUCTO A ESCALAR =====")

vector1=[1,2,3]
vector2=[-1,0,2]

producto=0

for i in range (len(vector1)):
    producto=producto+vector1[i]*vector2[i]

print("El producto a escalar es: ",producto)