
import tkinter as tk
from turtle import color

from ventana import display
def figuras(n):
    if (n=="0"):
        display.create_oval(0,5,5,10)
        display.addtag_all
    elif (n=="1"):
        display.create_line(10,10,20,20)
        display.addtag_all
