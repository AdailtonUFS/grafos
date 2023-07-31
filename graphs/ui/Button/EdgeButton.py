import tkinter as tk


class EdgeButton(tk.Button):
    def __init__(self, master=None, text="Aresta", bg="white", font=("Arial", 12),
                 relief="flat", bd=2, highlightbackground="gray", cursor="hand2", **kwargs):
        super().__init__(master, text=text, bg=bg, font=font, relief=relief, bd=bd,
                         highlightbackground=highlightbackground, cursor=cursor, **kwargs)

        self.pack(pady=5, padx=10, fill=tk.BOTH)
