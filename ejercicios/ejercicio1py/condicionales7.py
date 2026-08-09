#En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

print ("EVALUACIÓN FINAL DE EMPLEADOS")

print ("="*22)
puntuacion = float(input("Ingresa tu puntuación: "))
print ("="*22)

if  puntuacion== 0.0:
    nivel= "Inaceptable."
elif puntuacion== 0.4:
    nivel= "Aceptable."
elif puntuacion ==0.6:
    nivel ="Meritorio."
else:
    nivel = "Puntuación no válida. "


dinero = 2400*puntuacion

print ("="*22)

print ("Nivel de rendimiento: ", nivel)
print("dinero recibido: ", dinero, "Euros.")