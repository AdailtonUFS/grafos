import tkinter as tk
from graphs.ui.Button.EdgeButton import EdgeButton
from graphs.ui.Button.VertexButton import VertexButton


class OptionsMenu(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.config(bg="lightgray")
        self.grid(row=0, column=1, sticky="nsew")
        self.vertex_button = VertexButton(master=self)
        self.edge_button = EdgeButton(master=self)
