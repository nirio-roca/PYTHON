
#------------------------------------------------------------------------------

String = input("Introduce una cadena: ")
String  =" sdf "

print("¿Todas las letras estan en minusculas:",String.islower())

String = String.lower()

print("Cade en minusculas: ",String)

#------------------------------------------------------------------------------

String = input("Introduce una cadena: ")
String  =" sdf "

print("¿Todas las letras estan en mayusculas:",String.isupper())

String = String.upper()
print("Cade en mayusculas: ",String)

print()
#--------------------------CENTER() RJUST()   LJUST()------

txt = "Nirio"

print(txt)
print(txt.center(10))
print(txt.rjust(10))
print(txt.ljust(10))
print()

print(txt.center(10,"+"))
print(txt.rjust(10),"+")
print(txt.ljust(10),"+")



print()

#--------------------------CAPITALIZE()----------------------------------------------------

txt_upper = "inStituTo kHiPu"

print(txt_upper)
print(txt_upper.capitalize())

print()




#--------------------------------SWAPCASE()----------------------------------

txt_lower_upper = "iNSTITUTO kHIPU"

print(txt_lower_upper)
print(txt_lower_upper.swapcase())

print()
txt_lower = "cadena en minusculas"
print(txt_lower)
print(txt_lower.swapcase())
print()

txt_number = "1,2,3,4,5,6"
print(txt_number)
print(txt_number.swapcase());

print()





#--------------------------COUNT()----------------------------------------------------

txt_upper = "inStituTo kHiPu"
print(txt_upper)
txt_upper  = txt_upper.center(50,"x")
print(txt_upper.center(50,"x"))
print(txt_upper.count("x"))

txt_upper = "ma esta en mesa de madera en la que ma esta viendo amanda en la mensa"

print(txt_upper.count("m",10,15))
print(txt_upper.count("m",-10,-15))
print(txt_upper.count("m",0))


print()







