"""2 - Cuadrado de un binomio Plantear un script directamente en el shell de Python, que permita mostrar, para dos valores 𝑎 y 𝑏, que: Un binomio al cuadrado 
(suma) esigual al cuadrado del primer término, más el doble producto del primero por el segundo más el cuadrado del segundo"""
#inicializamos variales
num1 = 0.0;
num2 = 0.0;
#entrada: le pido al usuario que ingrese los valores de num 1 y 2
num1 = float(input("Ingrese el primer valor: ")) 
num2 = float(input("Ingrese el segundo valor: ")) 
#proceso: calculo el resultado
resultado = (num1 + num2)**2
#salida: imprimo por consola las cuentas que se hicieron y los resultados
print(f"El resultado del binomio al cuadrado, osea ({num1} + {num2})**2, es {resultado}; lo que es igual a el resultado de {num1}**2 + 2*{num1}*{num2} + {num2}**2 = {resultado}")