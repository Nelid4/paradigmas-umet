"1 - División con resto Plantear un algoritmo que permita informar, para dos valores a y b el resultado de la división a/b y el resto de esa división."
#declaro variables
resultado : int;
resto : int;
#inicializo variables
resultado = 0;
resto = 0;
#entrada: le pido al usuario que igrese los valores a y b
valor_a = int(input("Ingrese el primer valor:"));
valor_b = int(input("Ingrese el segundo valor:"));
#proceso: realizo la division y obtengo el resto
resultado = valor_a / valor_b;
resto = valor_a % valor_b;
#salida: muestro el resultado y el resto
print(f"El resultado es: {resultado}, y el resto es: {resto}");