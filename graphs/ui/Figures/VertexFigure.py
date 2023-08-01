import tkinter as tk
from typing import List


class VertexFigure:
    def __init__(self, canvas: tk.Canvas, position: List[int]):
        self.canvas = canvas
        self.position = position

    def make(self):
        x1, y1, x2, y2 = self.position
        return self.canvas.create_oval(x1, y1, x2, y2, fill='white', outline='black', width=2)
