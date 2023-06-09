print("Conjunciòn (and)")
num = int(input("\nIngrese un nùmero mayor a 2 y menor a 5: "))

if (num > 2 and num < 5):
    print("El nùmero ",num," cumple con la condiciòn")
else:
    print("El nùmero ",num," No cumple con la condiciòn")


print("\nDisyunciòn (or)")
text = input("\nPara cumplir con la condiciòn escribe 'si' o 'yes' ").lower()

if (text == "si" or text == "yes"):
    print("El nùmero ",text," cumple con la condiciòn")
else:
    print("El nùmero ",text," No cumple con la condiciòn")

print("\nNegaciòn (not)")
num = int(input("\nIngrese un nùmero que es igual 5: "))

if not(num == 5):
    print("El nùmero ",num," cumple con la condiciòn")
else:
    print("El nùmero ",num," No cumple con la condiciòn")
