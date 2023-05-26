
#Ejercicios

print("   TRIBUTARIO   ")

edad = int(input("Ingrese su edad: "))
ingreso = float(input("¿Cúanto es su ingreso mensual?\n    :"))

if edad >= 18 and ingreso >= 1000:
    print("Usted SI tributa");
else:
    print("Usted NO tributa");

#Ejercicio 2

print("   GRUPO ")

nombre = str(input("Ingrese nombre: "))
print("""Genero:
    M) Masculino
    F) Femenino""")
sexo = (str(input("Ingrese opciòn: "))).upper()

if (sexo == "M" and nombre[0].lower() > "n") or (sexo == "F" and nombre[0].lower() < "m"):
    print("Usted pertenece al GRUPO A")
else:
    print("Usted pertenece al GRUPO B")


#Ejercicio 3
print("   EMPRESA ")

"""
Escribir un programa para una empresa que tiene salas de cine
apto para todas las edades y quiere calcular de forma automática el
precio que debe cobrar a sus clientes por entrar. El programa debe
preguntar al usuario la edad del cliente y mostrar el precio de la entrada.
Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar S/5.00 y si es mayor de 18 años, S/10.00

"""


edad = int(input("Ingrese la edad del cliente: "))

if (edad < 4):
    print("El ingrese es gratuito para usted")
elif (4 <= edad <= 18):
  print("El precio de la entrada es: S/5.00")
else:
   print("El precio de la entrada es: S/10.00")




        
    


