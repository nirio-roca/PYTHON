#WHILE INTERES COMPUESTO



#Interes compuesto

C = 0;
I = 0;
M = 0;

while (C<=0) or (I<=0) or (I >= 100) or (M<=0):
    C = float(input("Ingrese capital: "))
    I = int(input("Ingrese interes: "))
    M = int(input("Ingrese tiempo en años: "))


CT = C*(1+(I/100))**M;

print(f"""
Capital: {C}
Interes: {I}
Tiempo (año): {M}
Monto Total: {CT}""");
