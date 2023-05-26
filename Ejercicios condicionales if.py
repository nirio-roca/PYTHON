

flag  = True
while flag:
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
        subflag = True
        while subflag:
            print("""
🍉🍊🍍🍎🍏🍓  VEGETARIA  🍉🍊🍍🍎🍏🍓 

    ------------------------------
                 SUB MENÚ
      Tenemos estos ingredientes:
            0) Regresar al menú
            1) Vegetaria
            2) No vegetaria
    ------------------------------""")
            subopcion = int(input("\t¿Cúal desea agregar a su pizza?\n\t\t: "))
            if subopcion == 0:
                print("Regreando al menú...:D")
                subflag = False
                flag  = False
            elif subopcion == 1:
                print("Perfecto tu pizza vegetaria en camino")
                subflag = False
                flag  = False
            elif subopcion == 2:
                print("Perfecto tu pizza vegetaria en camino")
                subflag = False
                flag  = False
            elif subopcion == 3:
                print("Perfecto tu pizza vegetaria en camino")
                subflag = False
                flag  = False
            else:
                print("Esa opción no existe")
    elif opcion == 2:
        subflag = True
        while subflag:
            print("""
🍖🍗🥩🍠🍤🍠  NO VEGETARIA  🍖🍗🥩🍠🍤🍠  

    ------------------------------
                 SUB MENÚ
      Tenemos estos ingredientes:
            0) Regresar al menú
            1) Vegetaria
            2) No vegetaria
    ------------------------------""")  
        subopcion = int(input("\t¿Cúal desea agregar a su pizza?\n\t\t: "))
        if subopcion == 0:
            print("Regreando al menú...:D")
            subflag = False
        elif subopcion == 1:
            print("\nPerfecto tu pizza vegetaria en camino")
            subflag = False
            flag  = False
        elif subopcion == 2:
            print("\nPerfecto tu pizza vegetaria en camino")
            subflag = False
            flag  = False
        elif subopcion == 3:
            print("\nPerfecto tu pizza vegetaria en camino")
            subflag = False
            flag  = False
        else:
            print("\nEsa opción no existe")
    else:
        print("\nEsa opción no existe\n")












