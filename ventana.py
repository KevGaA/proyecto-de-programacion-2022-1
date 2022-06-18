from cProfile import label
from email import parser
from sqlite3 import Row
from sre_parse import State
from tkinter import *
from tkinter import font
from tkinter import Canvas
from turtle import clear, color, width
from tkinter import *

#aa
i=0
c=10
modo_ven=0

color = "black"
color_ope="black"
ecuacion = []
anterior = " "
grande= 1
grandex=1
avance=0

def numeros(n):
    global i
    global c, anterior
    global x1,x2,y1,y2,y3
    global x11,x22,y11,y22,y33
    global grande,grandex

    
    d2.insert(i,n)
    
    x=i*10*grandex
    x1=x+5*grande
    x2=x+10*grande
    y1=10*grande
    y2=20*grande
    y3=30*grande

    ##elevados
    x11=x+1*grande
    x22=x+5*grande
    y11=5*grande
    y22=10*grande
    y33=15*grande
    
    if(c=="/"):
        i-=1
        x1=x-15
        x2=x-10
        y1=50
        y2=60
        y3=70
        ecuacion.append("/")
        display.addtag_below
    
    if (n==0):
        if anterior=="^":
            anterior=0
        else:
            display.create_oval(x1,y1,x2,y3,fill=color)
            display.addtag_below
            display.addtag_all
    
    elif (n==1):
        if anterior=="^":
            display.create_line(x11,y11,x11,y33,fill=color)
            anterior=1
        else:
            display.create_line(x1,y1,x1,y3,fill=color)
            display.addtag_below
            anterior=1
    
    #numero 2
    elif (n==2):
        if anterior=="^":
            display.create_line(x11,y11,x22,y11,fill=color)
            display.create_line(x22,y11,x22,y22,fill=color)
            display.create_line(x22,y22,x11,y22,fill=color)
            display.create_line(x11,y22,x11,y33,fill=color)
            display.create_line(x11,y33,x22,y33,fill=color)
            anterior=2
        else:
            display.create_line(x1,y1,x2,y1,fill=color)
            display.create_line(x2,y1,x2,y2,fill=color)
            display.create_line(x2,y2,x1,y2,fill=color)
            display.create_line(x1,y2,x1,y3,fill=color)
            display.create_line(x1,y3,x2,y3,fill=color)
            display.addtag_below
            anterior=2

    
    elif (n==3):
        if anterior=="^":
            display.create_line(x11,y11,x22,y11,fill=color)
            display.create_line(x22,y11,x22,y22,fill=color)
            display.create_line(x22,y22,x11,y22,fill=color)
            display.create_line(x22,y22,x22,y33,fill=color)
            display.create_line(x22,y33,x11,y33,fill=color)
            anterior=3
        else:
            display.create_line(x1,y1,x2,y1,fill=color)
            display.create_line(x2,y1,x2,y2,fill=color)
            display.create_line(x2,y2,x1,y2,fill=color)
            display.create_line(x2,y2,x2,y3,fill=color)
            display.create_line(x2,y3,x1,y3,fill=color)
            display.addtag_below
            anterior=3
    
    elif (n==4):
        if anterior=="^":
            display.create_line(x22,y11,x22,y33,fill=color)
            display.create_line(x11,y22,x22,y22,fill=color)
            display.create_line(x22,y11,x22,y22,fill=color)
            display.create_line(x11,y22,x11,y11,fill=color)
            anterior=4
        else:
            display.create_line(x2,y1,x2,y3,fill=color)
            display.create_line(x1,y2,x2,y2,fill=color)
            display.create_line(x2,y1,x2,y2,fill=color)
            display.create_line(x1,y2,x1,y1,fill=color)
            display.addtag_below
            anterior=4

    elif (n==5):
        if anterior=="^":
            display.create_line(x11,y11,x22+2,y11,fill=color) 
            display.create_line(x11,y11,x11,y22,fill=color)
            display.create_line(x22,y22,x11,y22,fill=color)
            display.create_line(x22+1,y22,x22+1,y33,fill=color)
            display.create_line(x11,y33,x22+2,y33,fill=color)
            anterior=5
        else:
            display.create_line(x1,y1,x2+2,y1,fill=color) 
            display.create_line(x1,y1,x1,y2,fill=color)
            display.create_line(x2,y2,x1,y2,fill=color)
            display.create_line(x2+1,y2,x2+1,y3,fill=color)
            display.create_line(x1,y3,x2+2,y3,fill=color)
            display.addtag_below
            anterior=5

    elif (n==6):
        if anterior=="^":
            display.create_line(x11,y11,x22+2,y11,fill=color) 
            display.create_line(x11,y11,x11,y22,fill=color)
            display.create_line(x22,y22,x11,y22,fill=color)
            display.create_line(x22+1,y22,x22+1,y33,fill=color)
            display.create_line(x11,y33,x22+2,y33,fill=color)
            display.create_line(x11,y22,x11,y33,fill=color)
            anterior=6
        else:
            display.create_line(x1,y1,x2+2,y1,fill=color) 
            display.create_line(x1,y1,x1,y2,fill=color)
            display.create_line(x2,y2,x1,y2,fill=color)
            display.create_line(x2+1,y2,x2+1,y3,fill=color)
            display.create_line(x1,y3,x2+2,y3,fill=color)
            display.create_line(x1,y2,x1,y3,fill=color)
            display.addtag_below
            anterior=6

    elif(n==7):
        if anterior=="^":
            display.create_line(x11,y11,x22+3,y11,fill=color)
            display.create_line(x22+3,y11,x11,y33,fill=color)
            anterior=7
        else:
            display.create_line(x1,y1,x2+3,y1,fill=color)
            display.create_line(x2+3,y1,x1,y3,fill=color)
            display.addtag_below
            anterior=7

    elif (n==8):
        if anterior=="^":
            display.create_line(x11,y11,x22+2,y11,fill=color) 
            display.create_line(x11,y11,x11,y22,fill=color)
            display.create_line(x22,y22,x11,y22,fill=color)
            display.create_line(x22+1,y11,x22+1,y22,fill=color)
            display.create_line(x22+1,y22,x22+1,y33,fill=color)
            display.create_line(x11,y33,x22+2,y33,fill=color)
            display.create_line(x11,y22,x11,y33,fill=color)
            anterior=8
        else:
            display.create_line(x1,y1,x2+2,y1,fill=color) 
            display.create_line(x1,y1,x1,y2,fill=color)
            display.create_line(x2,y2,x1,y2,fill=color)
            display.create_line(x2+1,y1,x2+1,y2,fill=color)
            display.create_line(x2+1,y2,x2+1,y3,fill=color)
            display.create_line(x1,y3,x2+2,y3,fill=color)
            display.create_line(x1,y2,x1,y3,fill=color)
            display.addtag_below
            anterior=8

    elif(n==9):
        if anterior=="^":
            display.create_line(x11,y11,x22+2,y11,fill=color) 
            display.create_line(x11,y11,x11,y22,fill=color)
            display.create_line(x22,y22,x11,y22,fill=color)
            display.create_line(x22+1,y11,x22+1,y22,fill=color)
            display.create_line(x22+1,y22,x22+1,y33,fill=color)
            display.create_line(x11,y33,x22+2,y33,fill=color)
            anterior=9
        else:
            display.create_line(x1,y1,x2+2,y1,fill=color) 
            display.create_line(x1,y1,x1,y2,fill=color)
            display.create_line(x2,y2,x1,y2,fill=color)
            display.create_line(x2+1,y1,x2+1,y2,fill=color)
            display.create_line(x2+1,y2,x2+1,y3,fill=color)
            display.create_line(x1,y3,x2+2,y3,fill=color)
            display.addtag_below
            anterior=9

    #operadores 
    elif (n=="/"):
        if anterior != "-" and anterior != "^" and anterior != "*" and anterior != "+" and anterior != " ":
            x1=x+5
            x2=x+10
            y1=10
            y2=20
            y3=30
            display.create_line(x2-5,y3+5,x1-10,y3+5,fill=color_ope)
            display.addtag_below
            anterior="/"
        else:
            i-=1
    
    elif (n=="-"):
        if anterior != "-" and anterior != "^" and anterior != "*":
            x1=x+5
            x2=x+10
            y1=10
            y2=20
            y3=30
            display.create_line(x1,y2,x2,y2,fill=color_ope)
            display.addtag_below
            anterior="-"
        else:
            i-=1

    elif (n=="+"):
        if anterior != "+" and anterior != "^" and anterior != "*" and anterior != " " and anterior != "-":
            x1=x+5
            x2=x+10
            y1=10
            y2=20
            y3=30
            display.create_line(x1,y2,x2,y2,fill=color_ope)
            display.create_line(x2-3,y1,x2-3,y3,fill=color_ope)
            display.addtag_below
            anterior="+"
        else:
            i-=1

 
    elif (n=="*"):
        if anterior != "+" and anterior != "^" and anterior != "*" and anterior != " " and anterior != "-":
            x1=x+5
            x2=x+10
            y1=10
            y2=20
            y3=30
            display.create_line(x2,y1,x1,y3,fill=color_ope)
            display.create_line(x1,y1,x2,y3,fill=color_ope)
            display.addtag_below

            anterior="*"
        else:
            i-=1

    elif (n=="!"): 
        if anterior != "+" and anterior != "^" and anterior != "*" and anterior != " " and anterior != "-" and anterior != "!" and anterior != "sen" and anterior != "cos" and anterior != "tan":
            display.create_line(x1,y1,x1,y3-5,fill=color_ope)
            display.create_line(x1,y1+19,x1,y3+2,fill=color_ope)
            display.addtag_below
            anterior="!"
        else:
            i-=1
    
    elif(n=="sen"): 
        if anterior != "^" and anterior != "!" and anterior != "sen" and anterior != "cos" and anterior != "tan":
            #s de sen
            display.create_line(x1,y1+5,x2+2,y1+5,fill=color_ope) 
            display.create_line(x1,y1+5,x1,y2+3,fill=color_ope)
            display.create_line(x2,y2+3,x1,y2+3,fill=color_ope)
            display.create_line(x2+1,y2+3,x2+1,y3+1,fill=color_ope)
            display.create_line(x1,y3,x2+2,y3,fill=color_ope)
            #e de sen
            display.create_line(x1+15,y1+5,x2+2,y1+5,fill=color_ope) 
            display.create_line(x1+8,y1+5,x1+8,y2+11,fill=color_ope)
            display.create_line(x2+10,y2+3,x1+8,y2+3,fill=color_ope)
            display.create_line(x2+10,y2-5,x2+10,y3-6,fill=color_ope)
            display.create_line(x1+8,y3,x2+10,y3,fill=color_ope)
            #n de sen
            display.create_line(x1+18,y1+5,x1+18,y3+1,fill=color_ope)
            display.create_line(x1+18,y1+5,x1+25,y3+1,fill=color_ope)
            display.create_line(x1+25,y1+5,x1+25,y3+1,fill=color_ope)
            display.addtag_below
            i+=3
            anterior="sen"
        else:
            i-=1

    elif(n=="cos"):
        if anterior != "^" and anterior != "!" and anterior != "sen" and anterior != "cos" and anterior != "tan":
            #c de cos
            display.create_line(x1,y1+5,x2+2,y1+5,fill=color_ope)
            display.create_line(x1,y1+5,x1,y2+10,fill=color_ope)
            display.create_line(x1,y2+10,x2+2,y2+10,fill=color_ope)
            #o de cos
            display.create_oval(x1+15,y1+5,x2+2,y3,fill=color_ope)
            #s de cos
            display.create_line(x1+18,y1+5,x2+18,y1+5,fill=color_ope) 
            display.create_line(x1+18,y1+5,x1+18,y2+3,fill=color_ope)
            display.create_line(x2+18,y2+3,x1+18,y2+3,fill=color_ope)
            display.create_line(x2+18,y2+3,x2+18,y3+1,fill=color_ope)
            display.create_line(x1+18,y3,x2+18,y3,fill=color_ope)
            display.addtag_below
            anterior="cos"
            i+=3
        else:
            i-=1


    elif(n=="tan"):
        if anterior != "^" and anterior != "!" and anterior != "sen" and anterior != "cos" and anterior != "tan":

            #t de tan
            display.create_line(x1,y1+5,x2+4,y1+5,fill=color_ope)
            display.create_line(x1+4,y1+5,x1+4,y3,fill=color_ope)
          
            #a de tan
            display.create_line(x1+13,y1+5,x1+8,y3,fill=color_ope)
            display.create_line(x1+13,y1+5,x1+18,y3,fill=color_ope)
            display.create_line(x1+10,y1+15,x1+17,y1+15,fill=color_ope)
            
            #n de tan
            display.create_line(x1+20,y1+5,x1+20,y3,fill=color_ope)
            display.create_line(x1+20,y1+5,x1+25,y3,fill=color_ope)
            display.create_line(x1+25,y1+5,x1+25,y3,fill=color_ope)
            display.addtag_below
            i+=3
            anterior="tan"
        else:
            i-=1
    
    elif n=="^": 
        if anterior != "+" and anterior != "^" and anterior != "*" and anterior != " " and anterior != "-" and anterior != "!" and anterior != "sen" and anterior != "cos" and anterior != "tan":
            anterior = "^"
        else:
            return 0

    #BORRAR TOD0
    if (n=="x"):
        i=0
        display.delete("all")
        d2.delete(0, END)
        anterior=" "

    ##AUMENTADOR DE TAMAÑO
    if n=="y":
        grande=1
        i=0
        d2.delete(0, END)
        display.delete("all")
    if n=="y1":
        grande=2
        i=0
        d2.delete(0, END)
        display.delete("all")
    if n=="y2":
        grande=4
        i=0
        d2.delete(0, END)
        display.delete("all")
    if n=="y3":
        grande=6
        i=0
        d2.delete(0, END)
        display.delete("all")
    if n=="y4":
        grande=8
        i=0
        d2.delete(0, END)
        display.delete("all")
    
    ##AUMENTADOR DE TAMAÑO LIENZO
    if n=="l":
        app.geometry("550x870")
        display.place(x=15,y=15,width=525,height=350)
        d2.delete(0, END)
    if n=="l1":
        app.geometry("650x870")
        display.place(x=15,y=15,width=625,height=350)
        d2.delete(0, END)
    if n=="l2":
        app.geometry("750x870")
        display.place(x=15,y=15,width=725,height=350)
        d2.delete(0, END)
    if n=="l3":
        app.geometry("850x870")
        display.place(x=15,y=15,width=825,height=350)
        d2.delete(0, END)
    if n=="l4":
        app.geometry("950x870")
        display.place(x=15,y=15,width=925,height=350)
        d2.delete(0, END)

    c=n    
    i+=1*grande
    
