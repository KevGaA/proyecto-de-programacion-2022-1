from tkinter import *
import tkinter as tk
from tkinter import font
from tkinter import Canvas

i=0
c=0
def numeros(n):
    global i 
    global c
    d2.insert(i,n)
    x=i*10
    x1=x+5
    x2=x+10
    y1=10
    y2=20
    y3=30
    
    if(c=="/"):
        i-=1
        x1=x-15
        x2=x-10
        y1=50
        y2=60
        y3=70

    if (n==0):
        
        display.create_oval(x1,y1,x2,y3)
        display.addtag_all

    elif (n==1):
        display.create_line(x1,y1,x1,y3)
        display.addtag_below

    elif (n==2):
        display.create_line(x1,y1,x2,y1)
        display.create_line(x2,y1,x2,y2)
        display.create_line(x2,y2,x1,y2)
        display.create_line(x1,y2,x1,y3)
        display.create_line(x1,y3,x2,y3)
    
    elif (n==3):
       
        display.create_line(x1,y1,x2,y1)
        display.create_line(x2,y1,x2,y2)
        display.create_line(x2,y2,x1,y2)
        display.create_line(x2,y2,x2,y3)
        display.create_line(x2,y3,x1,y3)
    
    elif (n==4):
       
        display.create_line(x2,y1,x2,y3)
        display.create_line(x1,y2,x2,y2)
        display.create_line(x2,y1,x2,y2)
        display.create_line(x1,y2,x1,y1)

    elif (n==5):
        
        display.create_line(x1,y1,x2+2,y1) 
        display.create_line(x1,y1,x1,y2)
        display.create_line(x2,y2,x1,y2)
        display.create_line(x2+1,y2,x2+1,y3)
        display.create_line(x1,y3,x2+2,y3)

    elif (n==6):
        
        display.create_line(x1,y1,x2+2,y1) 
        display.create_line(x1,y1,x1,y2)
        display.create_line(x2,y2,x1,y2)
        display.create_line(x2+1,y2,x2+1,y3)
        display.create_line(x1,y3,x2+2,y3)
        display.create_line(x1,y2,x1,y3)

    elif(n==7):
       
        display.create_line(x1,y1,x2+3,y1)
        display.create_line(x2+3,y1,x1,y3)

    elif (n==8):
       
        display.create_line(x1,y1,x2+2,y1) 
        display.create_line(x1,y1,x1,y2)
        display.create_line(x2,y2,x1,y2)
        display.create_line(x2+1,y1,x2+1,y2)
        display.create_line(x2+1,y2,x2+1,y3)
        display.create_line(x1,y3,x2+2,y3)
        display.create_line(x1,y2,x1,y3)

    elif(n==9):
        
        display.create_line(x1,y1,x2+2,y1) 
        display.create_line(x1,y1,x1,y2)
        display.create_line(x2,y2,x1,y2)
        display.create_line(x2+1,y1,x2+1,y2)
        display.create_line(x2+1,y2,x2+1,y3)
        display.create_line(x1,y3,x2+2,y3)
    
    #operadores 
    elif (n=="/"):
        
        x1=x+5
        x2=x+10
        y1=10
        y2=20
        y3=30
        display.create_line(x2-5,y3+5,x1-10,y3+5)
        display.addtag_below
    
    elif (n=="-"):
        x1=x+5
        x2=x+10
        y1=10
        y2=20
        y3=30
        display.create_line(x1,y2,x2,y2)
        display.addtag_below

    elif (n=="+"):
        x1=x+5
        x2=x+10
        y1=10
        y2=20
        y3=30
        display.create_line(x1,y2,x2,y2)
        display.create_line(x2-3,y1,x2-3,y3)
        display.addtag_below
    
    elif (n=="*"):
        x1=x+5
        x2=x+10
        y1=10
        y2=20
        y3=30
        display.create_line(x2,y1,x1,y3)
        display.create_line(x1,y1,x2,y3)
        display.create_line(x1,y2,x2,y2)

    elif (n=="!"): #funcion factorial, no tiene asociado el boton, asi que aún no se puede mostrar en la aplicación
        display.create_line(x1,y1,x1,y3-5)
        display.create_line(x1,y1+19,x1,y3+2)
        display.addtag_below
    
    elif(n=="sen"): #funcion seno, no tiene asociado el boton, asi que aún no se puede mostrar en la aplicación
        #s de sen
        display.create_line(x1,y1+5,x2+2,y1+5) 
        display.create_line(x1,y1+5,x1,y2+3)
        display.create_line(x2,y2+3,x1,y2+3)
        display.create_line(x2+1,y2+3,x2+1,y3+1)
        display.create_line(x1,y3,x2+2,y3)
        #e de sen
        display.create_line(x1+15,y1+5,x2+2,y1+5) 
        display.create_line(x1+8,y1+5,x1+8,y2+11)
        display.create_line(x2+10,y2+3,x1+8,y2+3)
        display.create_line(x2+10,y2-5,x2+10,y3-6)
        display.create_line(x1+8,y3,x2+10,y3)
        #n de sen
        display.create_line(x1+18,y1+5,x1+18,y3+1)
        display.create_line(x1+18,y1+5,x1+25,y3+1)
        display.create_line(x1+25,y1+5,x1+25,y3+1)

    elif(n=="cos"): #funcion coseno
        #c de cos
        display.create_line(x1,y1+5,x2+2,y1+5)
        display.create_line(x1,y1+5,x1,y2+10)
        display.create_line(x1,y2+10,x2+2,y2+10)
        #o de cos
        display.create_oval(x1+15,y1+5,x2+2,y3)
        #s de cos
        display.create_line(x1+18,y1+5,x2+18,y1+5) 
        display.create_line(x1+18,y1+5,x1+18,y2+3)
        display.create_line(x2+18,y2+3,x1+18,y2+3)
        display.create_line(x2+18,y2+3,x2+18,y3+1)
        display.create_line(x1+18,y3,x2+18,y3)


    elif(n=="tan"):
        #t de tan
        display.create_line(x1,y1+5,x2+4,y1+5)
        display.create_line(x1+4,y1+5,x1+4,y3)

        #a de tan
        display.create_line(x1+13,y1+5,x1+8,y3)
        display.create_line(x1+13,y1+5,x1+18,y3)
        display.create_line(x1+10,y1+15,x1+17,y1+15)

        #n de tan
        display.create_line(x1+20,y1+5,x1+20,y3)
        display.create_line(x1+20,y1+5,x1+25,y3)
        display.create_line(x1+25,y1+5,x1+25,y3)

        display.addtag_below
        
    elif (n=="x"):
        i=0
        display.delete("all")
        
    c=n    
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
btn0 = Button(app, text="C",height=5,width=10,command=lambda:numeros("x")).place(x=25,y=25)
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
