#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

print("=======BELLA NAPOLI PIZZA=======")
print("="*32)

tipo = int(input("¿Qué tipo de pizza quieres:?\n 1. Vegetariana\n 2. De carnes\n"))
print("="*32)

while tipo !=1 and tipo !=2:
    print ("Opción no válida")
    tipo= int(input("Selecciona 1 o 2: "))
print("="*32)

if tipo==1:
    print ("Elegiste: Vegetariana")
    print("="*32)
    print ("Ingredientes:")
    print ("1. Pimiento.\n2. Tofu.\n")
    ingrediente = int (input("Elige un ingrediente: "))
    print("="*32)
    while ingrediente!=1 and ingrediente!=2:
        print("Opción no válida.")
        ingrediente=int(input("Elige 1 o 2: "))
    if ingrediente==1:
        ingrediente= "Pimiento."
    else:
      
       ingrediente = "Tofu"
    print("Pizza vegetariana.")
    print ("Tus ingreidnetes son:\nmozarella, tomate y",ingrediente)
else:
    
    print("Elegiste pizza de carnes")
    print("="*32)
    print("Ingredientes:\n1. Peperoni.\n2. Jamón.\n3. Slamón.")

    ingrediente=int(input("Elige un ingrediente: "))
    print("="*32)

    while ingrediente != 1 and ingrediente != 2 and ingrediente !=3:
        print ("Opción no válida.")
        ingrediente= int(input("Selecciona 1,2 o 3: "))
    if ingrediente==1:
        ingreidnete= "Peperoni."
    elif ingrediente==2:
        ingrediente="Jamón."
    else:
        ingrediente="Salmón."
    print("="*32)
    print("elegiste pizza de carnes.")
    print("Ingredientes:\nMozaerla, Tomate y", ingrediente)