def colorpicker1(n):
    global color

    if n==0:
        color="black"
    elif n==1:
        color="red"
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

def colores():
        global avance
        
        c00.place(x=375,y=440)
        c01.place(x=425,y=440)
        c02.place(x=475,y=440)
        c03.place(x=375,y=470)
        c04.place(x=425,y=470)
        c05.place(x=475,y=470)
        c06.place(x=375,y=500)
        c07.place(x=425,y=500)
        c08.place(x=475,y=500)
        c09.place(x=375,y=530)
        c010.place(x=425,y=530)
        c011.place(x=475,y=530)


        #botones de los colores operadores
    

        c0.place(x=375,y=630)
        c1.place(x=425,y=630)
        c2.place(x=475,y=630)
        c3.place(x=375,y=660)
        c4.place(x=425,y=660)
        c5.place(x=475,y=660)
        c6.place(x=375,y=690)
        c7.place(x=425,y=690)
        c8.place(x=475,y=690)
        c9.place(x=375,y=720)
        c10.place(x=425,y=720)
        c11.place(x=475,y=720)

        

def mostrarlista(ecuacion,i=0):
    if i != len(ecuacion):
        print(ecuacion[i])
        mostrarlista(ecuacion,i+1)

def modo():
    global modo_ven

    if modo_ven%2==0:
        app.geometry("615x870")
        display.place(x=15,y=15,width=595,height=350)
        d2.place(x=15,y=375,width=595,height=30)
        m1.place(x=355,y=410)
        m2.place(x=355,y=500)        
        m3.place(x=355,y=590)       
        m4.place(x=355,y=680)       
        m5.place(x=355,y=770)

        numero.place(x=480,y=410)


        c00.place(x=375+80,y=440)
        c01.place(x=425+80,y=440)
        c02.place(x=475+80,y=440)
        c03.place(x=375+80,y=470)
        c04.place(x=425+80,y=470)
        c05.place(x=475+80,y=470)
        c06.place(x=375+80,y=500)
        c07.place(x=425+80,y=500)
        c08.place(x=475+80,y=500)
        c09.place(x=375+80,y=530)
        c010.place(x=425+80,y=530)
        c011.place(x=475+80,y=530)
    	
        operadores.place(x=480,y=600)
        c0.place(x=375+80,y=630)
        c1.place(x=425+80,y=630)
        c2.place(x=475+80,y=630)
        c3.place(x=375+80,y=660)
        c4.place(x=425+80,y=660)
        c5.place(x=475+80,y=660)
        c6.place(x=375+80,y=690)
        c7.place(x=425+80,y=690)
        c8.place(x=475+80,y=690)
        c9.place(x=375+80,y=720)
        c10.place(x=425+80,y=720)
        c11.place(x=475+80,y=720)

        
    if modo_ven%2!=0:
        app.geometry("550x870")
        display.place(x=15,y=15,width=525,height=350)
        d2.place(x=15,y=375,width=525,height=30)
        m1.place_forget()
        m2.place_forget()
        m3.place_forget()
        m4.place_forget()
        m5.place_forget()

        numero.place(x=400,y=410)
        c00.place(x=375,y=440)
        c01.place(x=425,y=440)
        c02.place(x=475,y=440)
        c03.place(x=375,y=470)
        c04.place(x=425,y=470)
        c05.place(x=475,y=470)
        c06.place(x=375,y=500)
        c07.place(x=425,y=500)
        c08.place(x=475,y=500)
        c09.place(x=375,y=530)
        c010.place(x=425,y=530)
        c011.place(x=475,y=530)

        operadores.place(x=400,y=600)
        c0.place(x=375,y=630)
        c1.place(x=425,y=630)
        c2.place(x=475,y=630)
        c3.place(x=375,y=660)
        c4.place(x=425,y=660)
        c5.place(x=475,y=660)
        c6.place(x=375,y=690)
        c7.place(x=425,y=690)
        c8.place(x=475,y=690)
        c9.place(x=375,y=720)
        c10.place(x=425,y=720)
        c11.place(x=475,y=720)

        
       
    modo_ven=modo_ven+1
    return modo_ven


