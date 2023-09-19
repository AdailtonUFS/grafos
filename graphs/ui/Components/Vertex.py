import tkinter as tk

from graphs.ui.Figures.VertexFigure import VertexFigure


class Vertex:
    def __init__(self, canvas: tk.Canvas, label: str):
        self.text = None
        self.object = None
        self.label = label
        self.canvas = canvas
        self.create_centered_vertex(70)

    def create_centered_vertex(self, size):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        center_x = canvas_width // 2
        center_y = canvas_height // 2

        x1, y1 = center_x - size // 2, center_y - size // 2
        x2, y2 = center_x + size // 2, center_y + size // 2


        position = [x1, y1, x2, y2]

        self.object = VertexFigure(self.canvas, position).make()
        self.canvas.tag_bind(self.object, '<B1-Motion>', self.on_drag)
        self.canvas.tag_bind(self.object, '<Enter>', self.on_enter)
        self.canvas.tag_bind(self.object, '<Leave>', self.on_leave)

        button_tag = 'vertex_button'
        self.canvas.addtag_withtag(button_tag, self.object)  # Adicionar a nova tag ao botão

        text_x = (x1 + x2) / 2
        text_y = (y1 + y2) / 2
        self.text = self.canvas.create_text(text_x, text_y, text=self.label, fill="black", tags=button_tag)
        self.canvas.tag_bind(self.text, '<B1-Motion>', self.on_drag)

    def on_enter(self, event):
        self.canvas.config(cursor='hand2')

    def on_leave(self, event):
        self.canvas.config(cursor='')

    def on_drag(self, event):
        x_center = (self.canvas.coords(self.object)[0] + self.canvas.coords(self.object)[2]) / 2
        y_center = (self.canvas.coords(self.object)[1] + self.canvas.coords(self.object)[3]) / 2
        delta_x = event.x - x_center
        delta_y = event.y - y_center

        self.canvas.move(self.object, delta_x, delta_y)
        self.canvas.move(self.text, delta_x, delta_y)
