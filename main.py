import tkinter as tk 
from utils.res_controller import try_rescontroller
from components.ventana import crear_ventana

try_rescontroller()

ventana = crear_ventana()

ventana.grid_columnconfigure(0, weight=1)

entrada_frame = tk.Frame(ventana)
entrada_frame.grid(row=0, column=0, sticky="ew")
entrada_frame.grid_columnconfigure(0, weight=1)

entrada = tk.Entry(entrada_frame)
entrada.config(font=("Consolas", 30))
entrada.grid(row=0, column=0, sticky="ew")

btns_frame= tk.Frame(ventana)
btns_frame.grid(row=1, column=0, sticky="ew")

buttons= [1,2,3,4,5,6,7,8,9,0, '+', '-', 'x','÷', '=' ]

def crear_botones(buttons, btns_frame):
    r = 0
    c = 0
    for btn in buttons:
        btn_creado = tk.Button(btns_frame)
        btn_creado.config(text=f"{btn}")
        btn_creado.grid(row= r, column=c,sticky= "nsew")
        c += 1
        if c > 2:
            r += 1

crear_botones(buttons, btns_frame)

ventana.mainloop()