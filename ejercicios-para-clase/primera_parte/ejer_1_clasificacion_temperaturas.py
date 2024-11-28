congelado = 0
frio = 15
templado = 16
calido = 25
categoria = ""

#entrada
temperatura_ingresada = float(input("Ingrese la temperatura en grados Celsius: "));

#proceso
if temperatura_ingresada < congelado:
    categoria = "CONGELANTE";

elif temperatura_ingresada <= frio:
    categoria = "FRÍO";

elif temperatura_ingresada <= calido:
    categoria = "TEMPLADA";

else:
    categoria = "CÁLIDA";

#salida
print(f"La temperatura ingresada, {temperatura_ingresada}°C, entra en la categoría: {categoria}");
