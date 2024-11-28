"""Una biblioteca necesita registrar los préstamos realizados por diferentes lectores durante un mes. Cada lector tiene un número
de identificación y se registra diariamente la cantidad de libros que ha tomado prestados.
Opciones del menú:

1Registrar libros prestados a un lector (sumar al total si ya está registrado).
2Calcular el promedio de libros prestados por cada lector.
3Mostrar el lector con mayor libros prestados (ID y cantidad).
4Calcular el total de libros prestados en el mes."""
total_prestamos = {1010: [2,5,7], 2020:[3,1]}

def registrar_prestamo():
    lector = input("Ingrese número de identificación del lector: ")
    cantidad = int(input("Ingrese la cantidad de libros que se tomaron: "))

    if lector in total_prestamos:
        total_prestamos[lector].append(cantidad)
    else:
        total_prestamos[lector] = [cantidad]
    
        print(total_prestamos)

def calcular_promedio():
    for lector, libros in total_prestamos.items():
        suma = sum(libros)
        promedio = suma / len(libros)
        print(f"-El lector {lector} tiene un promedio de {promedio} libros extraidos por día.")

def determinar_mayor_lector():
    mayor_lector = ""
    mayor_cantidad = None
    for lector, libros in total_prestamos.items():
        cantidad_extraida = sum(libros)

        if mayor_cantidad is None or mayor_cantidad < cantidad_extraida:
            mayor_cantidad = cantidad_extraida
            mayor_lector = lector

    print(f"El lector con mayor libros extraidos es: N°{mayor_lector} con {mayor_cantidad}")

def calcular_total_prestado():
    total_libros_prestados = 0
    for lector, libros in total_prestamos.items():
        total_libros_prestados += sum(libros)
    
    print(f"El total de libros prestados en el mes es: {total_libros_prestados}")




def menu():
    while True:
        print("""\n
    _____PRESTAMOS DE LA LIBRERIA______
    |                                 |
    |  1- Registrar prestamo          |
    |  2- Promedio de libros presta2  |
    |  3- Lector con mas libros       |
    |  4- Total de libros prestados   |
    |  5- Salir del menú              |
    |_________________________________|""")
        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            registrar_prestamo()

        elif opcion == 2:
            calcular_promedio()

        elif opcion == 3:
            determinar_mayor_lector()

        elif opcion== 4:
            calcular_total_prestado()

        elif opcion == 5:
            print("---> Fin del programa")
            break
        else:
            print("Asegurese de ingresar una opcion que esté en el menú.")


menu()