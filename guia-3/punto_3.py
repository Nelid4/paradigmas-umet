"""3. Menu de Opciones con secuencias Escribir un programa que le permita al usuario, a través de un menú de opciones, las 
siguientes operaciones: a) Generar una serie n de números (n ingresado por teclado y validando que sea mayor a cero) y mostrar la
suma de los cuadrados 
b) Ingresar un texto finalizado por un punto y determinar la cantidad de palabras que finalizan con vocales 
c) Ingresar una serie de números (la carga finaliza con cero) y determinar si hay mayor cantidad de valores pares o de impares 
d) Salir"""
opcion = 0
numero = 0
suma_total = 0
palabra = ""
total_vocales = 0
num_par = 0
num_impar = 0
num_ingresado = 0
resultado = 0

while True:
    opcion = input("""
        ----MENÚ----
    -A- Generar números y obtener suma al cuadrado.
    -B- Determinar cuantas vocales hay.
    -C- Determinar par/impar.
    -D- Salir
    -------------------
    ingrese una opcion: """).lower()
    while opcion != "a" and opcion != "b" and opcion != "c" and opcion != "d":
        opcion = input("Ingrese una opción válida: ")
    
    if opcion == "a":
        numero = int(input("Ingrese la cantidad de numero a generar, teniendo en cuenta que el 1er numero es 0: "))
        while numero <= 0:
            numero = int(input("Ingrese un numero mayor a 0: "))
        for i in range(0,numero):
            print(i)
            suma_total = suma_total + (i **2)
        print("La suma de los cuadrados es: ", suma_total)
        suma_total = 0

    elif opcion == "b":
        print("Ingrese una palabra a la vez palabra y lpara finalizar '.' ")
        while True:
            palabra = input("").lower()
            if palabra == ".":
                print("El total de vocales es: ",total_vocales)
                break
            else:
                if palabra[-1] == "a" or palabra[-1] == "e" or palabra[-1] == "i" or palabra[-1] == "o" or palabra[-1] == "u":
                    total_vocales += 1
        total_vocales = 0
    
    elif opcion == "c":
        while True:
            num_ingresado = float(input("Ingrese un número y 0 para terminar la serie: "))
            if num_ingresado == 0:
                break
            else:
                resultado = num_ingresado % 2
                if resultado == 0:
                    num_par += 1
                else:
                    num_impar += 1
        
        if num_par > num_impar :
            print("Hay mas números pares.")
        elif num_par == num_impar :
            print("Hay la misma cantidad de números pares que impares.")
        else:
            print("Hay mas números impares.")
        num_impar = 0
        num_par = 0
    
    else:
        print("Saliendo...")
        break


