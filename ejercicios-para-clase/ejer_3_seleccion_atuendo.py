"""Ejercicio 1: Selección de Atuendo
Estás diseñando una aplicación que ayuda a las personas a elegir su atuendo diario basado en la temperatura y la posibilidad de lluvia. 
La aplicación debe hacer recomendaciones sobre qué tipo de ropa y accesorios son apropiados para el día. La aplicación pedirá al usuario que introduzca 
la temperatura en grados Celsius y si espera lluvia o no. 
Basado en la información ingresada, deberás decidir si el atuendo debe incluir algo más abrigado o más ligero, y si es necesario agregar algún accesorio 
adicional para protegerse del clima. Al final, deberás mostrar la recomendación completa al usuario, considerando tanto la temperatura como 
la posibilidad de lluvia."""
# declaracion de variables:
temperatura : float;
lluvia : str;
recomendacion_atuendo : str;
recomendacion_clima : str;
# inicializacion d variables:
temperatura = 0.0;
lluvia = "";
recomendacion_atuendo = "";
recomendacion_clima = "";
TEMPERATURA_LIMITE = 22;
# entrada: le pido al usuario que ingrese la temperatura y si esta lloviendo
temperatura = float(input("Ingrese la temperatura en grados Celsius: "));
lluvia = input("¿Está lloviendo? (responda por si/no): ");
# proceso:  dependiiendo de la relacion que tenga la temperatura ingreasada con la costante de temperatura, se almacena un mensaje u otro en la varible recomendacion_atuendo
if temperatura <= TEMPERATURA_LIMITE:
    recomendacion_atuendo = "Usted deberia incluir prendas abrigadas en su atuendo.";
else:
    recomendacion_atuendo = "Usted podria optar por un atuendo más ligero que abrigado.";
# utilizo .upper() para evaluar si el usuario escribio ´si´ de alguna forma. utilizo la misma lógica anterior
if lluvia.upper() == "SI":
    recomendacion_clima = "Considere agregar algún accesorio adicional para protegerse del clima, como un paraguas o un impermeable.";
else:
    recomendacion_clima = "No necesita agregar accesorios adicionales para protegerse del clima.";
# salida: imprimo la recomendacion entera
print(F"""
        ---RECOMENDACIONES---
 *{recomendacion_atuendo}
 *{recomendacion_clima}
""");