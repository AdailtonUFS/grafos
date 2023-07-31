import tkinter as tk

from graphs.ui.Figures.VertexFigure import VertexFigure


class VertexButton(tk.Button):
    def __init__(self, master=None, text="Vértice", bg="white", font=("Arial", 12),
                 relief="flat", bd=2, highlightbackground="gray", cursor="hand2", **kwargs):
        super().__init__(master, text=text, bg=bg, font=font, relief=relief, bd=bd,
                         highlightbackground=highlightbackground, cursor=cursor, **kwargs)

        self.pack(pady=(10, 5), padx=10, fill=tk.BOTH)
        self.bind('<Button-1>', self.on_click)

    def on_click(self, event):
        x, y = event.x, event.y
        vertex_figure = VertexFigure(self.master.master)
        vertex_figure.place(x=x, y=y)
