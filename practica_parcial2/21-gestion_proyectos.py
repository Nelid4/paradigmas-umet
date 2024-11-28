"""Crea un programa que permita gestionar proyectos en un equipo. Cada proyecto tiene un nombre, una lista de integrantes y
un estado (en progreso, completado o pendiente). El programa debe permitir:

Agregar proyectos nuevos.
Cambiar el estado de un proyecto.
Consultar los proyectos que están en progreso.
Mostrar el proyecto con más integrantes."""
proyectos={}

def agregar_proyecto():
    nombre=input("nombre del proyecto: ").lower()
    cantidad=int(input("Ingrese cantidad de participantes"))
    integrantes=[]
    for i in range(cantidad):
        integ_nombre=input("ingrese uno a uno el nombre d los integrantes: ").lower()
        integrantes.append(integ_nombre)

    estado=input("estado: progreso, completado o pendiente: ").lower()
    proyectos[nombre]={"integrantes":integrantes, "estado":estado}
    print(proyectos)



def cambiar_estado():
    nombre_cambiar=input("nombre del proyecto a modificar: ").lower()
    estado_cambiar=input("a que estado cambia: ").lower()
    for nombre, info in proyectos.items():
        if nombre_cambiar == nombre:
            proyectos[nombre]={"integrantes":info["integrantes"], "estado":estado_cambiar}

while True:
    agregar_proyecto()
    agregar_proyecto()
    
    cambiar_estado()