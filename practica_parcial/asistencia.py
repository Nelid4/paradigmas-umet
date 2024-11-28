"""Se pide desarrollar un programa para un docente que permita registrar la asistencia de los estudiantes de una clase. 
Se ingresan los nombres de los estudiantes y se debe indicar si están presentes (P) o ausentes (A). Al finalizar, el programa debe
calcular el porcentaje de asistencia y mostrar cuántos estudiantes asistieron y cuántos no. Terminar la carga ingresando "FIN" 
como nombre del estudiante."""
estudiante = ""
asistencia = ""
ausentes = 0
presentes = 0
total_alumnos = 0

while True:
    estudiante = input("Ingrese el nombre: ").upper()
    while estudiante == "":
        estudiante = input("Ingrese el nombre, por favor: ").upper()
    
    if estudiante == "FIN":
        break
    
    asistencia = input(f"Está {estudiante} presente o ausente (P/A): ").upper()
    while asistencia != "A" and asistencia != "P":
        asistencia = input(f"Está {estudiante} P/A: ").upper()

    if asistencia == "A":
        ausentes += 1
    else:
        presentes += 1

total_alumnos = ausentes+ presentes
print(f"Total de alumnos que asistieron: {total_alumnos}\nAlumnos ausentes: {ausentes}\nAlumnos preentes: {presentes}, porcentaje de alumnos que asistieron: %{(presentes / total_alumnos) * 100}")