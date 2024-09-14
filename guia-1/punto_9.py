"""9. Escribir un programa que pida dos números y muestre como resultado su división, cociente y resto."""
# declarando variables:
division : float;
cociente : float;
resto : float;
# inicializando variables:
division = 0;
cociente = 0;
resto = 0;
# entrada: le pido al usuario que ingrese los números
numerador = float(input("Ingrese el numerador: "));
denominador = float(input("Ingrese el denominador: "));
# proceso: actualizo los valores de las variables
division = numerador / denominador;
cociente = numerador // denominador;
resto = numerador % denominador;
# salida: imprimo la division, cociente y resto.
print(f"Resultado de la division: {division}\nCociente: {cociente}\nResto: {resto}");