from commands.operation_equal import get_result
from tkinter import Button
from tkinter import END

def crear_botones(buttons, btns_frame, entrada):
    for r, fila in enumerate(buttons):
        for c, btn in enumerate(fila):
            btn_creado = Button(btns_frame)
            btn_creado.config(text=f"{btn}", font=("Consolas", 20))
            if btn == 'C' :
                btn_creado.config(command= lambda: entrada.delete(0, END))
            elif btn != '=':
                btn_creado.config(command=lambda valor=btn: entrada.insert(END, str(valor)))
            else:
                btn_creado.config(command=lambda: get_result(entrada))
            btn_creado.grid(row= r, column=c,sticky= "nsew")