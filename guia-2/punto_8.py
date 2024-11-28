"""Ingresar una serie de números por teclado que representan la cantidad de ventas realizadas en las diferentes sucursales de un 
país de una determinada empresa. Los requerimientos del programa son: Informar la cantidad de ventas ingresadas Total de ventas 
.Candad de ventas cuyo valores te comprendido entre 100 y 300 unidades Candad de ventas con 400,500y600 unidades.Indicar si hubo
 una cantidad de ventas inferior a 50 unidades. Usted deberá ingresar cantidad es de ventas hasta que se ingrese un valor negativo"""

cantidad_ventas = 0
total_ventas = 0
entre100y300 = 0
cantidad456 = 0
cantidad50 = 0

while True:
    cantidad_ventas = int(input("ingrese la cantidad de unidades de la venta: "))
    if cantidad_ventas < 0:
        print("Finlizando...")
        break
    total_ventas += 1
    if cantidad_ventas >= 100 and cantidad_ventas <= 300:
        entre100y300 = entre100y300 + 1

    if cantidad_ventas == 400 or cantidad_ventas == 500 or cantidad_ventas == 600:
        cantidad456 = cantidad456 +1
    
    if cantidad_ventas < 50:
        cantidad50 += 1
    
    print("Cantidad ingresada con éxito...")

print(f"""Las ventas ingresadas son: {total_ventas}
las ventas entre 100 y 300 son: {entre100y300}
Cantidad de ventas igual a 400, 500 o 600: {cantidad456}
Ventas de menos de 50: {cantidad50}""")
