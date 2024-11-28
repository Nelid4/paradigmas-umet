"""Comisión de vendedores Una empresa debe calcular el total de comisiones que debe abonar por ventas realizadas por sus vendedores
para ello les solicita un sistemita que le permita calcular dichos montos. Se tiene conocimiento que la empresa tiene cuatro 
categorías de vendedores(1 a 4).Usted debe solicitar el ingreso de la categoría del vendedor y el total de la venta(el proceso 
termina cuando se ingrese una categoría igual a cero) y acumular las comisiones de las ventas rendidas por los vendedores de 
diferentes en base a los siguientes cálculos: 
Categoría1:cobra una comisión de 10% 
Categoría2: cobra una comisión de 25% 
Categoría3:cobra una comisión de 30% 
Categoría4:cobra una comisión de 40% 
Una vez procesadas todas las ventas mostrar el total de comisiones a pagar por cada categoría de vendedor es que en el la empresa
junto con el total general
"""
categoria = 0
venta1 = 0
venta2 = 0
venta3 = 0
venta4 = 0
comision1 =0
comision2 =0
comision3 =0
comision4 =0
total1= 0
total2= 0
total3= 0
total4= 0
ventas_totales= 0

while True:
    categoria = int(input("\nIngrese la tegoria del 1 al 4, o 0 para terminar: "))
    while categoria > 4 or categoria < 0:
        categoria = int(input("Por favor,ingrese la tegoria del 1 al 4, o 0 para terminar: "))
    
    if categoria == 1:
        venta1 = float(input("ingresá el total de la venta: $"))
        comision1 = venta1 * 0.10
        total1 = total1 + comision1
    elif categoria == 2:
        venta2 = float(input("ingresá el total de la venta: $"))
        comision2 = venta2 * 0.25
        total2 = total2 + comision2
    elif categoria == 3:
        venta3 = float(input("ingresá el total de la venta: $"))
        comision3 = venta3 * 0.30
        total3 = total3 + comision3
    elif categoria == 4:
        venta4 = float(input("ingresá el total de la venta: $"))
        comision4 = venta4 * 0.40
        total4 = total4 + comision4
    else:
        print("Finalizando...")
        break

    print("Comision guardada.")

ventas_totales = total1 + total2 + total3 + total4
print(f"""El total de las comisiones por categoria es:
    -Categoria 1 : ${total1}
    -Categoria 2 : ${total2}
    -Categoria 3 : ${total3}
    -Categoria 4 : ${total4}
Y el total general es : ${ventas_totales}
""")
