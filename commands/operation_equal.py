from sympy import sympify
from tkinter import END

def get_result(entrada):
    contenido = entrada.get()
    resultado = sympify(contenido)
    entrada.delete(0, END)
    entrada.insert(END,resultado)

    