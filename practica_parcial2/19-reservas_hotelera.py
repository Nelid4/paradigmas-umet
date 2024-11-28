"""Un hotel necesita gestionar sus reservas. Crea un programa que permita:
Registrar reservas con el nombre del huésped, tipo de habitación (individual, doble, suite) y cantidad de noches.
Consultar reserva de un huésped específico.
Mostrar el tipo de habitación con mayor cantidad de reservas.
Calcular las ganancias totales del hotel en base a precios establecidos por tipo de habitación."""
reservas={}
def registrar_reservas():
    nombre=input("Ingrese el nombre: ").lower()
    habitacion=input("Habitacion: individual, doble o suite: ").lower()
    cantidad=int(input("Ingrese la cantidad de noches que se queda: "))
    reservas[nombre] = {"habitacion":habitacion, "cantidad":cantidad}
    print("Reserva agregada!")

def consultar_reserva():
    busqueda=input("Ingrese nombre: ").lower()
    encontrado=False

    for nombre, info in reservas.items():
        if busqueda ==nombre:
            print(f"{nombre}: reserva {info["cantidad"]} noches en habitacion {info["habitacion"]}")
            encontrado=True
    if not encontrado:
        print("No ha resrvas a ese nombre")

def habitacion_mas_reservada():
    calcular_habitacion={}

    for nombre, info in reservas.items():
        habitacion = info["habitacion"]

        if habitacion in calcular_habitacion:
            calcular_habitacion[habitacion]+=1
        else:
            calcular_habitacion[habitacion]=1
    
    mayor_habitacion = ""
    mayor_reserva=None

    for tipo, cantidad in calcular_habitacion.items():
        if mayor_reserva == None or mayor_reserva < cantidad:
            mayor_reserva = cantidad
            mayor_habitacion = tipo
    
    print(f"habitacio mas reservada: {mayor_habitacion} ({mayor_reserva} reservas.)")

def calcular_ganancias():
    VALOR_INDIVIDUAL = 100
    VALOR_DOBLE=180
    VALOR_SUITE=250
    valor_total=0

    for nombre, info in reservas.items():
        habitacion = info["habitacion"]
        cantidad= info["cantidad"]
        if habitacion =="individual":
            valor_total += (cantidad*VALOR_INDIVIDUAL)
        elif habitacion=="doble":
            valor_total += (cantidad*VALOR_DOBLE)
        else:
            valor_total += (cantidad*VALOR_SUITE)
    
    print("El valor total recaudado es: $", valor_total)

def menu():
    while True:
        print("\n---Menú---\n1-registrar reserva\n2-consultar reserva por nombre\n3-mostrar habitacion mas resrevada\n4-calcular ganancias\n5-salir")
        opcion=int(input("Ingrese una opcion: "))
        if opcion == 1:
            registrar_reservas()
        elif opcion == 2:
            consultar_reserva()
        elif opcion ==3:
            habitacion_mas_reservada()
        elif opcion ==4:
            calcular_ganancias()
        else:
            break

menu()