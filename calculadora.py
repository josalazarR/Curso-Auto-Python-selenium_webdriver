#calculadora
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