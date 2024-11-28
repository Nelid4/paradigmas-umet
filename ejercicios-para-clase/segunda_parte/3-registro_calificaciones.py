"""En una clase de programación, los estudiantes realizan varias evaluaciones, cada una con una calificación distinta. 
Desarrolla un programa que permita registrar y organizar las calificaciones de cada estudiante para luego realizar algunos 
cálculos básicos.
El programa debe permitir:
-Registrar calificaciones: Para cada estudiante, el programa debe almacenar las calificaciones que obtenga en sus evaluaciones. 
Los estudiantes pueden tener múltiples calificaciones, ya que realizan varias evaluaciones a lo largo del curso.

Cálculos y resultados:
-Calcular y mostrar el promedio de calificaciones de cada estudiante.
-Determinar y mostrar el nombre del estudiante con la calificación más alta de toda la clase (puede ser una calificación obtenida 
en cualquiera de sus evaluaciones).
-Mostrar la lista de estudiantes que tienen un promedio de calificaciones superior a 7."""

total_calificaciones = {}
continuar = ""
promedios_mayor7=[]
mayor_calificacion = -1
mayor_estudiante = ""

# cargando las notas de cada estudiantes
while continuar.lower() != "no":
    alumno = input("\nIngrese el nombre del alumno que quiere agregar: ")
    
    calificacion = []
    notas = -1 
    
    while notas != 0:
        notas = float(input("Ingrese una nota o 0 para terminar la carga: "))
        if notas != 0:
            calificacion.append(notas)

    total_calificaciones[alumno] = calificacion
    
    print(f"Calificaciones de {alumno}: {calificacion}")
    
    continuar = input("¿Quiere agregar más alumnos? (si/no): ")
print("\nCalificaciones finales de los estudiantes:", total_calificaciones)

# calculando el promedio por alumno
print("\nCalculando el promedio de cada estudiantes...\n")

for alumno, calificaciones in total_calificaciones.items():
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"El promedio de {alumno} es: {promedio}")

    # lista con estudiantes con promedio mayor a 7
    if promedio > 7:
        promedios_mayor7.append(alumno)

        # obteniendo alumno con la calificacion mas alta
    for nota in calificaciones:
        if nota > mayor_calificacion:
            mayor_calificacion = nota
            mayor_estudiante = alumno


print("\nLista de estudiantes con promedios mayor a 7:", promedios_mayor7)
print(f"\nEl estudiante con mayor nota es: {mayor_estudiante}, con una calificación de: {mayor_calificacion}")

