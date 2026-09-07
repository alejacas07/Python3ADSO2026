valor_matricula= float(input("Ingrese valor de la matrcula: "))
Extracto= int(input("Ingrese estracto(1/2): "))
Edad= int(input("Ingrese edad: "))

if extracto == 1 and edad < 18:
    pagar=valor_matricula*0,20
if extracto == 1  and edad >= 18:
    pagar=valor_matricula*0,15
if extracto == 2 and edad <18:
    pagar=valor_matricula*0,10
if extracto == 2 and edad >= 18:
     pagar=valor_matricula*0,5   

    
