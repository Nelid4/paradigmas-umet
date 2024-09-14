
"""18. Tarjeta de Bingo Realizar un programa que genere 15 numero aleatorios enteros en el rango del 1 al 100, que representaria la tarjeta de bingo de una 
persona. Una vez generado los numeros aleatorios solicitar al usuario que ingrese 3 numeros enteros, a parƟr de alli mostrar los siguientes mensajes: 
Si el usuario no marco ninguno de los numeros indicarlo diciendo “El jugador Ɵene mala suerte, no marco ninguna casilla”. Caso contrario mostrar “El jugador 
marco algun numero de la tarjeta”. """
import random;#importo libreria para crear números random
# declarando variables:
i : int;
numero : int;
# inicializando variables:
i = 1;
numero = 0;
lista_numeros = [];#creo un array/lista
#creo un bucle que genere 15 numeros aleatorios y los almacene en la lista
for i in range(15):
    numero = random.randint(1,100);
    lista_numeros.append(numero);

print("Su tarjeta es:",lista_numeros);#muestro el array de 15 numeros
num_ingresado1 = int(input("Ingrese un número entero: "));
num_ingresado2 = int(input("Ingrese otro número entero: "));
num_ingresado3 = int(input("Ingrese un último número entero: "));

if num_ingresado1 in lista_numeros or num_ingresado2 in lista_numeros or num_ingresado3 in lista_numeros:
    print("El jugador marco algún número de la tarjeta");
else:
    print("El jugador tiene mala suerte, no marco ninguna casilla");
