"""Sistema de Control de Inventario
Descripción: Estás creando un sistema para controlar el inventario de una tienda. La tienda tiene una lista de productos y sus
respectivas cantidades en stock. El programa debe permitir al usuario ingresar una serie de transacciones diarias, donde cada 
transacción puede ser una compra o una venta de un producto.
El programa debe solicitar al usuario que ingrese el nombre del producto y si es una compra o una venta. Si es una compra, se debe
incrementar la cantidad de ese producto en el inventario; si es una venta, se debe verificar si hay suficiente cantidad en el
stock antes de realizar la transacción. Si no hay suficientes productos en stock, el programa debe mostrar un mensaje adecuado.
A lo largo del día, el sistema debe procesar varias transacciones y, al final, mostrar un resumen del inventario con las 
cantidades finales de cada producto."""
# declaro variables
prod1 : str;
prod2 : str;
prod3 : str;
prod4 : str;
prod5 : str;
seguir : str;

stock1 : int;
stock2 : int;  
stock3 : int; 
stock4 : int;  
stock5 : int; 
# inicializo variables
prod1 = "lapicera";
prod2 = "marcador";
prod3 = "pincel";
prod4 = "cuaderno";
prod5 = "lapiz";
seguir = "si";

stock1 = 9;
stock2 = 8;  
stock3 = 5; 
stock4 = 3;  
stock5 = 10;  


print(f"""-----INVENTARIO INICIAL-----
       *Lapicera : {stock1}
       *Marcador : {stock2}
       *Pincel : {stock3}
       *Cuaderno : {stock4}
       *Lapiz : {stock5}
-----------------------------""")#muestro el inventario inicial

while seguir != "no":#encierro todo en un while para que se repita el proceso hasta que el usuario no quiera mas
    definir_prod = input("Ingrese el nombre del producto: ").lower();
    
    #bucle de validación de producto: mietras que el producto ingresado sea diferente a alguno de la lista
    while definir_prod != prod1 and definir_prod != prod2 and definir_prod != prod3 and definir_prod != prod4 and definir_prod != prod5:
        definir_prod = input("---> Recuerde ingresar un producto válido, uno que esté en la lista: ").lower();
    
    operacion = input("¿Compra o venta? Ingrese la operación que quiere realizar: ").lower();#le solicito la operación al usuario
    
    #bucle de validacion de operacion: se ejecunta mientras que la operacion no sea ni compra ni venta
    while operacion != "compra" and operacion != "venta":
        operacion = input("Operación no válida. Ingrese 'compra' o 'venta': ").lower();

    if operacion == "compra":
        cantidad_compra = int(input("Cuantas unidad/es adquirió: "));
        if definir_prod == prod1:
            stock1 += cantidad_compra;
        elif definir_prod == prod2:
            stock2 += cantidad_compra;
        elif definir_prod == prod3:
            stock3 += cantidad_compra;
        elif definir_prod == prod4:
            stock4 += cantidad_compra;
        else:
            stock5 += cantidad_compra;
        
        print("Se actualizó el stock");

    else:
        cantidad = int(input("Ingrese la cantidad que vendió: "));
        if definir_prod == prod1:
            if stock1 >= cantidad:
                stock1 -= cantidad;
                print("Venta exitosa!");
            else:
                print("No hay suficiente stock para realizar la venta. El stock disponible es: ", stock1);

        elif definir_prod == prod2:
            if stock2 >= cantidad:
                stock2 -= cantidad;
                print("Venta exitosa!");
            else:
                print("No hay suficiente stock para realizar la venta. El stock disponible es: ", stock2);

        elif definir_prod == prod3:
            if stock3 >= cantidad:
                stock3 -= cantidad;
                print("Venta exitosa!");
            else:
                print("No hay suficiente stock para realizar la venta. El stock disponible es: ", stock3);

        elif definir_prod == prod4:
            if stock4 >= cantidad:
                stock4 -= cantidad;
                print("Venta exitosa!");
            else:
                print("No hay suficiente stock para realizar la venta. El stock disponible es: ", stock4);

        else: 
            if stock5 >= cantidad:
                stock5 -= cantidad;
                print("Venta exitosa!");
            else:
                print("No hay suficiente stock para realizar la venta. El stock disponible es: ", stock5);
    
    #le pregunto al usuario si se quiere seguir haciendo operaciones
    seguir = input("¿Quiere hacer otra operación? (si/no): ").lower();

print(f"""------INVENTARIO FINAL------
       *Lapicera : {stock1}
       *Marcador : {stock2}
       *Pincel : {stock3}
       *Cuaderno : {stock4}
       *Lapiz : {stock5}
-----------------------------""");#muestro el inventario final