def cord(n):
    if n==1:
        display.place_forget()  
        
def menubar():
    ############################################################## barra de menu
    menubar = Menu(app)
    app.config(menu=menubar)

    filemenu = Menu(menubar)
    editmenu = Menu(menubar)
    helpmenu = Menu(menubar)

    menubar.add_cascade(label="agrandar", menu=filemenu)
    menubar.add_cascade(label="lienzo",menu=editmenu)
    menubar.add_cascade(label="Ayuda", menu=helpmenu)

    filemenu.add_command(label="X1",command=lambda:numeros("y"))
    filemenu.add_command(label="X2",command=lambda:numeros("y1"))
    filemenu.add_command(label="X4",command=lambda:numeros("y2"))
    filemenu.add_command(label="X8",command=lambda:numeros("y3"))
    filemenu.add_command(label="X10",command=lambda:numeros("y4"))

    filemenu.add_separator()
    filemenu.add_command(label="Salir", command=app.quit)

    helpmenu.add_command(label="Ayuda")
    helpmenu.add_separator()
    helpmenu.add_command(label="Acerca de...")

    editmenu.add_command(label="X1",command=lambda:numeros("l"))
    editmenu.add_command(label="X2",command=lambda:numeros("l1"))
    editmenu.add_command(label="X4",command=lambda:numeros("l2"))
    editmenu.add_command(label="X8",command=lambda:numeros("l3"))
    editmenu.add_command(label="X10",command=lambda:numeros("l4"))


