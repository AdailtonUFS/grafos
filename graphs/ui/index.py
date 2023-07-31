import tkinter as tk

root = tk.Tk()
root.title("Grafos")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width}x{screen_height}")
root.config(bg="white")
root.columnconfigure(0, weight=19)  # 80% da largura para a coluna 0
root.columnconfigure(1, weight=1)  # 20% da largura para a coluna 1
root.rowconfigure(0, weight=1)  # 100% da altura para a linha 0

frame_left = tk.Frame(root, bg="lightgray")
frame_right = tk.Frame(root, bg="lightgray")

frame_left.grid(row=0, column=0, sticky="nsew",  padx=(0,5))
frame_right.grid(row=0, column=1, sticky="nsew")

vertex_button = tk.Button(frame_right, text="Vértice", bg="white", font=("Arial", 12),
                    relief="flat",bd=2, highlightbackground="gray", cursor="hand2")
vertex_button.pack(pady=(50, 10), padx=10, fill=tk.BOTH)

edge_button = tk.Button(frame_right, text="Aresta", bg="white", font=("Arial", 12),
                    relief="flat",bd=2, highlightbackground="gray", cursor="hand2")
edge_button.pack(pady=(10, 50), padx=10, fill=tk.BOTH)

root.mainloop()
