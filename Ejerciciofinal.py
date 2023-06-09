
print("""
-------- LA COMPAÑIA MULTINACIONAL  --------
                   RAPPI
                
                BIENVENIDO
                   """)
# Solicitar nombre del trabajador
nombre = input("Ingrese el nombre del trabajador: ")

# Solicitar clave del departamento
clave_departamento = int(input("""
--------         DEPARTAMENTOS         --------
            1: Atención al cliente
            2: Logística 
            3: Gerencia
    Ingrese la clave del departamento 
                : """))

# Solicitar antigüedad del trabajador
antiguedad = float(input("Ingrese la antigüedad del trabajador en años: "))

# Determinar los días de vacaciones según la clave del departamento y la antigüedad
if clave_departamento == 1:
    if antiguedad < 1:
        dias_vacaciones = 6
    else:
        if antiguedad >= 1:
            dias_vacaciones = 8
elif clave_departamento == 2:
    if antiguedad < 1:
        dias_vacaciones = 7
    elif antiguedad <= 5:
        dias_vacaciones = 10
    else:
        dias_vacaciones = 15
elif clave_departamento == 3:
    if antiguedad < 1:
        dias_vacaciones = 10
    elif antiguedad <= 5:
        dias_vacaciones = 15
    else:
        dias_vacaciones = 20
else:
    print("Clave de departamento inválida")
    exit()

# Mostrar el nombre del trabajador y los días de vacaciones correspondientes
print(f"El trabajador {nombre} tiene derecho a {dias_vacaciones} días de vacaciones.")
