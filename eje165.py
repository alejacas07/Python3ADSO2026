conexion = float(input("Ingrese su conexion Mbps"))
if conexion > 20:
    print("Velocidad de descarga: 10 Mbps")
elif conexion > 5:
    print("Velocidad de descarga: 5 Mbps")
else:
    print("Velocidad de descarga: 1 Mbps")
