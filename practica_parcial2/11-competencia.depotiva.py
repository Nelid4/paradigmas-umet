"""3. Competencia Deportiva
Un club deportivo organiza una competencia y necesita registrar los puntajes de los participantes. Crea un programa que permita:

Registrar participantes con sus nombres y puntajes en diferentes rondas.
Consultar el puntaje total de un participante específico.
Mostrar el participante con el puntaje más alto.
obtener el promedio de puntos por participante"""

datos_competencia={}

def registar_puntos():
    nombre = input("Ingrese el nombre: ")
    puntos = float(input("Ingrese los puntos: "))

    if nombre in datos_competencia:
        datos_competencia[nombre].append(puntos)
    else:
        datos_competencia[nombre]=[puntos]
    print(datos_competencia)

def consultar_puntaje():
    busqueda = input("Ingrese le nombre que busca: ")
    encontrado = False
    puntaje_total=0
    for nombre, puntos in datos_competencia.items():
        if busqueda== nombre:
            puntaje_total = sum(puntos)
            print(f"{nombre} tiene {puntaje_total} puntos.")
            encontrado=True
    if not encontrado:
        print("No se encontró al participante.")

def obteenr_mayor_puntaje():
    mayor_puntaje=None
    mayor_nombre=""
    for nombre, puntos in datos_competencia.items():
        if mayor_puntaje ==None or mayor_puntaje < sum(puntos):
            mayor_puntaje = sum(puntos)
            mayor_nombre = nombre
    print(f"Puntaje mas alto: {mayor_nombre} con {mayor_puntaje}")

def calcular_promedio():
    promedio=0
    for nombre, puntos in datos_competencia.items():
        promedio = sum(puntos)/len(puntos)
        print(f"El promedio de {nombre} es: {promedio}")
    return promedio



def menu(promedio):
    while True:
        print(f"""\n----MENÚ----
        1-registrar puntos o participantes
        2-consultar puntaje x participante
        3-mostrar mayor puntaje
        4-promedio de puntaje x participante
        5-salir
              mira el promedio:{promedio} """)
        opcion = int(input("Ingrese opcion: "))
        if opcion == 1:
            registar_puntos()
        elif opcion ==2:
            consultar_puntaje()
        elif opcion==3:
            obteenr_mayor_puntaje()
        elif opcion ==4:
            calcular_promedio()
        elif opcion ==5:
            break
        else:
            print("Elija una opcion valida")

menu()