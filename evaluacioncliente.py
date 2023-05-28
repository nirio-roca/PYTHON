


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
