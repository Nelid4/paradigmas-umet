"""Secuencia de impares
Cargar por teclado dos números, e imprimir los números impares que se
 encuentran comprendidos entre ellos, en forma ascendente y descendente
"""
# num1 : int;
# num2 : int;
# numero_2: int;

# num1 = 0;
# num2 = 0;

# num1 = int( input("Ingrese el primer número: "));#1
# num2 = int( input("Ingrese el segundo número: "));#3

# i = num1#1
# numero_2 = num2 + 1 #4
# print("\nDe menor a mayor: ")
# for i in range( num1,  numero_2):#2, 1,4
#     if (i % 2 != 0):# 2 % 2 != 0   
#         print( i ) #1
#         i = i + 1 # 1 + 1

#     if i == numero_2: # 2 == 4
#         print("De mayor a menor: ")
#         i = i -1
#         while i > num1:
#             if (i % 2 != 0):
#                 print( i)

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

print("\nDe menor a mayor: ")
for i in range(num1, num2 + 1):
    if i % 2 != 0:
        print(i)

print("De mayor a menor: ")
i = num2
while i >= num1:
    if i % 2 != 0:  # Verificar si el número es impar
        print(i)
    i -= 1  # Disminuir i para continuar en orden descendente
