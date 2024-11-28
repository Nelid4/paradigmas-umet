"""Una tienda de ropa necesita administrar su inventario. Crea un programa que permita:
Agregar un producto con nombre, categoría y cantidad en stock.
Actualizar el stock de un producto (sumar o restar).
Mostrar todos los productos de una categoría específica.
Mostrar el producto con menor cantidad en stock."""

inventario ={"lola":{"categoria":"polleras","stock":20}, 
        "minu":{"categoria":"polleras","stock":10}, 
        "caro":{"categoria":"polleras","stock":7}}
def agregar_producto():
    nombre=input("Ingrese nombre del producto: ").lower()
    categoria=input("Ingrese categoria: ").lower()
    stock=int(input("ingrse stock inicial: "))
    inventario[nombre]={"categoria":categoria, "stock":stock}

def actualizar_stock():
    busqueda=input("nombre del producto que busca: ").lower()
    actualizar=input("Sumar o restas (s/r): ").lower()
    valor=int(input("ingrese valor: "))

    for nombre, info in inventario.items():
        if busqueda == nombre:
            if actualizar == "s":
                inventario[nombre]={"categoria":info["categoria"], "stock": (info["stock"]+valor)}
            else:
                inventario[nombre]={"categoria":info["categoria"], "stock": (info["stock"]-valor)}
    print("stock actualizado!")

def mostrar_productos():
    buscar=input("ingrese la categoria: ").lower()
    for nombre, info in inventario.items():
        categoria=info["categoria"]
        if buscar == categoria:
            print(f"{nombre}, {categoria}, stock:{info["stock"]}")

def mostrar_menor_stock():
    menor_stock=None
    menor_nombre=""
    for nombre, info in inventario.items():
        if menor_stock == None or menor_stock > info["stock"]:
            menor_stock=info["stock"]
            menor_nombre=nombre
    print(f"{menor_nombre} tiene el menor stock: {menor_stock}")

def menu():
    while True:
        print("\n---Menú---\n1-Agregar un producto\n2-actualizar stock\n3-mostrar producto por categoria\n4-mostrar producto con menor stock\n5-salir")
        opcion=int(input("Ingrese una opcion: "))
        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            actualizar_stock()
        elif opcion ==3:
            mostrar_productos()
        elif opcion ==4:
            mostrar_menor_stock()
        else:
            break

menu()