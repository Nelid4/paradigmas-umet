"""16. - Jornal de un Operario
Se necesita desarrollar un programa para el área de recursos humanos de una empresa que permita informar el jornal de un
determinado operario. Usted deberá cargar por teclado el código de turno que el operario trabajó ese día 
(1- representa Diurno y 2- representa Nocturno) y la cantidad de horas trabajadas. La política de trabajo en la 
empresa es que los operarios de la misma pueden trabajar en el turno diurno o nocturno. Si un operario trabaja en el 
turno nocturno el pago es 40.60 pesos la hora, si lo hace en el turno diurno cobra 35.50 pesos la hora.
"""
# declarando variables:
pago : int;
# inicializando variables:
pago = 0;
# entrada:
h_diurno = int(input("Ingrese la catidad de horas trabajadas en el turno diurno: "));
h_nocturno = int(input("Ingrese la catidad de horas trabajadas en el turno nocturno: "));
# procesos:
pago = (h_diurno * 35.50) + (h_nocturno * 40.60);
# salida:
print("Su pago es: $", pago);