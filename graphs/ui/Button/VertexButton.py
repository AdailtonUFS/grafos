import tkinter as tk

from graphs.ui.Figures.VertexFigure import VertexFigure


class VertexButton:
    def __init__(self, canvas: tk.Canvas):
        self.object = None
        self.text = None
        self.canvas = canvas
        self.radius = 20

        self.canvas.bind('<Configure>', self.on_canvas_resize)
        self.update_button_position()

    def update_button_position(self):
        canvas_width = self.canvas.winfo_width()
        button_width = 2 * self.radius
        x = (canvas_width - button_width) / 2
        y = 40

        x1, y1 = x, y - self.radius
        x2, y2 = x + button_width, y + self.radius

        if self.object is not None:
            self.canvas.delete(self.object)

        if self.text is not None:
            self.canvas.delete(self.text)

        button_tag = 'vertex_button'
        self.object = VertexFigure(self.canvas, [x1, y1, x2, y2]).make()
        self.canvas.addtag_withtag(button_tag, self.object)  # Adicionar a nova tag ao botão

        text_x = (x1 + x2) / 2
        text_y = (y1 + y2) / 2
        self.text = self.canvas.create_text(text_x, text_y, text="v1", fill="black", tags=button_tag)

        self.canvas.tag_bind(button_tag, '<Button-1>', self.on_click)

    def on_canvas_resize(self, event):
        self.update_button_position()

    def on_click(self, event):
        self.canvas.master.drawable_area.create_vertex()
