"""
Hacer un algoritmo, que dada una fecha del año 2000
(representada por el día, el mes y el año en formato numérico
dd/mm/aaaa), calcule el día siguiente. Asuma que el mes tiene 30
días.

"""
print("     Ingrese fecha   ")

## Bucle para que ingre un dia correcto
dia = int(input("Ingrese el dia (dd): "))
while not(0 < dia < 31):
    print(" Día no es válido")
    dia = int(input("Ingrese el dia: "))



mes = int(input("Ingrese el mes (mm): "))
## Bucle para que ingre un mes correcto
while not( ( 0 < len(str(mes)) < 3) and ( 0 < mes < 13) ):
    print(" Mes no es válido")
    mes = int(input("Ingrese el mes: "))


## Bucle para que ingre un año correcto
ano = int(input("Ingrese el año (aaaa): "))
while not(len(str(ano)) == 4):
    print(" Año no es válido")
    ano = int(input("Ingrese el año: "))



            #validar mes


if dia == 30:
    dia = 1
    if (mes == 12):
        mes = 1
        ano +=1
    else:
        mes += 1
else:
     dia +=1


if len(str(mes)) == 1 and len(str(dia)) == 1 :
   print("\nEl dia siguente es: 0",dia, "/","0",mes, "/", ano)
elif(len(str(mes)) == 1 ):
    print("\nEl dia siguente es: ",dia, "/0", mes, "/", ano)
elif(len(str(dia)) == 1):
    print("\nEl dia siguente es: 0",dia, "/",mes, "/", ano)
else:
    print("\nEl dia siguente es: ",dia, "/", mes, "/", ano)



"""
"""


nombreprod = input("""
                  MARCAS 

                0) Ninguna
                1) Jbil
                2) Huea
                3) Xio
                4) Nosy
        Ingrese la marca del producto: """);

print(" ")
costo  = float(input("Ingrese el costo del producto: "))
if costo >= 2000:
    if nombreprod == "Nosy":
        resultado = costo - (costo*0.15)
        resultado = resultado + (resultado*0.2)
    else:
         resultado = costo - (costo*0.1)
         resultado = resultado + (resultado*0.2)
else:
    if nombreprod == "Nosy":
        resultado = costo - (costo*0.05)
        resultado = resultado + (resultado*0.2)
    else:
        resultado = costo + (costo*0.2)
print("El coste a pagar es de:",resultado)
