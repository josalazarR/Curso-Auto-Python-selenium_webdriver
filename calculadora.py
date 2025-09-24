#calculadora
def sumar(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):      
    return a // b
      
def calculadora_simple(operacion, a, b):
    
    try:

        operacion = input("¿Qué operación deseas realizar? (sumar, resta, multiplicacion, division): ").strip().lower()
        if operacion not in ["sumar", "resta", "multiplicacion", "division"]:
            return KeyError("Operación no válida")
        a = int(input("Ingresa el primer número: "))
        b = int(input("Ingresa el segundo número: "))
   
        if operacion == "sumar":
            return sumar(a, b)
        elif operacion == "resta":
            return resta(a, b)
        elif operacion == "multiplicacion":
            return multiplicacion(a, b)
        elif operacion == "division":
            return division(a, b)
        else: 
            return KeyError("Operación no válida")
        
    except ZeroDivisionError:
        print("Error: No se puede dividir entre 0.")
    except ValueError:
        return("Error: Entrada inválida. Por favor, ingresa números válidos.")       
        
print(calculadora_simple("operacion", "a", "b"))