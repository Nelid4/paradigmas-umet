"""Se pide desarrollar un programa para un restaurante que permita registrar los pedidos de los clientes.
Cada pedido debe incluir la cantidad de platos solicitados y su costo unitario. El programa debe calcular el costo total de cada 
pedido. Se debe registrar el total de pedidos realizados durante el día y mostrar cuántos fueron superiores a $1000. Finalizar 
el registro cuando se ingrese "0" como cantidad de platos."""
pedido = 0
costo_unitario = 0
costo_total = 0
ganancia_total = 0
pedidos_totales = 0
pedido_mayor_mil = 0

while True:
    pedido = int(input("Ingrese cantidad de platos del pedido: "))
    if pedido <= 0:
        print("Finalizando...")
        break
    else:
        for i in range(1, pedido +1):
            costo_unitario = float(input("Ingrese el el costo de cada plato: $"))
            costo_total = costo_total + costo_unitario
        pedidos_totales += 1
        if costo_total > 1000:
            pedido_mayor_mil += 1
        print("-El costo total del pedido es de : $", costo_total)
        ganancia_total = ganancia_total + costo_total
        costo_unitario = 0
        costo_total = 0

print(f"""Los pedidos totales son: {pedidos_totales}
Las ganancias totales son: $ {ganancia_total}
La cantidad de pedidos superior a $1000 fueron: {pedido_mayor_mil}""")
