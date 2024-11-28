"""Una familia desea registrar y analizar sus gastos mensuales en distintas categorías (comida, transporte, entretenimiento, etc.).

Permitir al usuario ingresar los gastos realizados, asociados a una categoría.
Si la categoría ya existe, sumar el gasto al total mensual de esa categoría.
Si no existe, agregarla con el gasto inicial ingresado.
Mostrar un menú con las siguientes opciones:
1. Mostrar la categoría con el mayor gasto acumulado.
2. Calcular el porcentaje que representa cada categoría respecto al gasto total.
3. Mostrar todas las categorías con sus totales."""

gastos_totales = {}

def ingresar_gastos():
    categoria = input("Ingresar categoria: ")
    cantidad = float(input("Ingrese la cantidad gastada: $"))

    if categoria in gastos_totales:
        gastos_totales[categoria] += cantidad
    else:
        gastos_totales[categoria] = cantidad

def mostrar_mayor_gasto():
    mayor_gasto = None
    mayor_categoria = ""
    for categoria, cantidad in gastos_totales.items():
        if mayor_gasto == None or mayor_gasto < cantidad:
            mayor_gasto = cantidad
            mayor_categoria = categoria
    print(f"La categoria con mayor gasto acumulado es: {mayor_categoria} con ${mayor_gasto} acumulados.")

def calcular_porcentajes():
    total =0
    for categoria, cantidad in gastos_totales.items():
        total+= cantidad
    print(f"Sienso el gasto total ${total}:")
    porcentaje =0
    for categoria, cantidad in gastos_totales.items():
        porcentaje = (cantidad/total)*100
        print(f"-{categoria} respresenta el {porcentaje}%")

def mostrar_todas_categorias():
    for categoria, gasto in gastos_totales.items():
        print(f"{categoria}:$ {gasto}")

def menu():
    while True:
        print("""Menú:
1-ingresar gastos
2-mostrar categoria on mayor gasto
3.mostrar gastos en porentajes
4-mostrar todos los gastos
5-salir del menú""")
        opcion = int(input("IGRESE UNA OPCION: "))
        if opcion == 1:
            ingresar_gastos()
        elif opcion ==2:
            mostrar_mayor_gasto()
        elif opcion==3:
            calcular_porcentajes()
        elif opcion ==4:
            mostrar_todas_categorias()
        elif opcion ==5:
            break
        else:
            print("Elija una opcion valida")

menu()