

opcion = int(input("""
                              Menù

        Presione 1 para convertir de numero a palabra
        Presione 2 para convertir de numero a palabra
                ¿Cùal es la opciòn deseada?
                        : """))
if opcion == 1:
    num = int(input("""
        --------  Convertir de numero a palabra  --------

                  Ingrese el nùmero a convertir: """))
    if num == 0:
        text = "El nùmero es cero"    
    elif num == 1:
        text = "El nùmero es uno"
    elif num == 2:
        text = "El nùmero es dos"
    elif num == 3:
        text = "El nùmero es tres"
    elif num == 4:
        text = "El nùmero es cuatro"
    elif num == 5:
        text = "El nùmero es cinco"
    elif num == 6:
        text = "El nùmero es seis"
    elif num == 7:
        text = "El nùmero es siete" 
    elif num == 8:
        text = "El nùmero es ocho"
    elif num == 9:
        text = "El nùmero es nueve"
    else:
        text = "El nùmero no esta registrado "
    print(text)     
elif opcion == 2:
    txt = input("""
        --------  Convertir de numero a palabra  --------

                  Ingrese el nùmero a convertir: """).lower()
    if txt == "cero":
        num = "0"    
    elif txt == "uno":
        text = "1"
    elif txt == "dos":
        num = "2"
    elif txt == "tres":
        num = "3"
    elif txt == "cuatro":
        num = "4"
    elif txt == "cinco":
        num = "5"
    elif txt == "seis":
        num = "6"
    elif txt == "siete":
        num = "7" 
    elif txt == "ocho":
        num = "8"
    elif txt == "nueve":
        num = "9"
    else:
        text = "El nùmero no esta registrado "
    print(text) 
else:
    print("Opcion no esta registrado ")

    
