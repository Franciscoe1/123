import tkinter as tk
from calculadora import calcular_expresion

# Ventana
ventana = tk.Tk()
ventana.title("Calculadora")

entrada = tk.StringVar()
resultado_mostrado = False

# Pantalla
pantalla = tk.Entry(
    ventana,
    textvariable=entrada,
    font=("Arial", 18),
    bd=10,
    relief="sunken",
    justify="right"
)
pantalla.grid(row=0, column=0, columnspan=4, sticky="nsew")


# FUNCIONES

def limpiar():
    global resultado_mostrado
    entrada.set("")
    resultado_mostrado = False


def calcular():
    global resultado_mostrado

    expr = entrada.get()

    if expr == "Error":
        return

    resultado = calcular_expresion(expr)
    entrada.set(resultado)

    resultado_mostrado = True


def borrar():
    texto = entrada.get()

    # 🚫 Si hay error, borrar todo de una
    if texto == "Error":
        entrada.set("")
        return

    entrada.set(texto[:-1])


def click(valor):
    global resultado_mostrado

    texto_actual = entrada.get()

    # 🚫 Si hay error, empezar desde cero
    if texto_actual == "Error":
        if valor in "+-*/":
            return  # no permitir operador después de error
        entrada.set(valor)
        resultado_mostrado = False
        return

    if resultado_mostrado:
        if valor in "+-*/":
            resultado_mostrado = False
        else:
            entrada.set("")
            texto_actual = ""
            resultado_mostrado = False

    # Evitar operadores repetidos
    if texto_actual and texto_actual[-1] in "+-*/" and valor in "+-*/":
        return

    entrada.set(texto_actual + str(valor))

# BOTONES
botones = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("⌫", 4, 2), ("+", 4, 3),
    ("=", 5, 0)
]

for (texto, fila, col) in botones:
    if texto == "C":
        accion = limpiar
    elif texto == "=":
        accion = calcular
    elif texto == "⌫":
        accion = borrar
    else:
        accion = lambda t=texto: click(t)

    tk.Button(
        ventana,
        text=texto,
        width=5,
        height=2,
        command=accion
    ).grid(row=fila, column=col, sticky="nsew")


# Ajuste grid
for i in range(6):
    ventana.grid_rowconfigure(i, weight=1)

for i in range(4):
    ventana.grid_columnconfigure(i, weight=1)


ventana.mainloop()