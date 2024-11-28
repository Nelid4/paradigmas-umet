"""Eninciado 1 Análisis de Rendimiento en una Carrera de Autos
En una carrera de autos, cada vehículo registra sus tiempos en varias vueltas a lo largo de la competencia. Cada auto tiene un número de identificación único, y se quiere analizar su rendimiento en función de sus tiempos de vuelta.
Desarrolla un programa que permita registrar los tiempos de cada auto y realizar algunos análisis de rendimiento al final de la carrera.

El programa debe poder:

-Registrar tiempos de vuelta para cada auto: A medida que los autos completan vueltas, se debe almacenar el tiempo en segundos de cada vuelta. Si un auto registra múltiples tiempos, todos deben ser guardados para calcular estadísticas al final.
Calcular el tiempo promedio de vuelta para un auto específico: Dado el número de identificación de un auto, calcula y muestra el tiempo promedio de sus vueltas.
Determinar el auto más rápido: Identifica el auto con el menor tiempo promedio de vuelta y muestra su número de identificación y su tiempo promedio.
Mostrar el rendimiento de todos los autos: Muestra el número de identificación de cada auto junto con todos sus tiempos de vuelta registrados."""

carrera_completa={}
autos=[]

vueltas = int(input("---->Ingrese la cantidad de vueltas que tiene la competencia: "))


def definir_auto():
    while True:
        competidor = input("Ingrese el número de único de competidor (0 para finalizar): ")
        if competidor == "0":
            print("Carga finalizada...\n")
            break

        if competidor in autos:
            print("El número que ingresó ya pertenece a otro auto.")

        else:
            autos.append(competidor)
            print("Auto agregado con éxito\n")


def definir_tiempo():
    for i in range(vueltas):
        print(f"Vuelta: {i + 1}")

        for j in autos:
            tiempo_inicial = float(input(f"Ingrese el tiempo del auto '{j}' en segundos: "))
            if j not in carrera_completa:
                carrera_completa[j] = []
            carrera_completa[j].append(tiempo_inicial)

def calcular_promedio():
    for auto, tiempos in carrera_completa.items():
        suma_total = sum(tiempos)
        promedio = suma_total / len(tiempos)
        print(f"El promedio de tiempo del auto '{auto}' es: {promedio} segundos.")

def mostrar_auto_rapido():
    mejor_auto = None
    mejor_tiempo = None

    for auto, tiempos in carrera_completa.items():
        for tiempo in tiempos:
            if mejor_tiempo is None or tiempo < mejor_tiempo:
                mejor_tiempo = tiempo
                mejor_auto = auto

    print(f"El auto con el tiempo más rápido es '{mejor_auto}' con un tiempo de {mejor_tiempo} segundos.")


def menu():
    while True:
        print("""
1- Mostrar promedio.
2- Mostrar auto mas rápido.
3- Mostrar rendimiento de todos los autos.
4- Salir""")
        opcion = int(input("Ingrese una opcion del menú: "))
        while 1 < opcion > 4 :
            opcion = int(input("Ingrese una opcion válida del menú: "))
    
        if opcion == 1:
            print("\n---PRMEDIOS---")
            calcular_promedio()
    
        elif opcion == 2:
            print("\n---AUTO MÁS RÁPIDO---")
            mostrar_auto_rapido()

        elif opcion == 3:
            print("\n---RENDIMIENTOS---")
            print(carrera_completa)

        else: 
            print("\nSaliendo del programa...")
            break



def main():
    print("|| Binevenid@ al programa de análisis de rendimiento para carreras de autos ||")
    definir_auto()
    definir_tiempo()
    menu()

main()


