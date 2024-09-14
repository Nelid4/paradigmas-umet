"""13. Se desea un programa que: solicite al usuario un nombre, un apellido y el dominio y luego, proponga una dirección de mail 
para el nombre y apellido ingresado de acuerdo a las siguientes reglas: Componer la dirección de correo de la siguiente manera: 
@ Por ejemplo para Nombre = Felipe, Apellido= Steffolani y Dominio= umet.edu.ar la dirección de mail sería: fsteffolani@umet.edu.ar. 
Pero si la primera primera letra del nombre y la primera letra del apellido son la misma entonces uƟlizar: .@ Por ejemplo para 
Nombre= Soledad, Apellido= Steffolani y Dominio= colegiorosarito.edu.ar la dirección de mail sería: soledad.steffolani@umet.edu.ar"""
# declarando variables:
nombre : str;
apellido : str;
dominio : str;
primera_letra_nombre : str;
primera_letra_apellido : str;
# inicializando variables:
nombre = "";
apellido = "";
dominio = "";
primera_letra_nombre = "";
primera_letra_apellido = "";
# entrada: le pido al usuario que ingrese los datos y los almaceno en variables, utilizo .lower() para almacenarlo en minuscula 
nombre = input("Ingresá tu nombre: ").lower();
apellido = input("Ingresá tu apellido: ").lower();
dominio = input("Ingresá tu dominio: @").lower();
# procesos: accedo al indice 0 de la palabra ingresada y la almaceno en una variable
primera_letra_nombre = nombre[0].lower();
primera_letra_apellido = apellido[0].lower();
# salida: dependiedo de lo que haya ingresado el usuario, imprimo de una forma u otra el mail
if primera_letra_nombre == primera_letra_apellido:
    print(f"Su direccion de mail sería: {nombre}.{apellido}@{dominio}");
else: 
    print(f"Su direccion de mail sería: {primera_letra_nombre}{apellido}@{dominio}");