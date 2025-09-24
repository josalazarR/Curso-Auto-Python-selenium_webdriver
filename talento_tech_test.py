# print ("hola mundo")

# Variables
# Tipos de datos
# int, str, float, bool


# control + J = abre la terminal
# a¿salidas de datos a través del print

# Entrada de datos a través del input
# aniodenacimiento = int(input("ingresa tu Edad "))
# print(type(aniodenacimiento))

# matemáticas
# + - * / // doble barrita devuelve la parte entera de la divisón % ** potencia los 2 asteriscos  
#resultado = 3+5
# print(resultado)

# resto = 4 % 2
# print(resto)

# igual = 5 == 5
# print(igual)

#(edad >= 18) and (licencia == True) => True
# cursoOtra = True
# edad > 18 or cursoOtra => True



# edad = 17

# if edad >= 18:
#    print ("Eres mayor de edad.")
# else:
#     print ("Eres menor de edad.")


# puntaje = int(input("Ingresa tu puntaje - (0-10) "))

# if puntaje >= 9:
#     print("Excelente")

# for i in range(11):
#     if i == 5:
#         break
#     print(i)

# for i in range(10):
#     if i % 2 == 0:
#    	    continue
# print(i)

#Ejercicios clase 2
# Desafío: Solicitar al usuario su nombre, edad y profesión, luego mostrar un mensaje con esa información.
# Edad = int(input("Ingresa tu edad: "))
# Nombre = str(input("Ingresa tu nombre: "))
# profesion = str(input("Ingresa tu profesion: "))
# print("Hola", Nombre, "tienes", Edad, "años y tu profesion es", profesion)

# # Mostrar los primeros 10 números pares
# for i in range(10):
#     if i % 2 == 0:
#         print(i)

#10/09/2025

#Ejemplo WHILe
# i = 1
# while i <= 5:
#     print(i)
#     i = i + 1 # Es lo mismo i += 1 con CTRL + C para el bucle.

#listas:
# mi_lista = ["Argentina", 200, True]

# for i in mi_lista:
#     print(i)

# mi_lista.append(5000)
# mi_lista.insert(1, "paises bajos")
# print(mi_lista)

#tuplas (son inmutables):
# mi_tupla = ("Celeste", 200, "Rojo")
# print(mi_tupla[1])

# diccionarios:
# persona = {
#     "nombre": "Juan",
#     "apellido": "desconocido",
#     "edad": 30,
# }
# print(persona.keys())
# print(persona.values())
# print(persona.items())


# funciones f en print permite concatenar sin usar comas

# def saludo( nombre ):
#     print(f"Hola {nombre}")

# saludo( "Jose" )
# saludo( "Gabriel")

# def saludo( nombre ):
#     return f"Hola {nombre}"

# print(saludo("jose"))


# # Modularizar o funcion anidada
def sumar(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: No se puede dividir entre 0.")
        return None

def calculadora_simple():
    operacion = input("¿Qué operación deseas realizar? (sumar, resta, multiplicacion, division): ").strip().lower()
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    if operacion == "sumar":
        resultado = sumar(a, b)
    elif operacion == "resta":
        resultado = resta(a, b)
    elif operacion == "multiplicacion":
        resultado = multiplicacion(a, b)
    elif operacion == "division":
        resultado = division(a, b)
    else: 
        resultado = "Operación no válida"
    print(f"El resultado es: {resultado}")           
        
calculadora_simple()



# try: #manejo de errores
#     resultado = 10 / 0
# except ZeroDivisionError as e:
#     # numero = int(input("Ingresa un numero: "))
#     print(f"Error:[{e}]")

# try:
#     numero = int("123")
#     print(numero)
# except ValueError as e:
#     # numero = int(input("Ingresa un numero: "))
#     print(f"Error:[{e}]")


# persona = {
#     "nombre": "Juan",
#         "edad": 30,
# }

# try:
#     print(persona["nombre"])
    
# except KeyError as e:
#     print(f"la clave no existe")

# clase 17/09/2024


   


