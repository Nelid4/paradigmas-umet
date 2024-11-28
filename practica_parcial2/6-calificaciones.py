"""Un profesor necesita llevar el registro de las calificaciones de sus estudiantes en una materia.

Permitir al usuario ingresar las calificaciones de los estudiantes, identificados por su nombre.
Mostrar un menú con las siguientes opciones:
1. Mostrar la nota más alta y el estudiante que la obtuvo.
2. Calcular el porcentaje de estudiantes que aprobaron (nota >= 6).
3. Listar todos los estudiantes ."""

registro_calificaciones = {"ana":2, "mark":9, "mike":7, "pilar":3}

def agregar_estudiante():
    print(registro_calificaciones)
    nombre = input("Ingrese el nombre del estudiantes: ")
    nota = float(input("Ingrese la nota del estudiante: "))
    registro_calificaciones[nombre] = nota

    print(registro_calificaciones)

def mostrar_nota_alta():
    nota_alta = None
    nombre_alto = ""

    for nombre, nota in registro_calificaciones.items():
        if nota_alta == None or nota_alta < nota:
            nota_alta = nota
            nombre_alto = nombre
    print(f"El alumno con la nota más alta es: {nombre_alto} con una nota de {nota_alta}")

def cacular_porcentaje_aprobados():
    cantidad_notas=0
    cantidad_aprobados =0
    for nombre, nota in registro_calificaciones.items():
        cantidad_notas +=1
        if nota >= 7:
            cantidad_aprobados +=1
    porcentaje_aprobados = (cantidad_aprobados/cantidad_notas)*100

    print(f"El porcentaje de aprobados es de: {porcentaje_aprobados}%")

def mostrar_todas_notas():
    for nombre, nota in registro_calificaciones.items():
        print(f"-{nombre}: {nota}")

def menu():
    while True:
        print("""\n
---------menú-----------
  1- Agregar estudiante
  2- Mostrar nota más alta
  3- Porcentaje de aprobados
  4- Mostrar todas las notas
  5- Salir del menú
------------------------
        """)
        opcion = int(input("Ingree una opcion del menú: "))
        if opcion==1:
            print("---AGREGAR ESTUDIANTE---")
            agregar_estudiante()
        elif opcion==2:
            print("---MOSTAR NOTA MAS ALTA---")
            mostrar_nota_alta()
        elif opcion==3:
            print("---MOSTAR PORCENTAJE DE APROBADOS---")
            cacular_porcentaje_aprobados()
        elif opcion==4:
            print("---MOSTAR TODAS LAS NOTAS---")
            mostrar_todas_notas()
        else:
            print("---FIN DEL PROGRAMA---")
            break

menu()