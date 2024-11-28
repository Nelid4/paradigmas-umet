"""7. Secuencia de n números Ingresar una secuencia de n números, de a uno por vez. El valor de n se ingresa por teclado, 
validar que sea mayor a 0. Determinar: 
a) Cuántos números ingresados terminan en 5
b) La cantidad de veces que aparece el primer número ingresado por el usuario en la secuencia 
c) Cuántos números ingresados son mayores al anterior."""

num_anterior_contador = 0
contador_primer_num = 0
cantidad_num = 0
num_ingresado = 0
contador_5 = 0
primer_numero = 0
num_anterior = 0

cantidad_num = int(input("Ingrese la cantidad de numeros que tendrá la secuencia: "))

while cantidad_num <= 0:
    cantidad_num = int(input("Ingrese un número mayor a 0: "))

for i in range(1, cantidad_num + 1):
    num_ingresado = int(input("- Ingrese un número de la secuencia: "))
    if num_ingresado % 10 == 5:
        contador_5 += 1
    
    if i == 1:
        primer_numero = num_ingresado
    
    if i >= 2 and num_ingresado == primer_numero:
        contador_primer_num += 1
    
    if num_ingresado > num_anterior and i >= 2:
        num_anterior_contador += 1
    
    num_anterior = num_ingresado

print(f"""
cantidad de N° que terminan en 5: {contador_5}
cantidad de veces que aparacee el primer num en la secuencia: {contador_primer_num}
cantidad de veces que n° ingresado mayor a n° anterior: {num_anterior_contador}
""")