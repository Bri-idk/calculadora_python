import ctypes as ct

def try_rescontroller():
    try:
        ct.windll.shcore.SetProcessDpiAwareness(1)
    except:
        ct.windll.user32.SetProcessDpiAware()