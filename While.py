

print("\n EJERCIO DE COMPUESTO")
#capital
c = 0
while c <= 0 or c > 100:
    c = int(input("Ingrese su capital: "))
    continue
#interes
I = 0
while I <= 0 or I > 100:
    I = int(input("¿Cúanto es el interes?   "))
#años 
A =  int(input("¿Cúanto tiempo desea invertir?  "))
#Monto

M = 0.0;




M = c*(1+(I/100))**A;
print(f"""
Capital: {c}
Interes: {I}
Tiempo(año): {A} 
Monto total: """,int(M))






















print(" BREAK AND CONTINUE")



#break = romper
print("\nwhile con la sentencia break")
contador = 0;
while contador < 10:
    contador +=1;
    if contador == 5:
        print("Before del break")
        break
        print("After del break")
    print(f"Valor de contador: {contador}")
# continue = continue 
print("\nwhile con la sentencia continue")

count = 0;

while count < 10:
    count += 1;
    if count == 5: #omite es ta line de codigo 
        print("hola before del continue")
        continue
        print("hola after del continue")
    print(f"Valor de contador: {count}")
    









print("\n EJERCIO DE COMPUESTO")
#capital
c = 0
while c <= 0 or c > 100:
    c = int(input("Ingrese su capital: "))
    continue
#interes
I = 0
while I <= 0 or I > 100:
    I = int(input("¿Cúanto es el interes?   "))
#años 
A =  int(input("¿Cúanto tiempo desea invertir?  "))
#Monto
M = 0.0;




M = c*(1+(I/100))**A;
print(f"""
Capital: {c}
Interes: {I}
Tiempo(año): {A} 
Monto total: """,int(M))



print("\n EJERCIO DE FIVONACI \n")





x=0
valor=1
while(valor <= 1597):
    print(x,valor,end=" ")
    x +=valor
    valor += x


