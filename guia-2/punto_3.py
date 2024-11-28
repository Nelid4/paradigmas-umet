"""Sueldos y aguinaldo
Ingresar por teclado los sueldos de un vendedor, correspondientes al primer semestre del año y luego:
a) Calcular su aguinaldo, sabiendo que es la mitad del sueldo más alto del período.
b) Determinar en qué mes recibió el sueldo más bajo del período.
c) Informar el sueldo promedio del semestre.
"""
sueldo_ingresado = 0.0;
sueldo_mayor = 0.0;
sueldo_menor = 0.0;
sueldo_total = 0.0;
mes = 0;
mes_sueldo_menor = "";

for i in range (1, 7):
    if i == 1:
        mes = "Enero"
    elif i == 2:
        mes = "Febrero"
    elif i == 3:
        mes = "Marzo"
    elif i == 4:
        mes = "Abril"
    elif i == 5:
        mes = "Mayo"
    else:
        mes = "Junio"
    
    sueldo_ingresado = float(input(f"Ingrese el sueldo de {mes}: $"));
    sueldo_total = sueldo_total + sueldo_ingresado;
    
    if i == 1:
        sueldo_mayor = sueldo_ingresado;
        sueldo_menor = sueldo_ingresado;

    if sueldo_ingresado > sueldo_mayor:
        sueldo_mayor = sueldo_ingresado;

    if sueldo_ingresado < sueldo_menor:
        sueldo_menor = sueldo_ingresado;
        mes_sueldo_menor = mes

print("El aguinaldo será de: $", (sueldo_mayor/2));
print(f"El mes con el sueldo menor fué: {mes_sueldo_menor}, con ${sueldo_menor}");
print("El sueldo promedio es de: $", (sueldo_total/6))