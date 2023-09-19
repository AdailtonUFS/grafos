import tkinter as tk
import platform

from OptionsMenu import OptionsMenu
from graphs.entities.AdjacencyStructure import AdjacencyStructure

from graphs.ui.DrawableArea import DrawableArea


class Application(tk.Tk):
    def __init__(self, master=None):
        self.adjacency_structure:AdjacencyStructure = AdjacencyStructure()
        self.last_vertex = 0
        super().__init__()
        self.config(bg="white")
        self.layout()
        self.geometry("%dx%d" % (800, 600))
        self.maximized()

        self.drawable_area = DrawableArea(master=self)
        self.drawable_area.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.option_menu = OptionsMenu(master=self, application=self)

    def layout(self):
        self.columnconfigure(0, weight=95)
        self.columnconfigure(1, weight=5)
        self.rowconfigure(0, weight=1)


    def maximized(self):
        if platform.system() == "Linux":
            self.attributes('-zoomed', True)
        else:
            self.state('zoomed')


app = Application()
app.title('Grafos')
app.mainloop()
