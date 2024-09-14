"""10. Crear un conversor de dólares a pesos y pesos a dólares, donde se ingrese por teclado el valor del peso actual."""
# entrada: hago un menú y le pido al usuario que ingrese en numero de la opcion
opcion = int(input("1- Dólares a Pesos\n2- Pesos a Dólares\nEscriba el numero de la opción que desea realizar: "));
# proceso: dependiendo la opcion ingresada se calcula su equivalente
if opcion == 1:
    dolares_ingresados = float(input("Ingrese el monto a convertir: $"));#le pido al usuario que ingrese la cantidad en dolares
    resultado_pesos = dolares_ingresados * 966;#hago la conversion
    print(f"${dolares_ingresados} dólares equivalen a ${resultado_pesos} pesos.");#imprimo resultado
elif opcion == 2:
    pesos_ingresados = float(input("Ingrese el monto a convertir: $"));
    resultado_dolares = pesos_ingresados / 966;
    print(f"${pesos_ingresados} pesos equivalen a ${resultado_dolares} dólares.");
else:#si la opcion que ingresó no es ninguna valida, ni 1 ni 2
    print("La opcion que ingresó no es valida");