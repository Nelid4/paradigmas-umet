"""Ciclistas:La final de una carrera de ciclistas tiene n competidores (n se ingresa por teclado).
Desarrollar un programa que permita cargar, por cada competidor, nombre y tiempo de carrera. Luego se pide:
a) Determinar y mostrar el nombre del ganador de la carrera.
b) Ingresar por teclado el tiempo record registrado para dicha carrera. Determinar si el tiempo del ganador es menor
al tiempo record, mostrar un mensaje.
c) Calcular y mostrar el tiempo promedio entre todos los ciclistas"""
nombre = "";
ciclistas = 0;
tiempo = 0.0;
tiempo_total = 0.0;

ciclistas = int( input("ingrese la catidad de ciclistas que compitieron: "));

nombre_ganador = input("Ingrese el primer nombre: ");
tiempo_ganador = float( input("ingrese el tiempo: "));
tiempo_total = tiempo_total + tiempo_ganador

for i in range (1, ciclistas):
    nombre = input("ingrese el siguiente nombre: ");
    tiempo = float( input("ingrese el tiempo: "));

    tiempo_total= tiempo_total + tiempo

    if tiempo < tiempo_ganador:
        tiempo_ganador = tiempo;
        nombre_ganador = nombre;

print(f" El ganador es {nombre_ganador} con un tiempo de {tiempo_ganador}");

tiempo_record = float( input("ingrese el tiempo record registrado: "));

if tiempo_ganador < tiempo_record:
    print("¡Felicidades, rompio el record establecido!");

promedio = tiempo_total / ciclistas
print("El promedio de tiempo entre los ciclistas es: ", promedio);
