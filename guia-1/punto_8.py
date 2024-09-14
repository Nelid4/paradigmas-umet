"""8. Multiplicación. Ingresar un número cualquiera por teclado y que muestre su respectiva tabla del 1 al 10."""
# declaro variables:
i : int;
resultado : int;
# inicializo variables:
i = 1;
resultado = 0;
# entrada: le pido al usuario que ingrese el numero de la tabla que quiere imprimir
numero_ingresado = int(input("Ingrese el número del que desea ver su tabla: "));
# proceso y salida: utilizo un bucle for
for i in range (1,11): #hago que se repita 10 veces i
    resultado = numero_ingresado * i; #actualizo el valor de resultado
    print(f"{numero_ingresado} X {i} = {resultado}"); #imprimo la multiplicacion
    i = i + 1; #itero en 1 el valor de i 