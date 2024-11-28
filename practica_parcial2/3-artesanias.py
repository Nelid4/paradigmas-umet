"""Un taller de artesanías necesita registrar cuántos productos terminados genera cada artesano diariamente.
Menú:

Registrar la cantidad de productos terminados por un artesano: Si el artesano ya está registrado, agregar la cantidad al total 
diario; si no, crear un nuevo registro.
Calcular el promedio de productos terminados por cada artesano.
Mostrar el artesano que produjo menos productos en el mes (nombre y cantidad).
Mostrar el total de productos terminados por todos los artesanos."""
total_produccion ={"ana": [54,23,12], "ramon":[11,10,9] }

def registrar_produccion():
    artesano= input("Ingrese el nombre del artesano: ")
    producido = int(input("Ingrese la cantidad de piezas producidas: "))

    if artesano in total_produccion:
        total_produccion[artesano].append(producido)
    else:
        total_produccion[artesano] = [producido]
    print(total_produccion)

def calcular_promedio():
    for artesano, produccion in total_produccion.items():
        promedio= sum(produccion)/len(produccion)
        print(f"El promedio de produccion de {artesano} es: {promedio} de piezas al día.")

def mostrar_menor_produccion():
    menor_artesano=""
    menor_produccion = None

    for artesano, produccion in total_produccion.items():
        if menor_produccion == None or menor_produccion > sum(produccion):
            menor_produccion = sum(produccion)
            menor_artesano = artesano
    print(f"El artesano con menor produccion es: {menor_artesano} con {menor_produccion} piezas.")

def mostrar_produccion_total():
    produccion_mensual = 0
    for x, produccion in total_produccion.items():
        produccion_mensual += sum(produccion) 
    print("La produccion total del mes es: ", produccion_mensual, " piezas")

def menu():
    while True:
        print("""\n
 ______MENÚ DE ARTESANOS____
|                           |
|  -1 Registrar produccion  |
|  -2 Promedio por artesano |
|  -3 Artesano menor prducc.|
|  -4 Produccion total      |
|  -5 Salir                 |
|___________________________|
""")
        opcion = int(input("Ingrese una opcion del menú: "))
        if opcion == 1:
            registrar_produccion()
        elif opcion == 2:
            calcular_promedio()
        elif opcion == 3:
            mostrar_menor_produccion()
        elif opcion == 4:
            mostrar_produccion_total()
        elif opcion == 5:
            print("---> Finalizando programa")
            break
        else:
            print("Asegurese de ingresar un número que aparezca en el menú.")
menu()