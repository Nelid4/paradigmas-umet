"""11. Ahorros. Escribir un programa en el cual muestre a fin de año el total de ahorro obtenido, 
si se pide en cada mes el 10% del sueldo ganado."""
#-----> suponiendo que el sueldo sea el mismo a lo largo de todo el año
# declarando variables:
ahorro_total : float;
# inicializando variables:
ahorro_total = 0.0;
#entrada: le pido al usuario que ingrese su sueldo mensual
sueldo_obtenido = float(input("Ingrese su sueldo mensual: $"));
#procesos: calculo el 10% y lo multiplico por 12
ahorro_total = (sueldo_obtenido * 0.10)*12;
#salida: muestro el resultado
print(f"Despues de 12 meses, el ahorro es de: ${ahorro_total}");