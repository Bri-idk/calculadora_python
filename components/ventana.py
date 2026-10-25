from tkinter import Tk
from config import TITULO

def crear_ventana():
    ventana = Tk()
    ventana.title(TITULO)
    ventana.geometry("800x900")
    ventana.resizable(True, True)
    return ventana