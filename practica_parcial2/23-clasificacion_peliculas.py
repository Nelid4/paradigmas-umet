"""Crea un programa para registrar películas vistas. Cada película tiene un título, un género y una calificación del 1 al 10. 
El programa debe:
Registrar películas vistas.
Mostrar todas las películas de un género específico.
Mostrar la película con la calificación más alta.
Calcular el promedio de calificación de las películas vistas."""

peliculas={}

def agregar_pelicula():
    titulo=input("ingrese le titulo: ").lower()
    genero=input("ingrese el genero: ").lower()
    calificacion=float(input("calificacion de 1 al 10: "))

    peliculas[titulo]={"genero":genero, "calificacion":calificacion}
    print("pelicula agregada")

def mostrar_genero():
    buscar_genero=input("Ingrese el genero: ").lower()
    encontrados=False

    for titulo, info in peliculas.items():
        if buscar_genero==info["genero"]:
            print(f"pelicula: {titulo}")
            encontrados=True
    if not encontrados:
        print("no hay peliculas d ese genero")

def mostrar_mayor_calificacion():
    mayor_calificacion=None
    mayor_titulo=""

    for titulo, info in peliculas.items():
        if mayor_calificacion ==None or mayor_calificacion < info["calificacion"]:
            mayor_calificacion=info["calificacion"]
            mayor_titulo=titulo

    print(f"la mayor calificacion es de{mayor_titulo} con {mayor_calificacion}/10")

def calcular_promedio():
    promedio=0
    suma=0
    cantidad=0
    for titulo, info in peliculas.items():
        suma+=info["calificacion"]
        cantidad+=1
    promedio=suma/cantidad
    print("El promedio de calificaion es:", promedio)


def menu():
    while True:
        print("\n---Menú---\n1-Agregar pelicula\n2-buscar por generok\n3-mostrar mayor calificacion\n4-mostrar promedio\n5-salir")
        opcion=int(input("Ingrese una opcion: "))
        if opcion == 1:
            agregar_pelicula()
        elif opcion == 2:
            mostrar_genero()
        elif opcion ==3:
            mostrar_mayor_calificacion()
        elif opcion ==4:
            calcular_promedio()
        else:
            break

menu()