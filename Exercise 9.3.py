#Exercise 9.3
#Select geometric figures
#Rida Abdulwasay
#1/18/2018

from tkinter import *

class GeometricFigures:
    def __init__(self):
        window = Tk()
        window.title("Radiobuttons and Checkbuttons")

        self.canvas = Canvas(window, width = 200, height = 100,
                             bg = "white")
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()
        self.v1 = IntVar()
        cbtFill = Checkbutton(frame, text = "Fill",
                variable = self.v1, command = self.process)
        
        self.v2 = IntVar()
        rbRect = Radiobutton(frame, text = "Rectangle",
                 variable = self.v2, value = 1,
                 command = self.process)
        
        rbOval = Radiobutton(frame, text = "Oval",
                 variable = self.v2, value = 2,
                 command = self.process)
        

        rbRect.grid(row = 1, column = 1)
        rbOval.grid(row = 1, column = 2)
        cbtFill.grid(row = 1, column = 3)

        window.mainloop()

    def process(self):
        self.canvas.delete("rect", "oval")
        if self.v1.get() == 0:
            color = "white"
        elif self.v1.get() == 1:
            color = "red"
        if self.v2.get() == 1:
            self.canvas.create_rectangle(10, 10, 190, 90, tags = "rect", fill = color)
        elif self.v2.get() == 2:
           self.canvas.create_oval(10, 10, 190, 90, tags = "oval", fill = color)

       
GeometricFigures()   


