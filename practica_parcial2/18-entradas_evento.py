"""Un evento lleva un registro de las entradas vendidas. Crea un programa que permita:
-Registrar la venta de entradas por nombre del comprador, tipo de entrada (VIP o general) y cantidad.
-Consultar todas las entradas vendidas de un tipo específico.
-Mostrar el comprador con mayor cantidad de entradas adquiridas.
-Calcular el total de ingresos generados por las ventas (supón precios para VIP y general)."""

entradas_vendidas={}

def resgitrar_venta():
    nombre=input("Ingrese su nombre: ").lower()
    entrada=input("Ingrese el tipo de entrada Vip o General: ").lower()
    cantidad=int(input("Ingrese la cantidad: "))

    entradas_vendidas[nombre]={"entrada":entrada, "cantidad":cantidad}
    print("Venta registrada con éxito!")

def consultar_entrada_vendida():
    busqueda=input("Ingrese vip o general: ").lower()
    hay_entradas=False

    for nombre, info in entradas_vendidas.items():
        if busqueda == info["entrada"]:
            print(f"{nombre}: {info["cantidad"]}")
            hay_entradas=True
    if not hay_entradas:
        print("No hay venta de entradas", busqueda)

def determinar_mayor_comprador():
    mayor_cantidad=None
    mayor_nombre=""
    mayor_entrada=""

    for nombre, info in entradas_vendidas.items():
        if mayor_cantidad==None or mayor_cantidad < info["cantidad"]:
            mayor_cantidad = info["cantidad"]
            mayor_nombre=nombre
            mayor_entrada=info["entrada"]
    print(f"{mayor_nombre} adquirio la mayor cantidad de entradas: {mayor_cantidad} entradas tipo {mayor_entrada}")

def calcular_ingresos():
    VALOR_VIP=500
    VALOR_GENERAL=200
    total_recaudado=0

    for nombre, info in entradas_vendidas.items():
        if info["entrada"] =="vip":
            total_recaudado+=(info["cantidad"]*VALOR_VIP)
        else:
            total_recaudado+=(info["cantidad"]*VALOR_GENERAL)

    print(f"el total recaudado es : ${total_recaudado}")

def menu():
    while True:
        print("\n---Menú---\n1-Registar venta\n2-consultar entrdadas vendidas por categoria\n3-mostrar mayor comprador\n4-calculat total recaudado\n5-salir")
        opcion=int(input("Ingrese una opcion: "))
        if opcion == 1:
            resgitrar_venta()
        elif opcion == 2:
            consultar_entrada_vendida()
        elif opcion ==3:
            determinar_mayor_comprador()
        elif opcion ==4:
            calcular_ingresos()
        else:
            break

menu()



