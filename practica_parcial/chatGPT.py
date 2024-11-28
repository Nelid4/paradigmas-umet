frase = input("Ingresa una frase: ")  # Pedimos la frase
contador_vocales = 0  # Inicializamos el contador de vocales
contador_a = 0;
contador_e = 0;
contador_i = 0;
contador_o = 0;
contador_u = 0;


for letra in frase:
    if letra.lower() in "aeiou":  # Verificamos si la letra es una vocal
        contador_vocales += 1  # Si es una vocal, aumentamos el contador
        if letra.lower() == "a":
            contador_a += 1;
        elif letra.lower == "e":
            contador_e += 1;
        elif letra.lower == "i":
            contador_e += 1;
        elif letra.lower == "o":
            contador_o += 1;
        else: 
            contador_u += 1;

print(f"""La cantidad de vcales ttoales es: {contador_vocales}
-Cantidad de A: {contador_a}
-Cantidad de E: {contador_e}
-Cantidad de I: {contador_i}
-Cantidad de O: {contador_o}
-Cantidad de U: {contador_u}

""")