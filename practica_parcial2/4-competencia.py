"""Un club organiza una competencia deportiva donde cada participante registra su tiempo en segundos al completar una carrera.

Permitir al usuario registrar los tiempos de varios participantes, identificados por su nombre.
Mostrar un menú con las siguientes opciones:
1. Mostrar el nombre del participante con el tiempo más rápido.
2. Mostrar todos los participantes cuyo tiempo sea menor al promedio de la competencia.
3. Listar a los participantes y sus tiempos en orden ascendente de tiempo."""
info_competencia = {"ana": 239, "mike": 270, "thomas": 302, "zoe": 230, "luca": 80}
def registrar_participante():
    nombre = input("Ingrese el nombre del participante: ")
    tiempo = float(input("Ingrese su tiempo en segundos: "))

    info_competencia [nombre] = tiempo
    print(info_competencia)

def calcular_participante_rapido():
    rapido_tiempo= None
    rapido_nombre = ""
    for nombre, tiempo in info_competencia.items():
        if rapido_tiempo == None or rapido_tiempo > tiempo:
            rapido_tiempo = tiempo
            rapido_nombre = nombre

    print(f"El participante más rápido fue: {rapido_nombre} con {rapido_tiempo} segundos.")

def calcular_menor_al_promedio():
    total_tiempo = 0
    total_participantes = 0

    for nombre, tiempo in info_competencia.items():
        total_tiempo += tiempo
        total_participantes += 1

    promedio = total_tiempo / total_participantes
    print("El promedio de la competencia es:", promedio)

    for nombre, tiempo in info_competencia.items():
        if tiempo < promedio:
            print(f"{nombre} tiene un tiempo menor al promedio.")

def ordenar_ascendente():
    # Convertir el diccionario a una lista de tuplas (nombre, tiempo)
    lista_participantes = list(info_competencia.items())

    n = len(lista_participantes)
    for i in range(n):
        for j in range(0, n-i-1):
            # Si el tiempo del participante j es mayor que el de j+1, los intercambiamos
            if lista_participantes[j][1] > lista_participantes[j+1][1]:
                lista_participantes[j], lista_participantes[j+1] = lista_participantes[j+1], lista_participantes[j]

    # Mostrar los participantes ordenados por tiempo ascendente
    print("\nParticipantes ordenados por tiempo ascendente:")
    for nombre, tiempo in lista_participantes:
        print(f"{nombre}: {tiempo} segundos")




def main():
    while True:
        print("""\n
----Competencia----
1- Registrar participante 
2- Partcipante más rápido
3- Participantes con menor tiempo al promedio 
4- Participantes en orden ascendente
5- Salir del menu
--------------------------
""")
        opcion = int(input("Ingrese una opcion del menú: "))
        if opcion == 1:
            registrar_participante()

        elif opcion == 2:
            calcular_participante_rapido()

        elif opcion == 3:
            calcular_menor_al_promedio()

        elif opcion == 4:
            ordenar_ascendente()

        elif opcion == 5:
            break

        else:
            print("Use una opciondel menú.")

main()