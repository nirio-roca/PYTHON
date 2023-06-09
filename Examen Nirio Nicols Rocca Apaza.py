"""
1.	Crear un programa que permita al usuario
elegir un candidato por el cual votar.
Las posibilidades son: candidato A por
el partido rojo, candidato B por el
partido verde, candidato C por el
partido azul. Según el candidato
elegido (A, B ó C) se le debe imprimir
el mensaje “Usted ha votado por el partido
[color que corresponda al candidato elegido]”.
Si el usuario ingresa una opción que no
corresponde a ninguno de los candidatos
disponibles, indicar “Opción errónea”.

"""

#Definimos la varible opcion para guardar el valor ingresado

opcion=input("""
    ---------------------------------
        |       CANDIDATOS       | 
        |                        |
        |   A) Partido rojo      |
        |   B) Partido verde     |
        |   C) Partido azul      |
        |                        |
      ✔✔  ¿Por cual desea votar? ✔✔
                -> """).lower();

#comparamos si opcion es == a 
if opcion == "a":
    #Si es a imprime esta linea 
    print("\n     Usted ha votado por el ¡PARTIDO ROJO! ✔");
#comparamos si opcion es == b
elif opcion == "b":
    #Si es a imprime esta linea 
    print("\n     Usted ha votado por el ¡PARTIDO VERDE! ✔");
#comparamos si opcion es == c 
elif opcion == "c":
    #Si es a imprime esta linea 
    print("\n     Usted ha votado por el ¡PARTIDO AZUL! ✔");
#Sino es igual a ninguna de las anteriores imprime esta linea
else:
    print("\n ❌❌❌❌    “Opción errónea”    ❌❌❌❌");













