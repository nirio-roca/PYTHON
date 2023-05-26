## ASIGNACIÓN
print("ASIGNACIÓN")
mensaje = "hola";
mensaje += " ";
mensaje += "Nirio";
print(mensaje);


## CONCADENACIÓN
print("");
print("CONCADENACIÓN");
mensaje = "hola";
espacio  = " ";
nombre = "Nirio";
print(mensaje,espacio,nombre);

## CONCADENACIÓN
print("");
print("CONCADENACIÓN VALORES NUMERICOS");
n1 = 4;
n2 = 6;
resultado = n1 + n2
print("\n con ',' El resultado de la suma es: ",resultado)
## "," la concadenación con coma es para todos
## "+" la      "        es solo para textos  
resultado = str(n1 + n2)
print("\n con '+' El resultado de la suma es: "+resultado)

## Búsqueda de caracteres
print("\nBúsqueda de caracteres")
mensaje = "Hola Nirio"
          #012345  -> posición 
buscar_subcadena = mensaje.find("Nirio")
print(buscar_subcadena)

## Extración de caracteres
extraer_cadena  = mensaje[3:7]
print("Del mensaje",mensaje,"Extraer desde la posición 3 hasta 7(6)  es igual a: "+ extraer_cadena)

extraer_hasta = mensaje[:8]

print(extraer_hasta)

extraer_desde = mensaje[6:]

print(extraer_desde)


#COMPARACIÓN
print("COMPARACIÓN")
mensaje1 = "hola"
mensaje2 = "Hola"

print(mensaje1 == mensaje2)

mensaje1 = "Hola"

print(mensaje1 == mensaje2)

print(mensaje.splitlines)



