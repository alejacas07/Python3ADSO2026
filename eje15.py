numero = int(input("Ingrese el número de la tabla: "))
valor_inicial = int(input("Ingrese el valor inicial: "))

print("Tabla de multiplicar:")

for i in range(valor_inicial, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
