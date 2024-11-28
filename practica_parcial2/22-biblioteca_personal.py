"""Crea un programa para gestionar los libros de una biblioteca personal. Cada libro tiene un título, un autor y un estado 
(leído o no leído). El programa debe permitir:
Agregar libros.
Cambiar el estado de un libro a "leído."
Mostrar cuántos libros has leído.
Listar los libros de un autor específico."""

biblioteca = {}
def agregar_libro():
    titulo=input("ingrese el titulo: ").lower()
    autor=input("ingrese el autor: ").lower()
    estado=input("ingrese el estado, leido s/n: ").lower()

    biblioteca[titulo]={"autor":autor, "leido":estado}
    print("libro agregado!")

def cambiar_estado():
    titulo_cambiar=input("ingrese el titulo: ").lower()

    for titulo, info in biblioteca.items():
        if titulo_cambiar==titulo:
            biblioteca[titulo]={"autor":info["autor"], "leido":"s"}
    print("Estado modificado") 

def mostrar_leidos():
    for titulo, info in biblioteca.items():
        estado=info["leido"]
        if estado == "s":
            print(f"{titulo}, leido")

def listar_autor_especifico():
    buscar_autor=input("ingrese autor: ").lower()
    encontrado=False

    for titulo, info in biblioteca.items():
        if buscar_autor ==info["autor"]:
            print(f"{titulo} de {buscar_autor}")
            encontrado=True
    
    if not encontrado:
        print("no se encontró el autor")

def menu():
    while True:
        print("\n---Menú---\n1-Agregar libro\n2-actualizar estado\n3-mostrar libro leidos\n4-mostrar libro por autor\n5-salir")
        opcion=int(input("Ingrese una opcion: "))
        if opcion == 1:
            agregar_libro()
        elif opcion == 2:
            cambiar_estado()
        elif opcion ==3:
            mostrar_leidos()
        elif opcion ==4:
            listar_autor_especifico()
        else:
            break

menu()