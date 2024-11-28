# --------------- Recursos útiles para la segunda parte -----------------
"1------------- LISTAS => ARRAYS --------------"
# saludo="como estas?";
# nombreLista=["hola", 1, 3.5, True, saludo]; # Permite guardar diferentes tipos de valores

# lista_num = [0, 4, 6, 8, 10]

"accediendo a las posiciones de la lista"
# print(lista_num[:]); #imprime la lista entera == print(lista)
# print(lista_num[2]); #imprime por índice en orden
# print(lista_num[-1]); #imprime el último índice
# print(lista_num[1:4]); #imprime porcion (devuelve en lista), incluye el primer num pero no el último, si pones[:3] incluye directamente el 0 o al reves [2:] hasta el final

"agregado un elemento con .append()"
# lista_num.append(12); #se agrega al final de la lista
# print(lista_num[:]); #imprime la lista entera

"agregando un elemento con .insert()"
# lista_num.insert(1, 2); #pide 1-índice donde se agrega 2-valor a agregar
# print(lista_num[:]); #imprime la lista entera

"agregando varios elementos con .extend([])"
# lista_num.extend([14, 16, 18, 20]); #como si concatenara listas
# print(lista_num[:]); #imprime la lista entera

"acceder al indice de un elemento con .index()"
# print(lista_num.index(6)); #si hay un elemto repetido, accede al primero que encuetra

"comprobando si un elemento esta en la lista"
# print(8 in lista_num); #devuelve un boolean
# print(3 in lista_num); #espera el elemento a buscar y que le especifiquen en donde

"eliminando elementos con .remove()"
# lista_num.remove(14); 
# print(lista_num[:]); #imprime la lista entera

"eliminando el último elemento con .pop()"
# lista_num.pop(); 
# print(lista_num[:]); #imprime la lista entera

"concatenando listas con ' + ' "
# lista_letras=["a", "b", "c"];
# lista_concatenada = lista_letras + lista_num;
# print(lista_concatenada)

"1/2-------------------------ORDEN BURBUJA-------------------------------"
mi_lista = [4, 3, 1, 5, 2]
print("lista inicial:",mi_lista)  # Esto debería imprimir la lista ordenada

def bubble_sort(lista):
    n = len(lista)  # Longitud de la lista
    for i in range(n):  # Bucle para cada pasada
        # Variable para verificar si se realizaron intercambios en esta pasada
        intercambio = False
        
        # Bucle interno para comparar elementos adyacentes
        for j in range(0, n - i - 1):  # No necesitamos llegar al final en cada pasada
            if lista[j] > lista[j + 1]:  # Condición para el orden ascendente
                # Intercambia si están en el orden incorrecto
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True  # Hubo un intercambio, así que seguimos
                print(mi_lista)  # Esto debería imprimir la lista ordenada

        # Si no hubo intercambios, la lista ya está ordenada
        if not intercambio:
            break

# Ejemplo de uso
bubble_sort(mi_lista)
print("lista ordenada:",mi_lista)  # Esto debería imprimir la lista ordenada

"2--------------- TUPLAS => LISTAS INMUTABLES ----------------"
#No puede: añadir, eliminar, mover, elementos
#Si puede: extraer porciones creando nuevas tuplas,comprobar si un elemento se encuentra en la lista

# tupla_nombres = ("Lautaro", "Tomas", "Franco", "Pablo", "Lautaro")
# print(tupla_nombres[2]) #accediendo a un elemento por índice
# print("Lautaro" in tupla_nombres) #comproando si esta en la lista

#Permiten formatear strings, sirven de clave en un diccionario

"-> convirtiendo una tupla en una lista con list"
# lista_nombres = list(tupla_nombres)
# print(lista_nombres)

"-> convirtiendo una lista en una tupla con tuple"
# lista_colores = ["rojo", "amarillo", "azul"];
# print(lista_colores)
# tupla_colores = tuple(lista_colores)
# print(tupla_colores)

"Contando cunatas veces se encuenta un mismo elemento con .count()"
# print(tupla_nombres.count("Lautaro")); #devuelve la cantidad

"averiguando la longitud de una tupla con len()"
# print(len(tupla_nombres))

"asigando una variable a cada elemento, desempaquetado de tuplas"
# personaje = ("Homero", "Simpson", 40, True)

# nombre, apellido, edad, vivo = personaje
# print(f"El apellido es {apellido}, el nombre {nombre}, tiene {edad} años y su estado es {vivo}")


"3--------------- DICCIONARIO ----------------"
#CLAVE:VALOR
# mi_diccionario = {"nombre":"Rick", "apellido":"Sanchez", "edad": 44, "dimension":"c137", "status": True}
# print(mi_diccionario)

"accediendo a un valor, llamando al diccionario y [clave]"
# print("El nombre del pesonaje es:",mi_diccionario["nombre"])

"agregando un elemento al diccionario"
# mi_diccionario["condicion"] ="libre" #ingreso [clave] = valor

"sobreescribiendo un valor"
# mi_diccionario["condicion"] = "buscado"

"eliminando clave:valor del diccionario"
# del mi_diccionario["status"]

"usando tuplas para claves en nuevo diccionario"
# tupla_morty = ("nombre","apellido","genero", "planeta")
# mi_diccionario = {tupla_morty[0]:"Morty", tupla_morty[1]:"Smeat", tupla_morty[2]: "masculino", tupla_morty[3]:"tierra"}
# print(mi_diccionario)

"agregando a un diccionario una clave mediante tupla o lista"
# mi_diccionario["crimenes"] = ("robo", "ascesinato", "tráfico de semillas")
# print(mi_diccionario)

"diccionario dentro de diccionario y una lista"
# mi_diccionario["amigos"] = {"vivos":["Mr. Poppy But", "Evil Morty"], "muertos":["Hombre pájaro", "squanchy"]}
# print(mi_diccionario["amigos"])

"obteniendo todas las claves con .keys()"
# print(mi_diccionario.keys())

"obteniendo todos los valores con .values()"
# print(mi_diccionario.values())

"obtenemos longitud/cantidad de clave:valor con len()"
# print(len(mi_diccionario))

