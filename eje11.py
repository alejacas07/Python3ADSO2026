not1 = float(input("INGRESE NOTA 1: "))
not2 = float(input("INGRESE NOTA 2: "))

if not1 >= 2.5 and not2 >= 2.5:
    if not1 <= 5 and not2 <= 5:
        prom = (not1 + not2) / 2
        if prom >= 3.0:
            print("EL APRENDIZ APRUEBA CON: ", prom)
        else:
            print("EL APRENDIZ NO APRUEBA, SU NOTA ES: ", prom)
    else:
        print("SOLO SE ADMITEN NOTAS MENORES O IGUALES A 5.0")
else:
    print("SOLO SE ADMITEN NOTAS MAYORES O IGUALES A 2.5")
    


