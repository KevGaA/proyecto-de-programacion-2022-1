from cgitb import text
from tkinter import *
import tkinter as tk
from tkinter import font

##configuracion de la ventana 
app = Tk()
app.title("graficador de expresiones matematicas")
app.geometry("800x600") ##dimensiones de la ventanan principal ANCHOXALTO
app.configure(background="light blue")

#entrada de la calculadora
display = Entry(app)
display.grid(row=1, columnspan=6, sticky=W+E)

#botones de los numeros 
Button(app, text="C").grid(row=2,column=0)
Button(app, text="").grid(row=2,column=1)
Button(app, text="").grid(row=2,column=2)
Button(app, text="/").grid(row=2,column=3)

Button(app, text="7").grid(row=3,column=0)
Button(app, text="8").grid(row=3,column=1)
Button(app, text="9").grid(row=3,column=2)
Button(app, text="X").grid(row=3,column=3)

Button(app, text="4").grid(row=4,column=0)
Button(app, text="5").grid(row=4,column=1)
Button(app, text="6").grid(row=4,column=2)
Button(app, text="-").grid(row=4,column=3)

Button(app, text="1").grid(row=5,column=0)
Button(app, text="2").grid(row=5,column=1)
Button(app, text="3").grid(row=5,column=2)
Button(app, text="+").grid(row=5,column=3)

##BOTONES OPERADORES    
Button(app, text="0").grid(row=6,column=0)
Button(app, text=".").grid(row=6,column=1)
Button(app, text="=").grid(row=6,column=3)





app.mainloop()