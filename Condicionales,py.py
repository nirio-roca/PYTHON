#CONDICIONALES 
print("PROMEDIO DE NOTAS")

Nombre = str(input("Ingrese su nombre: "))

Fisica=float(input("Ingrese nota de Física: "))
Alge=float(input("Ingrese nota de Álgebra: "))
Quimica=float(input("Ingrese nota de Quimica: "))

promedio = int((Fisica + Alge + Quimica)//3);
"""
if promedio >= 13 :
    print("Felicidaes APROBASTE con un promedio de ",promedio," :D");
print("Ala próxima sera :(");   """

#CONDICIONALES COMPUESTAS
# Para redondear segun a la decimales se usa round("varibale",2)
if promedio >= 13 :
    print("\n",Nombre,"Felicidaes APROBASTE con un promedio de ",promedio," :D");
else:
    print("\n",Nombre,"DESAPROBASTE > Ala próxima sera :(");
print("\n    Fin del programa")    
