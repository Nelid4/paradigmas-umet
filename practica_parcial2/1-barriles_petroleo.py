"""Una empresa petrolea que necesita analizar datos de extraccion en distintas plataformas durante un mes, cada platarm 
tiene un numero de identif y se registra diariamente la cantidad de barriles extraidos.
1- registros de extraccion diaria por plataforma,si ya eesta registrada sumacantidad al total mensual, sino crear nuevo registro.
2-menu
-1promedio diario de plataforma
-2plataforma con menor produccion total(cual y cantidad)
-3total por todas las plataformas durante el mes"""
total_plataformas = {"22": [2,4,6,7], "33": [2,3]}

def cargar_plataforma():
    num_plataforma = input("Ingrese el número de la plataforma: ")
    cantidad_ingresada = float(input("Ingrese la cantidad de barriles extraidos: "))

    if num_plataforma in total_plataformas:
        total_plataformas[num_plataforma].append(cantidad_ingresada)
    else:
        total_plataformas[num_plataforma] = [cantidad_ingresada]

def calcular_promedio():
    for plataforma, cantidad in total_plataformas.items():
        promedio = sum(cantidad)/30
        print(f"-El promedio para la plataforma {plataforma} es {promedio}.")
        

def calcular_menor_produccion():
    menor_cantidad = None
    menor_plataforma = ""

    for plataforma, cantidades in total_plataformas.items():
        total_produccion = sum(cantidades)
        
        if menor_cantidad is None or total_produccion < menor_cantidad:
            menor_cantidad = total_produccion
            menor_plataforma = plataforma

    print(f"La plataforma con menor producción es: {menor_plataforma} con {menor_cantidad} barriles.")

def mostrar_todas_plataformas():
    total = 0
    for plataforma, cantidad in total_plataformas.items():
        total += sum(cantidad)

    print(f"La cantidad total extraida es: {total} de barries extraidos")


def menu():
    while True:
        print("""\n
 ____Bienvenid@ usuario_____
|                           |
| 1- Cargar a plataforma    |
| 2- Calcular promedio      |
| 3- Menor produccion       |
| 4- Todas las plataformas  |
| 5- Salir                  |
|___________________________|
        """)
        opcion = int(input("Ingrese un opción: "))
        if opcion == 1:
            print(total_plataformas)
            cargar_plataforma()
        
        elif opcion == 2:
            calcular_promedio()

        elif opcion == 3:
            calcular_menor_produccion()

        elif opcion == 4:
            mostrar_todas_plataformas()

        elif opcion == 5:
            print("--- Fin del programa ---")
            break

        else:
            print("--> Solo se permiten numeros del menú")


menu()