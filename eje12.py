import math 

entrada = input("ingresa el radio del circulo: ")

if entrada.replace('.', '', 1).replace('-', '', 1).isdigit():
    radio = float(entrada)

    if radio >= 0:
        area = math.pi * radio**2 
        print(f"El area del circulo es: {area:.2f}")
    else: 
        print("Error: el radio no puede ser negativo.")
else:
    print("Error: debes ingresar un numero valido.")
