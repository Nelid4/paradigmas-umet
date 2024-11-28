"""4. Control de Inventario de Librería
Una librería necesita gestionar su inventario. Crea un programa que permita:

Registrar libros con su título, autor y cantidad disponible.
Buscar libros por título o autor.
Listar los libros que tienen menos de 5 copias disponibles.
Calcular el total de libros en la librería."""

inventario ={}

def registar_libros():
    titulo = input("Ingrese el titulo: ").lower()
    autor= input("Ingrese el autor: ").lower()
    cantidad = int(input("Ingrese cantidad disponible: "))

    inventario[titulo] = {"autor": autor, "cantidad":cantidad}

def buscar_libro():
    busqueda = input("ingrese titulo o autor: ").lower()
    encontrado = False
    for titulo,info in inventario.items():
        if busqueda == titulo or busqueda == info["autor"]:
            print(f"titulo:{titulo}, autor:{info["autor"]}, cantidad:{info["cantidad"]}")
            encontrado = True
    if not encontrado:
        print("No se encontró el libro")

def listar_menos_copias():
    MINIMO_COPIAS = 5

    for titulo, info in inventario.items():
        if info["cantidad"] < MINIMO_COPIAS:
            print(f"{titulo} tiene {info["cantidad"]} ejemplares")

def calcular_total_libros():
    total_libros=0
    for titulo, info in inventario.items():
        total_libros+= info["cantidad"]
    print("El total de libros es:", total_libros)

def menu():
    while True:
        print("""\n----MENÚ----
        1-registrar libro
        2-buscar libro por titlo o autor
        3-listar libros con menos de 5 ejemplares
        4-mostarr libros totales
        5-salir""")
        opcion = int(input("Ingrese opcion: "))
        if opcion == 1:
            registar_libros()
        elif opcion ==2:
            buscar_libro()
        elif opcion==3:
            listar_menos_copias()
        elif opcion ==4:
            calcular_total_libros()
        elif opcion ==5:
            break
        else:
            print("Elija una opcion valida")

menu()