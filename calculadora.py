def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):    
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def calcular_expresion(expr):
    try:
        # Validación básica
        if not expr:
            return ""

        # Evaluar expresión completa
        resultado = eval(expr)

        return resultado

    except ZeroDivisionError:
        return "Error"
    except:
        return "Error"