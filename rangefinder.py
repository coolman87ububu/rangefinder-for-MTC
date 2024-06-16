import tkinter as tk
import math

xlength = 240
ylength = 240
xsquare = 1
ysquare = 5
range_value = 0

root = tk.Tk()
root.title("Range Calculator")
root.geometry("400x400")

xlengthinput = tk.Entry(root)
xlengthinput.place(x=20, y=20)

ylengthinput = tk.Entry(root)
ylengthinput.place(x=220, y=20)

xsquareinput = tk.Entry(root)
xsquareinput.place(x=20, y=80)

ysquareinput = tk.Entry(root)
ysquareinput.place(x=220, y=80)

rangelabel = tk.Label(root, text="Range: " + str(range_value))
rangelabel.place(x=80, y=320)

def calc():
    global xlength, ylength, xsquare, ysquare, range_value
    
    xlength = int(xlengthinput.get())
    ylength = int(ylengthinput.get())
    xsquare = int(xsquareinput.get())
    ysquare = int(ysquareinput.get())
    
    xtotal = xlength * xsquare
    ytotal = ylength * ysquare
    range_value = math.sqrt(xtotal**2 + ytotal**2)
    
    rangelabel.config(text="Range: " + str(range_value))

runbutton = tk.Button(root, text="Find Range", command=calc)
runbutton.place(x=120, y=150)

root.mainloop()