def calcular():
    display_state= d2.get()
    try:
        math_expression = parser.expr(display_state).compile()
        result = eval(math_expression)
        d2.delete(0, END)
        print(result)
        
    except Exception:
        d2.delete(0, END)

#############################################################
###############################################################configuracion de la ventana 

app = Tk()
app.title("Graficador de expresiones matematicas")
app.geometry("550x870") ##dimensiones de la ventanan principal ANCHOXALTO
app.configure(background="#515151")
app.resizable (0,0)
#############################################################

##############################################################entrada de la calculadora
display = Canvas(app)
display.place(x=15,y=15,width=525,height=350)
#############################################################

##############################################################entrada de teclado
d2 = Entry(app)
d2.place(x=15,y=375,width=525,height=30)
d2.config(font=('ARIAL',10))

##############################################################botones de los numeros 


btn0 = Button(app, text="CE",height=5,width=10,bg="#C2C2C2",relief="ridge",command=lambda:numeros("x"))
btn0.place(x=15,y=410)

btn1 = Button(app, text="CIENTIFICA",height=5,width=10,bg="#C2C2C2",relief="ridge",command=lambda:modo())
btn1.place(x=100,y=410)

btn2 = Button(app, text="COORD",height=5,width=10,bg="#C2C2C2",relief="ridge",command=lambda:cord(1))
btn2.place(x=185,y=410)

