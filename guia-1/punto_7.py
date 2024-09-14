"""7. Ingresar la cantidad de números de la sucesión de Fibonacci a mostrar"""
# declaro variables:
a : int;
b : int;
siguiente : int;
# inicializo variables:
a = 0;
b = 1;
siguiente = 0;
# entrada: le pido al usuario que ingrese la cantidad de numero a mostrar
cantidad = int(input("Ingrese la cantidad de números de la sucesión de Fibonacci a mostrar: "));
# proceso y salida: 
print("Sucesión de Fibonacci:");
for i in range(cantidad): #utilizo un bucle for que se repetira dependiendo del numero ingresado
    print(a, end='-'); #imprimo el valor actual de a seguido de un guion
    siguiente = a + b; #actualizo el valor de siguiente
    a = b; #actualizo el valor de a
    b = siguiente; #actualizo el valor de b
