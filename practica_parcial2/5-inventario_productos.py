"""Una tienda de electrodomésticos necesita organizar su inventario. Cada producto tiene un nombre y una cantidad disponible en stock.

Permitir al usuario agregar o actualizar productos en el inventario.
Si el producto ya existe, permitir actualizar la cantidad (sumar o restar).
Si no existe, agregarlo al inventario con la cantidad inicial ingresada.
Mostrar un menú con las siguientes opciones:
1. Buscar un producto por nombre y mostrar su cantidad disponible.
2. Listar los productos que tienen menos de 10 unidades en stock.
3. Mostrar el producto con la mayor cantidad en stock."""

inventario = {"horno":20, "cafetera":5}

def manejar_inventario():
    nombre = input("Ingrese el nombre del producto: ")
    stock = int(input("Ingrese cantidad de stock: "))
    
    if nombre in inventario:
        print(f"El producto '{nombre}' ya existe. Actualizando cantidad...")
        inventario[nombre] += stock  
    else:
        print(f"Agregando nuevo producto '{nombre}' al inventario...")
        inventario[nombre] = stock  
    print(f"Producto '{nombre}' ahora tiene {inventario[nombre]} unidades.\n")

def buscar_producto():
    busqueda = input("Ingrese el nombre del producto que quiere buscar: ").lower()

    if busqueda in inventario:
        print(f"-Stock de {busqueda}: {inventario[busqueda]}")
    else:
        print(f"-{busqueda} no se encuentra entre nuestros productos.")

def calcular_menor10_stock():
    for nombre, stock in inventario.items():
        if stock < 10:
            print(f"-{nombre} tiene menos de 10 unidades en stock({stock}).")

def mostrar_mayor_cantidad():
    mayor_stock=None
    mayor_nombre=""
    for nombre, stock in inventario.items():
        if mayor_stock == None or mayor_stock < stock:
            mayor_stock = stock
            mayor_nombre = nombre

    print(f"El producto con mayor stock es: {mayor_nombre} con {mayor_stock} unidades en stock.")

def menu():
    while True:
        print("""\n
---------------Menú-------------
1- Agregar o actualizar stock
2- Buscar produto y mostrar stock
3- Productos con menos de 10 uidades
4- Mostrar producto com mayor cantidad en stock
5- Salir del menú
---------------------------------
        """)
        opcion = int(input("Elija una opcion del menú: "))
        if opcion== 1:
            manejar_inventario()

        elif opcion ==2:
            buscar_producto()

        elif opcion ==3:
            calcular_menor10_stock()

        elif opcion == 4:
            mostrar_mayor_cantidad()

        else:
            break

menu()
