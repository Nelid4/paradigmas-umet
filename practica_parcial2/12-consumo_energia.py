"""Una empresa de electricidad necesita analizar el consumo de energía mensual por usuario. Crea un programa que permita:

Registrar el consumo (en kWh) de cada usuario con su número de cliente.
Consultar el consumo total de un cliente específico.
Mostrar el cliente con el consumo más bajo y más alto.
Calcular el promedio de consumo de todos los clientes."""

consumo_mensual = {}

def registro_usuario():
    numero = int(input("Ingrese n° de cliente: "))
    consumo= float(input("ingrese el consumo: "))
    if numero in consumo_mensual:
        consumo_mensual[numero].append(consumo)
    else:
        consumo_mensual[numero]=[consumo]

def consultar_consumo():
    buscar = int(input("ingrese n° de cliente a buscar: "))
    encontrado = False
    for cliente, consumo in consumo_mensual.items():
        if buscar == cliente:
            print(f"El consumo total de {cliente} es: {sum(consumo)}")
            encontrado = True
    if not encontrado:
        print("no se encontro el cliente")

def mostrar_consumo():
    mayor_consumo=None
    menor_consumo=None
    mayor_cliente=""
    menor_cliente=""

    for cliente, consumo in consumo_mensual.items():
        if mayor_consumo == None or mayor_consumo < sum(consumo):
            mayor_consumo = sum(consumo)
            mayor_cliente = cliente
        if menor_consumo == None or menor_consumo > sum(consumo):
            menor_consumo = sum(consumo)
            menor_cliente =cliente
    print(f"El usuario con mayor gasto es: n°{mayor_cliente} con {mayor_consumo}.\nEl usuario con menor consumo es: n° {menor_cliente} con {menor_consumo}.")

def calcular_promedio():
    promedio=0
    for cliente, consumo in consumo_mensual.items():
        promedio = sum(consumo)/len(consumo)
        print(f"-{cliente}: {promedio}")

def menu():
    while True:
        print("""\n----MENÚ----
        1-registrar consumo
        2-consultar consumo especifico
        3-mostrar mayor y menor consumo
        4-promedio x cliente
        5-salir""")
        opcion = int(input("Ingrese opcion: "))
        if opcion == 1:
            registro_usuario()
        elif opcion ==2:
            consultar_consumo()
        elif opcion==3:
            mostrar_consumo()
        elif opcion ==4:
            calcular_promedio()
        elif opcion ==5:
            break
        else:
            print("Elija una opcion valida")

menu()

