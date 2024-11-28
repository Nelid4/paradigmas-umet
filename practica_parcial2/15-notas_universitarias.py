"""Un profesor desea llevar un registro de las notas de sus estudiantes. Crea un programa que permita:

Registrar estudiantes con sus nombres y notas de diferentes exámenes.
Consultar el promedio de notas de un estudiante específico.
Mostrar el estudiante con el promedio más alto.
Listar a todos los estudiantes con promedios menores a 4 (reprobados)."""

total_notas={"ana":[9,10,8.5], "mike":[2,4,3]}
def registrar_estudiante():
    nombre=input("ingrese el nombre: ").lower()
    nota=float(input("ingrese nota: "))

    if nombre in total_notas:
        total_notas[nombre].append(nota)
    else:
        total_notas[nombre]=[nota]

def consultar_promedio():
    promedio=0
    busqueda = input("ingrese el nombre q busca: ").lower()
    encontrado=False

    for nombre, notas in total_notas.items():
        if busqueda == nombre:
            promedio=sum(notas)/len(notas)
            print(f"promedio de {nombre}: {promedio}")
            encontrado = True

    if not encontrado:
        print("no se encontro al alumno")

def mostrar_mayor_promedio():
    mayor_promedio =None
    mayor_nombre=""
    promedio =0

    for nombre, notas in total_notas.items():
        promedio=sum(notas)/len(notas)
        if mayor_promedio == None or mayor_promedio < promedio:
            mayor_promedio = promedio
            mayor_nombre = nombre
    print(f"{mayor_nombre}: {mayor_promedio}, mayor promedio")

def obtener_desaprobados():
    promedio =0
    for nombre, notas in total_notas.items():
        promedio=sum(notas)/len(notas)
        if promedio < 4:
            print(f"-{nombre}: {promedio}, reprobado")

def menu():
    while True:
        print("\n---Menú---\n1-registrar alumno\n2-Consultar promedio por estudiante\n3-mostrar mayor promedio\n4-mostrar reprobados\n5-salir")
        opcion=int(input("Ingrese una opcion: "))
        if opcion == 1:
            registrar_estudiante()
        elif opcion == 2:
            consultar_promedio()
        elif opcion ==3:
            mostrar_mayor_promedio()
        elif opcion ==4:
            obtener_desaprobados()
        else:
            break

menu()
