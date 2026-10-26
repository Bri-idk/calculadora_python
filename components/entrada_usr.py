from tkinter import Entry

def crear_entrada(frame_entry):
    entrada = Entry(frame_entry)
    entrada.config(font=("Consolas", 40))
    entrada.grid(row=0, column=0, sticky="ew")
    return entrada
