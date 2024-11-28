"""Se pide desarrollar un programa para un cine que permita vender boletos a los clientes. 
El programa debe solicitar la cantidad de boletos a comprar y el tipo de sala (2D o 3D). 
Por sala entran 30 personas, mostrar cuantos asientos quedan disponibles para cada sala a medida que se venden boletos.
Calcular el total a pagar según el tipo de sala (el boleto 3D cuesta un 20% más), valor base de entrada en 50.
También se debe registrar cuántos boletos se vendieron para cada tipo de sala. 
Finalizar cuando se ingresen "0" boletos."""
cantidad2d = 30
cantidad3d = 30
compra = 0
sala = ""
ventas3d = 0
ventas2d = 0
VALOR2D= 50
VALOR3D = VALOR2D + (VALOR2D * 0.20)

while True: 
    print(f"Cantidad disponible en 3D: {cantidad3d} y 2D: {cantidad2d}")
    compra = int(input("Cuantos boletos va a comprar (0 para fin): "))

    if compra <= 0:
        print("Finalizando...")
        break
    else:
        sala = input("¿En 3D o 2D?: ").upper()
        while sala != "3D" and sala != "2D":
            sala = input("Ingrese 3D o 2D: ").upper()
        
        
        if sala == "3D":
            if cantidad3d - compra < 0:
                print("No se puede realizar la compra, solo quedan:", cantidad3d, "boletos")
            else:
                cantidad3d -= compra
                print("El total a pagar es: $", compra * VALOR3D)
                ventas3d += compra
        else:
            if cantidad2d - compra < 0:
                print("No se puede realizar la compra, solo quedan:", cantidad2d, "boletos")
            else:
                cantidad2d -= compra
                print("El total a pagar es: $", compra * VALOR2D)
                ventas2d += compra
        print("Compra exitosa")

print(f"Total de entradas vendidas para 2D: {ventas2d} y para 3D: {ventas3d}")
