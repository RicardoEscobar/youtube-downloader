"""Set dpi Awareness on windows 10"""

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
