"""17. Galería de Arte Una galería de arte desea preparar un catálogo de sus cuadros más famosos. Se realiza una prueba con tres cuadros y por cada
uno se ingresa el año en que fue creado. El programa deberá verificar si todos los cuadros son anteriores al siglo XX (El siglo XX es el siglo pasado. 
Se inició en el año 1901 y terminó en el año 2000). Determinar cuántos tienen antigüedad inferior a 10 años. Si no hay ninguno, imprimir el mensaje
“Renovar stock”."""
# declarando variables:
cuadros_recientes : int;#creo una variable que itere si hay un cuadro con antuguedad menor a 10
# inicializando variables:
cuadros_recientes = 0; 
# entrada:
cuadro1 = int(input("Cuadro 1: Ingrese el año en el que fue creado: "));
cuadro2 = int(input("Cuadro 2: Ingrese el año en el que fue creado: "));
cuadro3 = int(input("Cuadro 3: Ingrese el año en el que fue creado: "));
# procesos y salidas:
if cuadro1 < 1901 and cuadro2 < 1901 and cuadro3 < 1901: #si todos los cuadros son anteriores al siglo xx
    print("Todos los cuadros son anteriores al siglo XX");
else:
    if 2014 <= cuadro1 <= 2024:#asi muestro exactamente el cuadro con antiguedad menor a 10
        cuadros_recientes += 1
        print("El cuadro 1 tiene una antigüedad inferior a 10 años");
    
    if 2014 <= cuadro2 <= 2024:
        cuadros_recientes += 1
        print("El cuadro 2 tiene una antigüedad inferior a 10 años");
    
    if 2014 <= cuadro3 <= 2024:
        cuadros_recientes += 1
        print("El cuadro 3 tiene una antigüedad inferior a 10 años");
    
    if cuadros_recientes == 0:#si no hay cuadros con antiguedda menor a 10
        print("Renovar stock");
