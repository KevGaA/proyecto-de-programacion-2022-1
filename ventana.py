from tkinter import *
from tkinter import colorchooser
import tkinter as tk
from tkinter import font
from tkinter import Canvas
from turtle import color

#aa
i=0
c=0

<<<<<<< HEAD

def numeros(n):
    global i 
    global c
=======
color = "black"
color_ope="black"
ecuacion = []

def numeros(n):
    global i
    global c

>>>>>>> kevgaa
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
<<<<<<< HEAD
=======
        ecuacion.append("/")
>>>>>>> kevgaa
    if (n==0):
        
        display.create_oval(x1,y1,x2,y3)
        display.addtag_all
    elif (n==1):

<<<<<<< HEAD
        display.create_line(x1,y1,x1,y3)
=======
        display.create_line(x1,y1,x1,y3,fill=color)
>>>>>>> kevgaa
        display.addtag_below
        ecuacion.append(1)
    
    #numero 2
    elif (n==2):

        display.create_line(x1,y1,x2,y1,fill=color)
        display.create_line(x2,y1,x2,y2,fill=color)
        display.create_line(x2,y2,x1,y2,fill=color)
        display.create_line(x1,y2,x1,y3,fill=color)
        display.create_line(x1,y3,x2,y3,fill=color)

    
    elif (n==3):
       

        display.create_line(x1,y1,x2,y1,fill=color)
        display.create_line(x2,y1,x2,y2,fill=color)
        display.create_line(x2,y2,x1,y2,fill=color)
        display.create_line(x2,y2,x2,y3,fill=color)
        display.create_line(x2,y3,x1,y3,fill=color)
    
    elif (n==4):
       

        display.create_line(x2,y1,x2,y3,fill=color)
        display.create_line(x1,y2,x2,y2,fill=color)
        display.create_line(x2,y1,x2,y2,fill=color)
        display.create_line(x1,y2,x1,y1,fill=color)

    elif (n==5):
        

        display.create_line(x1,y1,x2+2,y1,fill=color) 
        display.create_line(x1,y1,x1,y2,fill=color)
        display.create_line(x2,y2,x1,y2,fill=color)
        display.create_line(x2+1,y2,x2+1,y3,fill=color)
        display.create_line(x1,y3,x2+2,y3,fill=color)

    elif (n==6):
        

        display.create_line(x1,y1,x2+2,y1,fill=color) 
        display.create_line(x1,y1,x1,y2,fill=color)
        display.create_line(x2,y2,x1,y2,fill=color)
        display.create_line(x2+1,y2,x2+1,y3,fill=color)
        display.create_line(x1,y3,x2+2,y3,fill=color)
        display.create_line(x1,y2,x1,y3,fill=color)

    elif(n==7):
       
<<<<<<< HEAD
        display.create_line(x1,y1,x2+3,y1)
        display.create_line(x2+3,y1,x1,y3)
=======
        display.create_line(x1,y1,x2+3,y1,fill=color)
        display.create_line(x2+3,y1,x1,y3,fill=color)
>>>>>>> kevgaa

    elif (n==8):
       

        display.create_line(x1,y1,x2+2,y1,fill=color) 
        display.create_line(x1,y1,x1,y2,fill=color)
        display.create_line(x2,y2,x1,y2,fill=color)
        display.create_line(x2+1,y1,x2+1,y2,fill=color)
        display.create_line(x2+1,y2,x2+1,y3,fill=color)
        display.create_line(x1,y3,x2+2,y3,fill=color)
        display.create_line(x1,y2,x1,y3,fill=color)

    elif(n==9):
        
<<<<<<< HEAD

        display.create_line(x1,y1,x2+2,y1) 
        display.create_line(x1,y1,x1,y2)
        display.create_line(x2,y2,x1,y2)
        display.create_line(x2+1,y1,x2+1,y2)
        display.create_line(x2+1,y2,x2+1,y3)
        display.create_line(x1,y3,x2+2,y3)


=======
>>>>>>> kevgaa

        display.create_line(x1,y1,x2+2,y1,fill=color) 
        display.create_line(x1,y1,x1,y2,fill=color)
        display.create_line(x2,y2,x1,y2,fill=color)
        display.create_line(x2+1,y1,x2+1,y2,fill=color)
        display.create_line(x2+1,y2,x2+1,y3,fill=color)
        display.create_line(x1,y3,x2+2,y3,fill=color)

    #operadores 
    elif (n=="/"):
        
        x1=x+5
        x2=x+10
        y1=10
        y2=20
        y3=30
        display.create_line(x2-5,y3+5,x1-10,y3+5,fill=color_ope)
        display.addtag_below
    
    elif (n=="-"):
        x1=x+5
        x2=x+10
        y1=10
        y2=20
        y3=30
        display.create_line(x1,y2,x2,y2,fill=color_ope)
        display.addtag_below

    elif (n=="+"):
        x1=x+5
        x2=x+10
        y1=10
        y2=20
        y3=30
        display.create_line(x1,y2,x2,y2,fill=color_ope)
        display.create_line(x2-3,y1,x2-3,y3,fill=color_ope)
        display.addtag_below
    
    elif (n=="*"):
        x1=x+5
        x2=x+10
        y1=10
        y2=20
        y3=30
        display.create_line(x2,y1,x1,y3,fill=color_ope)
        display.create_line(x1,y1,x2,y3,fill=color_ope)
        display.create_line(x1,y2,x2,y2,fill=color_ope)
        
        display.addtag_below
    elif (n=="x"):
        i=0
        display.delete("all")
