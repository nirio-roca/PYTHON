

opcion =input("""
      .------------------------------------.
      |          Menú de Áreas             |
      |                                    |
      |         1) Círculo                 |
      |         2) Triángulo equilátero    |
      '------------------------------------'
            Eliga una opción: """)

if opcion == "1":

    print(" -------- Calculando el Area de un Círculo -------- ")

    r = float (input("Ingrese el radio del circulo: "))

    if (r <= 0) :
        print(" radio del círculo no válida")
    else:
        pi = 13.1416

        AreaCirulo = pi*(r**2)

        print("Area del círculo es: ",round(AreaCirulo,2))
      

    
elif opcion  == "2":

    print(" -------- Calculando el Area de un Triángulo Equilátero -------- ")

    lado = float (input("Ingrese la base del triángulo equilátero : "))
    if (lado <= 0) :
        print(" radio del círculo no válida")
    else:
        AreatrianguloE = ((3**0.5) *(lado**2)) /2;
        print("Area del triángulo equilátero es: ",round(AreatrianguloE,2))

else:
    print("Opcion no valida")


print("\n\n\n")


d = float(input("Ingrese la distancia que los separa (m): "))

    
v1 = float(input("Ingrese la velociadad del auto 1 (m/s): "))


v2 = float(input("Ingrese la velociadad del auto 2 (m/s): "))


t =  d / ( v1 + v2);

print("El tiempo de encuentro es ", round(t,2)," m/s ")




print("\n\n\n")


print("  🗓📆🗓📆📆   Ingrese fecha  🗓📆🗓📆📆  ")


dia = int(input("Ingrese el dia (dd): "))

mes = int(input("Ingrese el mes (mm): "))


ano = int(input("Ingrese el año (aaaa): "))


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













