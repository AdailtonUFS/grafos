import tkinter as tk


from graphs.ui.Components.Vertex import Vertex


class DrawableArea(tk.Canvas):
    def __init__(self, master=None):
        super().__init__(master)
        self.config(bg="white")
        self.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    def create_vertex(self):
        Vertex(self)