<<<<<<< HEAD
=======
        d2.delete(0, END)
>>>>>>> kevgaa
        
    c=n    
    i+=1
    
def colorpicker1(n):
    global color

    if n==0:
        color="black"
    elif n==1:
        color="red"
        geometry = "1000x800"
    elif n==2:
        color="yellow"
    elif n==3:
        color="orange" 
    elif n==4:
        color="pink" 
    elif n==5:
        color="blue" 
    elif n==6:
        color="green" 
    elif n==7:
        color="cyan" 
    elif n==8:
        color="purple" 
    elif n==9:
        color="brown"  
    elif n==10:
        color="grey" 
    elif n==11:
        color="teal" 
    elif n==12:
        color="lime"    
    return color
    
def colorpicker0(n):
    global color_ope

    if n==0:
        color_ope="black"
    elif n==1:
        color_ope="red"
    elif n==2:
        color_ope="yellow"
    elif n==3:
        color_ope="orange" 
    elif n==4:
        color_ope="pink" 
    elif n==5:
        color_ope="blue" 
    elif n==6:
        color_ope="green" 
    elif n==7:
        color_ope="cyan" 
    elif n==8:
        color_ope="purple" 
    elif n==9:
        color_ope="brown"  
    elif n==10:
        color_ope="grey" 
    elif n==11:
        color_ope="teal" 
    elif n==12:
        color_ope="lime"    
    return color_ope

def mostrarlista(ecuacion,i=0):
    if i != len(ecuacion):
        print(ecuacion[i])
        mostrarlista(ecuacion,i+1)




##configuracion de la ventana 

app = Tk()
app.title("Graficador de expresiones matematicas")
app.geometry("1000x600") ##dimensiones de la ventanan principal ANCHOXALTO
app.configure(background="light blue")

#entrada de la calculadora
display = Canvas(app)
display.place(x=460,y=25,width=375,height=550)

#entrada de teclado
d2 = Entry(app)
d2.place(x=10,y=525,width=434,height=30)
d2.config(font=('ARIAL',10))

#botones de los numeros 

<<<<<<< HEAD
btn0 = Button(app, text="C",height=5,width=10,command=lambda:numeros("x")).place(x=25,y=25)
btn1 = Button(app, text="",height=5,width=10).place(x=110,y=25)
btn2 = Button(app, text="",height=5,width=10).place(x=195,y=25)
=======
btn0 = Button(app, text="CE",height=5,width=10,command=lambda:numeros("x")).place(x=25,y=25)
btn1 = Button(app, text="CORD",height=5,width=10).place(x=110,y=25)
btn2 = Button(app, text="COLOR",height=5,width=10,command=mostrarlista(ecuacion)).place(x=195,y=25)
>>>>>>> kevgaa
btn3 = Button(app, text="/",height=5,width=10,command=lambda:numeros("/")).place(x=280,y=25)
btn3 = Button(app, text=" ",height=5,width=10,command=lambda:numeros(" ")).place(x=365,y=25)

