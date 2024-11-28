"""Un colegio necesita llevar un registro de asistencias diarias de estudiantes. Crea un programa que permita:

Agregar estudiantes con su asistencia diaria (presente/ausente).
Consultar la cantidad de días que un estudiante estuvo presente.
Listar estudiantes que estuvieron ausentes más del 50% de los días registrados.
Calcular el porcentaje promedio de asistencia de toda la clase."""

resgistro_completo = {"ana":["P", "A", "A", "P", "P"], "nolan":["P", "A", "P", "P"],"mike":["A", "A", "P"]}

def agregar_asistencia():
    nombre = input("Ingrese el nombre del alumno: ")
    asistencia = input("Ingrese por A para ausente o P para presente: ").upper()
    
    if nombre in resgistro_completo:
        resgistro_completo[nombre].append(asistencia)
    else:
        resgistro_completo[nombre] = [asistencia]

def consultar_dias():
    total_presente = 0
    for nombre, asistencia in resgistro_completo.items():
        total_presente = asistencia.count("P")
        print(f"{nombre} se presentó {total_presente} días.")

def calcular_ausentes():
    ausentes =0
    porcentaje=0
    total_dias=0
    for nombre, asistencia in resgistro_completo.items():
        total_dias = len(resgistro_completo[nombre])
        ausentes = asistencia.count("A")
        porcentaje = (ausentes/total_dias)*100
        if porcentaje > 50:
            print(f"{nombre}: {porcentaje}")

def calcular_promedio_general():
    total_dias =0
    presentes =0
    promedio=0
    total_estudiantes=0
    promedio_general=0

    for nombre, asistencia in resgistro_completo.items():
        total_dias = len(resgistro_completo[nombre])
        presentes = asistencia.count("P")
        promedio= presentes/total_dias
        total_estudiantes = len(resgistro_completo)
        promedio_general += promedio
    print(f"Promedio de aistencia:{(promedio_general/total_estudiantes)*100}")

def menu():
    while True:
        print("""----MENÚ----
        1-agregar estudiante
        2-consultar dias presentes x estudiante
        3-estudiantes con ausencia +50%
        4-porcentaje promedio total de assitencia
        5-salir""")
        opcion = int(input("Ingrese opcion: "))
        if opcion == 1:
            agregar_asistencia()
        elif opcion ==2:
            consultar_dias()
        elif opcion==3:
            calcular_ausentes()
        elif opcion ==4:
            calcular_promedio_general()
        elif opcion ==5:
            break
        else:
            print("Elija una opcion valida")

menu()