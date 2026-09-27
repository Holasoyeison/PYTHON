print("===== TARIFA PARQUEADERO =====")

horas=float(input("Tiempo de parqueo?: "))
fidelización=input("¿Pertenece al grupo de fideliazación?: (S/N)")

if horas<=2:
    total=horas*6000
elif horas >=2 and  horas <=5:
    total=horas * 5500
else: 
    total = horas * 5000

if fidelización == "S":
    total=total* 0.90

if total >= 40000:
    total= total* 0.85
    


print(F"="*33)
print("Valor a pagar: ",total)
print(F"="*33)