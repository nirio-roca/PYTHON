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

if opcion == "a":
    print("     Usted ha votado por el ¡PARTIDO ROJO! ✔");
elif opcion == "b":
    print("     Usted ha votado por el ¡PARTIDO VERDE! ✔");
elif opcion == "c":
    print("     Usted ha votado por el ¡PARTIDO AZUL! ✔");
else:
    print("             “Opción errónea”                ");













