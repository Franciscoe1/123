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
        if not expr:
            return ""

        expr = expr.replace("×", "*").replace("÷", "/")

        # 🔹 Tokenizar
        tokens = []
        numero = ""

        for c in expr:
            if c in "+-*/":
                if numero == "":
                    return "Error"
                tokens.append(float(numero))
                tokens.append(c)
                numero = ""
            else:
                if c not in "0123456789.":
                    return "Error"
                numero += c

        if numero != "":
            tokens.append(float(numero))

        # 🔥 Resolver * y /
        i = 0
        while i < len(tokens):
            if tokens[i] == "*":
                resultado = multiplicar(tokens[i-1], tokens[i+1])
                tokens[i-1:i+2] = [resultado]
                i -= 1
            elif tokens[i] == "/":
                resultado = dividir(tokens[i-1], tokens[i+1])
                tokens[i-1:i+2] = [resultado]
                i -= 1
            else:
                i += 1

        # 🔥 Resolver + y -
        i = 0
        while i < len(tokens):
            if tokens[i] == "+":
                resultado = sumar(tokens[i-1], tokens[i+1])
                tokens[i-1:i+2] = [resultado]
                i -= 1
            elif tokens[i] == "-":
                resultado = restar(tokens[i-1], tokens[i+1])
                tokens[i-1:i+2] = [resultado]
                i -= 1
            else:
                i += 1

        resultado_final = tokens[0]

        # Quitar .0 innecesario
        if resultado_final == int(resultado_final):
            return int(resultado_final)

        return resultado_final

    except:
        return "Error"