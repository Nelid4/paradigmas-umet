"""Una fundación lleva un registro de donaciones recibidas. Crea un programa que permita:

Registrar donaciones con el nombre del donante y el monto donado.
Consultar cuánto ha donado un donante específico.
Listar a los donantes que han contribuido más de $500.
Calcular el monto total donado."""

donaciones = {}

def registrar_donacion():
    nombre = input("nombre del donante: ").lower()
    monto = float(input("Ingrese el monto donado: $"))
    donaciones[nombre]=monto

def consultar_donacion():
    consulta = input("Ingrese nombre que quiere buscar: ").lower()
    encontrado = False

    for nombre, monto in donaciones.items():
        if consulta == nombre:
            print(f"-{nombre} donó: ${monto}")
            encontrado =True
    
    if not encontrado:
        print("No se encontró al donante.")

def listar_donantes():
    for nombre, monto in donaciones.items():
        if monto > 500:
            print(f"{nombre} donó mas de $500. (${monto})")

def calcular_monto():
    monto_total =0
    for nombre, monto in donaciones.items():
        monto_total += monto
    print("El monto total es: $", monto_total)

def menu():
    while True:
        print("""\n----MENÚ----
        1-resgistrar ddonaciones
        2-consultar donacion por nombre
        3-listar donantes con mas de $500
        4-calcular monto total
        5-salir""")
        opcion = int(input("Ingrese opcion: "))
        if opcion == 1:
            registrar_donacion()
        elif opcion ==2:
            consultar_donacion()
        elif opcion==3:
            listar_donantes()
        elif opcion ==4:
            calcular_monto()
        elif opcion ==5:
            break
        else:
            print("Elija una opcion valida")

menu()