btn3 = Button(app, text="/",height=5,width=10,bg="#FF980B",relief="ridge",command=lambda:numeros("/"))
btn3.place(x=270,y=410)

btn4 = Button(app, text="7",height=5,width=10,bg="#818181",relief="ridge",command=lambda:numeros(7))
btn4.place(x=15,y=500)

btn5 = Button(app, text="8",height=5,width=10,bg="#818181",relief="ridge",command=lambda:numeros(8))
btn5.place(x=100,y=500)

btn6 = Button(app, text="9",height=5,width=10,bg="#818181",relief="ridge",command=lambda:numeros(9))
btn6.place(x=185,y=500)

btn7 = Button(app, text="X",height=5,width=10,bg="#FF980B",relief="ridge",command=lambda:numeros("*"))
btn7.place(x=270,y=500)

btn8 = Button(app, text="4",height=5,width=10,bg="#818181",relief="ridge",command=lambda:numeros(4))
btn8.place(x=15,y=590)
btn9 = Button(app, text="5",height=5,width=10,bg="#818181",relief="ridge",command=lambda:numeros(5))
btn9.place(x=100,y=590)
btn10 = Button(app, text="6",height=5,width=10,bg="#818181",relief="ridge",command=lambda:numeros(6))
btn10.place(x=185,y=590)
btn11 = Button(app, text="-",height=5,width=10,bg="#FF980B",relief="ridge",command=lambda:numeros("-"))
btn11.place(x=270,y=590)

