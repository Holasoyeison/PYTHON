print("===== EDADES MAYOR Y MENOR =====")

edades =[15, 22, 18, 35, 12, 27, 41]
min=max=edades[0]

for edad in edades:
    if edad <min:
        min =edad
    elif edad>max:
        max=edad

print("La eda dminima es: ", min)
print("La edad maxima es: ", max)
