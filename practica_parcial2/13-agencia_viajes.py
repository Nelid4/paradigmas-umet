"""Una agencia de viajes organiza tours y necesita registrar información sobre las reservas. Crea un programa que permita:

Registrar reservas de clientes con su nombre, destino y cantidad de personas.
Calcular total individual por reserva y total general, considerando que indiferentemente del destino, el precio por persona es $250.
Mostrar los clientes que reservan para más de 4 personas.
Calcular el total de personas registradas para todos los destinos."""

total_reservas={}

def agregar_reservas():
    nombre = input("Ingresar nombre a cargo de la reserva: ")
    destino=input("Ingrese el destino: ")
    cantidad=int(input("Ingrese la cantidad de personas: "))

    total_reservas[nombre]={"destino":destino, "cantidad":cantidad}

def calcular_recaudado():
    total_individual=0
    total_general=0

    for nombre, info in total_reservas.items():
        total_individual = info["cantidad"]*250
        total_general += total_individual
        print(f"La reserva de {nombre} tiene un costo de : ${total_individual}")
    print(f"El total recaudado es: ${total_general}")

def calcular_reserva_4():
    for nombre, info in total_reservas.items():
        if info["cantidad"] > 4:
            print(f"{nombre} reservó para mas de 4 personas. ({info["cantidad"]})")

def calcular_total_personas():
    total_personas =0
    for nombre, info in total_reservas.items():
        total_personas += info["cantidad"]
    print("El total de personas que viajan es: ", total_personas)

def menu():
    while True:
        print("""\n----MENÚ----
        1-agregar reservas
        2-calcular recaudado individual y general
        3-mostrar reservas para mas de 4 personas
        4-calular total de personas que viajarán
        5-salir""")
        opcion = int(input("Ingrese opcion: "))
        if opcion == 1:
            agregar_reservas()
        elif opcion ==2:
            calcular_recaudado()
        elif opcion==3:
            calcular_reserva_4()
        elif opcion ==4:
            calcular_total_personas()
        elif opcion ==5:
            break
        else:
            print("Elija una opcion valida")

menu()