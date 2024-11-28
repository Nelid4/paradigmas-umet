"""Consigna 1: Inventario de Librería
Se pide desarrollar un programa para gestionar el inventario de una librería. Cada vez que se realice una venta, el programa debe 
pedir el nombre del libro, la cantidad vendida, y verificar si hay suficiente inventario para cubrir la venta. Si la venta es 
exitosa, se debe actualizar el inventario. Al final del día, el programa debe mostrar el valor total de las ventas, los libros más 
y menos vendidos, y el porcentaje del inventario inicial que ha sido vendido. Finalizar la operación cuando se ingrese "FIN" como 
nombre del libro."""
el_principito = 10
gato_negro=10
rayuela =10
titulo = ""
cantidad_vendida = 0
ventas_totales = 0
venta_principito = 0
venta_gato_negro = 0
venta_rayuela =0 
inventario_inicial = gato_negro+ el_principito+rayuela
print(f"Libros stock:\nEl principito:{el_principito}\nRayuela:{rayuela}\nGato Negro:{gato_negro}")

while True: 
    titulo=input("Ingrese nombre o fin: ").upper()
    while titulo == "":
        titulo=input("Ingrese nombre o fin: ").upper()
    if titulo == "FIN":
        break
    while titulo != "EL PRINCIPITO" and titulo != "RAYUELA" and titulo != "GATO NEGRO":
        titulo=input("Ingrese nombre o fin: ").upper()

    cantidad_vendida = int(input("Ingrese cantidad vendida: "))
    while cantidad_vendida <= 0:
        cantidad_vendida=int(input("Ingrese cantidad vendida: "))

    if titulo == "EL PRINCIPITO":
        if cantidad_vendida > el_principito:
            print("No se puede realizar la venta, el stock es:", el_principito)
        else:
            el_principito -= cantidad_vendida
            ventas_totales += cantidad_vendida
            print("Venta exitosa")
            venta_principito += cantidad_vendida

    elif titulo == "RAYUELA":
        if cantidad_vendida > rayuela:
            print("No se puede realizar la venta, el stock es:", rayuela)
        else:
            rayuela-= cantidad_vendida
            ventas_totales += cantidad_vendida
            print("Venta exitosa")
            venta_rayuela += cantidad_vendida

    else:
        if cantidad_vendida > gato_negro:
            print("No se puede realizar la venta, el stock es:", gato_negro)
        else:
            gato_negro -= cantidad_vendida
            ventas_totales += cantidad_vendida
            print("Venta exitosa")
            venta_gato_negro += cantidad_vendida

    print(f"Libros stock:\nEl principito:{el_principito}\nRayuela:{rayuela}\nGato Negro:{gato_negro}")

print("ventas totas: ", ventas_totales)
inventario_final = el_principito + gato_negro + rayuela
print("El inventario final es:", inventario_final)

# Determinar el libro más y menos vendido
valor_alto = venta_principito
nombre_alto = "El principito"
valor_bajo = venta_principito
nombre_bajo = "El principito"

# Comparación para el libro más vendido
if valor_alto < venta_gato_negro:
    valor_alto = venta_gato_negro
    nombre_alto = "Gato Negro"

if valor_alto < venta_rayuela:
    valor_alto = venta_rayuela
    nombre_alto = "Rayuela"

# Comparación para el libro menos vendido
if valor_bajo > venta_gato_negro:
    valor_bajo = venta_gato_negro
    nombre_bajo = "Gato Negro"

if valor_bajo > venta_rayuela:
    valor_bajo = venta_rayuela
    nombre_bajo = "Rayuela"

print("El mas vendido es ", nombre_bajo)
print("El menos vendido es ", nombre_alto)

print("el porcentaje es: %", (inventario_final/inventario_inicial)*100)

