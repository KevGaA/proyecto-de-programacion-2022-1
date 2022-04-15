from cgitb import text
from ctypes import sizeof
from msilib.schema import TextStyle
from struct import pack
from tkinter import *
import tkinter as tk
from tkinter import font


i=0

def numeros(n):
    global i 
    display.insert(i,n)
    i+=1

##configuracion de la ventana 
app = Tk()
app.title("Graficador de expresiones matematicas")
app.geometry("800x600") ##dimensiones de la ventanan principal ANCHOXALTO
app.configure(background="light blue")

#entrada de la calculadora
display = Entry(app)
display.place(x=400,y=25,width=375,height=550)
display.config(font=('Bradley hand ITC',20))

#entrada de teclado
d2 = Entry(app)
d2.place(x=10,y=25,width=375,height=30)
d2.config(font=('ARIAL',10))

#botones de los numeros 

btn0 = Button(app, text="C",height=5,width=10).place(x=25,y=25)
btn1 = Button(app, text="",height=5,width=10).place(x=110,y=25)
btn2 = Button(app, text="",height=5,width=10).place(x=195,y=25)
btn3 = Button(app, text="/",height=5,width=10,command=lambda:numeros("/")).place(x=280,y=25)

btn4 = Button(app, text="7",height=5,width=10,command=lambda:numeros(7)).place(x=25,y=120)
btn5 = Button(app, text="8",height=5,width=10,command=lambda:numeros(8)).place(x=110,y=120)
btn6 = Button(app, text="9",height=5,width=10,command=lambda:numeros(9)).place(x=195,y=120)
btn7 = Button(app, text="X",height=5,width=10,command=lambda:numeros("*")).place(x=280,y=120)

btn8 = Button(app, text="4",height=5,width=10,command=lambda:numeros(4)).place(x=25,y=215)
btn9 = Button(app, text="5",height=5,width=10,command=lambda:numeros(5)).place(x=110,y=215)
btn10 = Button(app, text="6",height=5,width=10,command=lambda:numeros(6)).place(x=195,y=215)
btn11 = Button(app, text="-",height=5,width=10,command=lambda:numeros("-")).place(x=280,y=215)

btn12 = Button(app, text="1",height=5,width=10,command=lambda:numeros(1)).place(x=25,y=310)
btn13 = Button(app, text="2",height=5,width=10,command=lambda:numeros(2)).place(x=110,y=310)
btn14 = Button(app, text="3",height=5,width=10,command=lambda:numeros(3)).place(x=195,y=310)
btn15 = Button(app, text="+",height=5,width=10,command=lambda:numeros("+")).place(x=280,y=310)

##BOTONES OPERADORES    
Button(app, text="0",height=5,width=10,command=lambda:numeros(0)).place(x=25,y=405,width=165)
Button(app, text=".",height=5,width=10,command=lambda:numeros(".")).place(x=195,y=405)
Button(app, text="=",height=5,width=10).place(x=280,y=405)

app.mainloop()