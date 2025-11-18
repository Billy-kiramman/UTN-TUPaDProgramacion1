# Ejercicio 1
from funciones_recursividad import factorial,fibonacci,potencia,decimal_a_binario,es_palindromo,suma_digitos,contar_bloques,contar_digito
num = int(input("Ingrese un numero para mostrar los factoriales: "))

print("Factoriales desde 1 hasta", num)
for i in range(1, num + 1):
    print(f"{i}! = {factorial(i)}")

#Ejercicio 2

num = int(input("Ingrese la posición hasta la que quiere mostrar la serie de Fibonacci: "))

print("Serie de Fibonacci:")
for i in range(num + 1):
    print(f"F({i}) = {fibonacci(i)}")

#Ejercicio 3

base = int(input("Ingrese la base: "))
exp = int(input("Ingrese el exponente: "))

print(f"{base}^{exp} = {potencia(base, exp)}")

#Ejercicio 4

num = int(input("Ingrese un numero decimal: "))
print("Binario:", decimal_a_binario(num))

#Ejercicio 5

pal = input("Ingrese una palabra: ")
print("Es palindromo?", es_palindromo(pal))


#EJercicio 6
sumados = int(input("Ingrese un numero para sumar sus digitos: "))
print("Suma de digitos:", suma_digitos(sumados))


#Ejercicio 7
bloque = int(input("Ingrese la cantidad de bloques de base: "))
print("Bloques totales:", contar_bloques(bloque))

#Ejercicio 8
entero = int(input("ingrese un numero entero positivo: "))
digito = int(input("Ingrese un numero entre 0 y 9"))
if str(entero).isdigit() and digito in [0,1,2,3,4,5,6,7,8,9]:
    print("Apariciones del digito:", contar_digito(entero, digito))
else:
    print("Los datos ingresados son invalidos.")