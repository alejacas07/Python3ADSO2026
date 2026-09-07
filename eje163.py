
estado_civil = input("Ingrese estado civil (s,c): ")
edad = int(input("Ingrese edad: "))
buena_persona = input("Es buena persona? (s,n): ")
linda = input("Es linda? (s,n): ")

if estado_civil == "c":
    print("No me caso! ni me comprometo")
elif (edad <= 30 and linda == "s") or buena_persona == "s":
    print("Si me caso!")
else:
    print("solo me comprometo")