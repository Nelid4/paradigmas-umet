"""Operaciones con Conjuntos de Números
Crea un programa que permita al usuario trabajar con dos conjuntos de números, almacenados en listas. El programa debe ofrecer las siguientes opciones:
Agregar números a los conjuntos: El usuario puede agregar números a cada conjunto, uno por uno.
Unión de los conjuntos: Muestra la lista de todos los números que pertenecen a al menos uno de los dos conjuntos (sin duplicados).
Intersección de los conjuntos: Muestra la lista de los números que están presentes en ambos conjuntos.
Diferencia entre los conjuntos: Muestra los números que están en el primer conjunto pero no en el segundo.
Salir del programa."""

import time

primer_conjunto = [1,2,3,4,5]
segundo_conjunto = [5,6,7,8] 

print("Aviso: Los conjuntos se encuentran vacios, debes ingresar al menos un número en cada uno para continuar!")
num_conjunto1 = int(input("Ingressá un número para el primer conjunto: "))
primer_conjunto.append(num_conjunto1)

num_conjunto2 = int(input("Ingresá un número para el segundo conjunto: "))
segundo_conjunto.append(num_conjunto2)
print("iniciado...")

while True:
    time.sleep(2)
    print(f"""
-Primer conjunto: {primer_conjunto}
-Segundo conjunto: {segundo_conjunto}
    ------menú------
  1- Agregar números a los conjuntos.
  2- Union de los conjuntos.
  3- Interseccion entre los conjuntos.
  4- Diferencia entre los conjuntos.
  5- Salir""")
    opcion = int(input("Ingrese la opción:"))
# utilizo una tupla y un while para validar la opcion
    tupla_opciones = (1,2,3,4,5)
    while opcion not in tupla_opciones:
        opcion = int(input("Ingrese una opción que se encuentre en el menú:"))

# opcion 1- agregar un numero
    if opcion == 1:
        agregar_num = int(input("Para agregar un num al primer conjuto ingrese 1, o para el segundo conjunto 2: "))
        while agregar_num != 1 and agregar_num != 2:
            agregar_num = int(input("Solo se admite el 1 o 2, ingrese de nuevo el número: "))
        
        if agregar_num == 1:
            agregar1 = int(input("Ingrese el número que quiere agregar: "))
            primer_conjunto.append(agregar1)
        
        else:
            agregar2 = int(input("Ingrese el número que quiere agregar: "))
            segundo_conjunto.append(agregar2)
        
        print("Se agregó correctamente\n")

# opcion 2- union de conjuntos
    elif opcion == 2:
        union = set(primer_conjunto).union(set(segundo_conjunto)) #hago las listas conjuntos y .union() las une y verifica que no se repitan nums
        print("Unión de los conjuntos:", list(union), "\n")


# opcion 3- interseccion de conjuntos
    elif opcion == 3:
        interseccion = set(primer_conjunto).intersection(set(segundo_conjunto)) #utilizo .intersection() para obtener los numeros que se encuentran en ambos conjuntos
        print("Intersección de los conjuntos:", list(interseccion), "\n")

# opcion 4- diferencias entre conjuntos
    elif opcion == 4:
        diferencia = set(primer_conjunto).difference(set(segundo_conjunto)) #uso .difference() para obtener la diferencia
        print("Diferencia entre los conjuntos:", list(diferencia), "\n")

# opcion 5- salir
    else:
        print("Saliendo del programa...")
        time.sleep(2)
        break