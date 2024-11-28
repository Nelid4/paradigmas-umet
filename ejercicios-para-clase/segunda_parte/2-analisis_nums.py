"""Enunciado 2: Análisis de Números
Crea un programa que permita almacenar una lista de números enteros y realizar diferentes análisis sobre ellos. El programa debe ofrecer las siguientes opciones:

Agregar número a la lista: El usuario puede agregar un número a la lista de números.

Mostrar el número mayor y el número menor: El programa muestra el número más grande y el más pequeño de la lista.

Calcular la suma y el promedio: El programa debe calcular y mostrar la suma de todos los números y el promedio.
"""
import time
lista=[]
tupla_validar=(1,2,3,4)
#agregar al menos un número para que las opciones del menu funcionen

agregar_num = int(input("Para mostrar el menú, debe ingresar un número que se agregara a la lista: "))
lista.append(agregar_num)

while True:
    time.sleep(2)
    print(f"""
Lista: {lista}
------menú------
1- Agregar un número entero.
2- Mostrar número mayor y menor.
3- Suma y promedio.
4- Salir.
""")
    opcion = int(input("Ingrese una opción: "))
    # uso una tupla y u while para validar la opcion ingresada
    while opcion not in tupla_validar:
        opcion = int(input("Ingrese una opción que aparezca en el menú: "))
    
    if opcion == 1:
        agregar_num = int(input("Ingrese el número que quiere agregar a la lista: "))
        lista.append(agregar_num)
        print("Número agregado con éxito\n")

    elif opcion == 2:
        print("El mayor número es:", max(lista))
        print("El menor número es:", min(lista))

    elif opcion == 3:
        suma= sum(lista)
        print(f"El resultado de la suma total es: {suma}, y el promedio es: {suma/len(lista)}")

    else:
        print("Saliendo...")
        time.sleep(2)
        break