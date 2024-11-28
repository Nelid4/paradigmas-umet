"""Se pide desarrollar un programa que permita analizar las ventas de una tienda de ropa. 
Ingresar la cantidad de prendas vendidas y el  precio de cada una. Calcular el total de ventas
del día, el promedio del precio de las prendas vendidas y la cantidad de ventas que fueron
superiores a $500. Finalizar el registro cuando se ingrese "0" como cantidad de prendas."""

prendas_vendidas = 0
ventas_dia = 0
valor_prenda = 0
total_valor = 0
promedio = 0
prendas_mayor_500 = 0



while True:
    prendas_vendidas = int(input("Ingrese prendas vendidas o 0 para fin: "))
    if prendas_vendidas == 0:
        print("Finalizando...")
        break
    while prendas_vendidas < 0:
        prendas_vendidas = int(input("Ingrese prendas vendidas: "))
        
    ventas_dia = ventas_dia + prendas_vendidas
    for i in range(1, prendas_vendidas +1):
        valor_prenda = float(input("ingrese valor de a prenda: "))
        total_valor += valor_prenda
        if valor_prenda > 500:
            prendas_mayor_500 += 1
    promedio = total_valor / ventas_dia
print(f"ventas del dia: {ventas_dia}.\npromedio precio ventas: {promedio}\nprendas valor myor a 500: {prendas_mayor_500} ")