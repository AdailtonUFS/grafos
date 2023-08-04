import tkinter as tk


from graphs.ui.Components.Vertex import Vertex


class DrawableArea(tk.Canvas):
    def __init__(self, master=None):
        super().__init__(master)
        self.config(bg="white")

    def create_vertex(self):
        Vertex(self)
