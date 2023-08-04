import tkinter as tk
from graphs.ui.Components.Buttons.EdgeButton import EdgeButton
from graphs.ui.Components.Buttons.VertexButton import VertexButton


class OptionsMenu(tk.Canvas):
    def __init__(self, master=None):
        super().__init__(master, width=10)
        self.config(bg="white")
        self.grid(row=0, column=1, sticky="nsew", padx=(0, 10), pady=10)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.vertex_button = VertexButton(self)
        self.edge_button = EdgeButton(master=self)
