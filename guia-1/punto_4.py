"""4 - Últimos dígitos ¿Cómo usaría el operador resto ( %) para obtener el valor del último dígito de un número entero? 
¿Y cómo obtendría los dos últimos dígitos? Desarrolle un programa que cargue un número entero por teclado, y muestre el último 
dígito del mismo (por un lado) y los dos últimos dígitos (por otro lado) """
# declaro variables:
ultimo : int;
ultimos2 : int;
# inicializacion de variables: 
ultimo : 0;
ultimos2 : 0;
# entrada: le pido al usuario que ingrese un numero entero
num_entero = int(input("Ingrese un número entero: "));
# proceso: calculo los restos, del numero ingresado
ultimo = num_entero % 10;
ultimos2 = num_entero % 100;
# salida: muestro el ultimo y los ultimos dos digitos del numero ingresado, y una explicación
print("El último digito del numero ingresado es: " , ultimo );
print("Los últimos dos digitos del numero ingersado son: " , ultimos2);
print("\n--> Explicación: El operador ' % ' devuelve el resto de una division entera, al dividir por 10, el resto\nes lo que queda tras contar las decenas, por lo que será el último dígito.\nLo mismo ocurre cuando lo dividimos por 100, el resto correspone a los dos últimos digitos, decena y unidad.");