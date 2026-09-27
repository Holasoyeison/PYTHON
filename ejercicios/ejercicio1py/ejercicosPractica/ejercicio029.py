print("=== CONTAR VOCALES ===")

txt = input("Ingresa la palabra: ")

vocales = 0

for letra in txt:
    if letra in "aeiouAEIOU":
        vocales= vocales + 1
print("La palabra contiene ",vocales, "vocales.")