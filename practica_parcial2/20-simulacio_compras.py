"""Crea un programa que simule el proceso de compras en línea. El programa debe permitir:

Registrar productos disponibles en la tienda (nombre, precio).
Mostrar una lista de productos con su precio y permitir al usuario agregar productos a su carrito de compras.
Mostrar el total de la compra y los productos agregados al carrito."""

carrito={}
productos={}
def registrar_productos():
    nombre = input("Ingrese nombre del producto: ").lower()
    precio = float(input("Ingrese precio: $"))

    productos[nombre]=precio

def mostrar_productos():
    for nombre, precio in productos.items():
        print(f"{nombre}: ${precio}")

def agregar_productos():
    agregar =input("nombre del producto que quiere agregar: ")
    cantidad=int(input("ingrse la cantidad que quiere llevar: "))

    for nombre, precio in productos.items():
        if agregar in nombre:
            if agregar in carrito:
                carrito[agregar] += precio*cantidad
            else:
                carrito[agregar]=precio*cantidad
            print("producto agregado con éxito!")
# aca quedó medio raro, faltaria el caso de no encontar el producto en productos{}

def finalizar_compra():
    total=0
    for nombre, subtotal in carrito.items():
        print(f"{nombre}: ${subtotal}")
        total += subtotal
    print("El total final es: $", total)

def menu():
    while True:
        print("menú\n1-agregar poducto\n2-agregar al carrito\n3-mostrar catalogo\n4-finalizar compra")
        opcion=int(input("Ingrese una opcion del menu: "))
        if opcion ==1:
            registrar_productos()
        elif opcion==2:
            agregar_productos()
        elif opcion==3:
            mostrar_productos()
        elif opcion==4:
            finalizar_compra()
            break
        else:
            print("Ingrese una opcion válida.")

menu()
