"""Programa: Adivianzas
Escribe un programa en el que el usuario deba adivinar un número secreto generado aleatoriamente entre 1 y 100. El usuario tendrá
un total de 10 intentos para lograrlo. Después de cada intento, el programa le indicará si el número ingresado es mayor o menor
que el número secreto. Además, el programa llevará un contador de los intentos restantes y lo mostrará en cada intento. Si el 
usuario acierta antes de que se le acaben los intentos, el programa lo felicitará y terminará. En caso contrario, una vez agotados
los intentos, el programa deberá revelar el número secreto y mostrar un mensaje de derrota. """
import random

num_secreto = random.randint(1, 100)
print("----->", num_secreto)  
intentos = 10
num_ingresado = 0 

while intentos > 0 and num_ingresado != num_secreto:
    num_ingresado = int(input("Ingrese un número entre 1 y 100: "))

    if num_ingresado == num_secreto:
        print("¡Felicidades, adivinaste el número secreto!")
    else:
        intentos -= 1
        if intentos == 0:
            print("Se acabaron los intentos. El número secreto era:", num_secreto)
        else:
            if num_ingresado < num_secreto:
                print("El número ingresado es más chico que el número secreto.")
            else:
                print("El número ingresado es más grande que el número secreto.")
            print("--> Te quedan:", intentos, "intentos\n")

