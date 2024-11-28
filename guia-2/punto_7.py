"""7.Complejo de cines Desarrollar un programa que permita procesar funciones de un complejo de cines. Por cada función se conoce:
cantidad de espectadores y descuento(S/N)
.La carga termina cuando la cantidad de espectadores sea igual a 0(cero).
El programa deberá:Calcular la recaudación total del complejo,considerando que el valor de la entrada e sde$50en los días con descuento
 y $75 en los días sin descuento.
 Determinar cuántas funciones con descuentos efectuaron y qué porcentaje representan sobre el total de funciones"""

descuento = ""
entradas_sin_d = 0
entradas_con_d = 0
funcion_con_d = 0
funcion_sin_d = 0
espectadores_con_d = 0
espectadores_sin_d = 0
valor_sin_d = 0
valor_con_d = 0
total_recaudado = 0
total_funciones = 0


funciones = int(input("Ingrese la cantidad de funciónes: "))

for i in range(1, funciones + 1):
    print("\nFuncion n°: ", i)
    descuento = input("¿La función tiene descuento?(si/no): ")
    while descuento.lower() != "si" and descuento.lower() != "no":
        descuento = input("¿La función tiene descuento? Responda por si o no: ")
    if descuento == "si":
        funcion_con_d += 1
        while True:
            espectadores_con_d = int(input("Ingrese cantidad de espectadores con descuento. Ingrese 0 para finalizar: "))
            entradas_con_d = entradas_con_d + espectadores_con_d
            if espectadores_con_d == 0:
                break
    
    else:
        funcion_sin_d += 1
        while True:
            espectadores_sin_d = int(input("Ingrese cantidad de espectadores sin descuento. Ingrese 0 para finalizar: "))
            entradas_sin_d = entradas_sin_d + espectadores_sin_d
            if espectadores_sin_d == 0:
                break

valor_con_d = entradas_con_d * 50
valor_sin_d = entradas_sin_d * 75

total_recaudado = valor_sin_d + valor_con_d
total_funciones = funcion_con_d + funcion_sin_d

print(f"La recaudacion total es de : ${total_recaudado}")
print(f"Las funciones totales son: {total_funciones}, de las cueles {funcion_con_d} son con descuento, lo que representa un %{(funcion_con_d/total_funciones)*100}")

