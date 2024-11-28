"""Descripción: Estás creando una herramienta que ayuda a los estudiantes a llevar un registro de sus calificaciones y obtener su 
promedio. El objetivo de la aplicación es permitir que el estudiante ingrese varias calificaciones una por una y luego calcule el
promedio de todas ellas.
El programa debe pedir al usuario que ingrese las calificaciones de manera secuencial. Una vez que se hayan ingresado todas las 
notas, deberá calcular y mostrar el promedio al estudiante. Asegúrate de que el programa permita ingresar varias calificaciones 
sin que se detenga antes de tiempo y que el promedio sea calculado correctamente cuando el usuario decida finalizar."""

cantidad = 0;
nota_acumulada = 0;
nota_ingresada = -1;

print("Ingrese sus calificaciones. Ingrese 0 para terminar y calcular el promedio.");

while nota_ingresada != 0:
    nota_ingresada = int(input("Ingrese calificación: "));
    
    if nota_ingresada != 0:
        nota_acumulada += nota_ingresada;
        cantidad += 1;  # Contamos solo las notas válidas

# Si no se ingresaron notas válidas (solo ingresaron 0 al inicio)
if cantidad == 0:
    print("No se ingresaron notas.");
else:
    # obtengo el promedio
    promedio = nota_acumulada / cantidad
    print(f"El promedio de las notas es: {promedio}")

