""" - Área de un triángulo Desarrolle un programa para calcular el área de un triángulo, cargando por teclado el valor de la base,
pero sabiendo que su altura es igual al cuadrado de la base. """
# declaro variables
altura : float;
resultado : float;
# inicializando variables:
base = 0;
altura = 0;
resultado = 0;
# entrda: le pido al usuario que ingrese el valor de la base
base = float(input("Ingrese el valor de la base: "));
# proceso: calculo el área
altura = base**2;
resultado = (base*altura)/2;
# salida: le muestro el resultado por consola
print("El área del triangulo es: " , resultado);
