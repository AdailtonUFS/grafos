import tkinter as tk


class VertexFigure(tk.Canvas):
    def __init__(self, master=None):
        super().__init__(master, width=50, height=50)
        self.vertex = self.create_oval(0, 0, 50, 50, fill='white', outline='black', width=2)

    def move_to(self, x, y):
        self.coords(self.vertex, x, y, x + 50, y + 50)
