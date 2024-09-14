"""6. Escribir un programa que pregunte un nombre de usuario, y que después muestre por pantalla si su cantidad de letras es par o impar."""
# declaro variables:
nombre : str;
# inicializo variables:
nombre = "";
# entrada: le pido al usuario que ingrese su nombre y lo guardo en una variable
nombre = input("¿Cuál es el nombre de usuario?: ");
# proceso: primero, mediante el len() cuento cuantas letras tiene nombre y lo guiardo en la variable letras
letras = len(nombre);
determinar_palabra = int(letras) % 2; #convierto el str en int y obtengo el resto de dividirlo por 2
if determinar_palabra == 0: #si no hay resto, es par
    print(f"La cantidad de letras en {nombre} es par");
else:#si hay resto, es impar
    print(f"La cantidad de letras en {nombre} es impar");
