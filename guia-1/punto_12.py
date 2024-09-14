"""12. Crear un conversor de pies y pulgadas a centímetros."""
# declarando variables:
pies_centimetros : float;
pulgadas_centimetros : float;

PIES_A_CENTIMETROS = 30.48  # 1 pie = 30.48 cm
PULGADAS_A_CENTIMETROS = 2.54  # 1 pulgada = 2.54 cm
# inicializando variables:
pies_centimetros = 0.0;
pulgadas_centimetros = 0.0;
# entrada: le pido al usuario que ingrese pies y pulgadas
pies = float(input("Ingrese la medida en pies: "));
pulgadas = float(input("Ingrese la medida en pulgadas: "));
# procesos: hago la conversion
pies_centimetros = pies * PIES_A_CENTIMETROS
pulgadas_centimetros = pulgadas * PULGADAS_A_CENTIMETROS
# salida: imprimo por pantalla las conversiones
print(f"La medida {pies} pies, corresponde a {pies_centimetros}cm y la medida {pulgadas} pulgadas equivale a {pulgadas_centimetros}")