opcion = input("""
         '------------ Calculadora Bàsica ----------'

         |          0) Salir                        |
                    1) Suma
         |          2) Resta                        |
                    3) Multiplicaciòn
         |          4) Divisiòn                     |
                    5) Divisiòn entera
         |          6) Exponente                    |
                    7) Mòdulo o resto
         |------------------------------------------|
               ¿Que operación desea desarrollar?
                  Ingrese la opción: """)

if opcion == "0":
    print("\n         Saliendo de la calculadora.....:D")
elif opcion == "1":
    print(" \n         OPERACIÓN SUMA       \n")
    numero = float(input("Ingrese el primer número: "))
    numero +=float(input("Ingrese el segundo número: "))
    print('El resutado de la operción suma es: ',numero)
elif opcion == "2":
    print(" \n         OPERACIÓN RESTA       \n")
    numero = float(input("Ingrese el primer número: "))
    numero -=float(input("Ingrese el segundo número: "))
    print('El resutado de la operación suma es: ',numero)

elif opcion == "3":
    print(" \n         OPERACIÓN MULTIPLICACIÓN       \n")
    numero = float(input("Ingrese el primer número: "))
    numero *=float(input("Ingrese el segundo número: "))
    print('El resutado de la operación suma es: ',numero)
elif opcion == "4":
    print(" \n       OPERACIÓN DIVISIÓN       \n")
    numero = float(input("Ingrese el primer número: "))
    numero /=float(input("Ingrese el segundo número: "))
    print('El resutado de la operación suma es: ',numero)

elif opcion == "5":
    print(" \n       OPERACIÓN DIVISIÓN EXACTA     \n")
    numero = float(input("Ingrese el primer número: "))
    numero //=float(input("Ingrese el segundo número: "))
    print('El resutado de la operación suma es: ',numero)

elif opcion == "6":
    print(" \n       OPERACIÓN EXPONETE       \n")
    numero = float(input("Ingrese el primer número: "))
    numero **=float(input("Ingrese el segundo número: "))
    print('El resutado de la operación suma es: ',numero)

elif opcion == "7":
    print(" \n       OPERACIÓN MODÚLO       \n")
    numero = float(input("Ingrese el primer número: "))
    numero %=float(input("Ingrese el segundo número: "))
    print('El resutado de la operación suma es: ',numero)
     
else:
    print("\nNo existe esa opción")
