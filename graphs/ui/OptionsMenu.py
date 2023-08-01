import tkinter as tk
from graphs.ui.Button.EdgeButton import EdgeButton
from graphs.ui.Button.VertexButton import VertexButton


class OptionsMenu(tk.Canvas):
    def __init__(self, master=None):
        super().__init__(master)
        self.config(bg="white")
        self.grid(row=0, column=1, sticky="nsew", padx=(0, 10), pady=10)
        self.vertex_button = VertexButton(self)
        # self.edge_button = EdgeButton(master=self)
