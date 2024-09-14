"""14. Suma - División - Potencia Se necesita desarrollar un programa que permita calcular la suma de tres números. Si el resultado es mayor a 10 dividir
por 2 (mostrar su resultado sin decimales), en caso contrario elevar el resultado al cubo."""
# declarando variables:
resultado : int;
# inicializando variables:
num1 = 0;
num2 = 0;
num3 = 0;
resultado = 0;
# entrada: le pido al usuario que ingrese los tren números.
num1 = int(input("Ingrese el primer número: "));
num2 = int(input("Ingrese el segundo número: "));
num3 = int(input("Ingrese el tercer número: "));
# procesos: calculo la suma de los 3 numeros y determio si hay q dividir o elevar, y guardo el resultado en una variable
suma = num1 + num2 + num3;
if suma > 10:
    resultado = suma // 2;
else:
    resultado = suma ** 2;
# salida: mprimo variable de resultado
print("Su resultado es: ", resultado);