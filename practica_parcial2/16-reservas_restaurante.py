# def determinar_horario_pico():
#     conteo_horarios={}
#     # mayor_concurrencia=None
#     # mayor_horario = 0
#     concurrencia_3 = False

#     for nombre, info in reseras_totales.items():
#         horario = info["horario"]

#         if horario in conteo_horarios:
#             conteo_horarios[horario]+=1
#         else:
#             conteo_horarios[horario]=1
    
#     print(conteo_horarios)
#     for hora, personas in conteo_horarios.items():
#         if personas > 3:
#             print(f"{personas} reservaron para {hora}hs")
#             concurrencia_3=True
    
#     if not concurrencia_3:
#         print("No hay mas de 3 reservas por horario")

#     # for hora, personas in conteo_horarios.items():
#     #     if mayor_concurrencia == None or mayor_concurrencia < personas:
#     #         mayor_concurrencia = personas
#     #         mayor_horario = hora

#     # print("Horario conmayor concurrencia: ", mayor_horario," ->", mayor_concurrencia)

# determinar_horario_pico()
"""Un restaurante lleva un registro de sus reservas diarias. Crea un programa que permita:

Registrar reservas con el nombre del cliente, cantidad de personas y horario.
Consultar las reservas de un cliente específico.
Listar los horarios con más de 3 reservas.
Calcular el total de personas reservadas en un día."""

reseras_totales={"juan": {"cantidad":4, "horario": 20.30},
    "ana": {"cantidad":8, "horario": 20.30},
    "luis": {"cantidad":2, "horario": 20.30},
    "carmen": {"cantidad":4, "horario": 21.30}}

def registrar_reserva():
    nombre = input("Ingrese nombre: ").lower()
    cantidad =int(input("Ingrese cantidad de personas: "))
    horario = float(input("Ingrese horario: "))

    reseras_totales[nombre]={"cantidad": cantidad, "horario": horario}

def consultar_reserva():
    busqueda = input("ingrese nombre: ").lower()
    encontrado=False

    for nombre, info in reseras_totales.items():
        if busqueda == nombre:
            print(f"{nombre}: {info["cantidad"]} personas, {info["horario"]}hs")
            encontrado =True

    if not encontrado:
        print("No hay reservas a ese nombre")

def listas_horario():
    contar_horario={}

    for nombre, info in reseras_totales.items():
        horario = info["horario"]

        if horario in contar_horario:
            contar_horario[horario]+=1
        else:
            contar_horario[horario]=1
    hay_reservas =False

    for hora, reservas in contar_horario.items():
        if reservas > 3:
            print(f"{hora}: {reservas} reservas")
            hay_reservas = True
    
    if not hay_reservas:
        print("No hay reservas para mas de 3 personas")

def calcular_personas_reservadas():
    total_personas=0
    for nombre, info in reseras_totales.items():
        total_personas += info["cantidad"]
    print("total reservas: ", total_personas)

def menu():
    while True:
        print("\n---Menú---\n1-registrar reserva\n2-Consultar reserva\n3-mostrar horario con mas de 3 reservas\n4-mostrar total de personas\n5-salir")
        opcion=int(input("Ingrese una opcion: "))
        if opcion == 1:
            registrar_reserva()
        elif opcion == 2:
            consultar_reserva()
        elif opcion ==3:
            listas_horario()
        elif opcion ==4:
            calcular_personas_reservadas()
        else:
            break

menu()


