"""5. Conversión de medidas Desarrolle un programa para convertir una medida dada en pies a sus equivalentes en: yardas pulgadas
cenơmetros metros Sabiendo que: 1 pie = 12 pulgadas 1 yarda = 3 pies 1 pulgada = 2.54 centímetros 1 metro =1000"""
# declaro variables:
pulgadas : float;
yardas : float;
centimetros : float;
metros : float;
# inicializo variables:
pulgadas = 0;
yardas = 0;
centimetros = 0;
metros = 0;
# entrada: le pido al usuario que ingrese la medida
pies_ingresados = float(input("Ingrese la medida en pies: "));
# proceso: calculo cada medida
pulgadas = pies_ingresados * 12;
yardas = pies_ingresados / 3;
centimetros = pulgadas * 2.54;
metros = centimetros / 100;
# salida: muestro cada medida
print(f"""
{pies_ingresados} pies, equivalen a:
-Pulgadas: {pulgadas}
-Yardas: {yardas}
-Centímetros: {centimetros}
-Metros: {metros}
""");


