"""4. Secuencia numérica Ingresar una secuencia de números, de a uno por vez, la carga finaliza cuando el usuario ingresa el cero.
Determinar 
a) Porcentaje que representan los números divisibles por 3 sobre el total de números ingresados en la secuencia 
b) Determinar la cantidad de números que son el cuadrado del número anterior 
c) Determinar la posición del mayor elemento impar de la secuencia """
num_ingresado = 0
num_divisible3 = 0
num_anterior = 0
cantidad_cuadrado = 0
posicion= 0
valor_impar =0
posicion_impar = 0
porcentaje =0

while True:
    num_ingresado = float(input("Ingrese un numero o 0 para terminar: "))

    if num_ingresado == 0:
        break
    else:
        posicion += 1
        if num_ingresado % 3 == 0:
            num_divisible3 += 1
        
        if num_anterior ** 2 == num_ingresado:
            cantidad_cuadrado += 1
        num_anterior = num_ingresado
        
        if num_ingresado % 2 != 0:
            if valor_impar < num_ingresado:
                valor_impar = num_ingresado
                posicion_impar = posicion

porcentaje = (num_divisible3/posicion)*100
print("El porcentaje de numeros divisibles por 3 es: %", porcentaje)
print("La cantidad de numeros que son el cuaddrado del anterior son: ", cantidad_cuadrado)
print("La posicion del numero impar mayor es: ", posicion_impar)