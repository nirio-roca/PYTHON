


evalucacion = float(input("¿Cúanto de evalucion me daria?\n\t\t\t: "))

if evalucacion >= 0.0 and evalucacion < 0.4:
    mensaje = "INACEPTABLE"
    resultado = evalucacion * 2400
elif evalucacion >= 0.4 and evalucacion < 0.6:
    mensaje = "ACEPTABLE"
    resultado = evalucacion * 2400
else:
    mensaje = "MERITORIO"
    resultado = evalucacion * 2400
print("Su evaluación es ",mensaje," y su recompensa S/",resultado)