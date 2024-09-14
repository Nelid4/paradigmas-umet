"""Descripción: Imagina que estás diseñando un contador para analizar una serie de números. Este programa debe ser capaz de 
procesar varios números y contar cuántos de ellos son pares y cuántos son impares.
El programa solicitará al usuario que ingrese una cantidad de números. A medida que se vayan introduciendo, se debe llevar un 
registro de cuántos son pares y cuántos son impares. Al final del proceso, se mostrará un resumen indicando cuántos números pares 
e impares fueron ingresados. El programa deberá continuar contando mientras se sigan ingresando números."""
# declaro variables:
num_par : int;  
num_impar : int;  
num_ingresado : int;
# inicializacion de variabes:
num_par = 0;  
num_impar = 0;  
# entrada: le pido al usuario que ingrese un munero y lo almaceno en una variable
print("--> Ingrese números los números a analizar. Para detener el programa ingrese 0 <--");
num_ingresado = int(input("Ingrese un número: "));

# proceso: utilizo un bucle while para repetir el input e ir almacenando si es par o impar 
while num_ingresado != 0:#hasta que no ingrese 0 le sigo pidiendo que ingrese numeros
    if num_ingresado % 2 == 0:#si al dividir por dos el numero ingresado da 0 el numero es par, de lo contrario, si es 1 es impar
        num_par += 1;#si el numero es par sumo uno
    else:
        num_impar += 1;#si el numero es impar sumo uno
    
    num_ingresado = int(input("Ingrese otro número: ")); #le pido que ingrese otro numero

# salida: le mustro al usuario los numeros pares e impares
print(f"Los números pares ingresados son: {num_par}");
print(f"Los números impares ingresados son: {num_impar}");
