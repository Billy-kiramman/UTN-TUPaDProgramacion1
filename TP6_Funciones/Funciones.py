
# Ejercicio 1
from Def_funciones import imprimir_hola_mundo
if __name__=="__main__":
    imprimir_hola_mundo()

# Ejercicio 2
from Def_funciones import saludar_usuario
if __name__=="__main__":
    nombre_2 = str(input("Ingrese un nombre: "))
    saludar_usuario(nombre_2)

# Ejercicio 3
from Def_funciones import informacion_personal
if __name__=="__main__":
    nombre_3 = str(input("Ingrese su nombre: "))
    apellido = str(input("Ingrese su apellido: "))
    edad = int(input("Ingrese su edad: "))
    residencia = str(input("Ingrese su lugar de residencia: "))
    informacion_personal(nombre_3, apellido, edad, residencia)

# Ejercicio 4
from Def_funciones import (calcular_perimetro_circulo,calcular_area_circulo)
if __name__=="__main__":
    radio: float = float(input("Ingrese el radio de un circulo: "))
    print(f"El perimetro del circulo es {calcular_perimetro_circulo(radio)} y su area es {calcular_area_circulo(radio)}")

# Ejercicio 5
from Def_funciones import segundos_a_horas
if __name__=="__main__":
    segundos: int = int(input("Ingrese la cantidad de segundos: "))
    print(f"Los {segundos} segundos, pasan a ser {segundos_a_horas(segundos)} horas")

# Ejercicio 6
from Def_funciones import tabla_multiplicar
if __name__=="__main__":
    numero_6:int = int(input("Ingrese un numero para su tabla de multiplicar: "))
    tabla_multiplicar(numero_6)

# Ejercicio 7
from Def_funciones import operaciones_basicas
if __name__=="__main__":
    num1: int = int(input("Ingrese el primer numero: "))
    num2: int = int(input("Ingrese el segundo numero: "))
    resultado = operaciones_basicas(num1,num2)
    print(resultado)

# Ejercicio 8
from Def_funciones import calcular_imc
if __name__=="__main__":    
    peso: float = float(input("Ingrese su peso en Kg: "))
    altura: float = float(input("Ingrese su altura en metros: "))
    print(f"Su indice de masa corporal es {calcular_imc(peso,altura):.2f}")

# Ejercicio 9
from Def_funciones import celsius_a_fahrenheit
if __name__=="__main__":
    celsius: float = float(input("Ingrese la temperatura en celsius: "))
    print(f"Su convercion a fahrenheit es {celsius_a_fahrenheit(celsius)}")

# Ejercicio 10
from Def_funciones import calcular_promedio
if __name__=="__main__":
    a: int = int(input("Ingrese el primer numero: "))
    b: int = int(input("Ingrese el segundo numero: "))
    c: int = int(input("Ingrese el tercer numero: "))
    print(f"El promedio de los numeros ingresados es {calcular_promedio(a,b,c)}")