btn4 = Button(app, text="7",height=5,width=10,command=lambda:numeros(7)).place(x=25,y=120)
btn5 = Button(app, text="8",height=5,width=10,command=lambda:numeros(8)).place(x=110,y=120)
btn6 = Button(app, text="9",height=5,width=10,command=lambda:numeros(9)).place(x=195,y=120)
btn7 = Button(app, text="X",height=5,width=10,command=lambda:numeros("*")).place(x=280,y=120)
Button(app, text=" ",height=5,width=10,command=lambda:numeros(" ")).place(x=365,y=120)
btn8 = Button(app, text="4",height=5,width=10,command=lambda:numeros(4)).place(x=25,y=215)
btn9 = Button(app, text="5",height=5,width=10,command=lambda:numeros(5)).place(x=110,y=215)
btn10 = Button(app, text="6",height=5,width=10,command=lambda:numeros(6)).place(x=195,y=215)
btn11 = Button(app, text="-",height=5,width=10,command=lambda:numeros("-")).place(x=280,y=215)
Button(app, text=" ",height=5,width=10,command=lambda:numeros(" ")).place(x=365,y=215)
btn12 = Button(app, text="1",height=5,width=10,command=lambda:numeros(1)).place(x=25,y=310)
btn13 = Button(app, text="2",height=5,width=10,command=lambda:numeros(2)).place(x=110,y=310)
btn14 = Button(app, text="3",height=5,width=10,command=lambda:numeros(3)).place(x=195,y=310)
btn15 = Button(app, text="+",height=5,width=10,command=lambda:numeros("+")).place(x=280,y=310)
Button(app, text=" ",height=5,width=10,command=lambda:numeros(" ")).place(x=365,y=310) 
Button(app, text="0",height=5,width=10,command=lambda:numeros(0)).place(x=25,y=405)
Button(app, text="0",height=5,width=10,command=lambda:numeros(0)).place(x=110,y=405)
Button(app, text=".",height=5,width=10,command=lambda:numeros(".")).place(x=195,y=405)
Button(app, text="=",height=5,width=10).place(x=280,y=405)
Button(app, text=" ",height=5,width=10,command=lambda:numeros(" ")).place(x=365,y=405)

#botones de los colores numeros
btnc0 = Button(app, text="",height=1,width=5,bg="black",command=lambda:colorpicker1(0)).place(x=850,y=40)
btnc1 = Button(app, text="",height=1,width=5,bg="red",command=lambda:colorpicker1(1)).place(x=850,y=70)
btnc2 = Button(app, text="",height=1,width=5,bg="yellow",command=lambda:colorpicker1(2)).place(x=850,y=100)
btnc3 = Button(app, text="",height=1,width=5,bg="orange",command=lambda:colorpicker1(3)).place(x=850,y=130)
btnc4 = Button(app, text="",height=1,width=5,bg="pink",command=lambda:colorpicker1(4)).place(x=850,y=160)
btnc5 = Button(app, text="",height=1,width=5,bg="blue",command=lambda:colorpicker1(5)).place(x=850,y=190)
btnc6 = Button(app, text="",height=1,width=5,bg="green",command=lambda:colorpicker1(6)).place(x=850,y=220)
btnc7 = Button(app, text="",height=1,width=5,bg="cyan",command=lambda:colorpicker1(7)).place(x=850,y=250)
btnc8 = Button(app, text="",height=1,width=5,bg="purple",command=lambda:colorpicker1(8)).place(x=850,y=280)
btnc9 = Button(app, text="",height=1,width=5,bg="brown",command=lambda:colorpicker1(9)).place(x=850,y=310)
btnc10 = Button(app, text="",height=1,width=5,bg="grey",command=lambda:colorpicker1(10)).place(x=850,y=340)
btnc11 = Button(app, text="",height=1,width=5,bg="teal",command=lambda:colorpicker1(11)).place(x=850,y=370)
btnc12 = Button(app, text="",height=1,width=5,bg="lime",command=lambda:colorpicker1(12)).place(x=850,y=400)

#botones de los colores operadores
btnc0 = Button(app, text="",height=1,width=5,bg="black",command=lambda:colorpicker0(0)).place(x=900,y=40)
btnc1 = Button(app, text="",height=1,width=5,bg="red",command=lambda:colorpicker0(1)).place(x=900,y=70)
btnc2 = Button(app, text="",height=1,width=5,bg="yellow",command=lambda:colorpicker0(2)).place(x=900,y=100)
btnc3 = Button(app, text="",height=1,width=5,bg="orange",command=lambda:colorpicker0(3)).place(x=900,y=130)
btnc4 = Button(app, text="",height=1,width=5,bg="pink",command=lambda:colorpicker0(4)).place(x=900,y=160)
btnc5 = Button(app, text="",height=1,width=5,bg="blue",command=lambda:colorpicker0(5)).place(x=900,y=190)
btnc6 = Button(app, text="",height=1,width=5,bg="green",command=lambda:colorpicker0(6)).place(x=900,y=220)
btnc7 = Button(app, text="",height=1,width=5,bg="cyan",command=lambda:colorpicker0(7)).place(x=900,y=250)
btnc8 = Button(app, text="",height=1,width=5,bg="purple",command=lambda:colorpicker0(8)).place(x=900,y=280)
btnc9 = Button(app, text="",height=1,width=5,bg="brown",command=lambda:colorpicker0(9)).place(x=900,y=310)
btnc10 = Button(app, text="",height=1,width=5,bg="grey",command=lambda:colorpicker0(10)).place(x=900,y=340)
btnc11 = Button(app, text="",height=1,width=5,bg="teal",command=lambda:colorpicker0(11)).place(x=900,y=370)
btnc12 = Button(app, text="",height=1,width=5,bg="lime",command=lambda:colorpicker0(12)).place(x=900,y=400)




app.mainloop()
