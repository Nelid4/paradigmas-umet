"""2 Análisis de Ventas Mensuales por Sucursal
Una tienda registra sus ventas mensuales en diferentes sucursales. Cada venta tiene un monto en pesos y está asociada a una 
sucursal específica. Se necesita desarrollar un programa para analizar estas ventas y proporcionar información importante a la 
gerencia.
El programa debe permitir:
-Calcular el total de ventas de la tienda: Sumar el monto de todas las ventas realizadas en todas las sucursales y mostrar el total.

-Identificar la sucursal con mayores ventas acumuladas: Determinar cuál sucursal ha generado el monto total más alto en ventas y
mostrar el número de esta sucursal junto con su total acumulado.

-Calcular el promedio de ventas por sucursal: Para cada sucursal, mostrar el promedio de ventas, considerando todas las ventas 
registradas para esa sucursal.

Ejemplo de datos:
Supongamos que la tienda tiene ventas como las siguientes:

Sucursal 1 tuvo una venta de $1000.
Sucursal 2 tuvo una venta de $1500.
Sucursal 1 tuvo otra venta de $750.
Sucursal 3 tuvo una venta de $1200.
Sucursal 2 tuvo otra venta de $500.
El programa debería ser capaz de:

Sumar el total de todas las ventas.
Identificar que la sucursal con mayores ventas acumuladas es la sucursal 2, con $2000.
Calcular y mostrar el promedio de ventas de cada sucursal."""
ventas_registradas = {}
continuar = "si"
ventas_totales = 0
mayor_venta = 0
mayor_sucursal = ""

# registrando ventas
while continuar.lower() != "no":
    nombre_sucursal = input("\nIngrese el número o nombre de la sucursal: ")
    venta_mensual = float(input("Ingrese el monto de la venta en pesos: $"))
    
    if nombre_sucursal in ventas_registradas:
        ventas_registradas[nombre_sucursal].append(venta_mensual)
    else:
        ventas_registradas[nombre_sucursal] = [venta_mensual]

    continuar = input("¿Quiere continuar agregando ventas por sucursal? (si/no): ")

for sucursal, ventas in ventas_registradas.items():
# total de ventas de todas las tiendas
    total_sucursal = sum(ventas)
    ventas_totales += total_sucursal
    
    # la mayor venta 
    if total_sucursal > mayor_venta:
        mayor_venta = total_sucursal
        mayor_sucursal = sucursal

    # promedio de ventas por sucursal
    promedio_sucursal = total_sucursal / len(ventas)
    print(f"\nEl promedio de ventas de la sucursal {sucursal} es: ${promedio_sucursal}")

print("\nEl total de ventas de la tienda es: $", ventas_totales)
print("La sucursal con mayores ventas acumuladas es:", mayor_sucursal, "con: $", mayor_venta)
