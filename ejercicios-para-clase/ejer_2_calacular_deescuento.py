"""Diseña un programa que calcule el precio final de un producto despues de aplicar un descuento basado en el valor de la compra.
Requisitos:
1. El programa debe solicitar al usuario que ingrese el precio original de un producto.

2. Utiliza variables para almacenar el precio original, el descuento a aplicar, y el precio final.

3. Define los siguientes rangos de descuentos:

    • Menos de $50: Sin descuento

    • Entre $50 y $100: 10% de descuento

    Más de $100: 20% de descuento

4. Utiliza sentencias para aplicar el descuento adecuado según el precio original.

5. Calcula y muestra el precio final después de aplicar el descuento."""
# declaro variables
descuento_10 : float;
descuento_20 : float;
precio_final_10 : float;
precio_final_20 : float;
# inicializo variables
descuento_10 = 0
descuento_20 = 0
precio_final_10 = 0
precio_final_20 = 0
# entrada: le pido al usuarioq ue ingrese el precio original
precio_orginal = float(input("Ingrese el precio original del producto: $"));
# proceso: 
if precio_orginal < 50:#si no hay descuento
    print(f"Sin descuento, precio final: ${precio_orginal}");

elif 50 <= precio_orginal <= 100:
    descuento_10 = precio_orginal * 0.10;#obtengo en 10%
    precio_final_10 = precio_orginal - descuento_10;#lo aplico
    print(f"Descuento del 10%, precio final: ${precio_final_10}");

else:
    descuento_20 = precio_orginal * 0.20;
    precio_final_20 = precio_orginal - descuento_20;
    print(f"Descuento del 20%, precio final: ${precio_final_20}");

