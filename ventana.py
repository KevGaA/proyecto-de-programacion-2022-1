from cgitb import text
from ctypes import sizeof
from msilib.schema import TextStyle
from numbers import Number
from struct import pack
from subprocess import call
from tkinter import *
import tkinter as tk
from tkinter import font
from tkinter import Canvas
from turtle import left

import graficador



i=0
operacion= []

def numeros(n):
    global i 
    d2.insert(i,n)
    if (n==0):
        display.create_oval(5,5,10,10)
        display.addtag_all
    elif (n==1):
        display.create_line(10,10,10,20)
        display.addtag_all
    elif (n==2):
        x1=30
        x2=40
        y1=10
        y2=20
        y3=30

        display.create_line(x1,y1,x2,y1)
        display.create_line(x2,y1,x2,y2)
        display.create_line(x2,y2,x1,y2)
        display.create_line(x1,y2,x1,y3)
        display.create_line(x1,y3,x2,y3)
    
    i+=1

##configuracion de la ventana 
app = Tk()
app.title("Graficador de expresiones matematicas")
app.geometry("800x600") ##dimensiones de la ventanan principal ANCHOXALTO
app.configure(background="light blue")

#entrada de la calculadora
display = Canvas(app)
display.place(x=400,y=25,width=375,height=550)


#entrada de teclado
d2 = Entry(app)
d2.place(x=10,y=525,width=375,height=30)
d2.config(font=('ARIAL',10))

#botones de los numeros 

btn0 = Button(app, text="C",height=5,width=10).place(x=25,y=25)
btn1 = Button(app, text="",height=5,width=10).place(x=110,y=25)
btn2 = Button(app, text="",height=5,width=10).place(x=195,y=25)
btn3 = Button(app, text="/",height=5,width=10).place(x=280,y=25)

btn4 = Button(app, text="7",height=5,width=10,command=lambda:numeros(7)).place(x=25,y=120)
btn5 = Button(app, text="8",height=5,width=10,command=lambda:numeros(8)).place(x=110,y=120)
btn6 = Button(app, text="9",height=5,width=10,command=lambda:numeros(9)).place(x=195,y=120)
btn7 = Button(app, text="X",height=5,width=10).place(x=280,y=120)

btn8 = Button(app, text="4",height=5,width=10,command=lambda:numeros(4)).place(x=25,y=215)
btn9 = Button(app, text="5",height=5,width=10,command=lambda:numeros(5)).place(x=110,y=215)
btn10 = Button(app, text="6",height=5,width=10,command=lambda:numeros(6)).place(x=195,y=215)
btn11 = Button(app, text="-",height=5,width=10).place(x=280,y=215)

btn12 = Button(app, text="1",height=5,width=10,command=lambda:numeros(1)).place(x=25,y=310)
btn13 = Button(app, text="2",height=5,width=10,command=lambda:numeros(2)).place(x=110,y=310)
btn14 = Button(app, text="3",height=5,width=10,command=lambda:numeros(3)).place(x=195,y=310)
btn15 = Button(app, text="+",height=5,width=10).place(x=280,y=310)

##BOTONES OPERADORES    
Button(app, text="0",height=5,width=10,command=lambda:numeros(0)).place(x=25,y=405,width=165)
Button(app, text=".",height=5,width=10).place(x=195,y=405)
Button(app, text="=",height=5,width=10).place(x=280,y=405)



app.mainloop()


