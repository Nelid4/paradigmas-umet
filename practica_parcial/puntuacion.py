"""Se pide desarrollar un programa que registre las puntuaciones de varios jugadores en un torneo de videojuegos. Ingresar el 
nombre del jugador y su puntuación. Determinar cuántos jugadores tienen una puntuación mayor a 500 y cuántos la tienen menor o 
igual a 500. Mostrar el nombre del jugador con la puntuación más alta y la más baja. Finalizar el registro ingresando "fin" como 
nombre del jugador. determinar porcentaje de jugadores con mas de 500 puntos"""

jugador=""
puntuacion=0.0
cantidad_jugadores=0
puntuacion_alta=0
puntuacion_baja=0
jugador_alta=""
jugador_baja=""
puntuacion_mayor_500=0
puntuacion_menor_500 =0

while True:
    jugador=input("ingrese el nombre del jugador: ").lower()
    if jugador=="fin":
        print("finalizaando programa...")
        break 
    else:
        puntuacion=float(input("ingrese puntuacion: "))
        cantidad_jugadores +=1
        if cantidad_jugadores==1:
            puntuacion_alta=puntuacion
            puntuacion_baja=puntuacion
        else:
            if puntuacion_alta < puntuacion:
                puntuacion_alta=puntuacion
                jugador_alta=jugador

            if puntuacion_baja > puntuacion:
                puntuacion_baja=puntuacion
                jugador_baja =jugador
        
        if puntuacion > 500:
            puntuacion_mayor_500 += 1
        if puntuacion <= 500:
            puntuacion_menor_500 += 1

print(f"""puntuacion mayor a 500: {puntuacion_mayor_500}
puntuacion menor o igual a 500: {puntuacion_menor_500}
jugador mas alta puntuacion: {jugador_alta} con {puntuacion_alta} puntos
jugador mas baja puntuacion: {jugador_baja} con {puntuacion_baja} puntos
el porcentje de jugadores con mas de 500 puntos es: {(puntuacion_mayor_500 / cantidad_jugadores) * 100}
""")
