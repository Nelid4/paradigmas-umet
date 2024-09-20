"""Sistema de Gestión de Reservas en un Restaurante
Descripción: Eres el encargado de desarrollar un sistema que permite al personal de un restaurante gestionar las reservas de mesas.
El sistema debe verificar la disponibilidad de mesas para un grupo de personas y procesar varias reservas en el transcurso de un día.
El programa debe solicitar al usuario que ingrese el tamaño del grupo y, según la cantidad de personas, determinar si hay una mesa
disponible. El restaurante tiene mesas para 2, 4, 6 y 8 personas, y cada mesa solo puede ser asignada si el número de personas del
grupo es igual o menor a la capacidad de la mesa. A lo largo del día, se recibirán múltiples solicitudes, y el sistema deberá 
manejar varias reservas mientras asegura que no se sobrepase la capacidad de cada mesa. Además, si el grupo es demasiado grande o
pequeño para las mesas disponibles, el programa debe indicar que no hay mesa para ese grupo"""
# declaro variables
adminitracion_reservas :str;
mesa2 :int;
mesa4 :int;
mesa6 :int;
mesa8 :int;
# inicializo variables
adminitracion_reservas = "";
mesa2 = 0;
mesa4 = 0;
mesa6 = 0;
mesa8 = 0;

while adminitracion_reservas.lower() != "no":#el bucle se repite hasta que el usuario no quiera ingresar mas reservas
    reserva = int(input("Ingrese la cantidad de personas: "));

    while reserva <= 0 or reserva > 8:#manejo entrdas que no permitan una reserva
        if reserva <= 0:
            print("El valor ingresado no es aceptable para reservar una mesa.");
        else:
            print("El grupo es demasiado grande para las mesas disponibles.");
        reserva = int(input("No hay mesas disponible para esa cantidad. Ingrese otra cantidad de personas: "));

    if 0 < reserva <= 2:
        print("Mesa para 2");
        mesa2 += 1;
    elif reserva <= 4:
        print("Mesa para 4");
        mesa4 += 1;
    elif reserva <= 6:
        print("Mesa para 6");
        mesa6 += 1;
    else:
        print("Mesa para 8");
        mesa8 += 1;

    print(f"""
        ------Reservas totales------
        Para mesa de 2 personas: {mesa2}
        Para mesa de 4 personas: {mesa4}
        Para mesa de 6 personas: {mesa6}
        Para mesa de 8 personas: {mesa8}
        ----------------------------
        """) 
    
    adminitracion_reservas = input("¿Quiere seguir ingresado reservas? (escriba 'no' para finalizar o presione enter para seguir): ");