btn12 = Button(app, text="1",height=5,width=10,bg="#818181",relief="ridge",command=lambda:numeros(1))
btn12.place(x=15,y=680)
btn13 = Button(app, text="2",height=5,width=10,bg="#818181",relief="ridge",command=lambda:numeros(2))
btn13.place(x=100,y=680)
btn14 = Button(app, text="3",height=5,width=10,bg="#818181",relief="ridge",command=lambda:numeros(3))
btn14.place(x=185,y=680)
btn15 = Button(app, text="+",height=5,width=10,bg="#FF980B",relief="ridge",command=lambda:numeros("+"))
btn15.place(x=270,y=680)

btn16=Button(app, text="0",height=5,width=10,bg="#818181",relief="ridge",command=lambda:numeros(0))
btn16.place(x=15,y=770)
btn17=Button(app, text=".",height=5,width=10,bg="#818181",relief="ridge",command=lambda:numeros("."))
btn17.place(x=100,y=770)
btn18=Button(app, text="^",height=5,width=10,bg="#818181",relief="ridge",command=lambda:numeros("^"))
btn18.place(x=185,y=770)
btn19=Button(app, text="=",height=5,width=10,bg="#FF980B",relief="ridge",command=lambda:calcular())
btn19.place(x=270,y=770)

