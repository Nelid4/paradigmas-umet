"""Una tienda de alquiler de bicicletas desea registrar las transacciones diarias. Crea un programa que permita:

Registrar alquileres por cliente con nombre, cantidad de bicicletas alquiladas y el tiempo (en horas).
Consultar cuánto tiempo ha alquilado bicicletas un cliente específico.
Mostrar el cliente que alquiló por más horas.
Calcular la ganancia total del día, suponiendo que cada bicicleta alquilada cuesta $10 por hora."""

alquileres={'ana': {'cantidad': 2, 'tiempo': 4.0}, 'mike': {'cantidad': 1, 'tiempo': 5.0}}

def registrar_alquiler():
    nombre = input("Ingrese el nombre: ")
    cantidad = int(input("Ingrese la cantidad de bicicletas alquiladas: "))
    tiempo = float(input("Ingrese el tiempo, en horas, del alquiler: "))

    alquileres[nombre] = {"cantidad":cantidad, "tiempo":tiempo}

    print(alquileres)

# registrar_alquiler()

def buscar_cliente():
    busqueda = input("Ingrese el nombre que busca: ")
    encontrado = False
    for nombre, info in alquileres.items():
        if busqueda == nombre:
            print(f"{nombre} alquiló {info['tiempo']} horas")
            encontrado = True

    if not encontrado:
        print("No se encontro el cliente")


# buscar_cliente()

def mostrar_mayor_alquiler():
    mayor_horas = None
    mayor_nombre = ""

    for nombre, info in alquileres.items():
        if mayor_horas == None or mayor_horas < info["tiempo"]:
            mayor_horas = info["tiempo"]
            mayor_nombre = nombre

    print(f"El cliente con mas horas de alquiler es: {mayor_nombre} con {mayor_horas} horas de alquiler.")

# mostrar_mayor_alquiler()

def calcular_ganancia():
    ganancia=0
    ganancia_total =0
    valor_bicicletas_alquiladas = 0
    for nombre, info in alquileres.items():
        valor_bicicletas_alquiladas = info["cantidad"] * 10
        ganancia = valor_bicicletas_alquiladas* info["tiempo"]
        ganancia_total += ganancia
        print(f"-{nombre} debe pagar: ${ganancia}")

    print(f"La ganancia total es: ${ganancia_total}")

# calcular_ganancia()

def menu():
    while True:
        print("""----MENÚ----
        1-agregar alquiler
        2-consultar por cliente
        3-mostrar mayor tiempo de alquiler
        4-mostar ganancia total e individual
        5-salir""")
        opcion = int(input("Ingrese opcion: "))
        if opcion == 1:
            registrar_alquiler()
        elif opcion ==2:
            buscar_cliente()
        elif opcion==3:
            mostrar_mayor_alquiler()
        elif opcion ==4:
            calcular_ganancia()
        elif opcion ==5:
            break
        else:
            print("Elija una opcion valida")

menu()