import tkinter as tk
from OptionsMenu import OptionsMenu
import platform

from graphs.ui.DrawableArea import DrawableArea


class Application(tk.Tk):
    def __init__(self, master=None):
        super().__init__()

        self.config(bg="white")
        self.columnconfigure(0, weight=19)  # 80% da largura para a coluna 0
        self.columnconfigure(1, weight=1)  # 20% da largura para a coluna 1
        self.rowconfigure(0, weight=1)  # 100% da altura para a linha 0

        if platform.system() == "Linux":
            self.attributes('-zoomed', True)
        else:
            self.state('zoomed')

        self.option_menu = OptionsMenu(master=self)
        self.drawable_area = DrawableArea(master=self)


app = Application()
app.title('Grafos')
app.mainloop()
