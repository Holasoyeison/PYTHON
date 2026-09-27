print("===== MAXIMA Y MINIMA TEMPERATURA =====")

temperaturas=[18, 25, 12, 30, 21, 15, 28]
min=max=temperaturas[0]

for temperatura in temperaturas:
    if temperatura < min:
        min=temperatura
    elif temperatura> max:
        max=temperatura

print(" La temperatura mas baja es : ", min)
print("La temperatura mas alta es: " ,max)