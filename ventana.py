from tkinter import *
import tkinter as tk
from tkinter import font

app = tk.Tk()
app.geometry("800x600") ##dimensiones de la ventanan principal ANCHOXALTO
app.configure(background="light blue")
#app.title("graficador de expresiones matematicas")
tk.Wm.wm_title(app, "graficador de expresiones matematicas")

tk.Button(
    app,
    text="click, me",
    font=("courier", 14),
    bg="#00a8e8",
    fg="white",
).pack(
    fill=tk.BOTH, 
    expand=True,
)



app.mainloop()