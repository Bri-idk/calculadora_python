from tkinter import Tk
from config import TITULO

def crear_ventana():
    ventana = Tk()
    ventana.title(TITULO)
    ventana.geometry("700x800")
    ventana.resizable(True, True)
    ventana.grid_columnconfigure(0, weight=1)
    ventana.grid_rowconfigure(1, weight=1)
    return ventana