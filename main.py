from utils.res_controller import try_rescontroller
from components.ventana import crear_ventana
from components.frames import entry_frame, buttons_frame
from components.btns import crear_botones
from components.entrada_usr import crear_entrada
from config import buttons

try_rescontroller()

ventana = crear_ventana()

entrada_frame = entry_frame(ventana)

entrada = crear_entrada(entrada_frame)

btns_frame= buttons_frame(ventana)

crear_botones(buttons, btns_frame, entrada)

ventana.mainloop()