############################################################# MODO CIENTIFICO
m1=Button(app, text="SEN",height=5,width=10,bg="#FF980B",relief="ridge",command=lambda:numeros("sen"))
m2=Button(app, text=" ",height=5,width=10,bg="#FF980B",relief="ridge")
m3=Button(app, text="TAN",height=5,width=10,bg="#FF980B",relief="ridge",command=lambda:numeros("tan"))
m4=Button(app, text="COS",height=5,width=10,bg="#FF980B",relief="ridge",command=lambda:numeros("cos"))
m5=Button(app, text="!",height=5,width=10,bg="#FF980B",relief="ridge",command=lambda:numeros("!"))

############################################################# colores
c0 = Button(app, text="",height=1,width=5,bg="black",command=lambda:colorpicker0(0))
c1 = Button(app, text="",height=1,width=5,bg="red",command=lambda:colorpicker0(1))
c2 = Button(app, text="",height=1,width=5,bg="yellow",command=lambda:colorpicker0(2))
c3 = Button(app, text="",height=1,width=5,bg="orange",command=lambda:colorpicker0(3))
c4 = Button(app, text="",height=1,width=5,bg="pink",command=lambda:colorpicker0(4))
c5 = Button(app, text="",height=1,width=5,bg="blue",command=lambda:colorpicker0(5))
c6 = Button(app, text="",height=1,width=5,bg="green",command=lambda:colorpicker0(6))
c7 = Button(app, text="",height=1,width=5,bg="cyan",command=lambda:colorpicker0(7))
c8 = Button(app, text="",height=1,width=5,bg="purple",command=lambda:colorpicker0(8))
c9 = Button(app, text="",height=1,width=5,bg="brown",command=lambda:colorpicker0(9))
c10 = Button(app, text="",height=1,width=5,bg="grey",command=lambda:colorpicker0(10))
c11 = Button(app, text="",height=1,width=5,bg="teal",command=lambda:colorpicker0(11))
operadores=Label(app,text="color operadores")
operadores.place(x=400,y=600)

#botones de los colores numeros
c00 = Button(app, text="",height=1,width=5,bg="black",command=lambda:colorpicker1(0))
c01 = Button(app, text="",height=1,width=5,bg="red",command=lambda:colorpicker1(1))
c02 = Button(app, text="",height=1,width=5,bg="yellow",command=lambda:colorpicker1(2))
c03 = Button(app, text="",height=1,width=5,bg="orange",command=lambda:colorpicker1(3))
c04 = Button(app, text="",height=1,width=5,bg="pink",command=lambda:colorpicker1(4))
c05 = Button(app, text="",height=1,width=5,bg="blue",command=lambda:colorpicker1(5))
c06 = Button(app, text="",height=1,width=5,bg="green",command=lambda:colorpicker1(6))
c07 = Button(app, text="",height=1,width=5,bg="cyan",command=lambda:colorpicker1(7))
c08 = Button(app, text="",height=1,width=5,bg="purple",command=lambda:colorpicker1(8))
c09 = Button(app, text="",height=1,width=5,bg="brown",command=lambda:colorpicker1(9))
c010 = Button(app, text="",height=1,width=5,bg="grey",command=lambda:colorpicker1(10))
c011 = Button(app, text="",height=1,width=5,bg="teal",command=lambda:colorpicker1(11))
numero=Label(app,text="color numeros")
numero.place(x=400,y=410)
############################################################ 
colores()
menubar()
############################################################ 


app.mainloop()