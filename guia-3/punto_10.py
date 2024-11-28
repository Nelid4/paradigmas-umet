"""10.  Menú de opciones y validación Se pide desarrollar un programa controlado por menú de opciones que permita lo siguiente: 
1. Ingresar números (la carga finaliza cuando se ingresa el -1) y calcular su promedio. 
2. Generar n valores aleatorios entre -100 y 100 (n se ingresa por teclado). Determinar la cantidad de valores negativos y positivos. 
3. Cargar la nota de un alumno e informar si está aprobado teniendo en cuenta que la nota es un valor entre 0 y 10, siendo mayor
o igual a 4 si está aprobado
"""
menu = 0
cantidad_num = 0
total_ingresado = 0
import random
cantidad = 0
cantidad0 = 0
num_aleatorio = 0
num_positivo = 0
num_negativo = 0
nota_alumno = 0

while True:
    menu = int(input("""\n
    --Menú--
    1- calcular promedio
    2- valores aleatorios entre -100 y 100
    3- calcular nota del estudiante
    0- salir
    Ingrese el número de la opción: """))
    
    while menu != 1 and menu != 2 and menu != 3 and menu != 0:
        menu = int(input("Ingrese una opcin válida"))
    
    if menu == 1:
        while True:
            num_ingresado = float(input("Ingrese un numero, o -1 para finalizar: "))
            
            if num_ingresado != -1:
                cantidad_num += 1
                total_ingresado = total_ingresado + num_ingresado
                print("Número ingresado correctamente")
            else: 
                print("fin de la carga")
                break
        print("El promedio de los numeros ingresados es:", total_ingresado / cantidad_num)

    elif menu == 2:
        cantidad = int(input("Ingrese la cantidad de numeros a generar: "))
        while cantidad <= 0:
            cantidad = int(input("Ingrese un numero mayor a 0: "))
        
        for i in range (1, cantidad + 1):
            num_aleatorio =random.randint(-100,100)
            print("-", num_aleatorio)

            if num_aleatorio < 0:
                num_negativo += 1
            elif num_aleatorio == 0:
                cantidad0 += 1
            else:
                num_positivo += 1
        
        print(f"Hay {num_negativo} numeros negativos y {num_positivo} numeros positivis. El 0 salió {cantidad0} veces")
    
    elif menu == 3:
        nota_alumno = float(input("Ingrese la nota: "))

        while nota_alumno > 10 or nota_alumno < 0:
            nota_alumno = float(input("Ingrese la nota entre 0 y 10: "))
        if nota_alumno >= 4:
            print("El alumno esta aprobado")
        else:
            print("El alumno NO esta aprobado")
        
    else: 
        print("fin del programa")
        break

