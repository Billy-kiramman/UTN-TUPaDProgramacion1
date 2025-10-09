#1
def imprimir_hola_mundo():
    print("Hola mundo!")

#2
def saludar_usuario(nombre_2):
    print(f"Hola {nombre_2}")

#3
def informacion_personal(nombre_3, apellido, edad, residencia):
    print(f"Soy {nombre_3} {apellido} tengo {edad} anos y vivo en {residencia}")

#4
def calcular_area_circulo(radio):
    area = 3.14 * (radio ** 2)
    return area
def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.14 * radio
    return perimetro

#5
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

#6
def tabla_multiplicar(numero_6):
    for i in range(1,11):
        print(f"// {numero_6} x {i} = {numero_6 * i}")
    
#7
def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma,
            resta,
            multiplicacion,
            division)

#8
def calcular_imc(peso,altura):
    imc = peso / (altura ** 2)
    return imc

#9
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * (9/5)) + 32
    return fahrenheit

#10
def calcular_promedio(a,b,c):
    promedio = (a + b + c) / 3
    return promedio