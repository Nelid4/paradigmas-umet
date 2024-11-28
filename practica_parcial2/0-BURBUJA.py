pacientes = {"juli":1.74, "neli": 1.75, "pocha":0.55, "debora":1.62, "javier":1.78}

def definir_perfil():
    nombre = input("Ingrese el nombre: ")
    altura = float(input("Ingrese la altura: "))
    pacientes[nombre] = altura

def ordenar_ascendente():
    lista_pacientes = list(pacientes.items())
    cantidada_pacientes = len(lista_pacientes)
    for i in range(cantidada_pacientes):
        for j in range(0, cantidada_pacientes-i-1):
            if lista_pacientes[j][1] > lista_pacientes[j+1][1]:
                lista_pacientes[j], lista_pacientes[j+1] = lista_pacientes[j+1], lista_pacientes[j]

    print("\nPacientes ordenados por altura ascendente:")
    for nombre, altura in lista_pacientes:
        print(f"{nombre}: {altura} cm")

definir_perfil()
ordenar_ascendente()
