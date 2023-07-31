import tkinter as tk
from OptionsMenu import OptionsMenu


class Application(tk.Tk):
    def __init__(self, master=None):
        super().__init__()

        self.config(bg="white")
        self.columnconfigure(0, weight=19)  # 80% da largura para a coluna 0
        self.columnconfigure(1, weight=1)  # 20% da largura para a coluna 1
        self.rowconfigure(0, weight=1)  # 100% da altura para a linha 0
        self.state('zoomed')
        self.option_menu = OptionsMenu(master=self)

    def on_mouse_move(self, event):
        self.option_menu.vertex_button.vertex_figure.move_to(event.x, event.y)


app = Application()
app.title('Grafos')
app.mainloop()
