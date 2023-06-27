
# Solicitar tipo de dulce 
tipo_dulce = input("""
                    
               		     DULCERIA DULCINA S.A 
                '--------------------------------------------------'                     
                |          Tipos        |    Precio Unitario   s/. |     
                |--------------------------------------------------|    
                |    1) Bubbaloo        |         3.00             |  
                |--------------------------------------------------|  
                |    2) Globo Pop       |         4.00             |  
                |--------------------------------------------------|  
                |    3) Sublime         |         5.00             |  
                |--------------------------------------------------|                         
                            ¿Qué tipo de dulce desea?
                                    : """);
# Determinar el tipo y leer la cantidad 
if(tipo_dulce == "1"):
    cantidad = int(input("""
    
                            ¿Cúantos Bubbaloos desea?
                                    : """));
    if(cantidad == 0):
        print("\n             No ingresaste la cantidad de Globo Pop")
    elif(cantidad > 0 and cantidad <=5):
        print("\n           Total apagar por S/.",(cantidad*3)-0.5," con su respectivo descuento de S/0.5 ")

    elif(cantidad > 5 and cantidad >= 10):
        print("\n           Total apagar por S/.", (cantidad * 3) - 0.07, " con su respectivo descuento del %7 ")
    else:
        print("\n           Total apagar por S/.",(cantidad*3)," no cuenta con descuento ")


elif (tipo_dulce == "2"):
    cantidad = int(input("""

                            ¿Cúantos Globo Pop desea?
                                    : """));
    if(cantidad == 0):
        print("\n             No ingresaste la cantidad de Globo Pop")
    elif(cantidad > 0 and cantidad <=7):
        print("\n           Total apagar por S/.",(cantidad*4)," no cuenta con descuento ")

    elif(cantidad > 7):
        print("\n           Total apagar por S/.", (cantidad * 3) - 0.05, " con su respectivo descuento del %5 ")

    else:
        print("\n           Total apagar por S/.",(cantidad*4)," no cuenta con descuento ")

elif (tipo_dulce == "3"):
    cantidad = int(input("""

                            ¿Cúantos Sublimes desea?
                                    : """));
    if(cantidad == 0):
        print("\n             No ingresaste la cantidad de Globo Pop")
    elif(cantidad <= 4):
        print("\n           Total apagar por S/.",(cantidad*5)," no cuenta con descuento ")
    else:
        print("\n           Total apagar por S/.", (cantidad * 5) - 0.15, " con su respectivo descuento del %15 ")

else:
    print("                   \nOpción no valida ")


