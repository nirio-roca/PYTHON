print(" -------------  1 ------------  ")

ingreso = float(input("¿Cúanto es su ingreso anual?\n    : "))
if (ingreso < 10000):
    print("5%")
    resultado =ingreso*0.5
elif(ingreso < 20000):
    print("15%")
    resultado = ingreso*0.15
elif (ingreso < 35000):
    print("20%")
    resultado =  ingreso*0.20
elif (ingreso < 60000 ):
    print("30%")
    resultado =ingreso*0.30
else:
    print("45%")
    resultado = (ingreso*0.45)
print("Usted sebe pagar S/",resultado)






print(" -------------  2 ------------  ")
print("""
***** BIENVENDIDOS A BELLA NAPOLI ***** 

    ------------------------------
                MENÚ
    
            0) Salir
            1) Vegetaria
            2) No vegetaria
    ------------------------------""")
opcion = int(input("        Tenemos estas opciones \n\t¿Cùal desea?\n\t\t: "))

if opcion == 0:
    print("\nVuelva pronto ......:D\n")
elif opcion == 1:
    print("""
🍉🍊🍍🍎🍏🍓  VEGETARIA  🍉🍊🍍🍎🍏🍓 

    ------------------------------
                 SUB MENÚ
      Tenemos estos ingredientes:
            0) Regresar al menú
            1) Pimiento
            2) Tofu
    ------------------------------""")  
    subopcion = int(input("\t¿Cúal desea agregar a su pizza?\n\t\t: "))    
    if subopcion == 0:
        print("Regreando al menú...:D")
    elif subopcion == 1:
        print("""

	Perfecto tu pizza vegetaria en camino

	  La Cual tiene como ingrentes: 

                 🍕  Mozzarella
                 🍕  Tomate
                 🍕  Pimiento

                PROVECHO  """)
    elif subopcion == 2:
            print("""

	Perfecto tu pizza vegetaria en camino

	  La Cual tiene como ingrentes: 

                 🍕  Mozzarella
                 🍕  Tomate
                 🍕  Tofu

                PROVECHO  """)
    else:
        print("Esa opción no existe")
elif opcion == 2:
    print("""
🍖🍗🥩🍠🍤🍠  NO VEGETARIA  🍖🍗🥩🍠🍤🍠  

    ------------------------------
                 SUB MENÚ
      Tenemos estos ingredientes:
            0) Regresar al menú
            1) Peperoni
            2) Jamòn
            3) Salmòn
    ------------------------------""")  
    subopcion = int(input("\t¿Cúal desea agregar a su pizza?\n\t\t: "))    
    if subopcion == 0:
        print("Regreando al menú...:D")
    elif subopcion == 1:
        print("""

	Perfecto tu pizza no vegetaria esta en camino

              La Cual tiene como ingrentes: 

                     🍕  Mozzarella
                     🍕  Tomate
                     🍕  Peperoni

                    PROVECHO  """)
    elif subopcion == 2:
        print("""

	Perfecto tu pizza no vegetaria esta en camino

              La Cual tiene como ingrentes: 

                     🍕  Mozzarella
                     🍕  Tomate
                     🍕  Jamòn

                    PROVECHO  """)
    elif subopcion == 3:
                print("""

	Perfecto tu pizza no vegetaria esta en camino

              La Cual tiene como ingrentes: 

                     🍕  Mozzarella
                     🍕  Tomate
                     🍕  Salmòn
                     

                    PROVECHO  """)
    else:
        print("\nEsa opción no existe")                   
else:
     print("\nEsa opción no existe\n")      




print(" -------------  3 ------------  ")

evalucacion = float(input("¿Cúanto de evalucion me daria?\n\t\t\t: "))

if evalucacion == 0.0:
    mensaje = "INACEPTABLE"
    resultado = 0
    print("Su evaluación es ",mensaje," y su recompensa S/",resultado)
elif evalucacion == 0.4:
    mensaje = "ACEPTABLE"
    resultado = evalucacion * 2400
    print("Su evaluación es ",mensaje," y su recompensa S/",resultado)
elif evalucacion >= 0.6:
    mensaje = "MERITORIO"
    resultado = evalucacion * 2400
    print("Su evaluación es ",mensaje," y su recompensa S/",resultado)
else:
    print("No existe la evaluaciòn")








