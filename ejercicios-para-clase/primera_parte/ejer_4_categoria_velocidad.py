"""Descripción: Imagina que estás desarrollando un software para un club de corredores que desea clasificar el rendimiento de sus miembros según la velocidad
promedio de una carrera reciente. El objetivo es determinar en qué categoría de velocidad se encuentra un corredor y proporcionar la clasificación adecuada.
El programa pedirá al usuario que introduzca la distancia recorrida en kilómetros y el tiempo tomado en minutos. 
Con esta información, se calculará la velocidad promedio. Dependiendo de cuán alta o baja sea esta velocidad, el corredor puede ser clasificado como alguien 
que tiene un ritmo más lento, moderado o rápido. Deberás mostrar esta clasificación al usuario, dejando que las circunstancias de la velocidad determinen 
la categoría."""
# declaracion de variables:
velocidad : float;
tiempo_minutos : float;
tiempo_horas : float;
categoria : str;
# inicializacion de variables:
velocidad = 0.0;
tiempo_minutos = 0.0;
tiempo_horas = 0.0;
categoria = "";
# entrda: le pido al usuario que ingree distancia y tiempo
distancia = float(input("Ingresá la distancia recorrida en kilometros: "))
tiempo_minutos = float(input("Ingresá el tiempo tomado en minutos: "))
# proceso;
tiempo_horas = tiempo_minutos / 60;#tiempo de minutos a horas para calcular la velocidad en km/h
velocidad = distancia / tiempo_horas;#establezco la velocidad
# poniendo limites para separar por categorias, determino en donde se encuentra
if velocidad < 8:
    categoria = "Lento"
elif 8 <= velocidad <= 12:
    categoria = "Moderado"
else:
    categoria = "Rápido"
# salida: le msutroa l usuario la velocidad en kmh y la categoria
print(f"La velocidad promedio es de {velocidad} km/h.")
print(f"Entra en la categoria: {categoria}.")

#revisar