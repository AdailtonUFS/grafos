import tkinter as tk
from OptionsMenu import OptionsMenu
import platform

from graphs.ui.DrawableArea import DrawableArea


class Application(tk.Tk):
    def __init__(self, master=None):
        super().__init__()

        self.config(bg="white")
        self.columnconfigure(0, weight=95)  # 95% da largura para a coluna 0
        self.columnconfigure(1, weight=5)  # 5% da largura para a coluna 1
        self.rowconfigure(0, weight=1)  # 100% da altura para a linha 0

        if platform.system() == "Linux":
            self.attributes('-zoomed', True)
        else:
            self.state('zoomed')

        self.drawable_area = DrawableArea(master=self)
        self.option_menu = OptionsMenu(master=self)


app = Application()
app.title('Grafos')
app.mainloop()
