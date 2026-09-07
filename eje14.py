print("Ingrese el numero de la tabla de multiplicar:")
multp = int(input())

print("Ingrese rango final:")
rango = int(input())

print("Ingrese rango inicial:")
i = int(input())

if i >= rango:
    print("El rango final no puede ser mayor que el rango inicial")
else:
    while i <= rango:
        res = multp * i
        print(multp, "x", i, "=", res)
        i = i + 1
while i <= valor_final:
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    i = i + 1
    