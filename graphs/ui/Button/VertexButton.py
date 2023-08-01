import tkinter as tk

from graphs.ui.Figures.VertexFigure import VertexFigure


class VertexButton:
    def __init__(self, canvas: tk.Canvas):
        self.canvas = canvas
        x = self.canvas.winfo_width() / 2
        radius = 30
        x1, y1 = x - radius, 30 - radius
        x2, y2 = x + radius, 30 + radius
        self.object = VertexFigure(self.canvas, [x1, y1, x2, y2]).make()
        self.canvas.tag_bind(self.object, '<Button-1>', self.on_click)

    def on_click(self, event):
        self.canvas.master.drawable_area.create_vertex()
