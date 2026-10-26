from tkinter import Frame

def entry_frame(ventana):
    entrada_frame = Frame(ventana)
    entrada_frame.grid(row=0, column=0, sticky="ew")
    entrada_frame.grid_columnconfigure(0, weight=1)
    return entrada_frame

def buttons_frame(ventana):
    btns_frame = Frame(ventana)
    btns_frame.grid(row=1, column=0, sticky="nsew")
    colums_btns= 0

    while colums_btns != 4:
        btns_frame.grid_columnconfigure(colums_btns,  weight=1)
        colums_btns += 1

    rows_btns = 0

    while rows_btns != 4:
        btns_frame.grid_rowconfigure(rows_btns, weight=1)
        rows_btns += 1  

    return btns_frame